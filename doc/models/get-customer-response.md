
# Get Customer Response

Response object for getting a customer

## Structure

`GetCustomerResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Optional | - |
| `name` | `string` | Optional | - |
| `email` | `string` | Optional | - |
| `delinquent` | `bool` | Optional | - |
| `created_at` | `datetime` | Optional | - |
| `updated_at` | `datetime` | Optional | - |
| `document` | `string` | Optional | - |
| `mtype` | `string` | Optional | - |
| `fb_access_token` | `string` | Optional | - |
| `address` | [`GetAddressResponse`](../../doc/models/get-address-response.md) | Optional | - |
| `metadata` | `dict` | Optional | - |
| `phones` | [`GetPhonesResponse`](../../doc/models/get-phones-response.md) | Optional | - |
| `fb_id` | `long\|int` | Optional | - |
| `code` | `string` | Optional | Código de referência do cliente no sistema da loja. Max: 52 caracteres |
| `document_type` | `string` | Optional | - |

## Example (as JSON)

```json
{
  "id": null,
  "name": null,
  "email": null,
  "delinquent": null,
  "created_at": null,
  "updated_at": null,
  "document": null,
  "type": null,
  "fb_access_token": null,
  "address": null,
  "metadata": null,
  "phones": null,
  "fb_id": null,
  "code": null,
  "document_type": null
}
```

