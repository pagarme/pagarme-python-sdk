
# Get Shipping Response

Response object for getting the shipping data

## Structure

`GetShippingResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | `int` | Optional | - |
| `description` | `str` | Optional | - |
| `recipient_name` | `str` | Optional | - |
| `recipient_phone` | `str` | Optional | - |
| `address` | [`GetAddressResponse`](../../doc/models/get-address-response.md) | Optional | - |
| `max_delivery_date` | `datetime` | Optional | Data máxima de entrega |
| `estimated_delivery_date` | `datetime` | Optional | Prazo estimado de entrega |
| `mtype` | `str` | Optional | Shipping Type |

## Example (as JSON)

```json
{
  "amount": 214,
  "description": "description8",
  "recipient_name": "recipient_name6",
  "recipient_phone": "recipient_phone0",
  "address": {
    "id": "id6",
    "street": "street6",
    "number": "number4",
    "complement": "complement2",
    "zip_code": "zip_code0"
  }
}
```

