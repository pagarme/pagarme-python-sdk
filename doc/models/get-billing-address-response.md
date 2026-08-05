
# Get Billing Address Response

Response object for getting a billing address

## Structure

`GetBillingAddressResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `street` | `str` | Optional | - |
| `number` | `str` | Optional | - |
| `zip_code` | `str` | Optional | - |
| `neighborhood` | `str` | Optional | - |
| `city` | `str` | Optional | - |
| `state` | `str` | Optional | - |
| `country` | `str` | Optional | - |
| `complement` | `str` | Optional | - |
| `line_1` | `str` | Optional | Line 1 for address |
| `line_2` | `str` | Optional | Line 2 for address |

## Example

```python
from pagarmeapisdk.models.get_billing_address_response import GetBillingAddressResponse

get_billing_address_response = GetBillingAddressResponse(
    street='street8',
    number='number4',
    zip_code='zip_code2',
    neighborhood='neighborhood4',
    city='city8'
)
```

