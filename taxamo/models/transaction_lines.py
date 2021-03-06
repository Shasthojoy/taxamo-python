#!/usr/bin/env python
"""
Copyright 2014-2015 Taxamo, Ltd.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""
class Transaction_lines:
    """NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually."""


    def __init__(self):
        self.swaggerTypes = {
            'product_type': 'str',
            'deducted_tax_amount': 'number',
            'deducted_tax_rate': 'number',
            'supply_date': 'str',
            'id': 'number',
            'unit_price': 'number',
            'unit_of_measure': 'str',
            'quantity': 'number',
            'custom_fields': 'list[custom_fields]',
            'line_key': 'str',
            'tax_name': 'str',
            'product_code': 'str',
            'amount': 'number',
            'custom_id': 'str',
            'informative': 'bool',
            'tax_amount': 'number',
            'tax_rate': 'number',
            'additional_currencies': 'additional_currencies',
            'total_amount': 'number',
            'product_tax_code': 'str',
            'refunded_tax_amount': 'number',
            'description': 'str',
            'refunded_total_amount': 'number'

        }


        #Product type, according to dictionary /dictionaries/product_types. 
        self.product_type = None # str
        #Deducted tax amount, calculated by taxmo.
        self.deducted_tax_amount = None # number
        #Deducted tax rate, calculated by taxamo.
        self.deducted_tax_rate = None # number
        #Date of supply in yyyy-MM-dd format.
        self.supply_date = None # str
        #Generated id.
        self.id = None # number
        #Unit price.
        self.unit_price = None # number
        #Unit of measure.
        self.unit_of_measure = None # str
        #Quantity Defaults to 1.
        self.quantity = None # number
        #Custom fields, stored as key-value pairs. This property is not processed and used mostly with Taxamo-built helpers.
        self.custom_fields = None # list[custom_fields]
        #Generated line key.
        self.line_key = None # str
        #Tax name, calculated by taxamo.  Can be overwritten when informative field is true.
        self.tax_name = None # str
        #Internal product code, used for invoicing for example.
        self.product_code = None # str
        #Amount. Required if total amount or both unit price and quantity are not provided.
        self.amount = None # number
        #Custom id, provided by ecommerce software.
        self.custom_id = None # str
        #If the line is provided for informative purposes. Such line must have :tax-rate and optionally :tax-name - if not, API validation will fail for this line.
        self.informative = None # bool
        #Tax amount, calculated by taxamo.
        self.tax_amount = None # number
        #Tax rate, calculated by taxamo. Must be provided when informative field is true.
        self.tax_rate = None # number
        #Additional currency information - can be used to receive additional information about invoice in another currency.
        self.additional_currencies = None # additional_currencies
        #Total amount. Required if amount or both unit price and quantity are not provided.
        self.total_amount = None # number
        #External product tax code for a line, for example TIC in US Sales tax.
        self.product_tax_code = None # str
        #Refunded tax amount, calculated by taxmo.
        self.refunded_tax_amount = None # number
        #Line contents description.
        self.description = None # str
        #Refunded total amount, calculated by taxmo.
        self.refunded_total_amount = None # number
        
