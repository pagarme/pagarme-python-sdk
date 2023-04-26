
# Create Card Request

Card data

## Structure

`CreateCardRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `number` | `string` | Optional | Credit card number |
| `holder_name` | `string` | Optional | Holder name, as written on the card |
| `exp_month` | `int` | Optional | The expiration month |
| `exp_year` | `int` | Optional | The expiration year, that can be informed with 2 or 4 digits |
| `cvv` | `string` | Optional | The card's security code |
| `billing_address` | [`CreateAddressRequest`](../../doc/models/create-address-request.md) | Optional | Card's billing address |
| `brand` | `string` | Optional | Card brand |
| `billing_address_id` | `string` | Optional | The address id for the billing address |
| `metadata` | `dict` | Optional | Metadata |
| `mtype` | `string` | Optional | Card type<br>**Default**: `'credit'` |
| `options` | [`CreateCardOptionsRequest`](../../doc/models/create-card-options-request.md) | Optional | Options for creating the card |
| `holder_document` | `string` | Optional | Document number for the card's holder |
| `private_label` | `bool` | Optional | Indicates whether it is a private label card |
| `label` | `string` | Optional | - |
| `id` | `string` | Optional | Identifier |
| `token` | `string` | Optional | token identifier |

## Example (as JSON)

```json
{
  "type": "credit"
}
```

