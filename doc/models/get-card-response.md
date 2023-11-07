
# Get Card Response

Response object for getting a credit card

## Structure

`GetCardResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | - |
| `last_four_digits` | `str` | Optional | - |
| `brand` | `str` | Optional | - |
| `holder_name` | `str` | Optional | - |
| `exp_month` | `int` | Optional | - |
| `exp_year` | `int` | Optional | - |
| `status` | `str` | Optional | - |
| `created_at` | `datetime` | Optional | - |
| `updated_at` | `datetime` | Optional | - |
| `billing_address` | [`GetBillingAddressResponse`](../../doc/models/get-billing-address-response.md) | Optional | - |
| `customer` | [`GetCustomerResponse`](../../doc/models/get-customer-response.md) | Optional | - |
| `metadata` | `Dict[str, str]` | Optional | - |
| `mtype` | `str` | Optional | Card type |
| `holder_document` | `str` | Optional | Document number for the card's holder |
| `deleted_at` | `datetime` | Optional | - |
| `first_six_digits` | `str` | Optional | First six digits |
| `label` | `str` | Optional | - |

## Example (as JSON)

```json
{
  "id": "id4",
  "last_four_digits": "last_four_digits0",
  "brand": "brand8",
  "holder_name": "holder_name0",
  "exp_month": 52
}
```

