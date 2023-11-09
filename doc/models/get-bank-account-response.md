
# Get Bank Account Response

## Structure

`GetBankAccountResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | Id |
| `holder_name` | `str` | Optional | Holder name |
| `holder_type` | `str` | Optional | Holder type |
| `bank` | `str` | Optional | Bank |
| `branch_number` | `str` | Optional | Branch number |
| `branch_check_digit` | `str` | Optional | Branch check digit |
| `account_number` | `str` | Optional | Account number |
| `account_check_digit` | `str` | Optional | Account check digit |
| `mtype` | `str` | Optional | Bank account type |
| `status` | `str` | Optional | Bank account status |
| `created_at` | `datetime` | Optional | Creation date |
| `updated_at` | `datetime` | Optional | Last update date |
| `deleted_at` | `datetime` | Optional | Deletion date |
| `recipient` | [`GetRecipientResponse`](../../doc/models/get-recipient-response.md) | Optional | Recipient |
| `metadata` | `Dict[str, str]` | Optional | Metadata |
| `pix_key` | `str` | Optional | Pix Key |

## Example (as JSON)

```json
{
  "id": "id6",
  "holder_name": "holder_name2",
  "holder_type": "holder_type8",
  "bank": "bank4",
  "branch_number": "branch_number2"
}
```

