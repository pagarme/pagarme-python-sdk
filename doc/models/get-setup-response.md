
# Get Setup Response

Response object for getting the setup from a subscription

## Structure

`GetSetupResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | - |
| `description` | `str` | Optional | - |
| `amount` | `int` | Optional | - |
| `status` | `str` | Optional | - |

## Example

```python
from pagarmeapisdk.models.get_setup_response import GetSetupResponse

get_setup_response = GetSetupResponse(
    id='id2',
    description='description2',
    amount=108,
    status='status4'
)
```

