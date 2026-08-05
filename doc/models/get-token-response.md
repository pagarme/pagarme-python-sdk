
# Get Token Response

Token data

## Structure

`GetTokenResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | - |
| `mtype` | `str` | Optional | - |
| `created_at` | `datetime` | Optional | - |
| `expires_at` | `str` | Optional | - |
| `card` | [`GetCardTokenResponse`](../../doc/models/get-card-token-response.md) | Optional | - |

## Example

```python
import dateutil.parser

from pagarmeapisdk.models.get_token_response import GetTokenResponse

get_token_response = GetTokenResponse(
    id='id2',
    mtype='type8',
    created_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    expires_at='expires_at4',
    card=None
)
```

