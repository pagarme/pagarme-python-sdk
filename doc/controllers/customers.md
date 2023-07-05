# Customers

```python
customers_controller = client.customers
```

## Class Name

`CustomersController`

## Methods

* [Update Card](../../doc/controllers/customers.md#update-card)
* [Update Address](../../doc/controllers/customers.md#update-address)
* [Delete Access Token](../../doc/controllers/customers.md#delete-access-token)
* [Create Address](../../doc/controllers/customers.md#create-address)
* [Create Customer](../../doc/controllers/customers.md#create-customer)
* [Create Card](../../doc/controllers/customers.md#create-card)
* [Get Cards](../../doc/controllers/customers.md#get-cards)
* [Renew Card](../../doc/controllers/customers.md#renew-card)
* [Get Address](../../doc/controllers/customers.md#get-address)
* [Delete Address](../../doc/controllers/customers.md#delete-address)
* [Get Access Token](../../doc/controllers/customers.md#get-access-token)
* [Update Customer Metadata](../../doc/controllers/customers.md#update-customer-metadata)
* [Get Card](../../doc/controllers/customers.md#get-card)
* [Delete Access Tokens](../../doc/controllers/customers.md#delete-access-tokens)
* [Create Access Token](../../doc/controllers/customers.md#create-access-token)
* [Get Access Tokens](../../doc/controllers/customers.md#get-access-tokens)
* [Get Customers](../../doc/controllers/customers.md#get-customers)
* [Update Customer](../../doc/controllers/customers.md#update-customer)
* [Delete Card](../../doc/controllers/customers.md#delete-card)
* [Get Addresses](../../doc/controllers/customers.md#get-addresses)
* [Get Customer](../../doc/controllers/customers.md#get-customer)


# Update Card

Updates a card

```python
def update_card(self,
               customer_id,
               card_id,
               request,
               idempotency_key=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer_id` | `string` | Template, Required | Customer Id |
| `card_id` | `string` | Template, Required | Card id |
| `request` | [`UpdateCardRequest`](../../doc/models/update-card-request.md) | Body, Required | Request for updating a card |
| `idempotency_key` | `string` | Header, Optional | - |

## Response Type

[`GetCardResponse`](../../doc/models/get-card-response.md)

## Example Usage

```python
customer_id = 'customer_id8'

card_id = 'card_id4'

request = UpdateCardRequest(
    holder_name='holder_name2',
    exp_month=10,
    exp_year=30,
    billing_address=CreateAddressRequest(
        street='street8',
        number='number4',
        zip_code='zip_code2',
        neighborhood='neighborhood4',
        city='city8',
        state='state4',
        country='country2',
        complement='complement6',
        line_1='line_18',
        line_2='line_26'
    ),
    metadata={
        "key0": 'metadata3'
    },
    label='label6'
)

result = customers_controller.update_card(
    customer_id,
    card_id,
    request
)
print(result)
```


# Update Address

Updates an address

```python
def update_address(self,
                  customer_id,
                  address_id,
                  request,
                  idempotency_key=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer_id` | `string` | Template, Required | Customer Id |
| `address_id` | `string` | Template, Required | Address Id |
| `request` | [`UpdateAddressRequest`](../../doc/models/update-address-request.md) | Body, Required | Request for updating an address |
| `idempotency_key` | `string` | Header, Optional | - |

## Response Type

[`GetAddressResponse`](../../doc/models/get-address-response.md)

## Example Usage

```python
customer_id = 'customer_id8'

address_id = 'address_id0'

request = UpdateAddressRequest(
    number='number4',
    complement='complement2',
    metadata={
        "key0": 'metadata3'
    },
    line_2='line_24'
)

result = customers_controller.update_address(
    customer_id,
    address_id,
    request
)
print(result)
```


# Delete Access Token

Delete a customer's access token

```python
def delete_access_token(self,
                       customer_id,
                       token_id,
                       idempotency_key=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer_id` | `string` | Template, Required | Customer Id |
| `token_id` | `string` | Template, Required | Token Id |
| `idempotency_key` | `string` | Header, Optional | - |

## Response Type

[`GetAccessTokenResponse`](../../doc/models/get-access-token-response.md)

## Example Usage

```python
customer_id = 'customer_id8'

token_id = 'token_id6'

result = customers_controller.delete_access_token(
    customer_id,
    token_id
)
print(result)
```


# Create Address

Creates a new address for a customer

```python
def create_address(self,
                  customer_id,
                  request,
                  idempotency_key=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer_id` | `string` | Template, Required | Customer Id |
| `request` | [`CreateAddressRequest`](../../doc/models/create-address-request.md) | Body, Required | Request for creating an address |
| `idempotency_key` | `string` | Header, Optional | - |

## Response Type

[`GetAddressResponse`](../../doc/models/get-address-response.md)

## Example Usage

```python
customer_id = 'customer_id8'

request = CreateAddressRequest(
    street='street6',
    number='number4',
    zip_code='zip_code0',
    neighborhood='neighborhood2',
    city='city6',
    state='state2',
    country='country0',
    complement='complement2',
    line_1='line_10',
    line_2='line_24'
)

result = customers_controller.create_address(
    customer_id,
    request
)
print(result)
```


# Create Customer

Creates a new customer

```python
def create_customer(self,
                   request,
                   idempotency_key=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request` | [`CreateCustomerRequest`](../../doc/models/create-customer-request.md) | Body, Required | Request for creating a customer |
| `idempotency_key` | `string` | Header, Optional | - |

## Response Type

[`GetCustomerResponse`](../../doc/models/get-customer-response.md)

## Example Usage

```python
request = CreateCustomerRequest(
    name='{\n    "name": "Tony Stark"\n}',
    email='email0',
    document='document0',
    mtype='type4',
    address=CreateAddressRequest(
        street='street2',
        number='number0',
        zip_code='zip_code6',
        neighborhood='neighborhood8',
        city='city2',
        state='state8',
        country='country6',
        complement='complement8',
        line_1='line_16',
        line_2='line_20'
    ),
    metadata={
        "key0": 'metadata3'
    },
    phones=CreatePhonesRequest(),
    code='code4'
)

result = customers_controller.create_customer(request)
print(result)
```


# Create Card

Creates a new card for a customer

```python
def create_card(self,
               customer_id,
               request,
               idempotency_key=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer_id` | `string` | Template, Required | Customer id |
| `request` | [`CreateCardRequest`](../../doc/models/create-card-request.md) | Body, Required | Request for creating a card |
| `idempotency_key` | `string` | Header, Optional | - |

## Response Type

[`GetCardResponse`](../../doc/models/get-card-response.md)

## Example Usage

```python
customer_id = 'customer_id8'

request = CreateCardRequest(
    mtype='credit'
)

result = customers_controller.create_card(
    customer_id,
    request
)
print(result)
```


# Get Cards

Get all cards from a customer

```python
def get_cards(self,
             customer_id,
             page=None,
             size=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer_id` | `string` | Template, Required | Customer Id |
| `page` | `int` | Query, Optional | Page number |
| `size` | `int` | Query, Optional | Page size |

## Response Type

[`ListCardsResponse`](../../doc/models/list-cards-response.md)

## Example Usage

```python
customer_id = 'customer_id8'

result = customers_controller.get_cards(customer_id)
print(result)
```


# Renew Card

Renew a card

```python
def renew_card(self,
              customer_id,
              card_id,
              idempotency_key=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer_id` | `string` | Template, Required | Customer id |
| `card_id` | `string` | Template, Required | Card Id |
| `idempotency_key` | `string` | Header, Optional | - |

## Response Type

[`GetCardResponse`](../../doc/models/get-card-response.md)

## Example Usage

```python
customer_id = 'customer_id8'

card_id = 'card_id4'

result = customers_controller.renew_card(
    customer_id,
    card_id
)
print(result)
```


# Get Address

Get a customer's address

```python
def get_address(self,
               customer_id,
               address_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer_id` | `string` | Template, Required | Customer id |
| `address_id` | `string` | Template, Required | Address Id |

## Response Type

[`GetAddressResponse`](../../doc/models/get-address-response.md)

## Example Usage

```python
customer_id = 'customer_id8'

address_id = 'address_id0'

result = customers_controller.get_address(
    customer_id,
    address_id
)
print(result)
```


# Delete Address

Delete a Customer's address

```python
def delete_address(self,
                  customer_id,
                  address_id,
                  idempotency_key=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer_id` | `string` | Template, Required | Customer Id |
| `address_id` | `string` | Template, Required | Address Id |
| `idempotency_key` | `string` | Header, Optional | - |

## Response Type

[`GetAddressResponse`](../../doc/models/get-address-response.md)

## Example Usage

```python
customer_id = 'customer_id8'

address_id = 'address_id0'

result = customers_controller.delete_address(
    customer_id,
    address_id
)
print(result)
```


# Get Access Token

Get a Customer's access token

```python
def get_access_token(self,
                    customer_id,
                    token_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer_id` | `string` | Template, Required | Customer Id |
| `token_id` | `string` | Template, Required | Token Id |

## Response Type

[`GetAccessTokenResponse`](../../doc/models/get-access-token-response.md)

## Example Usage

```python
customer_id = 'customer_id8'

token_id = 'token_id6'

result = customers_controller.get_access_token(
    customer_id,
    token_id
)
print(result)
```


# Update Customer Metadata

Updates the metadata a customer

```python
def update_customer_metadata(self,
                            customer_id,
                            request,
                            idempotency_key=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer_id` | `string` | Template, Required | The customer id |
| `request` | [`UpdateMetadataRequest`](../../doc/models/update-metadata-request.md) | Body, Required | Request for updating the customer metadata |
| `idempotency_key` | `string` | Header, Optional | - |

## Response Type

[`GetCustomerResponse`](../../doc/models/get-customer-response.md)

## Example Usage

```python
customer_id = 'customer_id8'

request = UpdateMetadataRequest(
    metadata={
        "key0": 'metadata3'
    }
)

result = customers_controller.update_customer_metadata(
    customer_id,
    request
)
print(result)
```


# Get Card

Get a customer's card

```python
def get_card(self,
            customer_id,
            card_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer_id` | `string` | Template, Required | Customer id |
| `card_id` | `string` | Template, Required | Card id |

## Response Type

[`GetCardResponse`](../../doc/models/get-card-response.md)

## Example Usage

```python
customer_id = 'customer_id8'

card_id = 'card_id4'

result = customers_controller.get_card(
    customer_id,
    card_id
)
print(result)
```


# Delete Access Tokens

Delete a Customer's access tokens

```python
def delete_access_tokens(self,
                        customer_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer_id` | `string` | Template, Required | Customer Id |

## Response Type

[`ListAccessTokensResponse`](../../doc/models/list-access-tokens-response.md)

## Example Usage

```python
customer_id = 'customer_id8'

result = customers_controller.delete_access_tokens(customer_id)
print(result)
```


# Create Access Token

Creates a access token for a customer

```python
def create_access_token(self,
                       customer_id,
                       request,
                       idempotency_key=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer_id` | `string` | Template, Required | Customer Id |
| `request` | [`CreateAccessTokenRequest`](../../doc/models/create-access-token-request.md) | Body, Required | Request for creating a access token |
| `idempotency_key` | `string` | Header, Optional | - |

## Response Type

[`GetAccessTokenResponse`](../../doc/models/get-access-token-response.md)

## Example Usage

```python
customer_id = 'customer_id8'

request = CreateAccessTokenRequest()

result = customers_controller.create_access_token(
    customer_id,
    request
)
print(result)
```


# Get Access Tokens

Get all access tokens from a customer

```python
def get_access_tokens(self,
                     customer_id,
                     page=None,
                     size=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer_id` | `string` | Template, Required | Customer Id |
| `page` | `int` | Query, Optional | Page number |
| `size` | `int` | Query, Optional | Page size |

## Response Type

[`ListAccessTokensResponse`](../../doc/models/list-access-tokens-response.md)

## Example Usage

```python
customer_id = 'customer_id8'

result = customers_controller.get_access_tokens(customer_id)
print(result)
```


# Get Customers

Get all Customers

```python
def get_customers(self,
                 name=None,
                 document=None,
                 page=1,
                 size=10,
                 email=None,
                 code=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Query, Optional | Name of the Customer |
| `document` | `string` | Query, Optional | Document of the Customer |
| `page` | `int` | Query, Optional | Current page the the search<br>**Default**: `1` |
| `size` | `int` | Query, Optional | Quantity pages of the search<br>**Default**: `10` |
| `email` | `string` | Query, Optional | Customer's email |
| `code` | `string` | Query, Optional | Customer's code |

## Response Type

[`ListCustomersResponse`](../../doc/models/list-customers-response.md)

## Example Usage

```python
page = 1

size = 10

result = customers_controller.get_customers(
    page,
    size
)
print(result)
```


# Update Customer

Updates a customer

```python
def update_customer(self,
                   customer_id,
                   request,
                   idempotency_key=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer_id` | `string` | Template, Required | Customer id |
| `request` | [`UpdateCustomerRequest`](../../doc/models/update-customer-request.md) | Body, Required | Request for updating a customer |
| `idempotency_key` | `string` | Header, Optional | - |

## Response Type

[`GetCustomerResponse`](../../doc/models/get-customer-response.md)

## Example Usage

```python
customer_id = 'customer_id8'

request = UpdateCustomerRequest()

result = customers_controller.update_customer(
    customer_id,
    request
)
print(result)
```


# Delete Card

Delete a customer's card

```python
def delete_card(self,
               customer_id,
               card_id,
               idempotency_key=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer_id` | `string` | Template, Required | Customer Id |
| `card_id` | `string` | Template, Required | Card Id |
| `idempotency_key` | `string` | Header, Optional | - |

## Response Type

[`GetCardResponse`](../../doc/models/get-card-response.md)

## Example Usage

```python
customer_id = 'customer_id8'

card_id = 'card_id4'

result = customers_controller.delete_card(
    customer_id,
    card_id
)
print(result)
```


# Get Addresses

Gets all adressess from a customer

```python
def get_addresses(self,
                 customer_id,
                 page=None,
                 size=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer_id` | `string` | Template, Required | Customer id |
| `page` | `int` | Query, Optional | Page number |
| `size` | `int` | Query, Optional | Page size |

## Response Type

[`ListAddressesResponse`](../../doc/models/list-addresses-response.md)

## Example Usage

```python
customer_id = 'customer_id8'

result = customers_controller.get_addresses(customer_id)
print(result)
```


# Get Customer

Get a customer

```python
def get_customer(self,
                customer_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer_id` | `string` | Template, Required | Customer Id |

## Response Type

[`GetCustomerResponse`](../../doc/models/get-customer-response.md)

## Example Usage

```python
customer_id = 'customer_id8'

result = customers_controller.get_customer(customer_id)
print(result)
```

