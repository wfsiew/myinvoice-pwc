data = '''{
  "_D": "urn:oasis:names:specification:ubl:schema:xsd:Invoice-2",
  "_A": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
  "_B": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
  "Invoice": [
    {
      "ID": [
        {
          "_": "INV1234589"
        }
      ],
      "IssueDate": [
        {
          "_": "2024-05-23"
        }
      ],
      "IssueTime": [
        {
          "_": "15:30:00Z"
        }
      ],
      "InvoiceTypeCode": [
        {
          "_": "01",
          "listVersionID": "1.0"
        }
      ],
      "DocumentCurrencyCode": [
        {
          "_": "MYR"
        }
      ],
      "InvoicePeriod": [
        {
          "StartDate": [
            {
              "_": "2024-05-01"
            }
          ],
          "EndDate": [
            {
              "_": "2024-05-31"
            }
          ],
          "Description": [
            {
              "_": "Monthly"
            }
          ]
        }
      ],
      "BillingReference": [
        {
          "AdditionalDocumentReference": [
            {
              "ID": [
                {
                  "_": "E12345678912"
                }
              ]
            }
          ]
        }
      ],
      "AdditionalDocumentReference": [
        {
          "ID": [
            {
              "_": "E12345678912"
            }
          ],
          "DocumentType": [
            {
              "_": "CustomsImportForm"
            }
          ]
        },
        {
          "ID": [
            {
              "_": "ASEAN-Australia-New Zealand FTA (AANZFTA)"
            }
          ],
          "DocumentType": [
            {
              "_": "FreeTradeAgreement"
            }
          ],
          "DocumentDescription": [
            {
              "_": "Sample Description"
            }
          ]
        },
        {
          "ID": [
            {
              "_": "E12345678912"
            }
          ],
          "DocumentType": [
            {
              "_": "K2"
            }
          ]
        },
        {
          "ID": [
            {
              "_": "CIF"
            }
          ]
        }
      ],
      "AccountingSupplierParty": [
        {
          "AdditionalAccountID": [
            {
              "_": "CPT-CCN-W-211111-KL-000002",
              "schemeAgencyName": "CertEX"
            }
          ],
          "Party": [
            {
              "IndustryClassificationCode": [
                {
                  "_": "01111",
                  "name": "Growing of maize"
                }
              ],
              "PartyIdentification": [
                {
                  "ID": [
                    {
                      "_": "C10924204010",
                      "schemeID": "TIN"
                    }
                  ]
                },
                {
                  "ID": [
                    {
                      "_": "200201024235",
                      "schemeID": "BRN"
                    }
                  ]
                }
              ],
              "PostalAddress": [
                {
                  "CityName": [
                    {
                      "_": "Kuala Lumpur"
                    }
                  ],
                  "PostalZone": [
                    {
                      "_": "50480"
                    }
                  ],
                  "CountrySubentityCode": [
                    {
                      "_": "14"
                    }
                  ],
                  "AddressLine": [
                    {
                      "Line": [
                        {
                          "_": "Lot 66"
                        }
                      ]
                    },
                    {
                      "Line": [
                        {
                          "_": "Bangunan Merdeka"
                        }
                      ]
                    },
                    {
                      "Line": [
                        {
                          "_": "Persiaran Jaya"
                        }
                      ]
                    }
                  ],
                  "Country": [
                    {
                      "IdentificationCode": [
                        {
                          "_": "MYS",
                          "listID": "ISO3166-1",
                          "listAgencyID": "6"
                        }
                      ]
                    }
                  ]
                }
              ],
              "PartyLegalEntity": [
                {
                  "RegistrationName": [
                    {
                      "_": "AMS Setia Jaya Sdn. Bhd."
                    }
                  ]
                }
              ],
              "Contact": [
                {
                  "Telephone": [
                    {
                      "_": "+60-123456789"
                    }
                  ],
                  "ElectronicMail": [
                    {
                      "_": "general.ams@supplier.com"
                    }
                  ]
                }
              ]
            }
          ]
        }
      ],
      "AccountingCustomerParty": [
        {
          "Party": [
            {
              "PostalAddress": [
                {
                  "CityName": [
                    {
                      "_": "Kuala Lumpur"
                    }
                  ],
                  "PostalZone": [
                    {
                      "_": "50480"
                    }
                  ],
                  "CountrySubentityCode": [
                    {
                      "_": "14"
                    }
                  ],
                  "AddressLine": [
                    {
                      "Line": [
                        {
                          "_": "Lot 66"
                        }
                      ]
                    },
                    {
                      "Line": [
                        {
                          "_": "Bangunan Merdeka"
                        }
                      ]
                    },
                    {
                      "Line": [
                        {
                          "_": "Persiaran Jaya"
                        }
                      ]
                    }
                  ],
                  "Country": [
                    {
                      "IdentificationCode": [
                        {
                          "_": "MYS",
                          "listID": "ISO3166-1",
                          "listAgencyID": "6"
                        }
                      ]
                    }
                  ]
                }
              ],
              "PartyLegalEntity": [
                {
                  "RegistrationName": [
                    {
                      "_": "Hebat Group"
                    }
                  ]
                }
              ],
              "PartyIdentification": [
                {
                  "ID": [
                    {
                      "_": "C2584563200",
                      "schemeID": "TIN"
                    }
                  ]
                },
                {
                  "ID": [
                    {
                      "_": "201901234567",
                      "schemeID": "BRN"
                    }
                  ]
                }
              ],
              "Contact": [
                {
                  "Telephone": [
                    {
                      "_": "+60-123456789"
                    }
                  ],
                  "ElectronicMail": [
                    {
                      "_": "name@buyer.com"
                    }
                  ]
                }
              ]
            }
          ]
        }
      ],
      "Delivery": [
        {
          "DeliveryParty": [
            {
              "PartyLegalEntity": [
                {
                  "RegistrationName": [
                    {
                      "_": "Greenz Sdn. Bhd."
                    }
                  ]
                }
              ],
              "PostalAddress": [
                {
                  "CityName": [
                    {
                      "_": "Kuala Lumpur"
                    }
                  ],
                  "PostalZone": [
                    {
                      "_": "50480"
                    }
                  ],
                  "CountrySubentityCode": [
                    {
                      "_": "14"
                    }
                  ],
                  "AddressLine": [
                    {
                      "Line": [
                        {
                          "_": "Lot 66"
                        }
                      ]
                    },
                    {
                      "Line": [
                        {
                          "_": "Bangunan Merdeka"
                        }
                      ]
                    },
                    {
                      "Line": [
                        {
                          "_": "Persiaran Jaya"
                        }
                      ]
                    }
                  ],
                  "Country": [
                    {
                      "IdentificationCode": [
                        {
                          "_": "MYS",
                          "listID": "ISO3166-1",
                          "listAgencyID": "6"
                        }
                      ]
                    }
                  ]
                }
              ],
              "PartyIdentification": [
                {
                  "ID": [
                    {
                      "_": "C2584563200",
                      "schemeID": "TIN"
                    }
                  ]
                },
                {
                  "ID": [
                    {
                      "_": "201901234567",
                      "schemeID": "BRN"
                    }
                  ]
                }
              ]
            }
          ],
          "Shipment": [
            {
              "ID": [
                {
                  "_": "1234"
                }
              ],
              "FreightAllowanceCharge": [
                {
                  "ChargeIndicator": [
                    {
                      "_": true
                    }
                  ],
                  "AllowanceChargeReason": [
                    {
                      "_": "Service charge"
                    }
                  ],
                  "Amount": [
                    {
                      "_": 100,
                      "currencyID": "MYR"
                    }
                  ]
                }
              ]
            }
          ]
        }
      ],
      "PaymentMeans": [
        {
          "PaymentMeansCode": [
            {
              "_": "01"
            }
          ],
          "PayeeFinancialAccount": [
            {
              "ID": [
                {
                  "_": "1234567890123"
                }
              ]
            }
          ]
        }
      ],
      "PaymentTerms": [
        {
          "Note": [
            {
              "_": "Payment method is cash"
            }
          ]
        }
      ],
      "PrepaidPayment": [
        {
          "ID": [
            {
              "_": "E12345678912"
            }
          ],
          "PaidAmount": [
            {
              "_": 1.00,
              "currencyID": "MYR"
            }
          ],
          "PaidDate": [
            {
              "_": "2024-05-02"
            }
          ],
          "PaidTime": [
            {
              "_": "12:00:00Z"
            }
          ]
        }
      ],
      "AllowanceCharge": [
        {
          "ChargeIndicator": [
            {
              "_": false
            }
          ],
          "AllowanceChargeReason": [
            {
              "_": "Sample Description"
            }
          ],
          "Amount": [
            {
              "_": 100,
              "currencyID": "MYR"
            }
          ]
        },
        {
          "ChargeIndicator": [
            {
              "_": true
            }
          ],
          "AllowanceChargeReason": [
            {
              "_": "Service charge"
            }
          ],
          "Amount": [
            {
              "_": 100,
              "currencyID": "MYR"
            }
          ]
        }
      ],
      "TaxTotal": [
        {
          "TaxAmount": [
            {
              "_": 87.63,
              "currencyID": "MYR"
            }
          ],
          "TaxSubtotal": [
            {
              "TaxableAmount": [
                {
                  "_": 87.63,
                  "currencyID": "MYR"
                }
              ],
              "TaxAmount": [
                {
                  "_": 87.63,
                  "currencyID": "MYR"
                }
              ],
              "TaxCategory": [
                {
                  "ID": [
                    {
                      "_": "E"
                    }
                  ],
                  "TaxScheme": [
                    {
                      "ID": [
                        {
                          "_": "OTH",
                          "schemeID": "UN/ECE 5153",
                          "schemeAgencyID": "6"
                        }
                      ]
                    }
                  ]
                }
              ]
            }
          ]
        }
      ],
      "LegalMonetaryTotal": [
        {
          "LineExtensionAmount": [
            {
              "_": 1436.50,
              "currencyID": "MYR"
            }
          ],
          "TaxExclusiveAmount": [
            {
              "_": 1436.50,
              "currencyID": "MYR"
            }
          ],
          "TaxInclusiveAmount": [
            {
              "_": 1436.50,
              "currencyID": "MYR"
            }
          ],
          "AllowanceTotalAmount": [
            {
              "_": 1436.50,
              "currencyID": "MYR"
            }
          ],
          "ChargeTotalAmount": [
            {
              "_": 1436.50,
              "currencyID": "MYR"
            }
          ],
          "PayableRoundingAmount": [
            {
              "_": 0.30,
              "currencyID": "MYR"
            }
          ],
          "PayableAmount": [
            {
              "_": 1436.50,
              "currencyID": "MYR"
            }
          ]
        }
      ],
      "InvoiceLine": [
        {
          "ID": [
            {
              "_": "1"
            }
          ],
          "InvoicedQuantity": [
            {
              "_": 1,
              "unitCode": "C62"
            }
          ],
          "LineExtensionAmount": [
            {
              "_": 1436.50,
              "currencyID": "MYR"
            }
          ],
          "AllowanceCharge": [
            {
              "ChargeIndicator": [
                {
                  "_": false
                }
              ],
              "AllowanceChargeReason": [
                {
                  "_": "Sample Description"
                }
              ],
              "MultiplierFactorNumeric": [
                {
                  "_": 0.15
                }
              ],
              "Amount": [
                {
                  "_": 100,
                  "currencyID": "MYR"
                }
              ]
            },
            {
              "ChargeIndicator": [
                {
                  "_": true
                }
              ],
              "AllowanceChargeReason": [
                {
                  "_": "Sample Description"
                }
              ],
              "MultiplierFactorNumeric": [
                {
                  "_": 0.10
                }
              ],
              "Amount": [
                {
                  "_": 100,
                  "currencyID": "MYR"
                }
              ]
            }
          ],
          "TaxTotal": [
            {
              "TaxAmount": [
                {
                  "_": 1460.50,
                  "currencyID": "MYR"
                }
              ],
              "TaxSubtotal": [
                {
                  "TaxableAmount": [
                    {
                      "_": 1460.50,
                      "currencyID": "MYR"
                    }
                  ],
                  "TaxAmount": [
                    {
                      "_": 0,
                      "currencyID": "MYR"
                    }
                  ],
                  "TaxCategory": [
                    {
                      "ID": [
                        {
                          "_": "E"
                        }
                      ],
                      "Percent": [
                        {
                          "_": 6.00
                        }
                      ],
                      "TaxScheme": [
                        {
                          "ID": [
                            {
                              "_": "OTH",
                              "schemeID": "UN/ECE 5153",
                              "schemeAgencyID": "6"
                            }
                          ]
                        }
                      ],
                      "TaxExemptionReason": [
                        {
                          "_": "Exempt New Means of Transport"
                        }
                      ]
                    }
                  ]
                }
              ]
            }
          ],
          "Item": [
            {
              "CommodityClassification": [
                {
                  "ItemClassificationCode": [
                    {
                      "_": "001",
                      "listID": "PTC"
                    }
                  ]
                },
                {
                  "ItemClassificationCode": [
                    {
                      "_": "002",
                      "listID": "CLASS"
                    }
                  ]
                }
              ],
              "Description": [
                {
                  "_": "Laptop Peripherals"
                }
              ],
              "OriginCountry": [
                {
                  "IdentificationCode": [
                    {
                      "_": "MYS"
                    }
                  ]
                }
              ]
            }
          ],
          "Price": [
            {
              "PriceAmount": [
                {
                  "_": 17,
                  "currencyID": "MYR"
                }
              ]
            }
          ],
          "ItemPriceExtension": [
            {
              "Amount": [
                {
                  "_": 100,
                  "currencyID": "MYR"
                }
              ]
            }
          ]
        }
      ]
    }
  ]
}
'''

import hashlib, base64
x = hashlib.sha256(data.encode('utf-8')).hexdigest()
s = data.encode('utf-8')
c = base64.b64encode(s)
v = c.decode('utf-8')
print(v)
print('===')
print(x)