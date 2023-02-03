
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
  "id": null,
  "holder_name": null,
  "holder_type": null,
  "bank": null,
  "branch_number": null,
  "branch_check_digit": null,
  "account_number": null,
  "account_check_digit": null,
  "type": null,
  "status": null,
  "created_at": null,
  "updated_at": null,
  "deleted_at": null,
  "recipient": null,
  "metadata": null,
  "pix_key": null
}
```

