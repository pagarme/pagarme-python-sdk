
# Get Checkout Debit Card Payment Response

## Structure

`GetCheckoutDebitCardPaymentResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `statement_descriptor` | `str` | Optional | Descrição na fatura |
| `authentication` | [`GetPaymentAuthenticationResponse`](../../doc/models/get-payment-authentication-response.md) | Optional | Payment Authentication response object data |

## Example

```python
from pagarmeapisdk.models.get_checkout_debit_card_payment_response import GetCheckoutDebitCardPaymentResponse

get_checkout_debit_card_payment_response = GetCheckoutDebitCardPaymentResponse(
    statement_descriptor='statement_descriptor8',
    authentication=None
)
```

