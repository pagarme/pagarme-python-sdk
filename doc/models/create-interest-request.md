
# Create Interest Request

Interest Request

## Structure

`CreateInterestRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `days` | `int` | Required | Days |
| `mtype` | `str` | Required | Type |
| `amount` | `int` | Required | Amount |

## Example

```python
from pagarmeapisdk.models.create_interest_request import CreateInterestRequest

create_interest_request = CreateInterestRequest(
    days=None,
    mtype='"percentage" or "flat"',
    amount=None
)
```

