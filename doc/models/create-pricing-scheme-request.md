
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
  "price_brackets": [
    {
      "start_quantity": 193,
      "price": 125,
      "end_quantity": 201,
      "overage_price": 215
    },
    {
      "start_quantity": 194,
      "price": 124,
      "end_quantity": 202,
      "overage_price": 216
    },
    {
      "start_quantity": 195,
      "price": 123,
      "end_quantity": 203,
      "overage_price": 217
    }
  ],
  "price": 16,
  "minimum_price": 176,
  "percentage": 4.18
}
```

