
# Get Antifraud Response

## Structure

`GetAntifraudResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `str` | Optional | - |
| `return_code` | `str` | Optional | - |
| `return_message` | `str` | Optional | - |
| `provider_name` | `str` | Optional | - |
| `score` | `str` | Optional | - |

## Example

```python
from pagarmeapisdk.models.get_antifraud_response import GetAntifraudResponse

get_antifraud_response = GetAntifraudResponse(
    status='status6',
    return_code='return_code2',
    return_message='return_message0',
    provider_name='provider_name0',
    score='score2'
)
```

