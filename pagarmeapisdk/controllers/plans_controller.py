# -*- coding: utf-8 -*-

"""
pagarmeapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from pagarmeapisdk.api_helper import APIHelper
from pagarmeapisdk.configuration import Server
from pagarmeapisdk.controllers.base_controller import BaseController
from pagarmeapisdk.models.get_plan_response import GetPlanResponse
from pagarmeapisdk.models.get_plan_item_response import GetPlanItemResponse
from pagarmeapisdk.models.list_plans_response import ListPlansResponse


class PlansController(BaseController):

    """A Controller to access Endpoints in the pagarmeapisdk API."""
    def __init__(self, config, auth_managers):
        super(PlansController, self).__init__(config, auth_managers)

    def get_plan(self,
                 plan_id):
        """Does a GET request to /plans/{plan_id}.

        Gets a plan

        Args:
            plan_id (string): Plan id

        Returns:
            GetPlanResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/plans/{plan_id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'plan_id': {'value': plan_id, 'encode': True}
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
        # Apply authentication scheme on request
        self.apply_auth_schemes(_request, 'global')

        _response = self.execute_request(_request)
        self.validate_response(_response)

        decoded = APIHelper.json_deserialize(_response.text, GetPlanResponse.from_dictionary)

        return decoded

    def update_plan(self,
                    plan_id,
                    request,
                    idempotency_key=None):
        """Does a PUT request to /plans/{plan_id}.

        Updates a plan

        Args:
            plan_id (string): Plan id
            request (UpdatePlanRequest): Request for updating a plan
            idempotency_key (string, optional): TODO: type description here.

        Returns:
            GetPlanResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/plans/{plan_id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'plan_id': {'value': plan_id, 'encode': True}
        })
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8',
            'idempotency-key': idempotency_key
        }

        # Prepare and execute request
        _request = self.config.http_client.put(_query_url, headers=_headers, parameters=APIHelper.json_serialize(request))
        # Apply authentication scheme on request
        self.apply_auth_schemes(_request, 'global')

        _response = self.execute_request(_request)
        self.validate_response(_response)

        decoded = APIHelper.json_deserialize(_response.text, GetPlanResponse.from_dictionary)

        return decoded

    def update_plan_metadata(self,
                             plan_id,
                             request,
                             idempotency_key=None):
        """Does a PATCH request to /Plans/{plan_id}/metadata.

        Updates the metadata from a plan

        Args:
            plan_id (string): The plan id
            request (UpdateMetadataRequest): Request for updating the plan
                metadata
            idempotency_key (string, optional): TODO: type description here.

        Returns:
            GetPlanResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/Plans/{plan_id}/metadata'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'plan_id': {'value': plan_id, 'encode': True}
        })
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8',
            'idempotency-key': idempotency_key
        }

        # Prepare and execute request
        _request = self.config.http_client.patch(_query_url, headers=_headers, parameters=APIHelper.json_serialize(request))
        # Apply authentication scheme on request
        self.apply_auth_schemes(_request, 'global')

        _response = self.execute_request(_request)
        self.validate_response(_response)

        decoded = APIHelper.json_deserialize(_response.text, GetPlanResponse.from_dictionary)

        return decoded

    def delete_plan_item(self,
                         plan_id,
                         plan_item_id,
                         idempotency_key=None):
        """Does a DELETE request to /plans/{plan_id}/items/{plan_item_id}.

        Removes an item from a plan

        Args:
            plan_id (string): Plan id
            plan_item_id (string): Plan item id
            idempotency_key (string, optional): TODO: type description here.

        Returns:
            GetPlanItemResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/plans/{plan_id}/items/{plan_item_id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'plan_id': {'value': plan_id, 'encode': True},
            'plan_item_id': {'value': plan_item_id, 'encode': True}
        })
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'idempotency-key': idempotency_key
        }

        # Prepare and execute request
        _request = self.config.http_client.delete(_query_url, headers=_headers)
        # Apply authentication scheme on request
        self.apply_auth_schemes(_request, 'global')

        _response = self.execute_request(_request)
        self.validate_response(_response)

        decoded = APIHelper.json_deserialize(_response.text, GetPlanItemResponse.from_dictionary)

        return decoded

    def get_plans(self,
                  page=None,
                  size=None,
                  name=None,
                  status=None,
                  billing_type=None,
                  created_since=None,
                  created_until=None):
        """Does a GET request to /plans.

        Gets all plans

        Args:
            page (int, optional): Page number
            size (int, optional): Page size
            name (string, optional): Filter for Plan's name
            status (string, optional): Filter for Plan's status
            billing_type (string, optional): Filter for plan's billing type
            created_since (datetime, optional): Filter for plan's creation
                date start range
            created_until (datetime, optional): Filter for plan's creation
                date end range

        Returns:
            ListPlansResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/plans'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'page': page,
            'size': size,
            'name': name,
            'status': status,
            'billing_type': billing_type,
            'created_since': APIHelper.when_defined(APIHelper.RFC3339DateTime, created_since),
            'created_until': APIHelper.when_defined(APIHelper.RFC3339DateTime, created_until)
        }
        _query_builder = APIHelper.append_url_with_query_parameters(
            _query_builder,
            _query_parameters
        )
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.get(_query_url, headers=_headers)
        # Apply authentication scheme on request
        self.apply_auth_schemes(_request, 'global')

        _response = self.execute_request(_request)
        self.validate_response(_response)

        decoded = APIHelper.json_deserialize(_response.text, ListPlansResponse.from_dictionary)

        return decoded

    def get_plan_item(self,
                      plan_id,
                      plan_item_id):
        """Does a GET request to /plans/{plan_id}/items/{plan_item_id}.

        Gets a plan item

        Args:
            plan_id (string): Plan id
            plan_item_id (string): Plan item id

        Returns:
            GetPlanItemResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/plans/{plan_id}/items/{plan_item_id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'plan_id': {'value': plan_id, 'encode': True},
            'plan_item_id': {'value': plan_item_id, 'encode': True}
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
        # Apply authentication scheme on request
        self.apply_auth_schemes(_request, 'global')

        _response = self.execute_request(_request)
        self.validate_response(_response)

        decoded = APIHelper.json_deserialize(_response.text, GetPlanItemResponse.from_dictionary)

        return decoded

    def delete_plan(self,
                    plan_id,
                    idempotency_key=None):
        """Does a DELETE request to /plans/{plan_id}.

        Deletes a plan

        Args:
            plan_id (string): Plan id
            idempotency_key (string, optional): TODO: type description here.

        Returns:
            GetPlanResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/plans/{plan_id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'plan_id': {'value': plan_id, 'encode': True}
        })
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'idempotency-key': idempotency_key
        }

        # Prepare and execute request
        _request = self.config.http_client.delete(_query_url, headers=_headers)
        # Apply authentication scheme on request
        self.apply_auth_schemes(_request, 'global')

        _response = self.execute_request(_request)
        self.validate_response(_response)

        decoded = APIHelper.json_deserialize(_response.text, GetPlanResponse.from_dictionary)

        return decoded

    def update_plan_item(self,
                         plan_id,
                         plan_item_id,
                         body,
                         idempotency_key=None):
        """Does a PUT request to /plans/{plan_id}/items/{plan_item_id}.

        Updates a plan item

        Args:
            plan_id (string): Plan id
            plan_item_id (string): Plan item id
            body (UpdatePlanItemRequest): Request for updating the plan item
            idempotency_key (string, optional): TODO: type description here.

        Returns:
            GetPlanItemResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/plans/{plan_id}/items/{plan_item_id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'plan_id': {'value': plan_id, 'encode': True},
            'plan_item_id': {'value': plan_item_id, 'encode': True}
        })
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8',
            'idempotency-key': idempotency_key
        }

        # Prepare and execute request
        _request = self.config.http_client.put(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        # Apply authentication scheme on request
        self.apply_auth_schemes(_request, 'global')

        _response = self.execute_request(_request)
        self.validate_response(_response)

        decoded = APIHelper.json_deserialize(_response.text, GetPlanItemResponse.from_dictionary)

        return decoded

    def create_plan_item(self,
                         plan_id,
                         request,
                         idempotency_key=None):
        """Does a POST request to /plans/{plan_id}/items.

        Adds a new item to a plan

        Args:
            plan_id (string): Plan id
            request (CreatePlanItemRequest): Request for creating a plan item
            idempotency_key (string, optional): TODO: type description here.

        Returns:
            GetPlanItemResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/plans/{plan_id}/items'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'plan_id': {'value': plan_id, 'encode': True}
        })
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8',
            'idempotency-key': idempotency_key
        }

        # Prepare and execute request
        _request = self.config.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(request))
        # Apply authentication scheme on request
        self.apply_auth_schemes(_request, 'global')

        _response = self.execute_request(_request)
        self.validate_response(_response)

        decoded = APIHelper.json_deserialize(_response.text, GetPlanItemResponse.from_dictionary)

        return decoded

    def create_plan(self,
                    body,
                    idempotency_key=None):
        """Does a POST request to /plans.

        Creates a new plan

        Args:
            body (CreatePlanRequest): Request for creating a plan
            idempotency_key (string, optional): TODO: type description here.

        Returns:
            GetPlanResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/plans'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8',
            'idempotency-key': idempotency_key
        }

        # Prepare and execute request
        _request = self.config.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        # Apply authentication scheme on request
        self.apply_auth_schemes(_request, 'global')

        _response = self.execute_request(_request)
        self.validate_response(_response)

        decoded = APIHelper.json_deserialize(_response.text, GetPlanResponse.from_dictionary)

        return decoded
