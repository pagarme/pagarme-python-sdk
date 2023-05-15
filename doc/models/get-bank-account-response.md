
# Get Bank Account Response

## Structure

`GetBankAccountResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Optional | Id |
| `holder_name` | `string` | Optional | Holder name |
| `holder_type` | `string` | Optional | Holder type |
| `bank` | `string` | Optional | Bank |
| `branch_number` | `string` | Optional | Branch number |
| `branch_check_digit` | `string` | Optional | Branch check digit |
| `account_number` | `string` | Optional | Account number |
| `account_check_digit` | `string` | Optional | Account check digit |
| `mtype` | `string` | Optional | Bank account type |
| `status` | `string` | Optional | Bank account status |
| `created_at` | `datetime` | Optional | Creation date |
| `updated_at` | `datetime` | Optional | Last update date |
| `deleted_at` | `datetime` | Optional | Deletion date |
| `recipient` | [`GetRecipientResponse`](../../doc/models/get-recipient-response.md) | Optional | Recipient |
| `metadata` | `dict` | Optional | Metadata |
| `pix_key` | `string` | Optional | Pix Key |

## Example (as JSON)

```json
{
  "id": "id0",
  "holder_name": "holder_name4",
  "holder_type": "holder_type2",
  "bank": "bank8",
  "branch_number": "branch_number6"
}
```

