
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

## Example

```python
try:
    # make the API call
except ErrorException as e:
    print(e)
except APIException as e:
    print(e)
```

