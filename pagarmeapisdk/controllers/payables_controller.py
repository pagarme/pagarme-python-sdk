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
from pagarmeapisdk.models.list_payables_response import ListPayablesResponse
from pagarmeapisdk.models.get_payable_response import GetPayableResponse


class PayablesController(BaseController):

    """A Controller to access Endpoints in the pagarmeapisdk API."""
    def __init__(self, config):
        super(PayablesController, self).__init__(config)

    def get_payables(self,
                     mtype=None,
                     split_id=None,
                     bulk_anticipation_id=None,
                     installment=None,
                     status=None,
                     recipient_id=None,
                     amount=None,
                     charge_id=None,
                     payment_date_until=None,
                     payment_date_since=None,
                     updated_until=None,
                     updated_since=None,
                     created_until=None,
                     created_since=None,
                     liquidation_arrangement_id=None,
                     page=None,
                     size=None,
                     gateway_id=None):
        """Does a GET request to /payables.

        TODO: type endpoint description here.

        Args:
            mtype (str, optional): TODO: type description here.
            split_id (str, optional): TODO: type description here.
            bulk_anticipation_id (str, optional): TODO: type description
                here.
            installment (int, optional): TODO: type description here.
            status (str, optional): TODO: type description here.
            recipient_id (str, optional): TODO: type description here.
            amount (int, optional): TODO: type description here.
            charge_id (str, optional): TODO: type description here.
            payment_date_until (str, optional): TODO: type description here.
            payment_date_since (datetime, optional): TODO: type description
                here.
            updated_until (datetime, optional): TODO: type description here.
            updated_since (datetime, optional): TODO: type description here.
            created_until (datetime, optional): TODO: type description here.
            created_since (datetime, optional): TODO: type description here.
            liquidation_arrangement_id (str, optional): TODO: type description
                here.
            page (int, optional): TODO: type description here.
            size (int, optional): TODO: type description here.
            gateway_id (long|int, optional): TODO: type description here.

        Returns:
            ListPayablesResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/payables')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('type')
                         .value(mtype))
            .query_param(Parameter()
                         .key('split_id')
                         .value(split_id))
            .query_param(Parameter()
                         .key('bulk_anticipation_id')
                         .value(bulk_anticipation_id))
            .query_param(Parameter()
                         .key('installment')
                         .value(installment))
            .query_param(Parameter()
                         .key('status')
                         .value(status))
            .query_param(Parameter()
                         .key('recipient_id')
                         .value(recipient_id))
            .query_param(Parameter()
                         .key('amount')
                         .value(amount))
            .query_param(Parameter()
                         .key('charge_id')
                         .value(charge_id))
            .query_param(Parameter()
                         .key('payment_date_until')
                         .value(payment_date_until))
            .query_param(Parameter()
                         .key('payment_date_since')
                         .value(APIHelper.when_defined(APIHelper.RFC3339DateTime, payment_date_since)))
            .query_param(Parameter()
                         .key('updated_until')
                         .value(APIHelper.when_defined(APIHelper.RFC3339DateTime, updated_until)))
            .query_param(Parameter()
                         .key('updated_since')
                         .value(APIHelper.when_defined(APIHelper.RFC3339DateTime, updated_since)))
            .query_param(Parameter()
                         .key('created_until')
                         .value(APIHelper.when_defined(APIHelper.RFC3339DateTime, created_until)))
            .query_param(Parameter()
                         .key('created_since')
                         .value(APIHelper.when_defined(APIHelper.RFC3339DateTime, created_since)))
            .query_param(Parameter()
                         .key('liquidation_arrangement_id')
                         .value(liquidation_arrangement_id))
            .query_param(Parameter()
                         .key('page')
                         .value(page))
            .query_param(Parameter()
                         .key('size')
                         .value(size))
            .query_param(Parameter()
                         .key('gateway_id')
                         .value(gateway_id))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('httpBasic'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ListPayablesResponse.from_dictionary)
        ).execute()

    def get_payable_by_id(self,
                          id):
        """Does a GET request to /payables/{id}.

        TODO: type endpoint description here.

        Args:
            id (long|int): TODO: type description here.

        Returns:
            GetPayableResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/payables/{id}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('id')
                            .value(id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('httpBasic'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(GetPayableResponse.from_dictionary)
        ).execute()
