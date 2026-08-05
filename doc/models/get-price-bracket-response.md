
# Get Price Bracket Response

Response object for getting a price bracket

## Structure

`GetPriceBracketResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `start_quantity` | `int` | Optional | - |
| `price` | `int` | Optional | - |
| `end_quantity` | `int` | Optional | - |
| `overage_price` | `int` | Optional | - |

## Example

```python
from pagarmeapisdk.models.get_price_bracket_response import GetPriceBracketResponse

get_price_bracket_response = GetPriceBracketResponse(
    start_quantity=206,
    price=112,
    end_quantity=214,
    overage_price=228
)
```

