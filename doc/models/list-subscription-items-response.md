
# List Subscription Items Response

Response model for listing subscription items

## Structure

`ListSubscriptionItemsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `data` | [`List[GetSubscriptionItemResponse]`](../../doc/models/get-subscription-item-response.md) | Optional | The subscription items |
| `paging` | [`PagingResponse`](../../doc/models/paging-response.md) | Optional | Paging object |

## Example

```python
from pagarmeapisdk.models.list_subscription_items_response import ListSubscriptionItemsResponse

list_subscription_items_response = ListSubscriptionItemsResponse(
    data=[
        None
    ],
    paging=None
)
```

