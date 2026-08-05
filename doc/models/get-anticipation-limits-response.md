
# Get Anticipation Limits Response

Anticipation limits

## Structure

`GetAnticipationLimitsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `max` | [`GetAnticipationLimitResponse`](../../doc/models/get-anticipation-limit-response.md) | Optional | Max limit |
| `min` | [`GetAnticipationLimitResponse`](../../doc/models/get-anticipation-limit-response.md) | Optional | Min limit |

## Example

```python
from pagarmeapisdk.models.get_anticipation_limits_response import GetAnticipationLimitsResponse

get_anticipation_limits_response = GetAnticipationLimitsResponse(
    max=None,
    min=None
)
```

