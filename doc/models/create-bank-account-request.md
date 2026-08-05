
# Create Bank Account Request

Request for creating a bank account

## Structure

`CreateBankAccountRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `holder_name` | `str` | Required | Bank account holder name |
| `holder_type` | `str` | Required | Bank account holder type |
| `holder_document` | `str` | Required | Bank account holder document |
| `bank` | `str` | Required | Bank |
| `branch_number` | `str` | Required | Branch number |
| `branch_check_digit` | `str` | Optional | Branch check digit |
| `account_number` | `str` | Required | Account number |
| `account_check_digit` | `str` | Required | Account check digit |
| `mtype` | `str` | Required | Bank account type |
| `metadata` | `Dict[str, str]` | Required | Metadata |
| `pix_key` | `str` | Optional | Pix key |

## Example

```python
from pagarmeapisdk.models.create_bank_account_request import CreateBankAccountRequest

create_bank_account_request = CreateBankAccountRequest(
    holder_name='holder_name6',
    holder_type='holder_type2',
    holder_document='holder_document6',
    bank='bank8',
    branch_number='branch_number6',
    account_number='account_number0',
    account_check_digit='account_check_digit6',
    mtype='type0',
    metadata={
        'key0': 'metadata3'
    },
    branch_check_digit='branch_check_digit4',
    pix_key='pix_key6'
)
```

