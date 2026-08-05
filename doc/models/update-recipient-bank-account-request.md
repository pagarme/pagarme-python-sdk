
# Update Recipient Bank Account Request

Updates the default bank account for a recipient

## Structure

`UpdateRecipientBankAccountRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `bank_account` | [`CreateBankAccountRequest`](../../doc/models/create-bank-account-request.md) | Required | Bank account |
| `payment_mode` | `str` | Required | Payment mode<br><br>**Default**: `"bank_transfer"` |

## Example

```python
from pagarmeapisdk.models.create_bank_account_request import CreateBankAccountRequest
from pagarmeapisdk.models.update_recipient_bank_account_request import UpdateRecipientBankAccountRequest

update_recipient_bank_account_request = UpdateRecipientBankAccountRequest(
    bank_account=CreateBankAccountRequest(
        holder_name=None,
        holder_type=None,
        holder_document=None,
        bank=None,
        branch_number=None,
        account_number=None,
        account_check_digit=None,
        mtype=None,
        metadata={}
    ),
    payment_mode='bank_transfer'
)
```

