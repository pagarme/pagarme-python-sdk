
# Get Split Options Response

## Structure

`GetSplitOptionsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `liable` | `bool` | Optional | - |
| `charge_processing_fee` | `bool` | Optional | - |
| `charge_remainder_fee` | `str` | Optional | - |

## Example

```python
from pagarmeapisdk.models.get_split_options_response import GetSplitOptionsResponse

get_split_options_response = GetSplitOptionsResponse(
    liable=False,
    charge_processing_fee=False,
    charge_remainder_fee='charge_remainder_fee4'
)
```

