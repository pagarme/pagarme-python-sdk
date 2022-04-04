
# Get Pricing Scheme Response

Response object for getting a pricing scheme

## Structure

`GetPricingSchemeResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `price` | `int` | Required | - |
| `scheme_type` | `string` | Required | - |
| `price_brackets` | [`List of GetPriceBracketResponse`](../../doc/models/get-price-bracket-response.md) | Required | - |
| `minimum_price` | `int` | Optional | - |
| `percentage` | `float` | Optional | percentual value used in pricing_scheme Percent |

## Example (as JSON)

```json
{
  "price": 16,
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
  "minimum_price": null,
  "percentage": null
}
```

