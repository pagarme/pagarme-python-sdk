
# Paging Response

Object used for returning lists of objects with pagination

## Structure

`PagingResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `total` | `int` | Optional | Total number of pages |
| `previous` | `str` | Optional | Previous page |
| `next` | `str` | Optional | Next page |

## Example

```python
from pagarmeapisdk.models.paging_response import PagingResponse

paging_response = PagingResponse(
    total=196,
    previous='previous8',
    next='next8'
)
```

