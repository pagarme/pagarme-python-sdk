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
from pagarmeapisdk.models.get_invoice_response import GetInvoiceResponse
from pagarmeapisdk.models.list_invoices_response import ListInvoicesResponse


class InvoicesController(BaseController):

    """A Controller to access Endpoints in the pagarmeapisdk API."""
    def __init__(self, config):
        super(InvoicesController, self).__init__(config)

    def update_invoice_metadata(self,
                                invoice_id,
                                request,
                                idempotency_key=None):
        """Does a PATCH request to /invoices/{invoice_id}/metadata.

        Updates the metadata from an invoice

        Args:
            invoice_id (str): The invoice id
            request (UpdateMetadataRequest): Request for updating the invoice
                metadata
            idempotency_key (str, optional): The request header parameter.

        Returns:
            GetInvoiceResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/invoices/{invoice_id}/metadata')
            .http_method(HttpMethodEnum.PATCH)
            .template_param(Parameter()
                            .key('invoice_id')
                            .value(invoice_id)
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
            .deserialize_into(GetInvoiceResponse.from_dictionary)
        ).execute()

    def get_partial_invoice(self,
                            subscription_id):
        """Does a GET request to /subscriptions/{subscription_id}/partial-invoice.

        Args:
            subscription_id (str): Subscription Id

        Returns:
            GetInvoiceResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/subscriptions/{subscription_id}/partial-invoice')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('subscription_id')
                            .value(subscription_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('httpBasic'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(GetInvoiceResponse.from_dictionary)
        ).execute()

    def cancel_invoice(self,
                       invoice_id,
                       idempotency_key=None):
        """Does a DELETE request to /invoices/{invoice_id}.

        Cancels an invoice

        Args:
            invoice_id (str): Invoice id
            idempotency_key (str, optional): The request header parameter.

        Returns:
            GetInvoiceResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/invoices/{invoice_id}')
            .http_method(HttpMethodEnum.DELETE)
            .template_param(Parameter()
                            .key('invoice_id')
                            .value(invoice_id)
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
            .deserialize_into(GetInvoiceResponse.from_dictionary)
        ).execute()

    def create_invoice(self,
                       subscription_id,
                       cycle_id,
                       request=None,
                       idempotency_key=None):
        """Does a POST request to /subscriptions/{subscription_id}/cycles/{cycle_id}/pay.

        Create an Invoice

        Args:
            subscription_id (str): Subscription Id
            cycle_id (str): Cycle Id
            request (CreateInvoiceRequest, optional): The request body
                parameter.
            idempotency_key (str, optional): The request header parameter.

        Returns:
            GetInvoiceResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/subscriptions/{subscription_id}/cycles/{cycle_id}/pay')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('subscription_id')
                            .value(subscription_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('cycle_id')
                            .value(cycle_id)
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
            .deserialize_into(GetInvoiceResponse.from_dictionary)
        ).execute()

    def get_invoices(self,
                     page=None,
                     size=None,
                     code=None,
                     customer_id=None,
                     subscription_id=None,
                     created_since=None,
                     created_until=None,
                     status=None,
                     due_since=None,
                     due_until=None,
                     customer_document=None):
        """Does a GET request to /invoices.

        Gets all invoices

        Args:
            page (int, optional): Page number
            size (int, optional): Page size
            code (str, optional): Filter for Invoice's code
            customer_id (str, optional): Filter for Invoice's customer id
            subscription_id (str, optional): Filter for Invoice's subscription
                id
            created_since (datetime, optional): Filter for Invoice's creation
                date start range
            created_until (datetime, optional): Filter for Invoices creation
                date end range
            status (str, optional): Filter for Invoice's status
            due_since (datetime, optional): Filter for Invoice's due date
                start range
            due_until (datetime, optional): Filter for Invoice's due date end
                range
            customer_document (str, optional): The request query parameter.

        Returns:
            ListInvoicesResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/invoices')
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
                         .key('customer_id')
                         .value(customer_id))
            .query_param(Parameter()
                         .key('subscription_id')
                         .value(subscription_id))
            .query_param(Parameter()
                         .key('created_since')
                         .value(APIHelper.when_defined(APIHelper.RFC3339DateTime, created_since)))
            .query_param(Parameter()
                         .key('created_until')
                         .value(APIHelper.when_defined(APIHelper.RFC3339DateTime, created_until)))
            .query_param(Parameter()
                         .key('status')
                         .value(status))
            .query_param(Parameter()
                         .key('due_since')
                         .value(APIHelper.when_defined(APIHelper.RFC3339DateTime, due_since)))
            .query_param(Parameter()
                         .key('due_until')
                         .value(APIHelper.when_defined(APIHelper.RFC3339DateTime, due_until)))
            .query_param(Parameter()
                         .key('customer_document')
                         .value(customer_document))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('httpBasic'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ListInvoicesResponse.from_dictionary)
        ).execute()

    def get_invoice(self,
                    invoice_id):
        """Does a GET request to /invoices/{invoice_id}.

        Gets an invoice

        Args:
            invoice_id (str): Invoice Id

        Returns:
            GetInvoiceResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/invoices/{invoice_id}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('invoice_id')
                            .value(invoice_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('httpBasic'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(GetInvoiceResponse.from_dictionary)
        ).execute()

    def update_invoice_status(self,
                              invoice_id,
                              request,
                              idempotency_key=None):
        """Does a PATCH request to /invoices/{invoice_id}/status.

        Updates the status from an invoice

        Args:
            invoice_id (str): Invoice Id
            request (UpdateInvoiceStatusRequest): Request for updating an
                invoice's status
            idempotency_key (str, optional): The request header parameter.

        Returns:
            GetInvoiceResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/invoices/{invoice_id}/status')
            .http_method(HttpMethodEnum.PATCH)
            .template_param(Parameter()
                            .key('invoice_id')
                            .value(invoice_id)
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
            .deserialize_into(GetInvoiceResponse.from_dictionary)
        ).execute()
