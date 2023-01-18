
# Create Pricing Scheme Request

Request for creating a pricing scheme

## Structure

`CreatePricingSchemeRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `scheme_type` | `string` | Required | Scheme type |
| `price_brackets` | [`List of CreatePriceBracketRequest`](../../doc/models/create-price-bracket-request.md) | Optional | Price brackets |
| `price` | `int` | Optional | Price |
| `minimum_price` | `int` | Optional | Minimum price |
| `percentage` | `float` | Optional | percentual value used in pricing_scheme Percent |

## Example (as JSON)

```json
{
  "scheme_type": "scheme_type0",
  "price_brackets": null,
  "price": null,
  "minimum_price": null,
  "percentage": null
}
```

