
# Create Pricing Scheme Request

Request for creating a pricing scheme

## Structure

`CreatePricingSchemeRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `scheme_type` | `str` | Required | Scheme type |
| `price_brackets` | [`List[CreatePriceBracketRequest]`](../../doc/models/create-price-bracket-request.md) | Optional | Price brackets |
| `price` | `int` | Optional | Price |
| `minimum_price` | `int` | Optional | Minimum price |
| `percentage` | `float` | Optional | percentual value used in pricing_scheme Percent |

## Example

```python
from pagarmeapisdk.models.create_price_bracket_request import CreatePriceBracketRequest
from pagarmeapisdk.models.create_pricing_scheme_request import CreatePricingSchemeRequest

create_pricing_scheme_request = CreatePricingSchemeRequest(
    scheme_type='scheme_type2',
    price_brackets=[
        None,
        CreatePriceBracketRequest(
            start_quantity=None,
            price=None
        ),
        CreatePriceBracketRequest(
            start_quantity=None,
            price=None
        )
    ],
    price=76,
    minimum_price=172,
    percentage=133.1
)
```

