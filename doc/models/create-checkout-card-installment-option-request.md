
# Create Checkout Card Installment Option Request

Options for card installment

## Structure

`CreateCheckoutCardInstallmentOptionRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `number` | `int` | Required | Installment quantity |
| `total` | `int` | Required | Total amount |

## Example

```python
from pagarmeapisdk.models.create_checkout_card_installment_option_request import CreateCheckoutCardInstallmentOptionRequest

create_checkout_card_installment_option_request = CreateCheckoutCardInstallmentOptionRequest(
    number=170,
    total=22
)
```

