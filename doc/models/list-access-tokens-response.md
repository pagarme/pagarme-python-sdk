
# List Access Tokens Response

Response object for listing access tokens

## Structure

`ListAccessTokensResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `data` | [`List[GetAccessTokenResponse]`](../../doc/models/get-access-token-response.md) | Optional | The access token objects |
| `paging` | [`PagingResponse`](../../doc/models/paging-response.md) | Optional | Paging object |

## Example

```python
from pagarmeapisdk.models.list_access_tokens_response import ListAccessTokensResponse

list_access_tokens_response = ListAccessTokensResponse(
    data=[
        None
    ],
    paging=None
)
```

