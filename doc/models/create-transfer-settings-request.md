
# Create Transfer Settings Request

Informações de transferência do recebedor

## Structure

`CreateTransferSettingsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transfer_enabled` | `bool` | Required | - |
| `transfer_interval` | `str` | Required | - |
| `transfer_day` | `int` | Required | - |

## Example (as JSON)

```json
{
  "transfer_enabled": false,
  "transfer_interval": "transfer_interval4",
  "transfer_day": 82
}
```

