# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class PixAdditionalInformation(object):

    """Implementation of the 'PixAdditionalInformation' model.

    Pix Additional Information

    Attributes:
        name (string): TODO: type description here.
        value (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'Name',
        "value": 'Value'
    }

    def __init__(self,
                 name=None,
                 value=None):
        """Constructor for the PixAdditionalInformation class"""

        # Initialize members of the class
        self.name = name 
        self.value = value 

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

        name = dictionary.get("Name") if dictionary.get("Name") else None
        value = dictionary.get("Value") if dictionary.get("Value") else None
        # Return an object of this model
        return cls(name,
                   value)
