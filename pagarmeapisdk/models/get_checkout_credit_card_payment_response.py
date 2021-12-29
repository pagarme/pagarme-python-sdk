# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.models.get_checkout_card_installment_options_response import GetCheckoutCardInstallmentOptionsResponse
from pagarmeapisdk.models.get_payment_authentication_response import GetPaymentAuthenticationResponse


class GetCheckoutCreditCardPaymentResponse(object):

    """Implementation of the 'GetCheckoutCreditCardPaymentResponse' model.

    TODO: type model description here.

    Attributes:
        statement_descriptor (string): Descrição na fatura
        installments (list of GetCheckoutCardInstallmentOptionsResponse):
            Parcelas
        authentication (GetPaymentAuthenticationResponse): Payment
            Authentication response

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "statement_descriptor": 'statementDescriptor',
        "installments": 'installments',
        "authentication": 'authentication'
    }

    def __init__(self,
                 statement_descriptor=None,
                 installments=None,
                 authentication=None):
        """Constructor for the GetCheckoutCreditCardPaymentResponse class"""

        # Initialize members of the class
        self.statement_descriptor = statement_descriptor
        self.installments = installments
        self.authentication = authentication

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
        statement_descriptor = dictionary.get('statementDescriptor')
        installments = None
        if dictionary.get('installments') is not None:
            installments = [GetCheckoutCardInstallmentOptionsResponse.from_dictionary(x) for x in dictionary.get('installments')]
        authentication = GetPaymentAuthenticationResponse.from_dictionary(dictionary.get('authentication')) if dictionary.get('authentication') else None

        # Return an object of this model
        return cls(statement_descriptor,
                   installments,
                   authentication)