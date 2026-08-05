
# Get Movement Object Transfer Response

## Structure

`GetMovementObjectTransferResponse`

## Inherits From

[`GetMovementObjectBaseResponse`](../../doc/models/get-movement-object-base-response.md)

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `source_type` | `str` | Optional | - |
| `source_id` | `str` | Optional | - |
| `target_type` | `str` | Optional | - |
| `target_id` | `str` | Optional | - |
| `fee` | `str` | Optional | - |
| `funding_date` | `str` | Optional | - |
| `funding_estimated_date` | `str` | Optional | - |
| `bank_account` | `str` | Optional | - |

## Example

```python
from pagarmeapisdk.models.get_movement_object_base_response import GetMovementObjectTransferResponse

get_movement_object_transfer_response = GetMovementObjectTransferResponse(
    source_type='source_type0',
    source_id='source_id4',
    target_type='target_type2',
    target_id='target_id0',
    fee='fee2',
    id='id2',
    status='status4',
    amount='amount4',
    created_at='created_at0'
)
```

