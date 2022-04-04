
# Update Pricing Scheme Request

Request for updating a pricing scheme

## Structure

`UpdatePricingSchemeRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `scheme_type` | `string` | Required | Scheme type |
| `price_brackets` | [`List of UpdatePriceBracketRequest`](../../doc/models/update-price-bracket-request.md) | Required | Price brackets |
| `price` | `int` | Optional | Price |
| `minimum_price` | `int` | Optional | Minimum price |
| `percentage` | `float` | Optional | percentual value used in pricing_scheme Percent |

## Example (as JSON)

```json
{
  "scheme_type": "scheme_type0",
  "price_brackets": [
    {
      "start_quantity": 193,
      "price": 125,
      "end_quantity": null,
      "overage_price": null
    },
    {
      "start_quantity": 194,
      "price": 124,
      "end_quantity": null,
      "overage_price": null
    },
    {
      "start_quantity": 195,
      "price": 123,
      "end_quantity": null,
      "overage_price": null
    }
  ],
  "price": null,
  "minimum_price": null,
  "percentage": null
}
```

