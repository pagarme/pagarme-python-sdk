
# Update Invoice Status Request

Invoice Update Status Request

## Structure

`UpdateInvoiceStatusRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `str` | Required | Status |

## Example

```python
from pagarmeapisdk.models.update_invoice_status_request import UpdateInvoiceStatusRequest

update_invoice_status_request = UpdateInvoiceStatusRequest(
    status='status0'
)
```

