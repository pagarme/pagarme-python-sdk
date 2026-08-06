
# Create Withdraw Request

## Structure

`CreateWithdrawRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | `int` | Required | - |
| `metadata` | `Dict[str, str]` | Optional | - |

## Example

```python
from pagarmeapisdk.models.create_withdraw_request import CreateWithdrawRequest

create_withdraw_request = CreateWithdrawRequest(
    amount=204,
    metadata={
        'key0': 'metadata9'
    }
)
```

