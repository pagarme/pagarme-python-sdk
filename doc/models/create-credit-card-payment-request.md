
# Create Credit Card Payment Request

The settings for creating a credit card payment

## Structure

`CreateCreditCardPaymentRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `installments` | `int` | Optional | Number of installments<br><br>**Default**: `1` |
| `statement_descriptor` | `str` | Optional | The text that will be shown on the credit card's statement |
| `card` | [`CreateCardRequest`](../../doc/models/create-card-request.md) | Optional | Credit card data |
| `card_id` | `str` | Optional | The credit card id |
| `card_token` | `str` | Optional | - |
| `recurrence` | `bool` | Optional | Indicates a recurrence |
| `capture` | `bool` | Optional | Indicates if the operation should be only authorization or auth and capture.<br><br>**Default**: `True` |
| `extended_limit_enabled` | `bool` | Optional | Indicates whether the extended label (private label) is enabled |
| `extended_limit_code` | `str` | Optional | Extended Limit Code |
| `merchant_category_code` | `int` | Optional | Customer business segment code |
| `authentication` | [`CreatePaymentAuthenticationRequest`](../../doc/models/create-payment-authentication-request.md) | Optional | The payment authentication request |
| `contactless` | [`CreateCardPaymentContactlessRequest`](../../doc/models/create-card-payment-contactless-request.md) | Optional | The Credit card payment contactless request |
| `auto_recovery` | `bool` | Optional | Indicates whether a particular payment will enter the offline retry flow |
| `operation_type` | `str` | Optional | AuthOnly, AuthAndCapture, PreAuth |
| `recurrency_cycle` | `str` | Optional | Defines whether the card has been used one or more times. |
| `payload` | [`CreateCardPayloadRequest`](../../doc/models/create-card-payload-request.md) | Optional | - |
| `initiated_type` | `str` | Optional | - |
| `recurrence_model` | `str` | Optional | - |
| `payment_origin` | [`CreatePaymentOriginRequest`](../../doc/models/create-payment-origin-request.md) | Optional | - |
| `indirect_acceptor` | `str` | Optional | Business model identifier |

## Example

```python
from pagarmeapisdk.models.create_card_request import CreateCardRequest
from pagarmeapisdk.models.create_credit_card_payment_request import CreateCreditCardPaymentRequest

create_credit_card_payment_request = CreateCreditCardPaymentRequest(
    installments=1,
    statement_descriptor='statement_descriptor6',
    card=CreateCardRequest(),
    card_id='card_id2',
    card_token='card_token4',
    capture=True,
    recurrency_cycle='"first" or "subsequent"'
)
```

