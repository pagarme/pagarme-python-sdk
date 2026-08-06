
# Update Transfer Settings Request

## Structure

`UpdateTransferSettingsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transfer_enabled` | `str` | Required | - |
| `transfer_interval` | `str` | Required | - |
| `transfer_day` | `str` | Required | - |

## Example

```python
from pagarmeapisdk.models.update_transfer_settings_request import UpdateTransferSettingsRequest

update_transfer_settings_request = UpdateTransferSettingsRequest(
    transfer_enabled='transfer_enabled4',
    transfer_interval='transfer_interval8',
    transfer_day='transfer_day8'
)
```

