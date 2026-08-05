
# Create Order Request

Request for creating an order

## Structure

`CreateOrderRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `items` | [`List[CreateOrderItemRequest]`](../../doc/models/create-order-item-request.md) | Required | Items |
| `customer` | [`CreateCustomerRequest`](../../doc/models/create-customer-request.md) | Required | Customer |
| `payments` | [`List[CreatePaymentRequest]`](../../doc/models/create-payment-request.md) | Required | Payment data |
| `code` | `str` | Required | The order code |
| `customer_id` | `str` | Optional | The customer id |
| `shipping` | [`CreateShippingRequest`](../../doc/models/create-shipping-request.md) | Optional | Shipping data |
| `metadata` | `Dict[str, str]` | Optional | Metadata |
| `antifraud_enabled` | `bool` | Optional | Defines whether the order will go through anti-fraud |
| `ip` | `str` | Optional | Ip address |
| `session_id` | `str` | Optional | Session id |
| `location` | [`CreateLocationRequest`](../../doc/models/create-location-request.md) | Optional | Request's location |
| `device` | [`CreateDeviceRequest`](../../doc/models/create-device-request.md) | Optional | Device's informations |
| `closed` | `bool` | Required | **Default**: `True` |
| `currency` | `str` | Optional | Currency |
| `antifraud` | [`CreateAntifraudRequest`](../../doc/models/create-antifraud-request.md) | Optional | - |
| `submerchant` | [`CreateSubMerchantRequest`](../../doc/models/create-sub-merchant-request.md) | Optional | SubMerchant |

## Example

```python
from pagarmeapisdk.models.create_address_request import CreateAddressRequest
from pagarmeapisdk.models.create_customer_request import CreateCustomerRequest
from pagarmeapisdk.models.create_order_request import CreateOrderRequest
from pagarmeapisdk.models.create_phones_request import CreatePhonesRequest
from pagarmeapisdk.models.create_shipping_request import CreateShippingRequest

create_order_request = CreateOrderRequest(
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
        code=None,
        gender='gender6',
        document_type='document_type8'
    ),
    payments=[
        None
    ],
    code=None,
    closed=True,
    customer_id='customer_id0',
    shipping=CreateShippingRequest(
        amount=None,
        description=None,
        recipient_name=None,
        recipient_phone=None,
        address_id=None,
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
        mtype=None
    ),
    metadata={
        'key0': 'metadata9'
    },
    antifraud_enabled=False,
    ip='ip6'
)
```

