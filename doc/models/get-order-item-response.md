
# Get Order Item Response

Response object for getting an order item

## Structure

`GetOrderItemResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Required | Id |
| `amount` | `int` | Required | - |
| `description` | `string` | Required | - |
| `quantity` | `int` | Required | - |
| `get_seller_response` | [`GetSellerResponse`](/doc/models/get-seller-response.md) | Optional | Seller data |
| `category` | `string` | Required | Category |
| `code` | `string` | Required | Code |

## Example (as JSON)

```json
{
  "id": "id0",
  "amount": 46,
  "description": "description0",
  "quantity": 68,
  "GetSellerResponse": null,
  "category": "category2",
  "code": "code8"
}
```

