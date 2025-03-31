
# Get Payable Response

Response object for getting an payable

## Structure

`GetPayableResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | - |
| `status` | `str` | Optional | - |
| `amount` | `int` | Optional | - |
| `fee` | `int` | Optional | - |
| `anticipation_fee` | `int` | Optional | - |
| `fraud_coverage_fee` | `int` | Optional | - |
| `installment` | `int` | Optional | - |
| `gateway_id` | `int` | Optional | - |
| `charge_id` | `str` | Optional | - |
| `split_id` | `str` | Optional | - |
| `bulk_anticipation_id` | `str` | Optional | - |
| `anticipation_id` | `str` | Optional | - |
| `recipient_id` | `str` | Optional | - |
| `originator_model` | `str` | Optional | - |
| `originator_model_id` | `str` | Optional | - |
| `payment_date` | `datetime` | Optional | - |
| `original_payment_date` | `datetime` | Optional | - |
| `mtype` | `str` | Optional | - |
| `payment_method` | `str` | Optional | - |
| `accrual_at` | `datetime` | Optional | - |
| `created_at` | `datetime` | Optional | - |
| `liquidation_arrangement_id` | `str` | Optional | - |

## Example (as JSON)

```json
{
  "id": 134,
  "status": "status8",
  "amount": 24,
  "fee": 190,
  "anticipation_fee": 118
}
```

