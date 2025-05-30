# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.api_helper import APIHelper


class GetAutomaticAnticipationResponse(object):

    """Implementation of the 'GetAutomaticAnticipationResponse' model.

    Attributes:
        enabled (bool): The model property of type bool.
        mtype (str): The model property of type str.
        volume_percentage (int): The model property of type int.
        delay (int): The model property of type int.
        days (List[int]): The model property of type List[int].

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "enabled": 'enabled',
        "mtype": 'type',
        "volume_percentage": 'volume_percentage',
        "delay": 'delay',
        "days": 'days'
    }

    _optionals = [
        'enabled',
        'mtype',
        'volume_percentage',
        'delay',
        'days',
    ]

    _nullables = [
        'enabled',
        'mtype',
        'volume_percentage',
        'delay',
        'days',
    ]

    def __init__(self,
                 enabled=APIHelper.SKIP,
                 mtype=APIHelper.SKIP,
                 volume_percentage=APIHelper.SKIP,
                 delay=APIHelper.SKIP,
                 days=APIHelper.SKIP):
        """Constructor for the GetAutomaticAnticipationResponse class"""

        # Initialize members of the class
        if enabled is not APIHelper.SKIP:
            self.enabled = enabled 
        if mtype is not APIHelper.SKIP:
            self.mtype = mtype 
        if volume_percentage is not APIHelper.SKIP:
            self.volume_percentage = volume_percentage 
        if delay is not APIHelper.SKIP:
            self.delay = delay 
        if days is not APIHelper.SKIP:
            self.days = days 

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
        enabled = dictionary.get("enabled") if "enabled" in dictionary.keys() else APIHelper.SKIP
        mtype = dictionary.get("type") if "type" in dictionary.keys() else APIHelper.SKIP
        volume_percentage = dictionary.get("volume_percentage") if "volume_percentage" in dictionary.keys() else APIHelper.SKIP
        delay = dictionary.get("delay") if "delay" in dictionary.keys() else APIHelper.SKIP
        days = dictionary.get("days") if "days" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(enabled,
                   mtype,
                   volume_percentage,
                   delay,
                   days)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'enabled={(self.enabled if hasattr(self, "enabled") else None)!r}, '
                f'mtype={(self.mtype if hasattr(self, "mtype") else None)!r}, '
                f'volume_percentage={(self.volume_percentage if hasattr(self, "volume_percentage") else None)!r}, '
                f'delay={(self.delay if hasattr(self, "delay") else None)!r}, '
                f'days={(self.days if hasattr(self, "days") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'enabled={(self.enabled if hasattr(self, "enabled") else None)!s}, '
                f'mtype={(self.mtype if hasattr(self, "mtype") else None)!s}, '
                f'volume_percentage={(self.volume_percentage if hasattr(self, "volume_percentage") else None)!s}, '
                f'delay={(self.delay if hasattr(self, "delay") else None)!s}, '
                f'days={(self.days if hasattr(self, "days") else None)!s})')
