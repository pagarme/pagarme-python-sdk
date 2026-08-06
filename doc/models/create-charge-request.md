
# Create Charge Request

Request for creating a new charge

## Structure

`CreateChargeRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `code` | `str` | Optional | Code |
| `amount` | `int` | Required | The amount of the charge, in cents |
| `customer_id` | `str` | Optional | The customer's id |
| `customer` | [`CreateCustomerRequest`](../../doc/models/create-customer-request.md) | Optional | Customer data |
| `payment` | [`CreatePaymentRequest`](../../doc/models/create-payment-request.md) | Required | Payment data |
| `metadata` | `Dict[str, str]` | Optional | Metadata |
| `due_at` | `datetime` | Optional | The charge due date |
| `antifraud` | [`CreateAntifraudRequest`](../../doc/models/create-antifraud-request.md) | Optional | - |
| `order_id` | `str` | Required | Order Id |

## Example

```python
import dateutil.parser

from pagarmeapisdk.models.create_charge_request import CreateChargeRequest
from pagarmeapisdk.models.create_payment_request import CreatePaymentRequest

create_charge_request = CreateChargeRequest(
    amount=156,
    payment=CreatePaymentRequest(
        payment_method=None
    ),
    order_id='order_id0',
    code='code4',
    customer_id='customer_id4',
    customer=None,
    metadata={
        'key0': 'metadata3',
        'key1': 'metadata2'
    },
    due_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
)
```

