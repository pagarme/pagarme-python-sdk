
# Create Automatic Anticipation Settings Request

## Structure

`CreateAutomaticAnticipationSettingsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enabled` | `bool` | Required | - |
| `mtype` | `str` | Required | - |
| `volume_percentage` | `int` | Required | - |
| `delay` | `int` | Required | - |
| `days` | `List[int]` | Required | - |

## Example

```python
from pagarmeapisdk.models.create_automatic_anticipation_settings_request import CreateAutomaticAnticipationSettingsRequest

create_automatic_anticipation_settings_request = CreateAutomaticAnticipationSettingsRequest(
    enabled=False,
    mtype='type8',
    volume_percentage=194,
    delay=96,
    days=[
        72,
        73
    ]
)
```

