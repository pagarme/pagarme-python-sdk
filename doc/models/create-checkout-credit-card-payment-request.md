
# Create Checkout Credit Card Payment Request

Checkout card payment request

## Structure

`CreateCheckoutCreditCardPaymentRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `statement_descriptor` | `str` | Optional | Card invoice text descriptor |
| `installments` | [`List[CreateCheckoutCardInstallmentOptionRequest]`](../../doc/models/create-checkout-card-installment-option-request.md) | Optional | Payment installment options |
| `authentication` | [`CreatePaymentAuthenticationRequest`](../../doc/models/create-payment-authentication-request.md) | Optional | Creates payment authentication |
| `capture` | `bool` | Optional | Authorize and capture? |

## Example

```python
from pagarmeapisdk.models.create_checkout_credit_card_payment_request import CreateCheckoutCreditCardPaymentRequest
from pagarmeapisdk.models.create_payment_authentication_request import CreatePaymentAuthenticationRequest
from pagarmeapisdk.models.create_three_d_secure_request import CreateThreeDSecureRequest

create_checkout_credit_card_payment_request = CreateCheckoutCreditCardPaymentRequest(
    statement_descriptor='statement_descriptor6',
    installments=[
        None
    ],
    authentication=CreatePaymentAuthenticationRequest(
        mtype=None,
        threed_secure=CreateThreeDSecureRequest(
            mpi=None
        )
    ),
    capture=False
)
```

