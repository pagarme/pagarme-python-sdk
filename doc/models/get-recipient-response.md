
# Get Recipient Response

Recipient response

## Structure

`GetRecipientResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Optional | Id |
| `name` | `string` | Optional | Name |
| `email` | `string` | Optional | Email |
| `document` | `string` | Optional | Document |
| `description` | `string` | Optional | Description |
| `mtype` | `string` | Optional | Type |
| `status` | `string` | Optional | Status |
| `created_at` | `datetime` | Optional | Creation date |
| `updated_at` | `datetime` | Optional | Last update date |
| `deleted_at` | `datetime` | Optional | Deletion date |
| `default_bank_account` | [`GetBankAccountResponse`](../../doc/models/get-bank-account-response.md) | Optional | Default bank account |
| `gateway_recipients` | [`List of GetGatewayRecipientResponse`](../../doc/models/get-gateway-recipient-response.md) | Optional | Info about the recipient on the gateway |
| `metadata` | `dict` | Optional | Metadata |
| `automatic_anticipation_settings` | [`GetAutomaticAnticipationResponse`](../../doc/models/get-automatic-anticipation-response.md) | Optional | - |
| `transfer_settings` | [`GetTransferSettingsResponse`](../../doc/models/get-transfer-settings-response.md) | Optional | - |
| `code` | `string` | Optional | Recipient code |
| `payment_mode` | `string` | Optional | Payment mode<br>**Default**: `'bank_transfer'` |

## Example (as JSON)

```json
{
  "payment_mode": "bank_transfer",
  "id": "id0",
  "name": "name0",
  "email": "email6",
  "document": "document6",
  "description": "description0"
}
```

