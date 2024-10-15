# Invoices

```python
invoices_controller = client.invoices
```

## Class Name

`InvoicesController`

## Methods

* [Get Invoices](../../doc/controllers/invoices.md#get-invoices)
* [Cancel Invoice](../../doc/controllers/invoices.md#cancel-invoice)
* [Update Invoice Status](../../doc/controllers/invoices.md#update-invoice-status)
* [Update Invoice Metadata](../../doc/controllers/invoices.md#update-invoice-metadata)
* [Get Partial Invoice](../../doc/controllers/invoices.md#get-partial-invoice)
* [Create Invoice](../../doc/controllers/invoices.md#create-invoice)
* [Get Invoice](../../doc/controllers/invoices.md#get-invoice)


# Get Invoices

Gets all invoices

```python
def get_invoices(self,
                page=None,
                size=None,
                code=None,
                customer_id=None,
                subscription_id=None,
                created_since=None,
                created_until=None,
                status=None,
                due_since=None,
                due_until=None,
                customer_document=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `page` | `int` | Query, Optional | Page number |
| `size` | `int` | Query, Optional | Page size |
| `code` | `str` | Query, Optional | Filter for Invoice's code |
| `customer_id` | `str` | Query, Optional | Filter for Invoice's customer id |
| `subscription_id` | `str` | Query, Optional | Filter for Invoice's subscription id |
| `created_since` | `datetime` | Query, Optional | Filter for Invoice's creation date start range |
| `created_until` | `datetime` | Query, Optional | Filter for Invoices creation date end range |
| `status` | `str` | Query, Optional | Filter for Invoice's status |
| `due_since` | `datetime` | Query, Optional | Filter for Invoice's due date start range |
| `due_until` | `datetime` | Query, Optional | Filter for Invoice's due date end range |
| `customer_document` | `str` | Query, Optional | - |

## Response Type

[`ListInvoicesResponse`](../../doc/models/list-invoices-response.md)

## Example Usage

```python
result = invoices_controller.get_invoices()
```


# Cancel Invoice

Cancels an invoice

```python
def cancel_invoice(self,
                  invoice_id,
                  idempotency_key=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `invoice_id` | `str` | Template, Required | Invoice id |
| `idempotency_key` | `str` | Header, Optional | - |

## Response Type

[`GetInvoiceResponse`](../../doc/models/get-invoice-response.md)

## Example Usage

```python
invoice_id = 'invoice_id0'

result = invoices_controller.cancel_invoice(invoice_id)
```


# Update Invoice Status

Updates the status from an invoice

```python
def update_invoice_status(self,
                         invoice_id,
                         request,
                         idempotency_key=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `invoice_id` | `str` | Template, Required | Invoice Id |
| `request` | [`UpdateInvoiceStatusRequest`](../../doc/models/update-invoice-status-request.md) | Body, Required | Request for updating an invoice's status |
| `idempotency_key` | `str` | Header, Optional | - |

## Response Type

[`GetInvoiceResponse`](../../doc/models/get-invoice-response.md)

## Example Usage

```python
invoice_id = 'invoice_id0'

request = UpdateInvoiceStatusRequest(
    status='status8'
)

result = invoices_controller.update_invoice_status(
    invoice_id,
    request
)
```


# Update Invoice Metadata

Updates the metadata from an invoice

```python
def update_invoice_metadata(self,
                           invoice_id,
                           request,
                           idempotency_key=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `invoice_id` | `str` | Template, Required | The invoice id |
| `request` | [`UpdateMetadataRequest`](../../doc/models/update-metadata-request.md) | Body, Required | Request for updating the invoice metadata |
| `idempotency_key` | `str` | Header, Optional | - |

## Response Type

[`GetInvoiceResponse`](../../doc/models/get-invoice-response.md)

## Example Usage

```python
invoice_id = 'invoice_id0'

request = UpdateMetadataRequest(
    metadata={
        'key0': 'metadata3'
    }
)

result = invoices_controller.update_invoice_metadata(
    invoice_id,
    request
)
```


# Get Partial Invoice

```python
def get_partial_invoice(self,
                       subscription_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `str` | Template, Required | Subscription Id |

## Response Type

[`GetInvoiceResponse`](../../doc/models/get-invoice-response.md)

## Example Usage

```python
subscription_id = 'subscription_id0'

result = invoices_controller.get_partial_invoice(subscription_id)
```


# Create Invoice

Create an Invoice

```python
def create_invoice(self,
                  subscription_id,
                  cycle_id,
                  request=None,
                  idempotency_key=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `str` | Template, Required | Subscription Id |
| `cycle_id` | `str` | Template, Required | Cycle Id |
| `request` | [`CreateInvoiceRequest`](../../doc/models/create-invoice-request.md) | Body, Optional | - |
| `idempotency_key` | `str` | Header, Optional | - |

## Response Type

[`GetInvoiceResponse`](../../doc/models/get-invoice-response.md)

## Example Usage

```python
subscription_id = 'subscription_id0'

cycle_id = 'cycle_id6'

result = invoices_controller.create_invoice(
    subscription_id,
    cycle_id
)
```


# Get Invoice

Gets an invoice

```python
def get_invoice(self,
               invoice_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `invoice_id` | `str` | Template, Required | Invoice Id |

## Response Type

[`GetInvoiceResponse`](../../doc/models/get-invoice-response.md)

## Example Usage

```python
invoice_id = 'invoice_id0'

result = invoices_controller.get_invoice(invoice_id)
```

