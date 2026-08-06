
# Update Pricing Scheme Request

Request for updating a pricing scheme

## Structure

`UpdatePricingSchemeRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `scheme_type` | `str` | Required | Scheme type |
| `price_brackets` | [`List[UpdatePriceBracketRequest]`](../../doc/models/update-price-bracket-request.md) | Required | Price brackets |
| `price` | `int` | Optional | Price |
| `minimum_price` | `int` | Optional | Minimum price |
| `percentage` | `float` | Optional | percentual value used in pricing_scheme Percent |

## Example

```python
from pagarmeapisdk.models.update_pricing_scheme_request import UpdatePricingSchemeRequest

update_pricing_scheme_request = UpdatePricingSchemeRequest(
    scheme_type=None,
    price_brackets=[
        None
    ],
    price=250,
    minimum_price=154,
    percentage=88.88
)
```

