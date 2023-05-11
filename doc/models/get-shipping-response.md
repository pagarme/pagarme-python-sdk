
# Get Shipping Response

Response object for getting the shipping data

## Structure

`GetShippingResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | `int` | Optional | - |
| `description` | `string` | Optional | - |
| `recipient_name` | `string` | Optional | - |
| `recipient_phone` | `string` | Optional | - |
| `address` | [`GetAddressResponse`](../../doc/models/get-address-response.md) | Optional | - |
| `max_delivery_date` | `datetime` | Optional | Data máxima de entrega |
| `estimated_delivery_date` | `datetime` | Optional | Prazo estimado de entrega |
| `mtype` | `string` | Optional | Shipping Type |

## Example (as JSON)

```json
{
  "amount": 46,
  "description": "description0",
  "recipient_name": "recipient_name8",
  "recipient_phone": "recipient_phone2",
  "address": {
    "id": "id6",
    "street": "street6",
    "number": "number4",
    "complement": "complement2",
    "zip_code": "zip_code0"
  }
}
```

