
# Create Bank Transfer Payment Request

Request for creating a bank transfer payment

## Structure

`CreateBankTransferPaymentRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `bank` | `str` | Required | Bank |
| `retries` | `int` | Required | Number of retries |

## Example

```python
from pagarmeapisdk.models.create_bank_transfer_payment_request import CreateBankTransferPaymentRequest

create_bank_transfer_payment_request = CreateBankTransferPaymentRequest(
    bank='bank6',
    retries=114
)
```

