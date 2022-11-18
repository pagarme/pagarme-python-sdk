# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class UpdateAddressRequest(object):

    """Implementation of the 'UpdateAddressRequest' model.

    Request for updating an address

    Attributes:
        number (string): Number
        complement (string): Complement
        metadata (dict): Metadata
        line_2 (string): Line 2 for address

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "number": 'number',
        "complement": 'complement',
        "metadata": 'metadata',
        "line_2": 'line_2'
    }

    def __init__(self,
                 number=None,
                 complement=None,
                 metadata=None,
                 line_2=None):
        """Constructor for the UpdateAddressRequest class"""

        # Initialize members of the class
        self.number = number 
        self.complement = complement 
        self.metadata = metadata 
        self.line_2 = line_2 

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

        number = dictionary.get("number") if dictionary.get("number") else None
        complement = dictionary.get("complement") if dictionary.get("complement") else None
        metadata = dictionary.get("metadata") if dictionary.get("metadata") else None
        line_2 = dictionary.get("line_2") if dictionary.get("line_2") else None
        # Return an object of this model
        return cls(number,
                   complement,
                   metadata,
                   line_2)
