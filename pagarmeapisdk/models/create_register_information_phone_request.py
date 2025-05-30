# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class CreateRegisterInformationPhoneRequest(object):

    """Implementation of the 'CreateRegisterInformationPhoneRequest' model.

    Register Information Phone

    Attributes:
        ddd (str): The model property of type str.
        number (str): The model property of type str.
        mtype (str): The model property of type str.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "ddd": 'ddd',
        "number": 'number',
        "mtype": 'type'
    }

    def __init__(self,
                 ddd=None,
                 number=None,
                 mtype=None):
        """Constructor for the CreateRegisterInformationPhoneRequest class"""

        # Initialize members of the class
        self.ddd = ddd 
        self.number = number 
        self.mtype = mtype 

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
        ddd = dictionary.get("ddd") if dictionary.get("ddd") else None
        number = dictionary.get("number") if dictionary.get("number") else None
        mtype = dictionary.get("type") if dictionary.get("type") else None
        # Return an object of this model
        return cls(ddd,
                   number,
                   mtype)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'ddd={self.ddd!r}, '
                f'number={self.number!r}, '
                f'mtype={self.mtype!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'ddd={self.ddd!s}, '
                f'number={self.number!s}, '
                f'mtype={self.mtype!s})')
