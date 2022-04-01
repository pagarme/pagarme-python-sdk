
# Get Recipient Response

Recipient response

## Structure

`GetRecipientResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Required | Id |
| `name` | `string` | Required | Name |
| `email` | `string` | Required | Email |
| `document` | `string` | Required | Document |
| `description` | `string` | Required | Description |
| `mtype` | `string` | Required | Type |
| `status` | `string` | Required | Status |
| `created_at` | `datetime` | Required | Creation date |
| `updated_at` | `datetime` | Required | Last update date |
| `deleted_at` | `datetime` | Required | Deletion date |
| `default_bank_account` | [`GetBankAccountResponse`](../../doc/models/get-bank-account-response.md) | Required | Default bank account |
| `gateway_recipients` | [`List of GetGatewayRecipientResponse`](../../doc/models/get-gateway-recipient-response.md) | Required | Info about the recipient on the gateway |
| `metadata` | `dict` | Required | Metadata |
| `automatic_anticipation_settings` | [`GetAutomaticAnticipationResponse`](../../doc/models/get-automatic-anticipation-response.md) | Optional | - |
| `transfer_settings` | [`GetTransferSettingsResponse`](../../doc/models/get-transfer-settings-response.md) | Optional | - |
| `code` | `string` | Required | Recipient code |
| `payment_mode` | `string` | Required | Payment mode<br>**Default**: `'bank_transfer'` |

## Example (as JSON)

```json
{
  "id": null,
  "name": null,
  "email": null,
  "document": null,
  "description": null,
  "type": null,
  "status": null,
  "created_at": null,
  "updated_at": null,
  "deleted_at": null,
  "default_bank_account": null,
  "gateway_recipients": null,
  "metadata": null,
  "code": null,
  "payment_mode": "bank_transfer"
}
```

