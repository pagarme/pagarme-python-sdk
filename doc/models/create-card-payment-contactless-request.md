
# Create Card Payment Contactless Request

The card payment contactless request

## Structure

`CreateCardPaymentContactlessRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | `str` | Required | The authentication type |
| `apple_pay` | [`CreateApplePayRequest`](../../doc/models/create-apple-pay-request.md) | Optional | The ApplePay encrypted request |
| `google_pay` | [`CreateGooglePayRequest`](../../doc/models/create-google-pay-request.md) | Optional | The GooglePay encrypted request |
| `emv` | [`CreateEmvDecryptRequest`](../../doc/models/create-emv-decrypt-request.md) | Optional | The Emv encrypted request |

## Example

```python
from pagarmeapisdk.models.create_apple_pay_header_request import CreateApplePayHeaderRequest
from pagarmeapisdk.models.create_apple_pay_request import CreateApplePayRequest
from pagarmeapisdk.models.create_card_payment_contactless_request import CreateCardPaymentContactlessRequest
from pagarmeapisdk.models.create_emv_data_decrypt_request import CreateEmvDataDecryptRequest
from pagarmeapisdk.models.create_emv_decrypt_request import CreateEmvDecryptRequest
from pagarmeapisdk.models.create_google_pay_request import CreateGooglePayRequest

create_card_payment_contactless_request = CreateCardPaymentContactlessRequest(
    mtype='type4',
    apple_pay=CreateApplePayRequest(
        version=None,
        data=None,
        header=CreateApplePayHeaderRequest(
            ephemeral_public_key=None
        ),
        signature=None,
        merchant_identifier=None
    ),
    google_pay=CreateGooglePayRequest(),
    emv=CreateEmvDecryptRequest(
        icc_data=None,
        card_sequence_number=None,
        data=CreateEmvDataDecryptRequest(
            cipher=None,
            tags=[]
        )
    )
)
```

