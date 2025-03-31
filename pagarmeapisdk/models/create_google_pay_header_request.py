# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class CreateGooglePayHeaderRequest(object):

    """Implementation of the 'CreateGooglePayHeaderRequest' model.

    The GooglePay header request

    Attributes:
        ephemeral_public_key (str): X.509 encoded key bytes, Base64 encoded as
            a string

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "ephemeral_public_key": 'ephemeral_public_key'
    }

    def __init__(self,
                 ephemeral_public_key=None):
        """Constructor for the CreateGooglePayHeaderRequest class"""

        # Initialize members of the class
        self.ephemeral_public_key = ephemeral_public_key 

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
        ephemeral_public_key = dictionary.get("ephemeral_public_key") if dictionary.get("ephemeral_public_key") else None
        # Return an object of this model
        return cls(ephemeral_public_key)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'ephemeral_public_key={self.ephemeral_public_key!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'ephemeral_public_key={self.ephemeral_public_key!s})')
