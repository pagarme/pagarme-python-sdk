
# Get Transfer Settings Response

## Structure

`GetTransferSettingsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transfer_enabled` | `bool` | Optional | - |
| `transfer_interval` | `str` | Optional | - |
| `transfer_day` | `int` | Optional | - |

## Example

```python
from pagarmeapisdk.models.get_transfer_settings_response import GetTransferSettingsResponse

get_transfer_settings_response = GetTransferSettingsResponse(
    transfer_enabled=False,
    transfer_interval='transfer_interval6',
    transfer_day=130
)
```

