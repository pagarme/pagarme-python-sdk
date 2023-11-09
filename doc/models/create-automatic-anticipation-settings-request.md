
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

## Example (as JSON)

```json
{
  "enabled": false,
  "type": "type8",
  "volume_percentage": 208,
  "delay": 82,
  "days": [
    58,
    59
  ]
}
```

