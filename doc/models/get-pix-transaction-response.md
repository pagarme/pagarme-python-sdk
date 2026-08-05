
# Get Pix Transaction Response

Response object when getting a pix transaction

## Structure

`GetPixTransactionResponse`

## Inherits From

[`GetTransactionResponse`](../../doc/models/get-transaction-response.md)

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `qr_code` | `str` | Optional | - |
| `qr_code_url` | `str` | Optional | - |
| `expires_at` | `datetime` | Optional | - |
| `additional_information` | [`List[PixAdditionalInformation]`](../../doc/models/pix-additional-information.md) | Optional | - |
| `end_to_end_id` | `str` | Optional | - |
| `payer` | [`GetPixPayerResponse`](../../doc/models/get-pix-payer-response.md) | Optional | - |
| `pix_provider_tid` | `str` | Optional | Pix provider TID |

## Example

```python
import dateutil.parser

from pagarmeapisdk.models.get_transaction_response import GetPixTransactionResponse

get_pix_transaction_response = GetPixTransactionResponse(
    qr_code='qr_code8',
    qr_code_url='qr_code_url4',
    expires_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    additional_information=[
        None
    ],
    end_to_end_id='end_to_end_id8',
    gateway_id='gateway_id8',
    amount=40,
    status='status6',
    success=False,
    created_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
)
```

