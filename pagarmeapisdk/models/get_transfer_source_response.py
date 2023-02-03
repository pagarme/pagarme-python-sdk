# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.api_helper import APIHelper


class GetTransferSourceResponse(object):

    """Implementation of the 'GetTransferSourceResponse' model.

    TODO: type model description here.

    Attributes:
        source_id (string): TODO: type description here.
        mtype (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "source_id": 'source_id',
        "mtype": 'type'
    }

    _optionals = [
        'source_id',
        'mtype',
    ]

    _nullables = [
        'source_id',
        'mtype',
    ]

    def __init__(self,
                 source_id=APIHelper.SKIP,
                 mtype=APIHelper.SKIP):
        """Constructor for the GetTransferSourceResponse class"""

        # Initialize members of the class
        if source_id is not APIHelper.SKIP:
            self.source_id = source_id 
        if mtype is not APIHelper.SKIP:
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
        if dictionary is None:
            return None

        # Extract variables from the dictionary

        source_id = dictionary.get("source_id") if "source_id" in dictionary.keys() else APIHelper.SKIP
        mtype = dictionary.get("type") if "type" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(source_id,
                   mtype)
