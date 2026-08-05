
# List Subscriptions Response

Response object for listing subscriptions

## Structure

`ListSubscriptionsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `data` | [`List[GetSubscriptionResponse]`](../../doc/models/get-subscription-response.md) | Optional | The subscription objects |
| `paging` | [`PagingResponse`](../../doc/models/paging-response.md) | Optional | Paging object |

## Example

```python
from pagarmeapisdk.models.get_subscription_response import GetSubscriptionResponse
from pagarmeapisdk.models.list_subscriptions_response import ListSubscriptionsResponse

list_subscriptions_response = ListSubscriptionsResponse(
    data=[
        None,
        GetSubscriptionResponse(),
        GetSubscriptionResponse()
    ],
    paging=None
)
```

