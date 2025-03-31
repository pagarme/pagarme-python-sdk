# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pagarmeapisdk.models.create_split_request import CreateSplitRequest


class UpdateSubscriptionSplitRequest(object):

    """Implementation of the 'UpdateSubscriptionSplitRequest' model.

    Attributes:
        enabled (bool): Defines if the split is enabled
        rules (List[CreateSplitRequest]): Split

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "enabled": 'enabled',
        "rules": 'rules'
    }

    def __init__(self,
                 enabled=None,
                 rules=None):
        """Constructor for the UpdateSubscriptionSplitRequest class"""

        # Initialize members of the class
        self.enabled = enabled 
        self.rules = rules 

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
        enabled = dictionary.get("enabled") if "enabled" in dictionary.keys() else None
        rules = None
        if dictionary.get('rules') is not None:
            rules = [CreateSplitRequest.from_dictionary(x) for x in dictionary.get('rules')]
        # Return an object of this model
        return cls(enabled,
                   rules)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'enabled={self.enabled!r}, '
                f'rules={self.rules!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'enabled={self.enabled!s}, '
                f'rules={self.rules!s})')
