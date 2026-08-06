
# Create Access Token Request

Request for creating a new Access Token

## Structure

`CreateAccessTokenRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `expires_in` | `int` | Optional | Minutes to expire the token |

## Example

```python
from pagarmeapisdk.models.create_access_token_request import CreateAccessTokenRequest

create_access_token_request = CreateAccessTokenRequest(
    expires_in=188
)
```

