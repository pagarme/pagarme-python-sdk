
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

## Example (as JSON)

```json
{
  "holder_name": "holder_name4",
  "holder_type": "holder_type0",
  "holder_document": "holder_document8",
  "bank": "bank6",
  "branch_number": "branch_number4",
  "branch_check_digit": "branch_check_digit4",
  "account_number": "account_number8",
  "account_check_digit": "account_check_digit4",
  "type": "type2",
  "metadata": {
    "key0": "metadata5",
    "key1": "metadata6",
    "key2": "metadata7"
  },
  "pix_key": "pix_key8"
}
```

