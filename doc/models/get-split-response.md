
# Get Split Response

Split response

## Structure

`GetSplitResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | `str` | Optional | Type |
| `amount` | `int` | Optional | Amount |
| `recipient` | [`GetRecipientResponse`](../../doc/models/get-recipient-response.md) | Optional | Recipient |
| `gateway_id` | `str` | Optional | The split rule gateway id |
| `options` | [`GetSplitOptionsResponse`](../../doc/models/get-split-options-response.md) | Optional | - |
| `id` | `str` | Optional | - |

## Example

```python
from pagarmeapisdk.models.get_split_response import GetSplitResponse

get_split_response = GetSplitResponse(
    mtype='type4',
    amount=192,
    recipient=None,
    gateway_id='gateway_id4',
    options=None
)
```

