# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.api_helper import APIHelper
from pagarmeapisdk.models.get_recipient_response import GetRecipientResponse


class GetAnticipationResponse(object):

    """Implementation of the 'GetAnticipationResponse' model.

    Anticipation

    Attributes:
        id (str): Id
        requested_amount (int): Requested amount
        approved_amount (int): Approved amount
        recipient (GetRecipientResponse): Recipient
        pgid (str): Anticipation id on the gateway
        created_at (datetime): Creation date
        updated_at (datetime): Last update date
        payment_date (datetime): Payment date
        status (str): Status
        timeframe (str): Timeframe

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "requested_amount": 'requested_amount',
        "approved_amount": 'approved_amount',
        "recipient": 'recipient',
        "pgid": 'pgid',
        "created_at": 'created_at',
        "updated_at": 'updated_at',
        "payment_date": 'payment_date',
        "status": 'status',
        "timeframe": 'timeframe'
    }

    _optionals = [
        'id',
        'requested_amount',
        'approved_amount',
        'recipient',
        'pgid',
        'created_at',
        'updated_at',
        'payment_date',
        'status',
        'timeframe',
    ]

    _nullables = [
        'id',
        'requested_amount',
        'approved_amount',
        'recipient',
        'pgid',
        'created_at',
        'updated_at',
        'payment_date',
        'status',
        'timeframe',
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 requested_amount=APIHelper.SKIP,
                 approved_amount=APIHelper.SKIP,
                 recipient=APIHelper.SKIP,
                 pgid=APIHelper.SKIP,
                 created_at=APIHelper.SKIP,
                 updated_at=APIHelper.SKIP,
                 payment_date=APIHelper.SKIP,
                 status=APIHelper.SKIP,
                 timeframe=APIHelper.SKIP):
        """Constructor for the GetAnticipationResponse class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        if requested_amount is not APIHelper.SKIP:
            self.requested_amount = requested_amount 
        if approved_amount is not APIHelper.SKIP:
            self.approved_amount = approved_amount 
        if recipient is not APIHelper.SKIP:
            self.recipient = recipient 
        if pgid is not APIHelper.SKIP:
            self.pgid = pgid 
        if created_at is not APIHelper.SKIP:
            self.created_at = APIHelper.apply_datetime_converter(created_at, APIHelper.RFC3339DateTime) if created_at else None 
        if updated_at is not APIHelper.SKIP:
            self.updated_at = APIHelper.apply_datetime_converter(updated_at, APIHelper.RFC3339DateTime) if updated_at else None 
        if payment_date is not APIHelper.SKIP:
            self.payment_date = APIHelper.apply_datetime_converter(payment_date, APIHelper.RFC3339DateTime) if payment_date else None 
        if status is not APIHelper.SKIP:
            self.status = status 
        if timeframe is not APIHelper.SKIP:
            self.timeframe = timeframe 

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
        id = dictionary.get("id") if "id" in dictionary.keys() else APIHelper.SKIP
        requested_amount = dictionary.get("requested_amount") if "requested_amount" in dictionary.keys() else APIHelper.SKIP
        approved_amount = dictionary.get("approved_amount") if "approved_amount" in dictionary.keys() else APIHelper.SKIP
        if 'recipient' in dictionary.keys():
            recipient = GetRecipientResponse.from_dictionary(dictionary.get('recipient')) if dictionary.get('recipient') else None
        else:
            recipient = APIHelper.SKIP
        pgid = dictionary.get("pgid") if "pgid" in dictionary.keys() else APIHelper.SKIP
        if 'created_at' in dictionary.keys():
            created_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("created_at")).datetime if dictionary.get("created_at") else None
        else:
            created_at = APIHelper.SKIP
        if 'updated_at' in dictionary.keys():
            updated_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("updated_at")).datetime if dictionary.get("updated_at") else None
        else:
            updated_at = APIHelper.SKIP
        if 'payment_date' in dictionary.keys():
            payment_date = APIHelper.RFC3339DateTime.from_value(dictionary.get("payment_date")).datetime if dictionary.get("payment_date") else None
        else:
            payment_date = APIHelper.SKIP
        status = dictionary.get("status") if "status" in dictionary.keys() else APIHelper.SKIP
        timeframe = dictionary.get("timeframe") if "timeframe" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(id,
                   requested_amount,
                   approved_amount,
                   recipient,
                   pgid,
                   created_at,
                   updated_at,
                   payment_date,
                   status,
                   timeframe)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'id={(self.id if hasattr(self, "id") else None)!r}, '
                f'requested_amount={(self.requested_amount if hasattr(self, "requested_amount") else None)!r}, '
                f'approved_amount={(self.approved_amount if hasattr(self, "approved_amount") else None)!r}, '
                f'recipient={(self.recipient if hasattr(self, "recipient") else None)!r}, '
                f'pgid={(self.pgid if hasattr(self, "pgid") else None)!r}, '
                f'created_at={(self.created_at if hasattr(self, "created_at") else None)!r}, '
                f'updated_at={(self.updated_at if hasattr(self, "updated_at") else None)!r}, '
                f'payment_date={(self.payment_date if hasattr(self, "payment_date") else None)!r}, '
                f'status={(self.status if hasattr(self, "status") else None)!r}, '
                f'timeframe={(self.timeframe if hasattr(self, "timeframe") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'id={(self.id if hasattr(self, "id") else None)!s}, '
                f'requested_amount={(self.requested_amount if hasattr(self, "requested_amount") else None)!s}, '
                f'approved_amount={(self.approved_amount if hasattr(self, "approved_amount") else None)!s}, '
                f'recipient={(self.recipient if hasattr(self, "recipient") else None)!s}, '
                f'pgid={(self.pgid if hasattr(self, "pgid") else None)!s}, '
                f'created_at={(self.created_at if hasattr(self, "created_at") else None)!s}, '
                f'updated_at={(self.updated_at if hasattr(self, "updated_at") else None)!s}, '
                f'payment_date={(self.payment_date if hasattr(self, "payment_date") else None)!s}, '
                f'status={(self.status if hasattr(self, "status") else None)!s}, '
                f'timeframe={(self.timeframe if hasattr(self, "timeframe") else None)!s})')
