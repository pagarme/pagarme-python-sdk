
# Get Address Response

Response object for getting an Address

## Structure

`GetAddressResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Optional | - |
| `street` | `string` | Optional | - |
| `number` | `string` | Optional | - |
| `complement` | `string` | Optional | - |
| `zip_code` | `string` | Optional | - |
| `neighborhood` | `string` | Optional | - |
| `city` | `string` | Optional | - |
| `state` | `string` | Optional | - |
| `country` | `string` | Optional | - |
| `status` | `string` | Optional | - |
| `created_at` | `datetime` | Optional | - |
| `updated_at` | `datetime` | Optional | - |
| `customer` | [`GetCustomerResponse`](../../doc/models/get-customer-response.md) | Optional | - |
| `metadata` | `dict` | Optional | - |
| `line_1` | `string` | Optional | Line 1 for address |
| `line_2` | `string` | Optional | Line 2 for address |
| `deleted_at` | `datetime` | Optional | - |

## Example (as JSON)

```json
{
  "id": "id0",
  "street": "street0",
  "number": "number2",
  "complement": "complement4",
  "zip_code": "zip_code4"
}
```

