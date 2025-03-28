# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.api_helper import APIHelper


class GetGatewayRecipientResponse(object):

    """Implementation of the 'GetGatewayRecipientResponse' model.

    Information about the recipient on the gateway

    Attributes:
        gateway (str): Gateway name
        status (str): Status of the recipient on the gateway
        pgid (str): Recipient id on the gateway
        created_at (str): Creation date
        updated_at (str): Last update date

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "gateway": 'gateway',
        "status": 'status',
        "pgid": 'pgid',
        "created_at": 'created_at',
        "updated_at": 'updated_at'
    }

    _optionals = [
        'gateway',
        'status',
        'pgid',
        'created_at',
        'updated_at',
    ]

    _nullables = [
        'gateway',
        'status',
        'pgid',
        'created_at',
        'updated_at',
    ]

    def __init__(self,
                 gateway=APIHelper.SKIP,
                 status=APIHelper.SKIP,
                 pgid=APIHelper.SKIP,
                 created_at=APIHelper.SKIP,
                 updated_at=APIHelper.SKIP):
        """Constructor for the GetGatewayRecipientResponse class"""

        # Initialize members of the class
        if gateway is not APIHelper.SKIP:
            self.gateway = gateway 
        if status is not APIHelper.SKIP:
            self.status = status 
        if pgid is not APIHelper.SKIP:
            self.pgid = pgid 
        if created_at is not APIHelper.SKIP:
            self.created_at = created_at 
        if updated_at is not APIHelper.SKIP:
            self.updated_at = updated_at 

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
        gateway = dictionary.get("gateway") if "gateway" in dictionary.keys() else APIHelper.SKIP
        status = dictionary.get("status") if "status" in dictionary.keys() else APIHelper.SKIP
        pgid = dictionary.get("pgid") if "pgid" in dictionary.keys() else APIHelper.SKIP
        created_at = dictionary.get("created_at") if "created_at" in dictionary.keys() else APIHelper.SKIP
        updated_at = dictionary.get("updated_at") if "updated_at" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(gateway,
                   status,
                   pgid,
                   created_at,
                   updated_at)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'gateway={(self.gateway if hasattr(self, "gateway") else None)!r}, '
                f'status={(self.status if hasattr(self, "status") else None)!r}, '
                f'pgid={(self.pgid if hasattr(self, "pgid") else None)!r}, '
                f'created_at={(self.created_at if hasattr(self, "created_at") else None)!r}, '
                f'updated_at={(self.updated_at if hasattr(self, "updated_at") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'gateway={(self.gateway if hasattr(self, "gateway") else None)!s}, '
                f'status={(self.status if hasattr(self, "status") else None)!s}, '
                f'pgid={(self.pgid if hasattr(self, "pgid") else None)!s}, '
                f'created_at={(self.created_at if hasattr(self, "created_at") else None)!s}, '
                f'updated_at={(self.updated_at if hasattr(self, "updated_at") else None)!s})')
