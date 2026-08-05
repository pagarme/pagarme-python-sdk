
# Create Recipient Request

Request for creating a recipient

## Structure

`CreateRecipientRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Optional | Recipient name. Required if the register_information field isn't populated. |
| `email` | `str` | Optional | Recipient email. Required if the register_information field isn't populated. |
| `description` | `str` | Optional | Recipient description |
| `document` | `str` | Optional | Recipient document number. Required if the register_information field isn't populated. |
| `mtype` | `str` | Optional | Recipient type. Required if the register_information field isn't populated. |
| `default_bank_account` | [`CreateBankAccountRequest`](../../doc/models/create-bank-account-request.md) | Required | Bank account |
| `metadata` | `Dict[str, str]` | Required | Metadata |
| `transfer_settings` | [`CreateTransferSettingsRequest`](../../doc/models/create-transfer-settings-request.md) | Optional | Receiver Transfer Information |
| `code` | `str` | Required | Recipient code |
| `payment_mode` | `str` | Required | Payment mode<br><br>**Default**: `"bank_transfer"` |
| `register_information` | [`CreateRegisterInformationBaseRequest`](../../doc/models/create-register-information-base-request.md) | Optional | Register Information |

## Example

```python
from pagarmeapisdk.models.create_bank_account_request import CreateBankAccountRequest
from pagarmeapisdk.models.create_recipient_request import CreateRecipientRequest

create_recipient_request = CreateRecipientRequest(
    default_bank_account=CreateBankAccountRequest(
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
    metadata={},
    code=None,
    payment_mode='bank_transfer',
    name='name6',
    email='email0',
    description='description6',
    document='document0',
    mtype='type4'
)
```

