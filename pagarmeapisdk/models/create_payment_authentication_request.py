# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.models.create_three_d_secure_request import CreateThreeDSecureRequest


class CreatePaymentAuthenticationRequest(object):

    """Implementation of the 'CreatePaymentAuthenticationRequest' model.

    The payment authentication request

    Attributes:
        mtype (str): The Authentication type
        threed_secure (CreateThreeDSecureRequest): The 3D-S authentication
            object

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mtype": 'type',
        "threed_secure": 'threed_secure'
    }

    def __init__(self,
                 mtype=None,
                 threed_secure=None):
        """Constructor for the CreatePaymentAuthenticationRequest class"""

        # Initialize members of the class
        self.mtype = mtype 
        self.threed_secure = threed_secure 

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
        mtype = dictionary.get("type") if dictionary.get("type") else None
        threed_secure = CreateThreeDSecureRequest.from_dictionary(dictionary.get('threed_secure')) if dictionary.get('threed_secure') else None
        # Return an object of this model
        return cls(mtype,
                   threed_secure)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'mtype={self.mtype!r}, '
                f'threed_secure={self.threed_secure!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'mtype={self.mtype!s}, '
                f'threed_secure={self.threed_secure!s})')
