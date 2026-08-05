
# Create Payment Origin Request

Request object for PaymentOrigin

## Structure

`CreatePaymentOriginRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `brand_id` | `str` | Optional | - |
| `charge_id` | `str` | Optional | - |

## Example

```python
from pagarmeapisdk.models.create_payment_origin_request import CreatePaymentOriginRequest

create_payment_origin_request = CreatePaymentOriginRequest(
    brand_id='brand_id8',
    charge_id='charge_id2'
)
```

