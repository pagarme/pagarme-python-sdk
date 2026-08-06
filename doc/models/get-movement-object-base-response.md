
# Get Movement Object Base Response

Generic response object for getting a MovementObjectBase.

## Structure

`GetMovementObjectBaseResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `object` | `str` | Optional | - |
| `id` | `str` | Optional | - |
| `status` | `str` | Optional | - |
| `amount` | `str` | Optional | - |
| `created_at` | `str` | Optional | - |
| `mtype` | `str` | Optional | - |
| `charge_id` | `str` | Optional | - |
| `gateway_id` | `str` | Optional | - |

## Example

```python
from pagarmeapisdk.models.get_movement_object_base_response import GetMovementObjectSettlementResponse

get_movement_object_base_response = GetMovementObjectSettlementResponse(
    product='product2',
    brand='brand6',
    payment_date='payment_date4',
    recipient_id='recipient_id2',
    document_type='document_type0',
    id='id2',
    status='status4',
    amount='amount4',
    created_at='created_at0'
)
```

