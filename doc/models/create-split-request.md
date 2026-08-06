
# Create Split Request

Split

## Structure

`CreateSplitRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | `str` | Required | Split type |
| `amount` | `int` | Required | Amount |
| `recipient_id` | `str` | Required | Recipient id |
| `options` | [`CreateSplitOptionsRequest`](../../doc/models/create-split-options-request.md) | Optional | The split options request |
| `split_rule_id` | `str` | Optional | Rule code used in cancellation. |

## Example

```python
from pagarmeapisdk.models.create_split_options_request import CreateSplitOptionsRequest
from pagarmeapisdk.models.create_split_request import CreateSplitRequest

create_split_request = CreateSplitRequest(
    mtype='type8',
    amount=206,
    recipient_id='recipient_id8',
    options=CreateSplitOptionsRequest(),
    split_rule_id='split_rule_id4'
)
```

