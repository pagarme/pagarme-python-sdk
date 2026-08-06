
# Update Recipient Code Request

Update code for a recipient

## Structure

`UpdateRecipientCodeRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `code` | `str` | Required | Code |

## Example

```python
from pagarmeapisdk.models.update_recipient_code_request import UpdateRecipientCodeRequest

update_recipient_code_request = UpdateRecipientCodeRequest(
    code='code4'
)
```

