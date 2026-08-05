
# Create Split Options Request

The Split Options Request

## Structure

`CreateSplitOptionsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `liable` | `bool` | Optional | Liable options |
| `charge_processing_fee` | `bool` | Optional | Charge processing fee |
| `charge_remainder_fee` | `bool` | Optional | - |

## Example

```python
from pagarmeapisdk.models.create_split_options_request import CreateSplitOptionsRequest

create_split_options_request = CreateSplitOptionsRequest(
    liable=False,
    charge_processing_fee=False,
    charge_remainder_fee=False
)
```

