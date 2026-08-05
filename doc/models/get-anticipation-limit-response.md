
# Get Anticipation Limit Response

Anticipation limit

## Structure

`GetAnticipationLimitResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | `int` | Optional | Amount |
| `anticipation_fee` | `int` | Optional | Anticipation fee |

## Example

```python
from pagarmeapisdk.models.get_anticipation_limit_response import GetAnticipationLimitResponse

get_anticipation_limit_response = GetAnticipationLimitResponse(
    amount=8,
    anticipation_fee=170
)
```

