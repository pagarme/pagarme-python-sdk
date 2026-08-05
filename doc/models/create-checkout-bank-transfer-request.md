
# Create Checkout Bank Transfer Request

Checkout bank transfer payment request

## Structure

`CreateCheckoutBankTransferRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `bank` | `List[str]` | Required | Bank |
| `retries` | `int` | Required | Number of retries for processing |

## Example

```python
from pagarmeapisdk.models.create_checkout_bank_transfer_request import CreateCheckoutBankTransferRequest

create_checkout_bank_transfer_request = CreateCheckoutBankTransferRequest(
    bank=[
        'bank7',
        'bank8',
        'bank9'
    ],
    retries=100
)
```

