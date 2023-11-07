
# Update Card Request

Request for updating a card

## Structure

`UpdateCardRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `holder_name` | `str` | Required | Holder name |
| `exp_month` | `int` | Required | Expiration month |
| `exp_year` | `int` | Required | Expiration year |
| `billing_address_id` | `str` | Optional | Id of the address to be used as billing address |
| `billing_address` | [`CreateAddressRequest`](../../doc/models/create-address-request.md) | Required | Billing address |
| `metadata` | `Dict[str, str]` | Required | Metadata |
| `label` | `str` | Required | - |

## Example (as JSON)

```json
{
  "holder_name": "holder_name6",
  "exp_month": 236,
  "exp_year": 60,
  "billing_address_id": "billing_address_id6",
  "billing_address": {
    "street": "street8",
    "number": "number4",
    "zip_code": "zip_code2",
    "neighborhood": "neighborhood4",
    "city": "city2",
    "state": "state6",
    "country": "country2",
    "complement": "complement6",
    "metadata": {
      "key0": "metadata5",
      "key1": "metadata6"
    },
    "line_1": "line_18",
    "line_2": "line_26"
  },
  "metadata": {
    "key0": "metadata3",
    "key1": "metadata4",
    "key2": "metadata5"
  },
  "label": "label0"
}
```

