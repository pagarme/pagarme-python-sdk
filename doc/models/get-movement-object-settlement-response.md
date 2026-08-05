
# Get Movement Object Settlement Response

Generic response object for getting a MovementObjectSettlement.

## Structure

`GetMovementObjectSettlementResponse`

## Inherits From

[`GetMovementObjectBaseResponse`](../../doc/models/get-movement-object-base-response.md)

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `product` | `str` | Optional | - |
| `brand` | `str` | Optional | - |
| `payment_date` | `str` | Optional | - |
| `recipient_id` | `str` | Optional | - |
| `document_type` | `str` | Optional | - |
| `document` | `str` | Optional | - |
| `contract_obligation_id` | `str` | Optional | - |
| `liquidation_arrangement_id` | `str` | Optional | - |
| `external_engine_payment_id` | `str` | Optional | - |

## Example

```python
from pagarmeapisdk.models.get_movement_object_base_response import GetMovementObjectSettlementResponse

get_movement_object_settlement_response = GetMovementObjectSettlementResponse(
    product='product6',
    brand='brand8',
    payment_date='payment_date4',
    recipient_id='recipient_id6',
    document_type='document_type2',
    id='id2',
    status='status4',
    amount='amount4',
    created_at='created_at0'
)
```

