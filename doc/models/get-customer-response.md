
# Get Customer Response

Response object for getting a customer

## Structure

`GetCustomerResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | - |
| `name` | `str` | Optional | - |
| `email` | `str` | Optional | - |
| `delinquent` | `bool` | Optional | - |
| `created_at` | `datetime` | Optional | - |
| `updated_at` | `datetime` | Optional | - |
| `document` | `str` | Optional | - |
| `mtype` | `str` | Optional | - |
| `fb_access_token` | `str` | Optional | - |
| `address` | [`GetAddressResponse`](../../doc/models/get-address-response.md) | Optional | - |
| `metadata` | `Dict[str, str]` | Optional | - |
| `phones` | [`GetPhonesResponse`](../../doc/models/get-phones-response.md) | Optional | - |
| `fb_id` | `int` | Optional | - |
| `code` | `str` | Optional | Código de referência do cliente no sistema da loja. Max: 52 caracteres |
| `document_type` | `str` | Optional | - |

## Example (as JSON)

```json
{
  "id": "id4",
  "name": "name4",
  "email": "email2",
  "delinquent": false,
  "created_at": "2016-03-13T12:52:32.123Z"
}
```

