
# Create Card Request

Card data

## Structure

`CreateCardRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `number` | `string` | Required | Credit card number |
| `holder_name` | `string` | Required | Holder name, as written on the card |
| `exp_month` | `int` | Required | The expiration month |
| `exp_year` | `int` | Required | The expiration year, that can be informed with 2 or 4 digits |
| `cvv` | `string` | Required | The card's security code |
| `billing_address` | [`CreateAddressRequest`](../../doc/models/create-address-request.md) | Required | Card's billing address |
| `brand` | `string` | Required | Card brand |
| `billing_address_id` | `string` | Required | The address id for the billing address |
| `metadata` | `dict` | Required | Metadata |
| `mtype` | `string` | Required | Card type<br>**Default**: `'credit'` |
| `options` | [`CreateCardOptionsRequest`](../../doc/models/create-card-options-request.md) | Required | Options for creating the card |
| `holder_document` | `string` | Optional | Document number for the card's holder |
| `private_label` | `bool` | Required | Indicates whether it is a private label card |
| `label` | `string` | Required | - |
| `id` | `string` | Optional | Identifier |
| `token` | `string` | Optional | token identifier |

## Example (as JSON)

```json
{
  "number": null,
  "holder_name": null,
  "exp_month": null,
  "exp_year": null,
  "cvv": null,
  "billing_address": null,
  "brand": null,
  "billing_address_id": null,
  "metadata": null,
  "type": "credit",
  "options": null,
  "private_label": null,
  "label": null
}
```

