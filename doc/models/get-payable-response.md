
# Get Payable Response

Response object for getting an payable

## Structure

`GetPayableResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `long\|int` | Optional | - |
| `status` | `string` | Optional | - |
| `amount` | `int` | Optional | - |
| `fee` | `int` | Optional | - |
| `anticipation_fee` | `int` | Optional | - |
| `fraud_coverage_fee` | `int` | Optional | - |
| `installment` | `int` | Optional | - |
| `gateway_id` | `int` | Optional | - |
| `charge_id` | `string` | Optional | - |
| `split_id` | `string` | Optional | - |
| `bulk_anticipation_id` | `string` | Optional | - |
| `anticipation_id` | `string` | Optional | - |
| `recipient_id` | `string` | Optional | - |
| `originator_model` | `string` | Optional | - |
| `originator_model_id` | `string` | Optional | - |
| `payment_date` | `datetime` | Optional | - |
| `original_payment_date` | `datetime` | Optional | - |
| `mtype` | `string` | Optional | - |
| `payment_method` | `string` | Optional | - |
| `accrual_at` | `datetime` | Optional | - |
| `created_at` | `datetime` | Optional | - |
| `liquidation_arrangement_id` | `string` | Optional | - |

## Example (as JSON)

```json
{
  "id": 112,
  "status": "status8",
  "amount": 46,
  "fee": 168,
  "anticipation_fee": 140
}
```

