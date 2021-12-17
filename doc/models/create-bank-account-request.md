
# Create Bank Account Request

Request for creating a bank account

## Structure

`CreateBankAccountRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `holder_name` | `string` | Required | Bank account holder name |
| `holder_type` | `string` | Required | Bank account holder type |
| `holder_document` | `string` | Required | Bank account holder document |
| `bank` | `string` | Required | Bank |
| `branch_number` | `string` | Required | Branch number |
| `branch_check_digit` | `string` | Required | Branch check digit |
| `account_number` | `string` | Required | Account number |
| `account_check_digit` | `string` | Required | Account check digit |
| `mtype` | `string` | Required | Bank account type |
| `metadata` | `dict` | Required | Metadata |
| `pix_key` | `string` | Required | Pix key |

## Example (as JSON)

```json
{
  "holder_name": "holder_name4",
  "holder_type": "holder_type2",
  "holder_document": "holder_document6",
  "bank": "bank8",
  "branch_number": "branch_number6",
  "branch_check_digit": "branch_check_digit4",
  "account_number": "account_number0",
  "account_check_digit": "account_check_digit6",
  "type": "type0",
  "metadata": {
    "key0": "metadata3",
    "key1": "metadata4",
    "key2": "metadata5"
  },
  "pix_key": "pix_key6"
}
```

