
# Update Price Bracket Request

Request for updating a price bracket

## Structure

`UpdatePriceBracketRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `start_quantity` | `int` | Required | Start quantity of the bracket |
| `price` | `int` | Required | Price |
| `end_quantity` | `int` | Optional | End quantity of the bracket |
| `overage_price` | `int` | Optional | Overage price |

## Example

```python
from pagarmeapisdk.models.update_price_bracket_request import UpdatePriceBracketRequest

update_price_bracket_request = UpdatePriceBracketRequest(
    start_quantity=230,
    price=168,
    end_quantity=238,
    overage_price=252
)
```

