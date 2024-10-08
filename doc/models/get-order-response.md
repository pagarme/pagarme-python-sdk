
# Get Order Response

Response object for getting an Order

## Structure

`GetOrderResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | - |
| `code` | `str` | Optional | - |
| `amount` | `int` | Optional | - |
| `currency` | `str` | Optional | - |
| `closed` | `bool` | Optional | Indicates whether the order is closed |
| `items` | [`List[GetOrderItemResponse]`](../../doc/models/get-order-item-response.md) | Optional | - |
| `customer` | [`GetCustomerResponse`](../../doc/models/get-customer-response.md) | Optional | - |
| `status` | `str` | Optional | - |
| `created_at` | `datetime` | Optional | - |
| `updated_at` | `datetime` | Optional | - |
| `closed_at` | `datetime` | Optional | - |
| `charges` | [`List[GetChargeResponse]`](../../doc/models/get-charge-response.md) | Optional | - |
| `invoice_url` | `str` | Optional | - |
| `shipping` | [`GetShippingResponse`](../../doc/models/get-shipping-response.md) | Optional | - |
| `metadata` | `Dict[str, str]` | Optional | - |
| `checkouts` | [`List[GetCheckoutPaymentResponse]`](../../doc/models/get-checkout-payment-response.md) | Optional | Checkout Payment Settings Response |
| `ip` | `str` | Optional | Ip address |
| `session_id` | `str` | Optional | Session id |
| `location` | [`GetLocationResponse`](../../doc/models/get-location-response.md) | Optional | Location |
| `device` | [`GetDeviceResponse`](../../doc/models/get-device-response.md) | Optional | Device's informations |
| `integration` | [`GetIntegrationResponse`](../../doc/models/get-integration-response.md) | Optional | - |

## Example (as JSON)

```json
{
  "id": "id6",
  "code": "code4",
  "amount": 64,
  "currency": "currency6",
  "closed": false
}
```

