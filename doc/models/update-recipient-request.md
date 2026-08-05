
# Update Recipient Request

Request for updating a Recipient

## Structure

`UpdateRecipientRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Required | Name |
| `email` | `str` | Required | Email |
| `description` | `str` | Required | Description |
| `mtype` | `str` | Required | Type |
| `status` | `str` | Required | Status |
| `metadata` | `Dict[str, str]` | Required | Metadata |

## Example

```python
from pagarmeapisdk.models.update_recipient_request import UpdateRecipientRequest

update_recipient_request = UpdateRecipientRequest(
    name='name8',
    email='email8',
    description='description8',
    mtype='type2',
    status='status0',
    metadata={
        'key0': 'metadata5',
        'key1': 'metadata4'
    }
)
```

