
# Get Pricing Scheme Response

Response object for getting a pricing scheme

## Structure

`GetPricingSchemeResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `price` | `int` | Optional | - |
| `scheme_type` | `str` | Optional | - |
| `price_brackets` | [`List[GetPriceBracketResponse]`](../../doc/models/get-price-bracket-response.md) | Optional | - |
| `minimum_price` | `int` | Optional | - |
| `percentage` | `float` | Optional | percentual value used in pricing_scheme Percent |

## Example

```python
from pagarmeapisdk.models.get_pricing_scheme_response import GetPricingSchemeResponse

get_pricing_scheme_response = GetPricingSchemeResponse(
    price=116,
    scheme_type='scheme_type0',
    price_brackets=[
        None
    ],
    minimum_price=20,
    percentage=92.78
)
```

