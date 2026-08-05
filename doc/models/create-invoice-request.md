
# Create Invoice Request

Request for creating a new Invoice

## Structure

`CreateInvoiceRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `metadata` | `Dict[str, str]` | Required | Metadata |

## Example

```python
from pagarmeapisdk.models.create_invoice_request import CreateInvoiceRequest

create_invoice_request = CreateInvoiceRequest(
    metadata={
        'key0': 'metadata9'
    }
)
```

