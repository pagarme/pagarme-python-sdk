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
from pagarmeapisdk.models.get_charge_response import GetChargeResponse
from pagarmeapisdk.models.list_charge_transactions_response import ListChargeTransactionsResponse
from pagarmeapisdk.models.list_charges_response import ListChargesResponse
from pagarmeapisdk.models.get_charges_summary_response import GetChargesSummaryResponse


class ChargesController(BaseController):

    """A Controller to access Endpoints in the pagarmeapisdk API."""
    def __init__(self, config):
        super(ChargesController, self).__init__(config)

    def update_charge_metadata(self,
                               charge_id,
                               request,
                               idempotency_key=None):
        """Does a PATCH request to /Charges/{charge_id}/metadata.

        Updates the metadata from a charge

        Args:
            charge_id (str): The charge id
            request (UpdateMetadataRequest): Request for updating the charge
                metadata
            idempotency_key (str, optional): TODO: type description here.

        Returns:
            GetChargeResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/Charges/{charge_id}/metadata')
            .http_method(HttpMethodEnum.PATCH)
            .template_param(Parameter()
                            .key('charge_id')
                            .value(charge_id)
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
            .auth(Single('httpBasic'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(GetChargeResponse.from_dictionary)
        ).execute()

    def update_charge_payment_method(self,
                                     charge_id,
                                     request,
                                     idempotency_key=None):
        """Does a PATCH request to /charges/{charge_id}/payment-method.

        Updates a charge's payment method

        Args:
            charge_id (str): Charge id
            request (UpdateChargePaymentMethodRequest): Request for updating
                the payment method from a charge
            idempotency_key (str, optional): TODO: type description here.

        Returns:
            GetChargeResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/charges/{charge_id}/payment-method')
            .http_method(HttpMethodEnum.PATCH)
            .template_param(Parameter()
                            .key('charge_id')
                            .value(charge_id)
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
            .auth(Single('httpBasic'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(GetChargeResponse.from_dictionary)
        ).execute()

    def get_charge_transactions(self,
                                charge_id,
                                page=None,
                                size=None):
        """Does a GET request to /charges/{charge_id}/transactions.

        TODO: type endpoint description here.

        Args:
            charge_id (str): Charge Id
            page (int, optional): Page number
            size (int, optional): Page size

        Returns:
            ListChargeTransactionsResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/charges/{charge_id}/transactions')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('charge_id')
                            .value(charge_id)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('page')
                         .value(page))
            .query_param(Parameter()
                         .key('size')
                         .value(size))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('httpBasic'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ListChargeTransactionsResponse.from_dictionary)
        ).execute()

    def update_charge_due_date(self,
                               charge_id,
                               request,
                               idempotency_key=None):
        """Does a PATCH request to /Charges/{charge_id}/due-date.

        Updates the due date from a charge

        Args:
            charge_id (str): Charge Id
            request (UpdateChargeDueDateRequest): Request for updating the due
                date
            idempotency_key (str, optional): TODO: type description here.

        Returns:
            GetChargeResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/Charges/{charge_id}/due-date')
            .http_method(HttpMethodEnum.PATCH)
            .template_param(Parameter()
                            .key('charge_id')
                            .value(charge_id)
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
            .auth(Single('httpBasic'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(GetChargeResponse.from_dictionary)
        ).execute()

    def get_charges(self,
                    page=None,
                    size=None,
                    code=None,
                    status=None,
                    payment_method=None,
                    customer_id=None,
                    order_id=None,
                    created_since=None,
                    created_until=None):
        """Does a GET request to /charges.

        Lists all charges

        Args:
            page (int, optional): Page number
            size (int, optional): Page size
            code (str, optional): Filter for charge's code
            status (str, optional): Filter for charge's status
            payment_method (str, optional): Filter for charge's payment
                method
            customer_id (str, optional): Filter for charge's customer id
            order_id (str, optional): Filter for charge's order id
            created_since (datetime, optional): Filter for the beginning of
                the range for charge's creation
            created_until (datetime, optional): Filter for the end of the
                range for charge's creation

        Returns:
            ListChargesResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/charges')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('page')
                         .value(page))
            .query_param(Parameter()
                         .key('size')
                         .value(size))
            .query_param(Parameter()
                         .key('code')
                         .value(code))
            .query_param(Parameter()
                         .key('status')
                         .value(status))
            .query_param(Parameter()
                         .key('payment_method')
                         .value(payment_method))
            .query_param(Parameter()
                         .key('customer_id')
                         .value(customer_id))
            .query_param(Parameter()
                         .key('order_id')
                         .value(order_id))
            .query_param(Parameter()
                         .key('created_since')
                         .value(APIHelper.when_defined(APIHelper.RFC3339DateTime, created_since)))
            .query_param(Parameter()
                         .key('created_until')
                         .value(APIHelper.when_defined(APIHelper.RFC3339DateTime, created_until)))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('httpBasic'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ListChargesResponse.from_dictionary)
        ).execute()

    def capture_charge(self,
                       charge_id,
                       request=None,
                       idempotency_key=None):
        """Does a POST request to /charges/{charge_id}/capture.

        Captures a charge

        Args:
            charge_id (str): Charge id
            request (CreateCaptureChargeRequest, optional): Request for
                capturing a charge
            idempotency_key (str, optional): TODO: type description here.

        Returns:
            GetChargeResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/charges/{charge_id}/capture')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('charge_id')
                            .value(charge_id)
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
            .auth(Single('httpBasic'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(GetChargeResponse.from_dictionary)
        ).execute()

    def update_charge_card(self,
                           charge_id,
                           request,
                           idempotency_key=None):
        """Does a PATCH request to /charges/{charge_id}/card.

        Updates the card from a charge

        Args:
            charge_id (str): Charge id
            request (UpdateChargeCardRequest): Request for updating a charge's
                card
            idempotency_key (str, optional): TODO: type description here.

        Returns:
            GetChargeResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/charges/{charge_id}/card')
            .http_method(HttpMethodEnum.PATCH)
            .template_param(Parameter()
                            .key('charge_id')
                            .value(charge_id)
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
            .auth(Single('httpBasic'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(GetChargeResponse.from_dictionary)
        ).execute()

    def get_charge(self,
                   charge_id):
        """Does a GET request to /charges/{charge_id}.

        Get a charge from its id

        Args:
            charge_id (str): Charge id

        Returns:
            GetChargeResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/charges/{charge_id}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('charge_id')
                            .value(charge_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('httpBasic'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(GetChargeResponse.from_dictionary)
        ).execute()

    def get_charges_summary(self,
                            status,
                            created_since=None,
                            created_until=None):
        """Does a GET request to /charges/summary.

        TODO: type endpoint description here.

        Args:
            status (str): TODO: type description here.
            created_since (datetime, optional): TODO: type description here.
            created_until (datetime, optional): TODO: type description here.

        Returns:
            GetChargesSummaryResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/charges/summary')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('status')
                         .value(status))
            .query_param(Parameter()
                         .key('created_since')
                         .value(APIHelper.when_defined(APIHelper.RFC3339DateTime, created_since)))
            .query_param(Parameter()
                         .key('created_until')
                         .value(APIHelper.when_defined(APIHelper.RFC3339DateTime, created_until)))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('httpBasic'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(GetChargesSummaryResponse.from_dictionary)
        ).execute()

    def retry_charge(self,
                     charge_id,
                     idempotency_key=None):
        """Does a POST request to /charges/{charge_id}/retry.

        Retries a charge

        Args:
            charge_id (str): Charge id
            idempotency_key (str, optional): TODO: type description here.

        Returns:
            GetChargeResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/charges/{charge_id}/retry')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('charge_id')
                            .value(charge_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('idempotency-key')
                          .value(idempotency_key))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('httpBasic'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(GetChargeResponse.from_dictionary)
        ).execute()

    def cancel_charge(self,
                      charge_id,
                      request=None,
                      idempotency_key=None):
        """Does a DELETE request to /charges/{charge_id}.

        Cancel a charge

        Args:
            charge_id (str): Charge id
            request (CreateCancelChargeRequest, optional): Request for
                cancelling a charge
            idempotency_key (str, optional): TODO: type description here.

        Returns:
            GetChargeResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/charges/{charge_id}')
            .http_method(HttpMethodEnum.DELETE)
            .template_param(Parameter()
                            .key('charge_id')
                            .value(charge_id)
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
            .auth(Single('httpBasic'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(GetChargeResponse.from_dictionary)
        ).execute()

    def create_charge(self,
                      request,
                      idempotency_key=None):
        """Does a POST request to /Charges.

        Creates a new charge

        Args:
            request (CreateChargeRequest): Request for creating a charge
            idempotency_key (str, optional): TODO: type description here.

        Returns:
            GetChargeResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/Charges')
            .http_method(HttpMethodEnum.POST)
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
            .auth(Single('httpBasic'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(GetChargeResponse.from_dictionary)
        ).execute()

    def confirm_payment(self,
                        charge_id,
                        request=None,
                        idempotency_key=None):
        """Does a POST request to /charges/{charge_id}/confirm-payment.

        TODO: type endpoint description here.

        Args:
            charge_id (str): TODO: type description here.
            request (CreateConfirmPaymentRequest, optional): Request for
                confirm payment
            idempotency_key (str, optional): TODO: type description here.

        Returns:
            GetChargeResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/charges/{charge_id}/confirm-payment')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('charge_id')
                            .value(charge_id)
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
            .auth(Single('httpBasic'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(GetChargeResponse.from_dictionary)
        ).execute()
