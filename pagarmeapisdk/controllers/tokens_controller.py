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
from pagarmeapisdk.models.get_token_response import GetTokenResponse


class TokensController(BaseController):

    """A Controller to access Endpoints in the pagarmeapisdk API."""
    def __init__(self, config):
        super(TokensController, self).__init__(config)

    def create_token(self,
                     public_key,
                     request,
                     idempotency_key=None):
        """Does a POST request to /tokens?appId={public_key}.

        TODO: type endpoint description here.

        Args:
            public_key (string): Public key
            request (CreateTokenRequest): Request for creating a token
            idempotency_key (string, optional): TODO: type description here.

        Returns:
            GetTokenResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/tokens?appId={public_key}')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('public_key')
                            .value(public_key)
                            .should_encode(True))
            .body_param(Parameter()
                        .value(request))
            .header_param(Parameter()
                          .key('idempotency-key')
                          .value(idempotency_key))
            .header_param(Parameter()
                          .key('content-type')
                          .value('application/json; charset=utf-8'))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(GetTokenResponse.from_dictionary)
        ).execute()

    def get_token(self,
                  id,
                  public_key):
        """Does a GET request to /tokens/{id}?appId={public_key}.

        Gets a token from its id

        Args:
            id (string): Token id
            public_key (string): Public key

        Returns:
            GetTokenResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/tokens/{id}?appId={public_key}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('id')
                            .value(id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('public_key')
                            .value(public_key)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(GetTokenResponse.from_dictionary)
        ).execute()
