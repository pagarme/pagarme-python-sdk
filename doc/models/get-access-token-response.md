
# Get Access Token Response

Response object for getting a access token

## Structure

`GetAccessTokenResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | - |
| `code` | `str` | Optional | - |
| `status` | `str` | Optional | - |
| `created_at` | `datetime` | Optional | - |
| `customer` | [`GetCustomerResponse`](../../doc/models/get-customer-response.md) | Optional | - |

## Example

```python
import dateutil.parser

from pagarmeapisdk.models.get_access_token_response import GetAccessTokenResponse

get_access_token_response = GetAccessTokenResponse(
    id='id8',
    code='code6',
    status='status0',
    created_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    customer=None
)
```

