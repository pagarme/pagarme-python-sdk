
# Create Card Request

Card data

## Structure

`CreateCardRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `number` | `str` | Optional | Credit card number |
| `holder_name` | `str` | Optional | Holder name, as written on the card |
| `exp_month` | `int` | Optional | The expiration month |
| `exp_year` | `int` | Optional | The expiration year, that can be informed with 2 or 4 digits |
| `cvv` | `str` | Optional | The card's security code |
| `billing_address` | [`CreateAddressRequest`](../../doc/models/create-address-request.md) | Optional | Card's billing address |
| `brand` | `str` | Optional | Card brand |
| `billing_address_id` | `str` | Optional | The address id for the billing address |
| `metadata` | `Dict[str, str]` | Optional | Metadata |
| `mtype` | `str` | Optional | Card type<br>**Default**: `'credit'` |
| `options` | [`CreateCardOptionsRequest`](../../doc/models/create-card-options-request.md) | Optional | Options for creating the card |
| `holder_document` | `str` | Optional | Document number for the card's holder |
| `private_label` | `bool` | Optional | Indicates whether it is a private label card |
| `label` | `str` | Optional | - |
| `id` | `str` | Optional | Identifier |
| `token` | `str` | Optional | token identifier |

## Example (as JSON)

```json
{
  "type": "credit",
  "number": "number0",
  "holder_name": "holder_name8",
  "exp_month": 92,
  "exp_year": 204,
  "cvv": "cvv0"
}
```

