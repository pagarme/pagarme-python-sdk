
# Create Subscription Split Request

## Structure

`CreateSubscriptionSplitRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enabled` | `bool` | Required | Defines if the split is enabled |
| `rules` | [`List[CreateSplitRequest]`](../../doc/models/create-split-request.md) | Required | Split |

## Example

```python
from pagarmeapisdk.models.create_subscription_split_request import CreateSubscriptionSplitRequest

create_subscription_split_request = CreateSubscriptionSplitRequest(
    enabled=None,
    rules=[
        None
    ]
)
```

