
# Update Seller Request

## Structure

`UpdateSellerRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Required | Seller name |
| `code` | `string` | Required | Seller code |
| `description` | `string` | Required | Seller description |
| `document` | `string` | Required | Seller document CPF or CNPJ |
| `status` | `string` | Required | - |
| `mtype` | `string` | Required | - |
| `address` | [`CreateAddressRequest`](/doc/models/create-address-request.md) | Required | - |
| `metadata` | `dict` | Required | - |

## Example (as JSON)

```json
{
  "name": "name0",
  "code": "code8",
  "description": "description0",
  "document": "document6",
  "status": "status8",
  "type": "type0",
  "address": {
    "street": "street6",
    "number": "number4",
    "zip_code": "zip_code0",
    "neighborhood": "neighborhood2",
    "city": "city6",
    "state": "state2",
    "country": "country0",
    "complement": "complement2",
    "metadata": {
      "key0": "metadata3",
      "key1": "metadata2",
      "key2": "metadata1"
    },
    "line_1": "line_10",
    "line_2": "line_24"
  },
  "metadata": {
    "key0": "metadata3",
    "key1": "metadata4",
    "key2": "metadata5"
  }
}
```

