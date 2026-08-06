
# Create Token Request

Token data

## Structure

`CreateTokenRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | `str` | Required | Token type<br><br>**Default**: `"card"` |
| `card` | [`CreateCardTokenRequest`](../../doc/models/create-card-token-request.md) | Required | Card data |

## Example

```python
from pagarmeapisdk.models.create_card_token_request import CreateCardTokenRequest
from pagarmeapisdk.models.create_token_request import CreateTokenRequest

create_token_request = CreateTokenRequest(
    mtype='card',
    card=CreateCardTokenRequest(
        number=None,
        holder_name=None,
        exp_month=None,
        exp_year=None,
        cvv=None,
        brand=None,
        label=None
    )
)
```

