# Orders

```python
orders_controller = client.orders
```

## Class Name

`OrdersController`

## Methods

* [Get Orders](../../doc/controllers/orders.md#get-orders)
* [Get Order Item](../../doc/controllers/orders.md#get-order-item)
* [Get Order](../../doc/controllers/orders.md#get-order)
* [Close Order](../../doc/controllers/orders.md#close-order)
* [Create Order](../../doc/controllers/orders.md#create-order)
* [Update Order Item](../../doc/controllers/orders.md#update-order-item)
* [Delete All Order Items](../../doc/controllers/orders.md#delete-all-order-items)
* [Update Order Metadata](../../doc/controllers/orders.md#update-order-metadata)
* [Delete Order Item](../../doc/controllers/orders.md#delete-order-item)
* [Create Order Item](../../doc/controllers/orders.md#create-order-item)


# Get Orders

Gets all orders

```python
def get_orders(self,
              page=None,
              size=None,
              code=None,
              status=None,
              created_since=None,
              created_until=None,
              customer_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `page` | `int` | Query, Optional | Page number |
| `size` | `int` | Query, Optional | Page size |
| `code` | `string` | Query, Optional | Filter for order's code |
| `status` | `string` | Query, Optional | Filter for order's status |
| `created_since` | `datetime` | Query, Optional | Filter for order's creation date start range |
| `created_until` | `datetime` | Query, Optional | Filter for order's creation date end range |
| `customer_id` | `string` | Query, Optional | Filter for order's customer id |

## Response Type

[`ListOrderResponse`](../../doc/models/list-order-response.md)

## Example Usage

```python
result = orders_controller.get_orders()
```


# Get Order Item

```python
def get_order_item(self,
                  order_id,
                  item_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `order_id` | `string` | Template, Required | Order Id |
| `item_id` | `string` | Template, Required | Item Id |

## Response Type

[`GetOrderItemResponse`](../../doc/models/get-order-item-response.md)

## Example Usage

```python
order_id = 'orderId2'
item_id = 'itemId8'

result = orders_controller.get_order_item(order_id, item_id)
```


# Get Order

Gets an order

```python
def get_order(self,
             order_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `order_id` | `string` | Template, Required | Order id |

## Response Type

[`GetOrderResponse`](../../doc/models/get-order-response.md)

## Example Usage

```python
order_id = 'order_id6'

result = orders_controller.get_order(order_id)
```


# Close Order

```python
def close_order(self,
               id,
               request,
               idempotency_key=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Template, Required | Order Id |
| `request` | [`UpdateOrderStatusRequest`](../../doc/models/update-order-status-request.md) | Body, Required | Update Order Model |
| `idempotency_key` | `string` | Header, Optional | - |

## Response Type

[`GetOrderResponse`](../../doc/models/get-order-response.md)

## Example Usage

```python
id = 'id0'
request = UpdateOrderStatusRequest()
request.status = 'status8'

result = orders_controller.close_order(id, request)
```


# Create Order

Creates a new Order

```python
def create_order(self,
                body,
                idempotency_key=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CreateOrderRequest`](../../doc/models/create-order-request.md) | Body, Required | Request for creating an order |
| `idempotency_key` | `string` | Header, Optional | - |

## Response Type

[`GetOrderResponse`](../../doc/models/get-order-response.md)

## Example Usage

```python
body = CreateOrderRequest()
body.items = []

body.items.append(CreateOrderItemRequest())
body.items[0].amount = 101
body.items[0].description = 'description3'
body.items[0].quantity = 215
body.items[0].category = 'category1'

body.items.append(CreateOrderItemRequest())
body.items[1].amount = 102
body.items[1].description = 'description4'
body.items[1].quantity = 216
body.items[1].category = 'category2'

body.items.append(CreateOrderItemRequest())
body.items[2].amount = 103
body.items[2].description = 'description5'
body.items[2].quantity = 217
body.items[2].category = 'category3'

body.customer = CreateCustomerRequest()
body.customer.name = '{\n    "name": "Tony Stark"\n}'
body.customer.email = 'email2'
body.customer.document = 'document2'
body.customer.mtype = 'type6'
body.customer.address = CreateAddressRequest()
body.customer.address.street = 'street0'
body.customer.address.number = 'number8'
body.customer.address.zip_code = 'zip_code4'
body.customer.address.neighborhood = 'neighborhood6'
body.customer.address.city = 'city0'
body.customer.address.state = 'state6'
body.customer.address.country = 'country4'
body.customer.address.complement = 'complement6'
body.customer.address.metadata = {'key0' : 'metadata7', 'key1' : 'metadata6' } 
body.customer.address.line_1 = 'line_16'
body.customer.address.line_2 = 'line_28'
body.customer.metadata = {'key0' : 'metadata9', 'key1' : 'metadata0' } 
body.customer.phones = CreatePhonesRequest()
body.customer.code = 'code2'
body.payments = []

body.payments.append(CreatePaymentRequest())
body.payments[0].payment_method = 'payment_method0'

body.payments.append(CreatePaymentRequest())
body.payments[1].payment_method = 'payment_method9'

body.code = 'code4'
body.metadata = {'key0' : 'metadata7', 'key1' : 'metadata8' } 
body.closed = True

result = orders_controller.create_order(body)
```


# Update Order Item

```python
def update_order_item(self,
                     order_id,
                     item_id,
                     request,
                     idempotency_key=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `order_id` | `string` | Template, Required | Order Id |
| `item_id` | `string` | Template, Required | Item Id |
| `request` | [`UpdateOrderItemRequest`](../../doc/models/update-order-item-request.md) | Body, Required | Item Model |
| `idempotency_key` | `string` | Header, Optional | - |

## Response Type

[`GetOrderItemResponse`](../../doc/models/get-order-item-response.md)

## Example Usage

```python
order_id = 'orderId2'
item_id = 'itemId8'
request = UpdateOrderItemRequest()
request.amount = 242
request.description = 'description6'
request.quantity = 100
request.category = 'category4'

result = orders_controller.update_order_item(order_id, item_id, request)
```


# Delete All Order Items

```python
def delete_all_order_items(self,
                          order_id,
                          idempotency_key=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `order_id` | `string` | Template, Required | Order Id |
| `idempotency_key` | `string` | Header, Optional | - |

## Response Type

[`GetOrderResponse`](../../doc/models/get-order-response.md)

## Example Usage

```python
order_id = 'orderId2'

result = orders_controller.delete_all_order_items(order_id)
```


# Update Order Metadata

Updates the metadata from an order

```python
def update_order_metadata(self,
                         order_id,
                         request,
                         idempotency_key=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `order_id` | `string` | Template, Required | The order id |
| `request` | [`UpdateMetadataRequest`](../../doc/models/update-metadata-request.md) | Body, Required | Request for updating the order metadata |
| `idempotency_key` | `string` | Header, Optional | - |

## Response Type

[`GetOrderResponse`](../../doc/models/get-order-response.md)

## Example Usage

```python
order_id = 'order_id6'
request = UpdateMetadataRequest()
request.metadata = {'key0' : 'metadata3' } 

result = orders_controller.update_order_metadata(order_id, request)
```


# Delete Order Item

```python
def delete_order_item(self,
                     order_id,
                     item_id,
                     idempotency_key=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `order_id` | `string` | Template, Required | Order Id |
| `item_id` | `string` | Template, Required | Item Id |
| `idempotency_key` | `string` | Header, Optional | - |

## Response Type

[`GetOrderItemResponse`](../../doc/models/get-order-item-response.md)

## Example Usage

```python
order_id = 'orderId2'
item_id = 'itemId8'

result = orders_controller.delete_order_item(order_id, item_id)
```


# Create Order Item

```python
def create_order_item(self,
                     order_id,
                     request,
                     idempotency_key=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `order_id` | `string` | Template, Required | Order Id |
| `request` | [`CreateOrderItemRequest`](../../doc/models/create-order-item-request.md) | Body, Required | Order Item Model |
| `idempotency_key` | `string` | Header, Optional | - |

## Response Type

[`GetOrderItemResponse`](../../doc/models/get-order-item-response.md)

## Example Usage

```python
order_id = 'orderId2'
request = CreateOrderItemRequest()
request.amount = 242
request.description = 'description6'
request.quantity = 100
request.category = 'category4'

result = orders_controller.create_order_item(order_id, request)
```

