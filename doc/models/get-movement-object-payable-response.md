
# Get Movement Object Payable Response

## Structure

`GetMovementObjectPayableResponse`

## Inherits From

[`GetMovementObjectBaseResponse`](../../doc/models/get-movement-object-base-response.md)

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `fee` | `string` | Optional | - |
| `anticipation_fee` | `string` | Required | - |
| `fraud_coverage_fee` | `string` | Required | - |
| `installment` | `string` | Required | - |
| `split_id` | `string` | Required | - |
| `bulk_anticipation_id` | `string` | Required | - |
| `anticipation_id` | `string` | Required | - |
| `recipient_id` | `string` | Required | - |
| `originator_model` | `string` | Required | - |
| `originator_model_id` | `string` | Required | - |
| `payment_date` | `string` | Required | - |
| `original_payment_date` | `string` | Required | - |
| `payment_method` | `string` | Required | - |
| `accrual_at` | `string` | Required | - |
| `liquidation_arrangement_id` | `string` | Required | - |

## Example (as JSON)

```json
{
  "object": "payable",
  "id": "id0",
  "status": "status2",
  "amount": "amount2",
  "created_at": "created_at8",
  "fee": "fee2",
  "anticipation_fee": "anticipation_fee8",
  "fraud_coverage_fee": "fraud_coverage_fee2",
  "installment": "installment8",
  "split_id": "split_id2",
  "bulk_anticipation_id": "bulk_anticipation_id4",
  "anticipation_id": "anticipation_id0",
  "recipient_id": "recipient_id0",
  "originator_model": "originator_model4",
  "originator_model_id": "originator_model_id4",
  "payment_date": "payment_date8",
  "original_payment_date": "original_payment_date8",
  "payment_method": "payment_method0",
  "accrual_at": "accrual_at8",
  "liquidation_arrangement_id": "liquidation_arrangement_id6"
}
```

