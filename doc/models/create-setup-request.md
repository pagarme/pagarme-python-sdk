
# Create Setup Request

Request for creating a Setup for a subscription. The setup is an order that will be created at the subscription creation.

## Structure

`CreateSetupRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | `int` | Required | Setup amount |
| `description` | `str` | Required | Description |
| `payment` | [`CreatePaymentRequest`](../../doc/models/create-payment-request.md) | Required | Payment data |

## Example

```python
from pagarmeapisdk.models.create_payment_request import CreatePaymentRequest
from pagarmeapisdk.models.create_setup_request import CreateSetupRequest

create_setup_request = CreateSetupRequest(
    amount=242,
    description='description4',
    payment=CreatePaymentRequest(
        payment_method=None
    )
)
```

