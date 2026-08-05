
# Update Address Request

Request for updating an address

## Structure

`UpdateAddressRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `number` | `str` | Required | Number |
| `complement` | `str` | Required | Complement |
| `metadata` | `Dict[str, str]` | Required | Metadata |
| `line_2` | `str` | Required | Line 2 for address |

## Example

```python
from pagarmeapisdk.models.update_address_request import UpdateAddressRequest

update_address_request = UpdateAddressRequest(
    number='number4',
    complement='complement2',
    metadata={
        'key0': 'metadata3'
    },
    line_2='line_24'
)
```

