
# Create Fine Request

Fine Request

## Structure

`CreateFineRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `days` | `int` | Required | Days |
| `mtype` | `str` | Required | Type |
| `amount` | `int` | Required | Amount |

## Example

```python
from pagarmeapisdk.models.create_fine_request import CreateFineRequest

create_fine_request = CreateFineRequest(
    days=None,
    mtype='"percentage" or "flat"',
    amount=None
)
```

