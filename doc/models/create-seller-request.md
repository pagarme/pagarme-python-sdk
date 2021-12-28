
# Create Seller Request

## Structure

`CreateSellerRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Required | Name |
| `code` | `string` | Optional | Seller's code identification |
| `description` | `string` | Optional | Description |
| `document` | `string` | Optional | Document number (individual / company) |
| `address` | [`CreateAddressRequest`](/doc/models/create-address-request.md) | Optional | Address |
| `mtype` | `string` | Optional | Person type (individual / company) |
| `metadata` | `dict` | Required | Metadata |

## Example (as JSON)

```json
{
  "name": "name0",
  "code": null,
  "description": null,
  "document": null,
  "address": null,
  "type": null,
  "metadata": {
    "key0": "metadata3",
    "key1": "metadata4",
    "key2": "metadata5"
  }
}
```

