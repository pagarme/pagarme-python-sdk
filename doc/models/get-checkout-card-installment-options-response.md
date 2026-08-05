
# Get Checkout Card Installment Options Response

## Structure

`GetCheckoutCardInstallmentOptionsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `number` | `int` | Required | Número de parcelas |
| `total` | `int` | Required | Valor total da compra |

## Example

```python
from pagarmeapisdk.models.get_checkout_card_installment_options_response import GetCheckoutCardInstallmentOptionsResponse

get_checkout_card_installment_options_response = GetCheckoutCardInstallmentOptionsResponse(
    number=76,
    total=184
)
```

