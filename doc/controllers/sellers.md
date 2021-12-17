# Sellers

```python
sellers_controller = client.sellers
```

## Class Name

`SellersController`

## Methods

* [Create Seller](/doc/controllers/sellers.md#create-seller)
* [Update Seller Metadata](/doc/controllers/sellers.md#update-seller-metadata)
* [Update Seller](/doc/controllers/sellers.md#update-seller)
* [Delete Seller](/doc/controllers/sellers.md#delete-seller)
* [Get Seller by Id](/doc/controllers/sellers.md#get-seller-by-id)
* [Get Sellers](/doc/controllers/sellers.md#get-sellers)


# Create Seller

```python
def create_seller(self,
                 request,
                 idempotency_key=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request` | [`CreateSellerRequest`](/doc/models/create-seller-request.md) | Body, Required | Seller Model |
| `idempotency_key` | `string` | Header, Optional | - |

## Response Type

[`GetSellerResponse`](/doc/models/get-seller-response.md)

## Example Usage

```python
request = CreateSellerRequest()
request.name = 'name6'
request.metadata = {'key0' : 'metadata3' } 

result = sellers_controller.create_seller(request)
```


# Update Seller Metadata

```python
def update_seller_metadata(self,
                          seller_id,
                          request,
                          idempotency_key=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `seller_id` | `string` | Template, Required | Seller Id |
| `request` | [`UpdateMetadataRequest`](/doc/models/update-metadata-request.md) | Body, Required | Request for updating the charge metadata |
| `idempotency_key` | `string` | Header, Optional | - |

## Response Type

[`GetSellerResponse`](/doc/models/get-seller-response.md)

## Example Usage

```python
seller_id = 'seller_id8'
request = UpdateMetadataRequest()
request.metadata = {'key0' : 'metadata3' } 

result = sellers_controller.update_seller_metadata(seller_id, request)
```


# Update Seller

```python
def update_seller(self,
                 id,
                 request,
                 idempotency_key=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Template, Required | - |
| `request` | [`UpdateSellerRequest`](/doc/models/update-seller-request.md) | Body, Required | Update Seller model |
| `idempotency_key` | `string` | Header, Optional | - |

## Response Type

[`GetSellerResponse`](/doc/models/get-seller-response.md)

## Example Usage

```python
id = 'id0'
request = UpdateSellerRequest()
request.name = 'name6'
request.code = 'code4'
request.description = 'description6'
request.document = 'document0'
request.status = 'status8'
request.mtype = 'type4'
request.address = CreateAddressRequest()
request.address.street = 'street2'
request.address.number = 'number0'
request.address.zip_code = 'zip_code6'
request.address.neighborhood = 'neighborhood8'
request.address.city = 'city2'
request.address.state = 'state8'
request.address.country = 'country6'
request.address.complement = 'complement8'
request.address.metadata = {'key0' : 'metadata7' } 
request.address.line_1 = 'line_16'
request.address.line_2 = 'line_20'
request.metadata = {'key0' : 'metadata3' } 

result = sellers_controller.update_seller(id, request)
```


# Delete Seller

```python
def delete_seller(self,
                 seller_id,
                 idempotency_key=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `seller_id` | `string` | Template, Required | Seller Id |
| `idempotency_key` | `string` | Header, Optional | - |

## Response Type

[`GetSellerResponse`](/doc/models/get-seller-response.md)

## Example Usage

```python
seller_id = 'sellerId4'

result = sellers_controller.delete_seller(seller_id)
```


# Get Seller by Id

```python
def get_seller_by_id(self,
                    id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Template, Required | Seller Id |

## Response Type

[`GetSellerResponse`](/doc/models/get-seller-response.md)

## Example Usage

```python
id = 'id0'

result = sellers_controller.get_seller_by_id(id)
```


# Get Sellers

```python
def get_sellers(self,
               page=None,
               size=None,
               name=None,
               document=None,
               code=None,
               status=None,
               mtype=None,
               created_since=None,
               created_until=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `page` | `int` | Query, Optional | Page number |
| `size` | `int` | Query, Optional | Page size |
| `name` | `string` | Query, Optional | - |
| `document` | `string` | Query, Optional | - |
| `code` | `string` | Query, Optional | - |
| `status` | `string` | Query, Optional | - |
| `mtype` | `string` | Query, Optional | - |
| `created_since` | `datetime` | Query, Optional | - |
| `created_until` | `datetime` | Query, Optional | - |

## Response Type

[`ListSellerResponse`](/doc/models/list-seller-response.md)

## Example Usage

```python
result = sellers_controller.get_sellers()
```

