
# Create Emv Data Decrypt Request

## Structure

`CreateEmvDataDecryptRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `cipher` | `str` | Required | Emv Decrypt cipher type |
| `dukpt` | [`CreateEmvDataDukptDecryptRequest`](../../doc/models/create-emv-data-dukpt-decrypt-request.md) | Optional | Dukpt data request |
| `tags` | [`List[CreateEmvDataTlvDecryptRequest]`](../../doc/models/create-emv-data-tlv-decrypt-request.md) | Required | Encrypted tags list |

## Example

```python
from pagarmeapisdk.models.create_emv_data_decrypt_request import CreateEmvDataDecryptRequest
from pagarmeapisdk.models.create_emv_data_dukpt_decrypt_request import CreateEmvDataDukptDecryptRequest

create_emv_data_decrypt_request = CreateEmvDataDecryptRequest(
    cipher=None,
    tags=[
        None
    ],
    dukpt=CreateEmvDataDukptDecryptRequest(
        ksn=None
    )
)
```

