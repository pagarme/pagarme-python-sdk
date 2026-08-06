
# Create Cash Payment Request

## Structure

`CreateCashPaymentRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `description` | `str` | Required | Description |
| `confirm` | `bool` | Required | Indicates whether cash collection will be confirmed in the act of creation |

## Example

```python
from pagarmeapisdk.models.create_cash_payment_request import CreateCashPaymentRequest

create_cash_payment_request = CreateCashPaymentRequest(
    description='description8',
    confirm=False
)
```

