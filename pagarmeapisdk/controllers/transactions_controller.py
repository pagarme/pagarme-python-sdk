# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from pagarmeapisdk.api_helper import APIHelper
from pagarmeapisdk.configuration import Server
from pagarmeapisdk.controllers.base_controller import BaseController
from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter
from pagarmeapisdk.http.http_method_enum import HttpMethodEnum
from apimatic_core.authentication.multiple.single_auth import Single
from pagarmeapisdk.models.get_transaction_response import GetTransactionResponse


class TransactionsController(BaseController):

    """A Controller to access Endpoints in the pagarmeapisdk API."""
    def __init__(self, config):
        super(TransactionsController, self).__init__(config)

    def get_transaction(self,
                        transaction_id):
        """Does a GET request to /transactions/{transaction_id}.

        Args:
            transaction_id (str): The request template parameter.

        Returns:
            GetTransactionResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/transactions/{transaction_id}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('transaction_id')
                            .value(transaction_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('httpBasic'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(GetTransactionResponse.from_dictionary)
        ).execute()
