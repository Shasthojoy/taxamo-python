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
class Transactions:
    """NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually."""


    def __init__(self):
        self.swaggerTypes = {
            'confirm_timestamp': 'str',
            'fully_informative': 'bool',
            'deducted_tax_amount': 'number',
            'order_date_type': 'str',
            'buyer_credit_card_prefix': 'str',
            'custom_data': 'str',
            'buyer_name': 'str',
            'invoice_date': 'str',
            'create_timestamp': 'str',
            'currency_code': 'str',
            'sub_account_id': 'str',
            'supply_date': 'str',
            'buyer_tax_number_normalized': 'str',
            'invoice_image_url': 'str',
            'key': 'str',
            'buyer_tax_number_format_valid': 'bool',
            'tax_number_service': 'str',
            'control_flags': 'list[control_flags]',
            'invoice_address': 'invoice_address',
            'buyer_tax_number_valid': 'bool',
            'verification_token': 'str',
            'note': 'str',
            'tax_supported': 'bool',
            'tax_data': 'tax_data_schema',
            'transaction_lines': 'list[transaction_lines]',
            'buyer_tax_number': 'str',
            'external_key': 'str',
            'status': 'str',
            'custom_fields': 'list[custom_fields]',
            'force_country_code': 'str',
            'countries': 'countries',
            'invoice_number': 'str',
            'order_date': 'str',
            'customer_id': 'str',
            'kind': 'str',
            'source': 'str',
            'amount': 'number',
            'comments': 'str',
            'buyer_ip': 'str',
            'buyer_email': 'str',
            'original_transaction_key': 'str',
            'billing_country_code': 'str',
            'custom_id': 'str',
            'tax_amount': 'number',
            'tax_entity_additional_id': 'str',
            'warnings': 'list[warnings]',
            'additional_currencies': 'additional_currencies',
            'invoice_place': 'str',
            'total_amount': 'number',
            'tax_entity_name': 'str',
            'evidence': 'evidence',
            'refunded_tax_amount': 'number',
            'manual': 'bool',
            'tax_timezone': 'str',
            'description': 'str',
            'test': 'bool',
            'tax_deducted': 'bool',
            'tax_country_code': 'str',
            'refunded_total_amount': 'number'

        }


        #Date and time of transaction confirmation.
        self.confirm_timestamp = None # str
        #Set to true if transaction has only informative lines.
        self.fully_informative = None # bool
        #How much tax has been deducted.
        self.deducted_tax_amount = None # number
        #'timestamp' means that an order date was captured with a full timestamp and can be applied to an FX source which distinguishes time of the day. Empty value or 'day' means that only day information is present.
        self.order_date_type = None # str
        #First 6 digits of buyer's credit card prefix.
        self.buyer_credit_card_prefix = None # str
        #Custom data related to transaction.
        self.custom_data = None # str
        #Buyer's name - first name and last name or company name.
        self.buyer_name = None # str
        #Invoice date of issue.
        self.invoice_date = None # str
        #Date and time of transaction creation.
        self.create_timestamp = None # str
        #Currency code for transaction - e.g. EUR.
        self.currency_code = None # str
        #Sub account identifier.
        self.sub_account_id = None # str
        #Supply date in yyyy-MM-dd format.
        self.supply_date = None # str
        #Buyer's tax number - normalized form.
        self.buyer_tax_number_normalized = None # str
        #Invoice image URL - provided by Taxamo.
        self.invoice_image_url = None # str
        #Id generated by taxamo.
        self.key = None # str
        #If the buyer tax number has been checked for syntax and is correct. It does not determine if the transaction should be tax deducted.
        self.buyer_tax_number_format_valid = None # bool
        #Tax number service identifier - if available for a given region and the region is enabled.
        self.tax_number_service = None # str
        #Control flags, stored as key-value pairs.
        self.control_flags = None # list[control_flags]
        #Invoice address.
        self.invoice_address = None # invoice_address
        #If the buyer tax number has been provided and was validated successfully. Always true for domestic transactions (billing country same as merchant's country), tax number doesn't get validated in that case.
        self.buyer_tax_number_valid = None # bool
        #Verification token
        self.verification_token = None # str
        #Additional note related to transaction state - for example if the transaction was created in a 'catch-all' mode or the VAT number re-check for subscriptions has failed.
        self.note = None # str
        #Is tax calculation supported for a detected tax location?
        self.tax_supported = None # bool
        #Tax additional information - e.g. US sales tax exemption certificate data.
        self.tax_data = None # tax_data_schema
        #Transaction lines.
        self.transaction_lines = None # list[transaction_lines]
        # Buyer's tax number - EU VAT number for example. If using EU VAT number, it is possible to provide country code in it (e.g. IE1234567X) or simply use billing_country_code field for that. In the first case, if billing_country_code value was provided, it will be overwritten with country code value extracted from VAT number - but only if the VAT has been verified properly.
        self.buyer_tax_number = None # str
        #Transaction external key
        self.external_key = None # str
        #Transaction status: 'N' - new, 'C' - confirmed. Can use 'C' in store-transaction! with private-token to create confirmed transaction, otherwise 'N' is default status. Not applicable for update-transaction!.
        self.status = None # str
        #Custom fields, stored as key-value pairs. This property is not processed and used mostly with Taxamo-built helpers.
        self.custom_fields = None # list[custom_fields]
        #Two-letter ISO country code, e.g. FR. Use it to force country code for tax calculation.
        self.force_country_code = None # str
        #Map of countries calculated from evidence provided. This value is not stored and is available only upon tax calculation.
        self.countries = None # countries
        #Invoice number.
        self.invoice_number = None # str
        #Order date in yyyy-MM-dd or yyyy-MM-dd HH:mm:ss or yyyy-MM-dd'T'HH:mm:ss'Z' format, in merchant's timezone. If provided by the API caller, no timezone conversion is performed. Default value is current date and time in merchant's timezone. When using public token, the default value is used. When time is provided, it is assumed that the date has full resolution, which affects some regions FX rate calculation - Serbia for example.
        self.order_date = None # str
        #Free-form field for storing customer id.
        self.customer_id = None # str
        #Transaction kind: eu-b2c, eu-b2b, domestic, untaxed
        self.kind = None # str
        #Transaction source software - e.g. plugin
        self.source = None # str
        #Amount of transaction without tax.
        self.amount = None # number
        #Additional information about the transaction - for example if the evidence has been amended.
        self.comments = None # str
        #IP address of the buyer in dotted decimal (IPv4) or text format (IPv6).
        self.buyer_ip = None # str
        #Buyer's declared email address.
        self.buyer_email = None # str
        #Use data and evidence from original transaction. Tax will be re-calculated, but evidence won't be re-checked. This parameter is taken into account only when 'manual' flag is raised.
        self.original_transaction_key = None # str
        #Billing two letter ISO country code.
        self.billing_country_code = None # str
        #Custom identifier provided upon transaction creation.
        self.custom_id = None # str
        #Tax amount of transaction.
        self.tax_amount = None # number
        #Tax entity additional id.
        self.tax_entity_additional_id = None # str
        #Warnings for the transaction process, usually related to contacting B2B validation service.
        self.warnings = None # list[warnings]
        #Additional currency information - can be used to receive additional information about invoice in another currency.
        self.additional_currencies = None # additional_currencies
        #Invoice place of issue.
        self.invoice_place = None # str
        #Total amount of transaction.
        self.total_amount = None # number
        #To which entity is the tax due.
        self.tax_entity_name = None # str
        #Tax country of residence evidence.
        self.evidence = None # evidence
        #Refunded tax amount.
        self.refunded_tax_amount = None # number
        #Is the transaction created manually - using private token. In manual mode, it is the merchant who calculates tax country and validates evidence. If you need API to do that when accessing the API with private token, just skip the 'manual' flag or use false value there and provide customer's ip address through buyer_ip field. Manual mode is also used when using original_transaction_key field.
        self.manual = None # bool
        #Timezone name for tax transaction.
        self.tax_timezone = None # str
        #Transaction description.
        self.description = None # str
        #Was this transaction created in test mode?
        self.test = None # bool
        #If the transaction is in a country supported by Taxamo, but the tax is not calculated due to merchant settings or EU B2B transaction for example.
        self.tax_deducted = None # bool
        #Two-letter ISO country code, e.g. FR. This code applies to detected/set country for transaction, but can be set using manual mode.
        self.tax_country_code = None # str
        #Total amount refunde (including tax).
        self.refunded_total_amount = None # number
        
