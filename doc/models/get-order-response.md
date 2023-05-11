
# Get Order Response

Response object for getting an Order

## Structure

`GetOrderResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Optional | - |
| `code` | `string` | Optional | - |
| `currency` | `string` | Optional | - |
| `items` | [`List of GetOrderItemResponse`](../../doc/models/get-order-item-response.md) | Optional | - |
| `customer` | [`GetCustomerResponse`](../../doc/models/get-customer-response.md) | Optional | - |
| `status` | `string` | Optional | - |
| `created_at` | `datetime` | Optional | - |
| `updated_at` | `datetime` | Optional | - |
| `charges` | [`List of GetChargeResponse`](../../doc/models/get-charge-response.md) | Optional | - |
| `invoice_url` | `string` | Optional | - |
| `shipping` | [`GetShippingResponse`](../../doc/models/get-shipping-response.md) | Optional | - |
| `metadata` | `dict` | Optional | - |
| `checkouts` | [`List of GetCheckoutPaymentResponse`](../../doc/models/get-checkout-payment-response.md) | Optional | Checkout Payment Settings Response |
| `ip` | `string` | Optional | Ip address |
| `session_id` | `string` | Optional | Session id |
| `location` | [`GetLocationResponse`](../../doc/models/get-location-response.md) | Optional | Location |
| `device` | [`GetDeviceResponse`](../../doc/models/get-device-response.md) | Optional | Device's informations |
| `closed` | `bool` | Optional | Indicates whether the order is closed |

## Example (as JSON)

```json
{
  "id": "id0",
  "code": "code8",
  "currency": "currency0",
  "items": [
    {
      "id": "id7",
      "amount": 13,
      "description": "description7",
      "quantity": 127,
      "category": "category5"
    },
    {
      "id": "id8",
      "amount": 14,
      "description": "description8",
      "quantity": 128,
      "category": "category6"
    }
  ],
  "customer": {
    "id": "id0",
    "name": "name0",
    "email": "email6",
    "delinquent": false,
    "created_at": "2016-03-13T12:52:32.123Z"
  }
}
```

