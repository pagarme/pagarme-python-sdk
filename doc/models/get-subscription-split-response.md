
# Get Subscription Split Response

## Structure

`GetSubscriptionSplitResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enabled` | `bool` | Optional | Defines if the split is enabled |
| `rules` | [`List[GetSplitResponse]`](../../doc/models/get-split-response.md) | Optional | Split |

## Example

```python
from pagarmeapisdk.models.get_subscription_split_response import GetSubscriptionSplitResponse

get_subscription_split_response = GetSubscriptionSplitResponse(
    enabled=False,
    rules=[
        None
    ]
)
```

