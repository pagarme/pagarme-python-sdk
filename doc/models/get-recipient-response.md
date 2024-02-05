
# Get Recipient Response

Recipient response

## Structure

`GetRecipientResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | Id |
| `name` | `str` | Optional | Name |
| `email` | `str` | Optional | Email |
| `document` | `str` | Optional | Document |
| `description` | `str` | Optional | Description |
| `mtype` | `str` | Optional | Type |
| `status` | `str` | Optional | Status |
| `created_at` | `datetime` | Optional | Creation date |
| `updated_at` | `datetime` | Optional | Last update date |
| `deleted_at` | `datetime` | Optional | Deletion date |
| `default_bank_account` | [`GetBankAccountResponse`](../../doc/models/get-bank-account-response.md) | Optional | Default bank account |
| `gateway_recipients` | [`List[GetGatewayRecipientResponse]`](../../doc/models/get-gateway-recipient-response.md) | Optional | Info about the recipient on the gateway |
| `metadata` | `Dict[str, str]` | Optional | Metadata |
| `automatic_anticipation_settings` | [`GetAutomaticAnticipationResponse`](../../doc/models/get-automatic-anticipation-response.md) | Optional | - |
| `transfer_settings` | [`GetTransferSettingsResponse`](../../doc/models/get-transfer-settings-response.md) | Optional | - |
| `code` | `str` | Optional | Recipient code |
| `payment_mode` | `str` | Optional | Payment mode<br>**Default**: `'bank_transfer'` |
| `register_information` | [`GetRegisterInformationResponse`](../../doc/models/get-register-information-response.md) | Optional | - |

## Example (as JSON)

```json
{
  "payment_mode": "bank_transfer",
  "id": "id4",
  "name": "name4",
  "email": "email2",
  "document": "document2",
  "description": "description6"
}
```

