
# Update Subscription Split Request

## Structure

`UpdateSubscriptionSplitRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enabled` | `bool` | Required | Defines if the split is enabled |
| `rules` | [`List[CreateSplitRequest]`](../../doc/models/create-split-request.md) | Required | Split |

## Example

```python
from pagarmeapisdk.models.update_subscription_split_request import UpdateSubscriptionSplitRequest

update_subscription_split_request = UpdateSubscriptionSplitRequest(
    enabled=None,
    rules=[
        None
    ]
)
```

