# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class UpdateRecipientCodeRequest(object):

    """Implementation of the 'UpdateRecipientCodeRequest' model.

    Update code for a recipient

    Attributes:
        code (str): Code

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "code": 'code'
    }

    def __init__(self,
                 code=None):
        """Constructor for the UpdateRecipientCodeRequest class"""

        # Initialize members of the class
        self.code = code 

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
        code = dictionary.get("code") if dictionary.get("code") else None
        # Return an object of this model
        return cls(code)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'code={self.code!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'code={self.code!s})')
