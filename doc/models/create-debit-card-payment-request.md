
# Create Debit Card Payment Request

The settings for creating a debit card payment

## Structure

`CreateDebitCardPaymentRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `statement_descriptor` | `str` | Optional | The text that will be shown on the debit card's statement |
| `card` | [`CreateCardRequest`](../../doc/models/create-card-request.md) | Optional | Debit card data |
| `card_id` | `str` | Optional | The debit card id |
| `card_token` | `str` | Optional | The debit card token |
| `recurrence` | `bool` | Optional | Indicates a recurrence |
| `authentication` | [`CreatePaymentAuthenticationRequest`](../../doc/models/create-payment-authentication-request.md) | Optional | The payment authentication request |
| `token` | [`CreateCardPaymentContactlessRequest`](../../doc/models/create-card-payment-contactless-request.md) | Optional | The Debit card payment token request |
| `initiated_type` | `str` | Optional | - |
| `recurrence_model` | `str` | Optional | - |
| `payment_origin` | [`CreatePaymentOriginRequest`](../../doc/models/create-payment-origin-request.md) | Optional | - |

## Example

```python
from pagarmeapisdk.models.create_card_request import CreateCardRequest
from pagarmeapisdk.models.create_debit_card_payment_request import CreateDebitCardPaymentRequest

create_debit_card_payment_request = CreateDebitCardPaymentRequest(
    statement_descriptor='statement_descriptor2',
    card=CreateCardRequest(),
    card_id='card_id8',
    card_token='card_token8',
    recurrence=False
)
```

