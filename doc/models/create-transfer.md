
# Create Transfer

## Structure

`CreateTransfer`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | `int` | Required | - |
| `source_id` | `str` | Required | - |
| `target_id` | `str` | Required | - |
| `metadata` | `List[str]` | Optional | - |

## Example

```python
from pagarmeapisdk.models.create_transfer import CreateTransfer

create_transfer = CreateTransfer(
    amount=202,
    source_id='source_id2',
    target_id='target_id8',
    metadata=[
        'metadata5'
    ]
)
```

