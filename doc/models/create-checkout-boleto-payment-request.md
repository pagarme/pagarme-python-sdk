
# Create Checkout Boleto Payment Request

## Structure

`CreateCheckoutBoletoPaymentRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `bank` | `str` | Required | Bank identifier |
| `instructions` | `str` | Required | Instructions |
| `due_at` | `datetime` | Required | Due date |

## Example

```python
import dateutil.parser

from pagarmeapisdk.models.create_checkout_boleto_payment_request import CreateCheckoutBoletoPaymentRequest

create_checkout_boleto_payment_request = CreateCheckoutBoletoPaymentRequest(
    bank='bank6',
    instructions='instructions4',
    due_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
)
```

