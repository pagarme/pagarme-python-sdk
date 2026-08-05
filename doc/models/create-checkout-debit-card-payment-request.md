
# Create Checkout Debit Card Payment Request

Checkout credit card payment request

## Structure

`CreateCheckoutDebitCardPaymentRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `statement_descriptor` | `str` | Optional | Card invoice text descriptor |
| `authentication` | [`CreatePaymentAuthenticationRequest`](../../doc/models/create-payment-authentication-request.md) | Required | Creates payment authentication |

## Example

```python
from pagarmeapisdk.models.create_checkout_debit_card_payment_request import CreateCheckoutDebitCardPaymentRequest
from pagarmeapisdk.models.create_payment_authentication_request import CreatePaymentAuthenticationRequest
from pagarmeapisdk.models.create_three_d_secure_request import CreateThreeDSecureRequest

create_checkout_debit_card_payment_request = CreateCheckoutDebitCardPaymentRequest(
    authentication=CreatePaymentAuthenticationRequest(
        mtype=None,
        threed_secure=CreateThreeDSecureRequest(
            mpi=None
        )
    ),
    statement_descriptor='statement_descriptor8'
)
```

