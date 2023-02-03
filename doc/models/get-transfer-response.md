
# Get Transfer Response

Transfer response

## Structure

`GetTransferResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Optional | Id |
| `amount` | `int` | Optional | Transfer amount |
| `status` | `string` | Optional | Transfer status |
| `created_at` | `datetime` | Optional | Transfer creation date |
| `updated_at` | `datetime` | Optional | Transfer last update date |
| `bank_account` | [`GetBankAccountResponse`](../../doc/models/get-bank-account-response.md) | Optional | Bank account |
| `metadata` | `dict` | Optional | Metadata |

## Example (as JSON)

```json
{
  "id": null,
  "amount": null,
  "status": null,
  "created_at": null,
  "updated_at": null,
  "bank_account": null,
  "metadata": null
}
```

