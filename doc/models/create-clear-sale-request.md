
# Create Clear Sale Request

## Structure

`CreateClearSaleRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `custom_sla` | `int` | Required | - |

## Example

```python
from pagarmeapisdk.models.create_clear_sale_request import CreateClearSaleRequest

create_clear_sale_request = CreateClearSaleRequest(
    custom_sla=10
)
```

