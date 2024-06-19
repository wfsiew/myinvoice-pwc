from fastapi import Depends, FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.responses import FileResponse
from contextlib import asynccontextmanager
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.jobstores.memory import MemoryJobStore
from functools import lru_cache
from typing import Annotated

from .config import Settings
from .constants import *
import httpx, jinja2, json, base64

@lru_cache
def get_settings():
    return Settings()

class DataManager:
    
    access_token = None

class HTTPXClientWrapper:
    
    async_client = None
    
    def start(self):
        """ Instantiate the client. Call from the FastAPI startup hook."""
        self.async_client = httpx.AsyncClient()
        
    async def stop(self):
        """ Gracefully shutdown. Call from FastAPI shutdown hook."""
        await self.async_client.aclose()
        self.async_client = None
        
    def __call__(self):
        """ Calling the instantiated HTTPXClientWrapper returns the wrapped singleton."""
        # Ensure we don't use it if not started / running
        assert self.async_client is not None
        return self.async_client
    
httpx_client_wrapper = HTTPXClientWrapper()
jobstores = {
    'default': MemoryJobStore()
}
scheduler = AsyncIOScheduler(jobstores=jobstores, timezone='Asia/Kuala_Lumpur')
    
@asynccontextmanager
async def lifespan(app: FastAPI):
    httpx_client_wrapper.start()
    scheduler.start()
    await get_token()
    yield
    await httpx_client_wrapper.stop()
    scheduler.shutdown()
    
templates = Jinja2Templates(directory='templates')
app = FastAPI(dependencies=[], title='App', description='App API description', version='1.0', lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
    expose_headers=['*'],
)

async def get_token():
    cli = httpx_client_wrapper()
    # headers = {
    #     'Content-Type': 'application/x-www-form-urlencoded'
    # }
    settings = get_settings()
    data = {
        'client_id': settings.client_id,
        'client_secret': settings.client_secret,
        'grant_type': 'client_credentials',
        'scope': settings.scope
    }
    res = await cli.post(f'{settings.api_base_url}/oauth2/v2.0/token', data=data)
    m = res.json()
    DataManager.access_token = m.get('access_token')
    print(DataManager.access_token)

@scheduler.scheduled_job('interval', minutes=50)
async def interval_task_test():
    await get_token()

@app.get('/login')
async def login(settings: Annotated[Settings, Depends(get_settings)]):
    cli = httpx_client_wrapper()
    # headers = {
    #     'Content-Type': 'application/x-www-form-urlencoded'
    # }
    data = {
        'client_id': settings.client_id,
        'client_secret': settings.client_secret,
        'grant_type': 'client_credentials',
        'scope': settings.scope
    }
    res = await cli.post(f'{settings.api_base_url}/oauth2/v2.0/token', data=data)
    m = res.json()
    DataManager.access_token = m.get('access_token')
    return m

@app.get('/submissions')
async def submissions(settings: Annotated[Settings, Depends(get_settings)]):
    cli = httpx_client_wrapper()
    headers = {
        'Authorization': f'Bearer {DataManager.access_token}',
        'Content-Type': 'application/xml',
        'Accept': '*/*',
        'Connection': 'keep-alive',
        'User-Agent': 'wf001',
        'ErpId': 'wf001'
    }
    doc = '''<document>
    <supplier_name>SupplierCompany</supplier_name>
    <supplier_tin>sup1234567890</supplier_tin>
    <supplier_regnumber>123456789100</supplier_regnumber>
    <supplier_sst>abcd12345678910</supplier_sst>
    <supplier_tourismtax_number></supplier_tourismtax_number>
    <supplier_email>supplier@test.com</supplier_email>
    <supplier_msic>00000</supplier_msic>
    <supplier_business_activity_description>test activity description</supplier_business_activity_description>
    <supplier_contactnumber>123456789</supplier_contactnumber>
    <supplier_address_line>Building 1 Road 2</supplier_address_line>
    <supplier_address_postalZone>51470</supplier_address_postalZone>
    <supplier_address_city>Kuala Lumpur</supplier_address_city>
    <supplier_address_countrysubentitycode>Region 1</supplier_address_countrysubentitycode>
    <supplier_address_country>MYS</supplier_address_country>
    <buyer_name>BuyerCompany</buyer_name>
    <buyer_tin>buy1234567890</buyer_tin>
    <buyer_regnumber>123456789100</buyer_regnumber>
    <buyer_sst>abcd12345678910</buyer_sst>
    <buyer_email>buyer@test.com</buyer_email>
    <buyer_contactnumber>123456789</buyer_contactnumber>
    <buyer_address_line>Building 1 Road 2</buyer_address_line>
    <buyer_address_postalZone>51470</buyer_address_postalZone>
    <buyer_address_city>Kuala Lumpur</buyer_address_city>
    <buyer_address_countrysubentitycode>Region 1</buyer_address_countrysubentitycode>
    <buyer_address_country>MYS</buyer_address_country>
    <shipping_recipient_name>shipping recipient name</shipping_recipient_name>
    <shipping_recipient_address_line>Building 1 Road 2</shipping_recipient_address_line>
    <shipping_recipient_address_postalZone>51470</shipping_recipient_address_postalZone>
    <shipping_recipient_address_city>Kuala Lumpur</shipping_recipient_address_city>
    <shipping_recipient_address_countrysubentitycode>Region 1</shipping_recipient_address_countrysubentitycode>
    <shipping_recipient_address_country>MYS</shipping_recipient_address_country>
    <shipping_recipient_tin>shi1234567890</shipping_recipient_tin>
    <shipping_recipient_regnumber>123456789100</shipping_recipient_regnumber>
    <invoice_number>invnumber123</invoice_number>
    <invoice_type>01</invoice_type>
    <original_invoice_number></original_invoice_number>
    <issue_date>2002-05-30T09:00:00</issue_date>
    <currency_code>MYR</currency_code>
    <exchange_rate>1</exchange_rate>
    <billing_frequency>Daily</billing_frequency>
    <billing_period_start>2025-01-01</billing_period_start>
    <billing_period_end>2025-01-31</billing_period_end>
    <payment_mode>05</payment_mode>
    <payment_terms>30 days</payment_terms>
    <prepayment_amount>100</prepayment_amount>
    <prepayment_date>2002-05-30T09:00:00</prepayment_date>
    <prepayment_reference_number>pre123456789</prepayment_reference_number>
    <bill_reference_number>brf123456789</bill_reference_number>
    <customs_form_reference_number>cfr123456789</customs_form_reference_number>
    <incoterms>testincoterm</incoterms>
    <tax_summary>
        <total_excluding_tax>10000</total_excluding_tax>
        <total_including_tax>10400</total_including_tax>
        <total_tax_amount>400</total_tax_amount>
        <total_net_amount>10000</total_net_amount>
        <total_payable_amount>10400</total_payable_amount>
        <rounding_amount>0</rounding_amount>
        <discount_amount>500</discount_amount>
        <fee_amount>100</fee_amount>
        <tax_type>
            <tax_type>01</tax_type>
            <tax_amount>400</tax_amount>
            <tax_exemption></tax_exemption>
            <exempted_tax_amount></exempted_tax_amount>
            <taxable_amount>5000</taxable_amount>
        </tax_type>
        <tax_type>
            <tax_type>02</tax_type>
            <tax_amount>0</tax_amount>
            <tax_exemption>Buyer’s sales tax exemption certificate number</tax_exemption>
            <exempted_tax_amount>400</exempted_tax_amount>
            <taxable_amount>5000</taxable_amount>
        </tax_type>
    </tax_summary>
    <line>
        <classification>service</classification>
        <description>service</description>
        <unit_price>5000</unit_price>
        <tax_type>02</tax_type>
        <tax_rate>0.08</tax_rate>
        <tax_amount>0</tax_amount>
        <tax_exemption>Buyer’s sales tax exemption certificate number</tax_exemption>
        <exempted_tax_amount>400</exempted_tax_amount>
        <subtotal>5000</subtotal>
        <total_excluding_tax>5000</total_excluding_tax>
        <quantity></quantity>
        <measurement></measurement>
        <discount_rate></discount_rate>
        <discount_amount></discount_amount>
        <fee_rate></fee_rate>
        <fee_amount></fee_amount>
    </line>
      <line>
        <classification>goods</classification>
        <description>goods</description>
        <unit_price>500</unit_price>
        <tax_type>01</tax_type>
        <tax_rate>0.08</tax_rate>
        <tax_amount>400</tax_amount>
        <tax_exemption></tax_exemption>
        <exempted_tax_amount></exempted_tax_amount>
        <subtotal>4400</subtotal>
        <total_excluding_tax>5000</total_excluding_tax>
        <quantity>10</quantity>
        <measurement>piece</measurement>
        <discount_rate>0.1</discount_rate>
        <discount_amount>500</discount_amount>
        <fee_rate>0.1</fee_rate>
        <fee_amount>100</fee_amount>
    </line>
</document>'''
    xml = doc.encode('utf-8')
    v = base64.b64encode(xml)
    k = v.decode('utf-8')
    res = await cli.post(f'{settings.api_base_url}/api/submissions', headers=headers, content=k)
    print(res.status_code)
    return 'ok'

@app.get('/getsubmission')
async def getsubmission_by_erpid(erpid: str, settings: Annotated[Settings, Depends(get_settings)]):
    cli = httpx_client_wrapper()
    headers = {
        'Authorization': f'Bearer {DataManager.access_token}',
        'PwC-User-Agent': 'pwc_excel',
        'Accept': '*/*',
        'Connection': 'keep-alive',
        'User-Agent': 'wf001'
    }
    prm = {
        'erp_id': erpid
    }
    res = await cli.get(f'{settings.api_base_url}/api/submissions', headers=headers, params=prm)
    return res.json()

@app.get('/validate')
async def validate(settings: Annotated[Settings, Depends(get_settings)]):
    cli = httpx_client_wrapper()
    headers = {
        'Authorization': f'Bearer {DataManager.access_token}'
    }
    prm = {
        'idType': 'BRN',
        'idValue': '200201024235'
    }
    res = await cli.get(f'{settings.api_base_url}/api/v1.0/taxpayer/validate/C10924204010', headers=headers, params=prm)
    if res.status_code == 200:
        return 'success'
    
    return 'fail'

# @app.get('/documentsubmissions')
# async def documentsubmissions(settings: Annotated[Settings, Depends(get_settings)]):
#     # S79HNH3XM3CBA7Y1FB1GPNYH10
#     data = {
#         'inv': 'INV1234598',
#         'issue_date': '2024-05-28',
#         'tin': settings.tin,
#         'brn': settings.brn
#     }
#     templateLoader = jinja2.FileSystemLoader(searchpath='./templates')
#     templateEnv = jinja2.Environment(loader=templateLoader)
#     template = templateEnv.get_template('invoice.xml.jinja2')
#     s = template.render(data)
#     doc = Document(s)
    
#     cli = httpx_client_wrapper()
#     headers = {
#         'Authorization': f'Bearer {DataManager.access_token}'
#     }
#     fx = {
#         'documents': [
#             doc.getDoc('INV1234598')
#         ]
#     }
#     res = await cli.post(f'{settings.api_base_url}/api/v1.0/documentsubmissions', headers=headers, json=fx)
#     return res.json()

@app.get('/getsubmission/:submissionUid')
async def getsubmission(submissionUid: str, settings: Annotated[Settings, Depends(get_settings)]):
    cli = httpx_client_wrapper()
    headers = {
        'Authorization': f'Bearer {DataManager.access_token}'
    }
    res = await cli.get(f'{settings.api_base_url}/api/v1.0/documentsubmissions/{submissionUid}', headers=headers)
    return res.json()

@app.get('/documenttypes')
async def documenttypes(settings: Annotated[Settings, Depends(get_settings)]):
    cli = httpx_client_wrapper()
    headers = {
        'Authorization': f'Bearer {DataManager.access_token}'
    }
    res = await cli.get(f'{settings.api_base_url}/api/v1.0/documenttypes', headers=headers)
    return res.json()

@app.get('/datax')
async def test():
    templateLoader = jinja2.FileSystemLoader(searchpath='./templates')
    templateEnv = jinja2.Environment(loader=templateLoader)
    template = templateEnv.get_template('data.json.jinja2')
    outputText = template.render({"name": 'ben'})
    return json.loads(outputText)

@app.get('/data', response_class=FileResponse)
async def data(req: Request, settings: Annotated[Settings, Depends(get_settings)]):
    prm = {
        'inv': 'INV1234595',
        'issue_date': '2024-05-25',
        'tin': settings.tin,
        'brn': settings.brn
    }
    return templates.TemplateResponse(
        request=req, name='invoice.xml.jinja2', context=prm,
        media_type='application/xml',
        headers={
            'Content-disposition': 'attachment; filename=invoice.xml',
            'Content-Type': 'application/xml',
            'Cache-Control': 'no-cache, no-store, must-revalidate',
            'Pragma': 'no-cache',
            'Expires': '0',
            'filename': 'invoice.xml'
        }
    )