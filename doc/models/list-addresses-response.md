
# List Addresses Response

Response object for listing addresses

## Structure

`ListAddressesResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `data` | [`List[GetAddressResponse]`](../../doc/models/get-address-response.md) | Optional | The address objects |
| `paging` | [`PagingResponse`](../../doc/models/paging-response.md) | Optional | Paging object |

## Example

```python
from pagarmeapisdk.models.get_address_response import GetAddressResponse
from pagarmeapisdk.models.list_addresses_response import ListAddressesResponse

list_addresses_response = ListAddressesResponse(
    data=[
        None,
        GetAddressResponse(),
        GetAddressResponse()
    ],
    paging=None
)
```

