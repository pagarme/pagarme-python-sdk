# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.models.create_card_payment_contactless_request import CreateCardPaymentContactlessRequest
from pagarmeapisdk.models.create_card_request import CreateCardRequest
from pagarmeapisdk.models.create_payment_authentication_request import CreatePaymentAuthenticationRequest


class CreateCreditCardPaymentRequest(object):

    """Implementation of the 'CreateCreditCardPaymentRequest' model.

    The settings for creating a credit card payment

    Attributes:
        installments (int): Number of installments
        statement_descriptor (string): The text that will be shown on the
            credit card's statement
        card (CreateCardRequest): Credit card data
        card_id (string): The credit card id
        card_token (string): TODO: type description here.
        recurrence (bool): Indicates a recurrence
        capture (bool): Indicates if the operation should be only
            authorization or auth and capture.
        extended_limit_enabled (bool): Indicates whether the extended label
            (private label) is enabled
        extended_limit_code (string): Extended Limit Code
        merchant_category_code (long|int): Customer business segment code
        authentication (CreatePaymentAuthenticationRequest): The payment
            authentication request
        contactless (CreateCardPaymentContactlessRequest): The Credit card
            payment contactless request
        auto_recovery (bool): Indicates whether a particular payment will
            enter the offline retry flow
        operation_type (string): AuthOnly, AuthAndCapture, PreAuth

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "installments": 'installments',
        "statement_descriptor": 'statement_descriptor',
        "card": 'card',
        "card_id": 'card_id',
        "card_token": 'card_token',
        "recurrence": 'recurrence',
        "capture": 'capture',
        "extended_limit_enabled": 'extended_limit_enabled',
        "extended_limit_code": 'extended_limit_code',
        "merchant_category_code": 'merchant_category_code',
        "authentication": 'authentication',
        "contactless": 'contactless',
        "auto_recovery": 'auto_recovery',
        "operation_type": 'operation_type'
    }

    def __init__(self,
                 installments=1,
                 statement_descriptor=None,
                 card=None,
                 card_id=None,
                 card_token=None,
                 recurrence=None,
                 capture=True,
                 extended_limit_enabled=None,
                 extended_limit_code=None,
                 merchant_category_code=None,
                 authentication=None,
                 contactless=None,
                 auto_recovery=None,
                 operation_type=None):
        """Constructor for the CreateCreditCardPaymentRequest class"""

        # Initialize members of the class
        self.installments = installments
        self.statement_descriptor = statement_descriptor
        self.card = card
        self.card_id = card_id
        self.card_token = card_token
        self.recurrence = recurrence
        self.capture = capture
        self.extended_limit_enabled = extended_limit_enabled
        self.extended_limit_code = extended_limit_code
        self.merchant_category_code = merchant_category_code
        self.authentication = authentication
        self.contactless = contactless
        self.auto_recovery = auto_recovery
        self.operation_type = operation_type

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
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        installments = dictionary.get("installments") if dictionary.get("installments") else 1
        statement_descriptor = dictionary.get('statement_descriptor')
        card = CreateCardRequest.from_dictionary(dictionary.get('card')) if dictionary.get('card') else None
        card_id = dictionary.get('card_id')
        card_token = dictionary.get('card_token')
        recurrence = dictionary.get('recurrence')
        capture = dictionary.get("capture") if dictionary.get("capture") else True
        extended_limit_enabled = dictionary.get('extended_limit_enabled')
        extended_limit_code = dictionary.get('extended_limit_code')
        merchant_category_code = dictionary.get('merchant_category_code')
        authentication = CreatePaymentAuthenticationRequest.from_dictionary(dictionary.get('authentication')) if dictionary.get('authentication') else None
        contactless = CreateCardPaymentContactlessRequest.from_dictionary(dictionary.get('contactless')) if dictionary.get('contactless') else None
        auto_recovery = dictionary.get('auto_recovery')
        operation_type = dictionary.get('operation_type')

        # Return an object of this model
        return cls(installments,
                   statement_descriptor,
                   card,
                   card_id,
                   card_token,
                   recurrence,
                   capture,
                   extended_limit_enabled,
                   extended_limit_code,
                   merchant_category_code,
                   authentication,
                   contactless,
                   auto_recovery,
                   operation_type)