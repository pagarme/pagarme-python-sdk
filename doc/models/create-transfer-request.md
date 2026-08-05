
# Create Transfer Request

Request for creating a transfer

## Structure

`CreateTransferRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | `int` | Required | Transfer amount |
| `metadata` | `Dict[str, str]` | Required | Metadata |

## Example

```python
from pagarmeapisdk.models.create_transfer_request import CreateTransferRequest

create_transfer_request = CreateTransferRequest(
    amount=224,
    metadata={
        'key0': 'metadata3'
    }
)
```

