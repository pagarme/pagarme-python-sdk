
# Get Boleto Transaction Response

Response object for getting a boleto transaction

## Structure

`GetBoletoTransactionResponse`

## Inherits From

[`GetTransactionResponse`](../../doc/models/get-transaction-response.md)

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `url` | `str` | Optional | - |
| `barcode` | `str` | Optional | - |
| `nosso_numero` | `str` | Optional | - |
| `bank` | `str` | Optional | - |
| `document_number` | `str` | Optional | - |
| `instructions` | `str` | Optional | - |
| `billing_address` | [`GetBillingAddressResponse`](../../doc/models/get-billing-address-response.md) | Optional | - |
| `due_at` | `datetime` | Optional | - |
| `qr_code` | `str` | Optional | - |
| `line` | `str` | Optional | - |
| `pdf_password` | `str` | Optional | - |
| `pdf` | `str` | Optional | - |
| `paid_at` | `datetime` | Optional | - |
| `paid_amount` | `str` | Optional | - |
| `mtype` | `str` | Optional | - |
| `credit_at` | `datetime` | Optional | - |
| `statement_descriptor` | `str` | Optional | Soft Descriptor |

## Example

```python
import dateutil.parser

from pagarmeapisdk.models.get_transaction_response import GetBoletoTransactionResponse

get_boleto_transaction_response = GetBoletoTransactionResponse(
    url='url2',
    barcode='barcode2',
    nosso_numero='nosso_numero8',
    bank='bank6',
    document_number='document_number8',
    gateway_id='gateway_id8',
    amount=40,
    status='status6',
    success=False,
    created_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
)
```

