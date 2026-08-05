
# Update Metadata Request

Request for updating an metadata

## Structure

`UpdateMetadataRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `metadata` | `Dict[str, str]` | Required | Metadata |

## Example

```python
from pagarmeapisdk.models.update_metadata_request import UpdateMetadataRequest

update_metadata_request = UpdateMetadataRequest(
    metadata={
        'key0': 'metadata1'
    }
)
```

