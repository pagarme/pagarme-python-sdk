
# List Cards Response

Response object for listing cards

## Structure

`ListCardsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `data` | [`List[GetCardResponse]`](../../doc/models/get-card-response.md) | Optional | The card objects |
| `paging` | [`PagingResponse`](../../doc/models/paging-response.md) | Optional | Paging object |

## Example

```python
from pagarmeapisdk.models.get_card_response import GetCardResponse
from pagarmeapisdk.models.list_cards_response import ListCardsResponse

list_cards_response = ListCardsResponse(
    data=[
        None,
        GetCardResponse(),
        GetCardResponse()
    ],
    paging=None
)
```

