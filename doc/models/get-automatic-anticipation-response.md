
# Get Automatic Anticipation Response

## Structure

`GetAutomaticAnticipationResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enabled` | `bool` | Optional | - |
| `mtype` | `str` | Optional | - |
| `volume_percentage` | `int` | Optional | - |
| `delay` | `int` | Optional | - |
| `days` | `List[int]` | Optional | - |

## Example

```python
from pagarmeapisdk.models.get_automatic_anticipation_response import GetAutomaticAnticipationResponse

get_automatic_anticipation_response = GetAutomaticAnticipationResponse(
    enabled=False,
    mtype='type0',
    volume_percentage=114,
    delay=176,
    days=[
        152,
        153,
        154
    ]
)
```

