
# List Recipient Response

Response for the listing recipient method

## Structure

`ListRecipientResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `data` | [`List[GetRecipientResponse]`](../../doc/models/get-recipient-response.md) | Optional | Recipients |
| `paging` | [`PagingResponse`](../../doc/models/paging-response.md) | Optional | Paging |

## Example

```python
from pagarmeapisdk.models.list_recipient_response import ListRecipientResponse

list_recipient_response = ListRecipientResponse(
    data=[
        None
    ],
    paging=None
)
```

