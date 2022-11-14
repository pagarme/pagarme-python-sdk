# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class GetUsageReportResponse(object):

    """Implementation of the 'GetUsageReportResponse' model.

    TODO: type model description here.

    Attributes:
        url (string): TODO: type description here.
        usage_report_url (string): TODO: type description here.
        grouped_report_url (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "url": 'url',
        "usage_report_url": 'usage_report_url',
        "grouped_report_url": 'grouped_report_url'
    }

    def __init__(self,
                 url=None,
                 usage_report_url=None,
                 grouped_report_url=None):
        """Constructor for the GetUsageReportResponse class"""

        # Initialize members of the class
        self.url = url 
        self.usage_report_url = usage_report_url 
        self.grouped_report_url = grouped_report_url 

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

        url = dictionary.get("url") if dictionary.get("url") else None
        usage_report_url = dictionary.get("usage_report_url") if dictionary.get("usage_report_url") else None
        grouped_report_url = dictionary.get("grouped_report_url") if dictionary.get("grouped_report_url") else None
        # Return an object of this model
        return cls(url,
                   usage_report_url,
                   grouped_report_url)
