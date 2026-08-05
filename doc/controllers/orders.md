# Orders

```python
orders_controller = client.orders
```

## Class Name

`OrdersController`

## Methods

* [Close Order](../../doc/controllers/orders.md#close-order)
* [Create Order](../../doc/controllers/orders.md#create-order)
* [Create Order Item](../../doc/controllers/orders.md#create-order-item)
* [Delete All Order Items](../../doc/controllers/orders.md#delete-all-order-items)
* [Delete Order Item](../../doc/controllers/orders.md#delete-order-item)
* [Get Order](../../doc/controllers/orders.md#get-order)
* [Get Order Item](../../doc/controllers/orders.md#get-order-item)
* [Get Orders](../../doc/controllers/orders.md#get-orders)
* [Update Order Item](../../doc/controllers/orders.md#update-order-item)
* [Update Order Metadata](../../doc/controllers/orders.md#update-order-metadata)


# Close Order

```python
def close_order(self,
               id,
               request,
               idempotency_key=None)
```

## Authentication

This endpoint requires [httpBasic](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | Order Id |
| `request` | [`UpdateOrderStatusRequest`](../../doc/models/update-order-status-request.md) | Body, Required | Update Order Model |
| `idempotency_key` | `str` | Header, Optional | - |

## Response Type

**200**

[`GetOrderResponse`](../../doc/models/get-order-response.md)

## Example Usage

```python
id = 'id0'

request = UpdateOrderStatusRequest(
    status='status8'
)

result = orders_controller.close_order(
    id,
    request
)
print(result)
```


# Create Order

Creates a new Order

```python
def create_order(self,
                body,
                idempotency_key=None)
```

## Authentication

This endpoint requires [httpBasic](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CreateOrderRequest`](../../doc/models/create-order-request.md) | Body, Required | Request for creating an order |
| `idempotency_key` | `str` | Header, Optional | - |

## Response Type

**200**

[`GetOrderResponse`](../../doc/models/get-order-response.md)

## Example Usage

```python
body = CreateOrderRequest(
    items=[
        None
    ],
    customer=CreateCustomerRequest(
        name='Tony Stark',
        email=None,
        document=None,
        mtype=None,
        address=CreateAddressRequest(
            street=None,
            number=None,
            zip_code=None,
            neighborhood=None,
            city=None,
            state=None,
            country=None,
            complement=None,
            line_1=None,
            line_2=None
        ),
        metadata={},
        phones=CreatePhonesRequest(),
        code=None
    ),
    payments=[
        None
    ],
    code=None,
    closed=True
)

result = orders_controller.create_order(body)
print(result)
```


# Create Order Item

```python
def create_order_item(self,
                     order_id,
                     request,
                     idempotency_key=None)
```

## Authentication

This endpoint requires [httpBasic](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `order_id` | `str` | Template, Required | Order Id |
| `request` | [`CreateOrderItemRequest`](../../doc/models/create-order-item-request.md) | Body, Required | Order Item Model |
| `idempotency_key` | `str` | Header, Optional | - |

## Response Type

**200**

[`GetOrderItemResponse`](../../doc/models/get-order-item-response.md)

## Example Usage

```python
order_id = 'orderId2'

request = CreateOrderItemRequest(
    amount=242,
    description='description6',
    quantity=100,
    category='category4'
)

result = orders_controller.create_order_item(
    order_id,
    request
)
print(result)
```


# Delete All Order Items

```python
def delete_all_order_items(self,
                          order_id,
                          idempotency_key=None)
```

## Authentication

This endpoint requires [httpBasic](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `order_id` | `str` | Template, Required | Order Id |
| `idempotency_key` | `str` | Header, Optional | - |

## Response Type

**200**

[`GetOrderResponse`](../../doc/models/get-order-response.md)

## Example Usage

```python
order_id = 'orderId2'

result = orders_controller.delete_all_order_items(order_id)
print(result)
```


# Delete Order Item

```python
def delete_order_item(self,
                     order_id,
                     item_id,
                     idempotency_key=None)
```

## Authentication

This endpoint requires [httpBasic](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `order_id` | `str` | Template, Required | Order Id |
| `item_id` | `str` | Template, Required | Item Id |
| `idempotency_key` | `str` | Header, Optional | - |

## Response Type

**200**

[`GetOrderItemResponse`](../../doc/models/get-order-item-response.md)

## Example Usage

```python
order_id = 'orderId2'

item_id = 'itemId8'

result = orders_controller.delete_order_item(
    order_id,
    item_id
)
print(result)
```


# Get Order

Gets an order

```python
def get_order(self,
             order_id)
```

## Authentication

This endpoint requires [httpBasic](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `order_id` | `str` | Template, Required | Order id |

## Response Type

**200**

[`GetOrderResponse`](../../doc/models/get-order-response.md)

## Example Usage

```python
order_id = 'order_id6'

result = orders_controller.get_order(order_id)
print(result)
```


# Get Order Item

```python
def get_order_item(self,
                  order_id,
                  item_id)
```

## Authentication

This endpoint requires [httpBasic](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `order_id` | `str` | Template, Required | Order Id |
| `item_id` | `str` | Template, Required | Item Id |

## Response Type

**200**

[`GetOrderItemResponse`](../../doc/models/get-order-item-response.md)

## Example Usage

```python
order_id = 'orderId2'

item_id = 'itemId8'

result = orders_controller.get_order_item(
    order_id,
    item_id
)
print(result)
```


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

## Authentication

This endpoint requires [httpBasic](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `page` | `int` | Query, Optional | Page number |
| `size` | `int` | Query, Optional | Page size |
| `code` | `str` | Query, Optional | Filter for order's code |
| `status` | `str` | Query, Optional | Filter for order's status |
| `created_since` | `datetime` | Query, Optional | Filter for order's creation date start range |
| `created_until` | `datetime` | Query, Optional | Filter for order's creation date end range |
| `customer_id` | `str` | Query, Optional | Filter for order's customer id |

## Response Type

**200**

[`ListOrderResponse`](../../doc/models/list-order-response.md)

## Example Usage

```python
result = orders_controller.get_orders()
print(result)
```


# Update Order Item

```python
def update_order_item(self,
                     order_id,
                     item_id,
                     request,
                     idempotency_key=None)
```

## Authentication

This endpoint requires [httpBasic](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `order_id` | `str` | Template, Required | Order Id |
| `item_id` | `str` | Template, Required | Item Id |
| `request` | [`UpdateOrderItemRequest`](../../doc/models/update-order-item-request.md) | Body, Required | Item Model |
| `idempotency_key` | `str` | Header, Optional | - |

## Response Type

**200**

[`GetOrderItemResponse`](../../doc/models/get-order-item-response.md)

## Example Usage

```python
order_id = 'orderId2'

item_id = 'itemId8'

request = UpdateOrderItemRequest(
    amount=242,
    description='description6',
    quantity=100,
    category='category4'
)

result = orders_controller.update_order_item(
    order_id,
    item_id,
    request
)
print(result)
```


# Update Order Metadata

Updates the metadata from an order

```python
def update_order_metadata(self,
                         order_id,
                         request,
                         idempotency_key=None)
```

## Authentication

This endpoint requires [httpBasic](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `order_id` | `str` | Template, Required | The order id |
| `request` | [`UpdateMetadataRequest`](../../doc/models/update-metadata-request.md) | Body, Required | Request for updating the order metadata |
| `idempotency_key` | `str` | Header, Optional | - |

## Response Type

**200**

[`GetOrderResponse`](../../doc/models/get-order-response.md)

## Example Usage

```python
order_id = 'order_id6'

request = UpdateMetadataRequest(
    metadata={
        'key0': 'metadata3'
    }
)

result = orders_controller.update_order_metadata(
    order_id,
    request
)
print(result)
```

