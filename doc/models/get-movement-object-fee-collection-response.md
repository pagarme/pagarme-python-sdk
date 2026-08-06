
# Get Movement Object Fee Collection Response

Generic response object for getting a MovementObjectFeeCollection.

## Structure

`GetMovementObjectFeeCollectionResponse`

## Inherits From

[`GetMovementObjectBaseResponse`](../../doc/models/get-movement-object-base-response.md)

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `description` | `str` | Optional | - |
| `payment_date` | `str` | Optional | - |
| `recipient_id` | `str` | Optional | - |

## Example

```python
from pagarmeapisdk.models.get_movement_object_base_response import GetMovementObjectFeeCollectionResponse

get_movement_object_fee_collection_response = GetMovementObjectFeeCollectionResponse(
    description='description4',
    payment_date='payment_date4',
    recipient_id='recipient_id6',
    id='id2',
    status='status4',
    amount='amount4',
    created_at='created_at0'
)
```

