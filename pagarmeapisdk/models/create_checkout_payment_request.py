# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.api_helper import APIHelper
from pagarmeapisdk.models.create_address_request import CreateAddressRequest
from pagarmeapisdk.models.create_checkout_bank_transfer_request import CreateCheckoutBankTransferRequest
from pagarmeapisdk.models.create_checkout_boleto_payment_request import CreateCheckoutBoletoPaymentRequest
from pagarmeapisdk.models.create_checkout_credit_card_payment_request import CreateCheckoutCreditCardPaymentRequest
from pagarmeapisdk.models.create_checkout_debit_card_payment_request import CreateCheckoutDebitCardPaymentRequest
from pagarmeapisdk.models.create_checkout_pix_payment_request import CreateCheckoutPixPaymentRequest


class CreateCheckoutPaymentRequest(object):

    """Implementation of the 'CreateCheckoutPaymentRequest' model.

    Checkout payment request

    Attributes:
        accepted_payment_methods (List[str]): Accepted Payment Methods
        accepted_multi_payment_methods (List[Any]): Accepted Multi Payment
            Methods
        success_url (str): Success url
        default_payment_method (str): Default payment method
        gateway_affiliation_id (str): Gateway Affiliation Id
        credit_card (CreateCheckoutCreditCardPaymentRequest): Credit Card
            payment request
        debit_card (CreateCheckoutDebitCardPaymentRequest): Debit Card payment
            request
        boleto (CreateCheckoutBoletoPaymentRequest): Boleto payment request
        customer_editable (bool): Customer is editable?
        expires_in (int): Time in minutes for expiration
        skip_checkout_success_page (bool): Skip postpay success screen?
        billing_address_editable (bool): Billing Address is editable?
        billing_address (CreateAddressRequest): Billing Address
        bank_transfer (CreateCheckoutBankTransferRequest): Bank Transfer
            payment request
        accepted_brands (List[str]): Accepted Brands
        pix (CreateCheckoutPixPaymentRequest): Pix payment request

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "accepted_payment_methods": 'accepted_payment_methods',
        "accepted_multi_payment_methods": 'accepted_multi_payment_methods',
        "success_url": 'success_url',
        "skip_checkout_success_page": 'skip_checkout_success_page',
        "billing_address_editable": 'billing_address_editable',
        "billing_address": 'billing_address',
        "accepted_brands": 'accepted_brands',
        "default_payment_method": 'default_payment_method',
        "gateway_affiliation_id": 'gateway_affiliation_id',
        "credit_card": 'credit_card',
        "debit_card": 'debit_card',
        "boleto": 'boleto',
        "customer_editable": 'customer_editable',
        "expires_in": 'expires_in',
        "bank_transfer": 'bank_transfer',
        "pix": 'pix'
    }

    _optionals = [
        'default_payment_method',
        'gateway_affiliation_id',
        'credit_card',
        'debit_card',
        'boleto',
        'customer_editable',
        'expires_in',
        'bank_transfer',
        'pix',
    ]

    def __init__(self,
                 accepted_payment_methods=None,
                 accepted_multi_payment_methods=None,
                 success_url=None,
                 skip_checkout_success_page=None,
                 billing_address_editable=None,
                 billing_address=None,
                 accepted_brands=None,
                 default_payment_method=APIHelper.SKIP,
                 gateway_affiliation_id=APIHelper.SKIP,
                 credit_card=APIHelper.SKIP,
                 debit_card=APIHelper.SKIP,
                 boleto=APIHelper.SKIP,
                 customer_editable=APIHelper.SKIP,
                 expires_in=APIHelper.SKIP,
                 bank_transfer=APIHelper.SKIP,
                 pix=APIHelper.SKIP):
        """Constructor for the CreateCheckoutPaymentRequest class"""

        # Initialize members of the class
        self.accepted_payment_methods = accepted_payment_methods 
        self.accepted_multi_payment_methods = accepted_multi_payment_methods 
        self.success_url = success_url 
        if default_payment_method is not APIHelper.SKIP:
            self.default_payment_method = default_payment_method 
        if gateway_affiliation_id is not APIHelper.SKIP:
            self.gateway_affiliation_id = gateway_affiliation_id 
        if credit_card is not APIHelper.SKIP:
            self.credit_card = credit_card 
        if debit_card is not APIHelper.SKIP:
            self.debit_card = debit_card 
        if boleto is not APIHelper.SKIP:
            self.boleto = boleto 
        if customer_editable is not APIHelper.SKIP:
            self.customer_editable = customer_editable 
        if expires_in is not APIHelper.SKIP:
            self.expires_in = expires_in 
        self.skip_checkout_success_page = skip_checkout_success_page 
        self.billing_address_editable = billing_address_editable 
        self.billing_address = billing_address 
        if bank_transfer is not APIHelper.SKIP:
            self.bank_transfer = bank_transfer 
        self.accepted_brands = accepted_brands 
        if pix is not APIHelper.SKIP:
            self.pix = pix 

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """

        if not isinstance(dictionary, dict) or dictionary is None:
            return None

        # Extract variables from the dictionary
        accepted_payment_methods = dictionary.get("accepted_payment_methods") if dictionary.get("accepted_payment_methods") else None
        accepted_multi_payment_methods = dictionary.get("accepted_multi_payment_methods") if dictionary.get("accepted_multi_payment_methods") else None
        success_url = dictionary.get("success_url") if dictionary.get("success_url") else None
        skip_checkout_success_page = dictionary.get("skip_checkout_success_page") if "skip_checkout_success_page" in dictionary.keys() else None
        billing_address_editable = dictionary.get("billing_address_editable") if "billing_address_editable" in dictionary.keys() else None
        billing_address = CreateAddressRequest.from_dictionary(dictionary.get('billing_address')) if dictionary.get('billing_address') else None
        accepted_brands = dictionary.get("accepted_brands") if dictionary.get("accepted_brands") else None
        default_payment_method = dictionary.get("default_payment_method") if dictionary.get("default_payment_method") else APIHelper.SKIP
        gateway_affiliation_id = dictionary.get("gateway_affiliation_id") if dictionary.get("gateway_affiliation_id") else APIHelper.SKIP
        credit_card = CreateCheckoutCreditCardPaymentRequest.from_dictionary(dictionary.get('credit_card')) if 'credit_card' in dictionary.keys() else APIHelper.SKIP
        debit_card = CreateCheckoutDebitCardPaymentRequest.from_dictionary(dictionary.get('debit_card')) if 'debit_card' in dictionary.keys() else APIHelper.SKIP
        boleto = CreateCheckoutBoletoPaymentRequest.from_dictionary(dictionary.get('boleto')) if 'boleto' in dictionary.keys() else APIHelper.SKIP
        customer_editable = dictionary.get("customer_editable") if "customer_editable" in dictionary.keys() else APIHelper.SKIP
        expires_in = dictionary.get("expires_in") if dictionary.get("expires_in") else APIHelper.SKIP
        bank_transfer = CreateCheckoutBankTransferRequest.from_dictionary(dictionary.get('bank_transfer')) if 'bank_transfer' in dictionary.keys() else APIHelper.SKIP
        pix = CreateCheckoutPixPaymentRequest.from_dictionary(dictionary.get('pix')) if 'pix' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(accepted_payment_methods,
                   accepted_multi_payment_methods,
                   success_url,
                   skip_checkout_success_page,
                   billing_address_editable,
                   billing_address,
                   accepted_brands,
                   default_payment_method,
                   gateway_affiliation_id,
                   credit_card,
                   debit_card,
                   boleto,
                   customer_editable,
                   expires_in,
                   bank_transfer,
                   pix)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'accepted_payment_methods={self.accepted_payment_methods!r}, '
                f'accepted_multi_payment_methods={self.accepted_multi_payment_methods!r}, '
                f'success_url={self.success_url!r}, '
                f'default_payment_method={(self.default_payment_method if hasattr(self, "default_payment_method") else None)!r}, '
                f'gateway_affiliation_id={(self.gateway_affiliation_id if hasattr(self, "gateway_affiliation_id") else None)!r}, '
                f'credit_card={(self.credit_card if hasattr(self, "credit_card") else None)!r}, '
                f'debit_card={(self.debit_card if hasattr(self, "debit_card") else None)!r}, '
                f'boleto={(self.boleto if hasattr(self, "boleto") else None)!r}, '
                f'customer_editable={(self.customer_editable if hasattr(self, "customer_editable") else None)!r}, '
                f'expires_in={(self.expires_in if hasattr(self, "expires_in") else None)!r}, '
                f'skip_checkout_success_page={self.skip_checkout_success_page!r}, '
                f'billing_address_editable={self.billing_address_editable!r}, '
                f'billing_address={self.billing_address!r}, '
                f'bank_transfer={(self.bank_transfer if hasattr(self, "bank_transfer") else None)!r}, '
                f'accepted_brands={self.accepted_brands!r}, '
                f'pix={(self.pix if hasattr(self, "pix") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'accepted_payment_methods={self.accepted_payment_methods!s}, '
                f'accepted_multi_payment_methods={self.accepted_multi_payment_methods!s}, '
                f'success_url={self.success_url!s}, '
                f'default_payment_method={(self.default_payment_method if hasattr(self, "default_payment_method") else None)!s}, '
                f'gateway_affiliation_id={(self.gateway_affiliation_id if hasattr(self, "gateway_affiliation_id") else None)!s}, '
                f'credit_card={(self.credit_card if hasattr(self, "credit_card") else None)!s}, '
                f'debit_card={(self.debit_card if hasattr(self, "debit_card") else None)!s}, '
                f'boleto={(self.boleto if hasattr(self, "boleto") else None)!s}, '
                f'customer_editable={(self.customer_editable if hasattr(self, "customer_editable") else None)!s}, '
                f'expires_in={(self.expires_in if hasattr(self, "expires_in") else None)!s}, '
                f'skip_checkout_success_page={self.skip_checkout_success_page!s}, '
                f'billing_address_editable={self.billing_address_editable!s}, '
                f'billing_address={self.billing_address!s}, '
                f'bank_transfer={(self.bank_transfer if hasattr(self, "bank_transfer") else None)!s}, '
                f'accepted_brands={self.accepted_brands!s}, '
                f'pix={(self.pix if hasattr(self, "pix") else None)!s})')
