
# Get Fine Response

Fine Response

## Structure

`GetFineResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `days` | `int` | Optional | Days |
| `mtype` | `str` | Optional | Type |
| `amount` | `int` | Optional | Amount |

## Example

```python
from pagarmeapisdk.models.get_fine_response import GetFineResponse

get_fine_response = GetFineResponse(
    days=192,
    mtype='"percentage" or "flat"',
    amount=10
)
```

