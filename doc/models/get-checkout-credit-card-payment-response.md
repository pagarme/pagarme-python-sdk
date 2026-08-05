
# Get Checkout Credit Card Payment Response

## Structure

`GetCheckoutCreditCardPaymentResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `statement_descriptor` | `str` | Optional | Descrição na fatura |
| `installments` | [`List[GetCheckoutCardInstallmentOptionsResponse]`](../../doc/models/get-checkout-card-installment-options-response.md) | Optional | Parcelas |
| `authentication` | [`GetPaymentAuthenticationResponse`](../../doc/models/get-payment-authentication-response.md) | Optional | Payment Authentication response |

## Example

```python
from pagarmeapisdk.models.get_checkout_card_installment_options_response import GetCheckoutCardInstallmentOptionsResponse
from pagarmeapisdk.models.get_checkout_credit_card_payment_response import GetCheckoutCreditCardPaymentResponse

get_checkout_credit_card_payment_response = GetCheckoutCreditCardPaymentResponse(
    statement_descriptor='statementDescriptor8',
    installments=[
        None,
        GetCheckoutCardInstallmentOptionsResponse(
            number=None,
            total=None
        ),
        GetCheckoutCardInstallmentOptionsResponse(
            number=None,
            total=None
        )
    ],
    authentication=None
)
```

