
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

## Example (as JSON)

```json
{
  "name": "name0",
  "email": "email6",
  "description": "description0",
  "type": "type0",
  "status": "status8",
  "metadata": {
    "key0": "metadata3",
    "key1": "metadata4"
  }
}
```

