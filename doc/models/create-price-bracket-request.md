
# Create Price Bracket Request

Request for creating a price bracket

## Structure

`CreatePriceBracketRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `start_quantity` | `int` | Required | Start quantity |
| `price` | `int` | Required | Price |
| `end_quantity` | `int` | Optional | End quantity |
| `overage_price` | `int` | Optional | Overage price |

## Example

```python
from pagarmeapisdk.models.create_price_bracket_request import CreatePriceBracketRequest

create_price_bracket_request = CreatePriceBracketRequest(
    start_quantity=216,
    price=102,
    end_quantity=224,
    overage_price=238
)
```

