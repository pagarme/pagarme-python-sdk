
# Get Payment Origin Response

## Structure

`GetPaymentOriginResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `charge_id` | `str` | Optional | - |
| `brand_id` | `str` | Optional | - |

## Example

```python
from pagarmeapisdk.models.get_payment_origin_response import GetPaymentOriginResponse

get_payment_origin_response = GetPaymentOriginResponse(
    charge_id='charge_id6',
    brand_id='brand_id2'
)
```

