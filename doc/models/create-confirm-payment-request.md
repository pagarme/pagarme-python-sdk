
# Create Confirm Payment Request

## Structure

`CreateConfirmPaymentRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `description` | `str` | Required | Description |
| `amount` | `int` | Optional | Amount |
| `code` | `str` | Required | Code reference |

## Example

```python
from pagarmeapisdk.models.create_confirm_payment_request import CreateConfirmPaymentRequest

create_confirm_payment_request = CreateConfirmPaymentRequest(
    description='description4',
    code='Code6',
    amount=88
)
```

