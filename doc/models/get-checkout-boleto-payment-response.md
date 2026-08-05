
# Get Checkout Boleto Payment Response

## Structure

`GetCheckoutBoletoPaymentResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `due_at` | `datetime` | Optional | Data de vencimento do boleto |
| `instructions` | `str` | Optional | Instruções do boleto |

## Example

```python
import dateutil.parser

from pagarmeapisdk.models.get_checkout_boleto_payment_response import GetCheckoutBoletoPaymentResponse

get_checkout_boleto_payment_response = GetCheckoutBoletoPaymentResponse(
    due_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    instructions='instructions2'
)
```

