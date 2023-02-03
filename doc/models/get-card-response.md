
# Get Card Response

Response object for getting a credit card

## Structure

`GetCardResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Optional | - |
| `last_four_digits` | `string` | Optional | - |
| `brand` | `string` | Optional | - |
| `holder_name` | `string` | Optional | - |
| `exp_month` | `int` | Optional | - |
| `exp_year` | `int` | Optional | - |
| `status` | `string` | Optional | - |
| `created_at` | `datetime` | Optional | - |
| `updated_at` | `datetime` | Optional | - |
| `billing_address` | [`GetBillingAddressResponse`](../../doc/models/get-billing-address-response.md) | Optional | - |
| `customer` | [`GetCustomerResponse`](../../doc/models/get-customer-response.md) | Optional | - |
| `metadata` | `dict` | Optional | - |
| `mtype` | `string` | Optional | Card type |
| `holder_document` | `string` | Optional | Document number for the card's holder |
| `deleted_at` | `datetime` | Optional | - |
| `first_six_digits` | `string` | Optional | First six digits |
| `label` | `string` | Optional | - |

## Example (as JSON)

```json
{
  "id": null,
  "last_four_digits": null,
  "brand": null,
  "holder_name": null,
  "exp_month": null,
  "exp_year": null,
  "status": null,
  "created_at": null,
  "updated_at": null,
  "billing_address": null,
  "customer": null,
  "metadata": null,
  "type": null,
  "holder_document": null,
  "deleted_at": null,
  "first_six_digits": null,
  "label": null
}
```

