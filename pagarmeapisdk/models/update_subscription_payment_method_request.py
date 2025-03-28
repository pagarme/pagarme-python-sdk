# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.api_helper import APIHelper
from pagarmeapisdk.models.create_card_request import CreateCardRequest
from pagarmeapisdk.models.create_subscription_boleto_request import CreateSubscriptionBoletoRequest


class UpdateSubscriptionPaymentMethodRequest(object):

    """Implementation of the 'UpdateSubscriptionPaymentMethodRequest' model.

    Request for updating a subscription's payment method

    Attributes:
        payment_method (str): The new payment method
        card_id (str): Card id
        card (CreateCardRequest): Card data
        card_token (str): The Card Token
        boleto (CreateSubscriptionBoletoRequest): Information about fines and
            interest on the "boleto" used from payment
        indirect_acceptor (str): Business model identifier

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "payment_method": 'payment_method',
        "card_id": 'card_id',
        "card": 'card',
        "card_token": 'card_token',
        "boleto": 'boleto',
        "indirect_acceptor": 'indirect_acceptor'
    }

    _optionals = [
        'card_token',
        'boleto',
        'indirect_acceptor',
    ]

    _nullables = [
        'indirect_acceptor',
    ]

    def __init__(self,
                 payment_method=None,
                 card_id=None,
                 card=None,
                 card_token=APIHelper.SKIP,
                 boleto=APIHelper.SKIP,
                 indirect_acceptor=APIHelper.SKIP):
        """Constructor for the UpdateSubscriptionPaymentMethodRequest class"""

        # Initialize members of the class
        self.payment_method = payment_method 
        self.card_id = card_id 
        self.card = card 
        if card_token is not APIHelper.SKIP:
            self.card_token = card_token 
        if boleto is not APIHelper.SKIP:
            self.boleto = boleto 
        if indirect_acceptor is not APIHelper.SKIP:
            self.indirect_acceptor = indirect_acceptor 

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
        payment_method = dictionary.get("payment_method") if dictionary.get("payment_method") else None
        card_id = dictionary.get("card_id") if dictionary.get("card_id") else None
        card = CreateCardRequest.from_dictionary(dictionary.get('card')) if dictionary.get('card') else None
        card_token = dictionary.get("card_token") if dictionary.get("card_token") else APIHelper.SKIP
        boleto = CreateSubscriptionBoletoRequest.from_dictionary(dictionary.get('boleto')) if 'boleto' in dictionary.keys() else APIHelper.SKIP
        indirect_acceptor = dictionary.get("indirect_acceptor") if "indirect_acceptor" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(payment_method,
                   card_id,
                   card,
                   card_token,
                   boleto,
                   indirect_acceptor)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'payment_method={self.payment_method!r}, '
                f'card_id={self.card_id!r}, '
                f'card={self.card!r}, '
                f'card_token={(self.card_token if hasattr(self, "card_token") else None)!r}, '
                f'boleto={(self.boleto if hasattr(self, "boleto") else None)!r}, '
                f'indirect_acceptor={(self.indirect_acceptor if hasattr(self, "indirect_acceptor") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'payment_method={self.payment_method!s}, '
                f'card_id={self.card_id!s}, '
                f'card={self.card!s}, '
                f'card_token={(self.card_token if hasattr(self, "card_token") else None)!s}, '
                f'boleto={(self.boleto if hasattr(self, "boleto") else None)!s}, '
                f'indirect_acceptor={(self.indirect_acceptor if hasattr(self, "indirect_acceptor") else None)!s})')
