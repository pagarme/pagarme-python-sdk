# Orders

```python
orders_controller = client.orders
```

## Class Name

`OrdersController`

## Methods

* [Get Orders](../../doc/controllers/orders.md#get-orders)
* [Update Order Item](../../doc/controllers/orders.md#update-order-item)
* [Delete All Order Items](../../doc/controllers/orders.md#delete-all-order-items)
* [Delete Order Item](../../doc/controllers/orders.md#delete-order-item)
* [Close Order](../../doc/controllers/orders.md#close-order)
* [Create Order](../../doc/controllers/orders.md#create-order)
* [Create Order Item](../../doc/controllers/orders.md#create-order-item)
* [Get Order Item](../../doc/controllers/orders.md#get-order-item)
* [Update Order Metadata](../../doc/controllers/orders.md#update-order-metadata)
* [Get Order](../../doc/controllers/orders.md#get-order)


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
print(result)
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

result = orders_controller.delete_order_item(
    order_id,
    item_id
)
print(result)
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

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CreateOrderRequest`](../../doc/models/create-order-request.md) | Body, Required | Request for creating an order |
| `idempotency_key` | `string` | Header, Optional | - |

## Response Type

[`GetOrderResponse`](../../doc/models/get-order-response.md)

## Example Usage

```python
body = CreateOrderRequest(
    items=[
        CreateOrderItemRequest(
            amount=101,
            description='description3',
            quantity=215,
            category='category1'
        ),
        CreateOrderItemRequest(
            amount=102,
            description='description4',
            quantity=216,
            category='category2'
        ),
        CreateOrderItemRequest(
            amount=103,
            description='description5',
            quantity=217,
            category='category3'
        )
    ],
    customer=CreateCustomerRequest(
        name='{\n    "name": "Tony Stark"\n}',
        email='email2',
        document='document2',
        mtype='type6',
        address=CreateAddressRequest(
            street='street0',
            number='number8',
            zip_code='zip_code4',
            neighborhood='neighborhood6',
            city='city0',
            state='state6',
            country='country4',
            complement='complement6',
            metadata={
                "key0": 'metadata7',
                "key1": 'metadata6'
            },
            line_1='line_16',
            line_2='line_28'
        ),
        metadata={
            "key0": 'metadata9',
            "key1": 'metadata0'
        },
        phones=CreatePhonesRequest(),
        code='code2'
    ),
    payments=[
        CreatePaymentRequest(
            payment_method='payment_method0'
        ),
        CreatePaymentRequest(
            payment_method='payment_method9'
        )
    ],
    code='code4',
    metadata={
        "key0": 'metadata7',
        "key1": 'metadata8'
    },
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

result = orders_controller.get_order_item(
    order_id,
    item_id
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

request = UpdateMetadataRequest(
    metadata={
        "key0": 'metadata3'
    }
)

result = orders_controller.update_order_metadata(
    order_id,
    request
)
print(result)
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
print(result)
```

