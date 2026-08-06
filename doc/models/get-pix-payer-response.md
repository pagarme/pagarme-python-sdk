
# Get Pix Payer Response

Pix payer data.

## Structure

`GetPixPayerResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Optional | - |
| `document` | `str` | Optional | - |
| `document_type` | `str` | Optional | - |
| `bank_account` | [`GetPixBankAccountResponse`](../../doc/models/get-pix-bank-account-response.md) | Optional | - |

## Example

```python
from pagarmeapisdk.models.get_pix_payer_response import GetPixPayerResponse

get_pix_payer_response = GetPixPayerResponse(
    name='name0',
    document='document4',
    document_type='document_type8',
    bank_account=None
)
```

