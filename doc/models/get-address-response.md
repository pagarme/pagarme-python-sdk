
# Get Address Response

Response object for getting an Address

## Structure

`GetAddressResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | - |
| `street` | `str` | Optional | - |
| `number` | `str` | Optional | - |
| `complement` | `str` | Optional | - |
| `zip_code` | `str` | Optional | - |
| `neighborhood` | `str` | Optional | - |
| `city` | `str` | Optional | - |
| `state` | `str` | Optional | - |
| `country` | `str` | Optional | - |
| `status` | `str` | Optional | - |
| `created_at` | `datetime` | Optional | - |
| `updated_at` | `datetime` | Optional | - |
| `customer` | [`GetCustomerResponse`](../../doc/models/get-customer-response.md) | Optional | - |
| `metadata` | `Dict[str, str]` | Optional | - |
| `line_1` | `str` | Optional | Line 1 for address |
| `line_2` | `str` | Optional | Line 2 for address |
| `deleted_at` | `datetime` | Optional | - |

## Example

```python
from pagarmeapisdk.models.get_address_response import GetAddressResponse

get_address_response = GetAddressResponse(
    id='id4',
    street='street4',
    number='number2',
    complement='complement0',
    zip_code='zip_code8'
)
```

