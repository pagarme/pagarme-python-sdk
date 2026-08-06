
# Create Emv Decrypt Request

## Structure

`CreateEmvDecryptRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `icc_data` | `str` | Required | - |
| `card_sequence_number` | `str` | Required | - |
| `data` | [`CreateEmvDataDecryptRequest`](../../doc/models/create-emv-data-decrypt-request.md) | Required | - |
| `poi` | [`CreateCardPaymentContactlessPOIRequest`](../../doc/models/create-card-payment-contactless-poi-request.md) | Optional | - |

## Example

```python
from pagarmeapisdk.models.create_card_payment_contactless_poi_request import CreateCardPaymentContactlessPOIRequest
from pagarmeapisdk.models.create_emv_data_decrypt_request import CreateEmvDataDecryptRequest
from pagarmeapisdk.models.create_emv_data_dukpt_decrypt_request import CreateEmvDataDukptDecryptRequest
from pagarmeapisdk.models.create_emv_decrypt_request import CreateEmvDecryptRequest

create_emv_decrypt_request = CreateEmvDecryptRequest(
    icc_data=None,
    card_sequence_number=None,
    data=CreateEmvDataDecryptRequest(
        cipher=None,
        tags=[
            None
        ],
        dukpt=CreateEmvDataDukptDecryptRequest(
            ksn=None
        )
    ),
    poi=CreateCardPaymentContactlessPOIRequest(
        system_name=None,
        model=None,
        provider=None,
        serial_number=None,
        version_number=None
    )
)
```

