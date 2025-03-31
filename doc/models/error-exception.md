
# Error Exception

Api Error Exception

## Structure

`ErrorException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `message` | `str` | Required | - |
| `errors` | `Any` | Required | - |
| `request` | `Any` | Required | - |

## Example (as JSON)

```json
{
  "message": "message4",
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

