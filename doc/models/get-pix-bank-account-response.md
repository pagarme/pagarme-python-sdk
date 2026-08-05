
# Get Pix Bank Account Response

Payer's bank details.

## Structure

`GetPixBankAccountResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `bank_name` | `str` | Optional | - |
| `ispb` | `str` | Optional | - |
| `branch_code` | `str` | Optional | - |
| `account_number` | `str` | Optional | - |

## Example

```python
from pagarmeapisdk.models.get_pix_bank_account_response import GetPixBankAccountResponse

get_pix_bank_account_response = GetPixBankAccountResponse(
    bank_name='bank_name0',
    ispb='ispb8',
    branch_code='branch_code2',
    account_number='account_number4'
)
```

