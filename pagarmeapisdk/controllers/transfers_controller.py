# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from pagarmeapisdk.api_helper import APIHelper
from pagarmeapisdk.configuration import Server
from pagarmeapisdk.controllers.base_controller import BaseController
from pagarmeapisdk.http.auth.basic_auth import BasicAuth
from pagarmeapisdk.models.get_transfer import GetTransfer
from pagarmeapisdk.models.list_transfers import ListTransfers


class TransfersController(BaseController):

    """A Controller to access Endpoints in the pagarmeapisdk API."""

    def __init__(self, config, call_back=None):
        super(TransfersController, self).__init__(config, call_back)

    def get_transfer_by_id(self,
                           transfer_id):
        """Does a GET request to /transfers/{transfer_id}.

        TODO: type endpoint description here.

        Args:
            transfer_id (string): TODO: type description here.

        Returns:
            GetTransfer: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/transfers/{transfer_id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'transfer_id': {'value': transfer_id, 'encode': True}
        })
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.get(_query_url, headers=_headers)
        BasicAuth.apply(self.config, _request)
        _response = self.execute_request(_request)
        self.validate_response(_response)

        decoded = APIHelper.json_deserialize(_response.text, GetTransfer.from_dictionary)

        return decoded

    def create_transfer(self,
                        request):
        """Does a POST request to /transfers/recipients.

        TODO: type endpoint description here.

        Args:
            request (CreateTransfer): TODO: type description here.

        Returns:
            GetTransfer: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/transfers/recipients'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.config.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(request))
        BasicAuth.apply(self.config, _request)
        _response = self.execute_request(_request)
        self.validate_response(_response)

        decoded = APIHelper.json_deserialize(_response.text, GetTransfer.from_dictionary)

        return decoded

    def get_transfers(self):
        """Does a GET request to /transfers.

        Gets all transfers

        Returns:
            ListTransfers: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/transfers'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.get(_query_url, headers=_headers)
        BasicAuth.apply(self.config, _request)
        _response = self.execute_request(_request)
        self.validate_response(_response)

        decoded = APIHelper.json_deserialize(_response.text, ListTransfers.from_dictionary)

        return decoded