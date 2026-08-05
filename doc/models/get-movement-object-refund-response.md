
# Get Movement Object Refund Response

Generic response object for getting a MovementObjectRefund.

## Structure

`GetMovementObjectRefundResponse`

## Inherits From

[`GetMovementObjectBaseResponse`](../../doc/models/get-movement-object-base-response.md)

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `fraud_coverage_fee` | `str` | Optional | - |
| `charge_fee_recipient_id` | `str` | Optional | - |
| `bank_account_id` | `str` | Optional | - |
| `local_transaction_id` | `str` | Optional | - |
| `updated_at` | `str` | Optional | - |

## Example

```python
from pagarmeapisdk.models.get_movement_object_base_response import GetMovementObjectRefundResponse

get_movement_object_refund_response = GetMovementObjectRefundResponse(
    fraud_coverage_fee='fraud_coverage_fee8',
    charge_fee_recipient_id='charge_fee_recipient_id4',
    bank_account_id='bank_account_id0',
    local_transaction_id='local_transaction_id6',
    updated_at='updated_at6',
    id='id2',
    status='status4',
    amount='amount4',
    created_at='created_at0'
)
```

