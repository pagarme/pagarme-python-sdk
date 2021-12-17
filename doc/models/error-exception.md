
# Error Exception

Api Error Exception

## Structure

`ErrorException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `message` | `string` | Required | - |
| `errors` | `object` | Required | - |
| `request` | `object` | Required | - |

## Example (as JSON)

```json
{
  "message": "message0",
  "errors": {
    "key1": "val1",
    "key2": "val2"
  },
  "request": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

