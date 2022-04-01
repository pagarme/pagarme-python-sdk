
# Get Bank Account Response

## Structure

`GetBankAccountResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Required | Id |
| `holder_name` | `string` | Required | Holder name |
| `holder_type` | `string` | Required | Holder type |
| `bank` | `string` | Required | Bank |
| `branch_number` | `string` | Required | Branch number |
| `branch_check_digit` | `string` | Required | Branch check digit |
| `account_number` | `string` | Required | Account number |
| `account_check_digit` | `string` | Required | Account check digit |
| `mtype` | `string` | Required | Bank account type |
| `status` | `string` | Required | Bank account status |
| `created_at` | `datetime` | Required | Creation date |
| `updated_at` | `datetime` | Required | Last update date |
| `deleted_at` | `datetime` | Required | Deletion date |
| `recipient` | [`GetRecipientResponse`](../../doc/models/get-recipient-response.md) | Optional | Recipient |
| `metadata` | `dict` | Required | Metadata |
| `pix_key` | `string` | Required | Pix Key |

## Example (as JSON)

```json
{
  "id": "id0",
  "holder_name": "holder_name4",
  "holder_type": "holder_type2",
  "bank": "bank8",
  "branch_number": "branch_number6",
  "branch_check_digit": "branch_check_digit4",
  "account_number": "account_number0",
  "account_check_digit": "account_check_digit6",
  "type": "type0",
  "status": "status8",
  "created_at": "2016-03-13T12:52:32.123Z",
  "updated_at": "2016-03-13T12:52:32.123Z",
  "deleted_at": "2016-03-13T12:52:32.123Z",
  "recipient": null,
  "metadata": {
    "key0": "metadata3",
    "key1": "metadata4",
    "key2": "metadata5"
  },
  "pix_key": "pix_key6"
}
```

