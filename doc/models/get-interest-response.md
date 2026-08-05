
# Get Interest Response

Interest Response

## Structure

`GetInterestResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `days` | `int` | Optional | Days |
| `mtype` | `str` | Optional | Type |
| `amount` | `int` | Optional | Amount |

## Example

```python
from pagarmeapisdk.models.get_interest_response import GetInterestResponse

get_interest_response = GetInterestResponse(
    days=102,
    mtype='"percentage" or "flat"',
    amount=176
)
```

