
# Update Automatic Anticipation Settings Request

## Structure

`UpdateAutomaticAnticipationSettingsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enabled` | `bool` | Optional | - |
| `mtype` | `str` | Optional | - |
| `volume_percentage` | `int` | Optional | - |
| `delay` | `int` | Optional | - |
| `days` | `int` | Optional | - |

## Example

```python
from pagarmeapisdk.models.update_automatic_anticipation_settings_request import UpdateAutomaticAnticipationSettingsRequest

update_automatic_anticipation_settings_request = UpdateAutomaticAnticipationSettingsRequest(
    enabled=False,
    mtype='type2',
    volume_percentage=146,
    delay=144,
    days=52
)
```

