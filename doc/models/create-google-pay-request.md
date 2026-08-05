
# Create Google Pay Request

The GooglePay Token Payment Request

## Structure

`CreateGooglePayRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Optional | Informação sobre a versão do token. Único valor aceito é EC_v2 |
| `data` | `str` | Optional | Dados de pagamento criptografados. Corresponde ao encryptedMessage do token Google. |
| `intermediate_signing_key` | [`CreateGooglePayIntermediateSigningKeyRequest`](../../doc/models/create-google-pay-intermediate-signing-key-request.md) | Optional | The GooglePay intermediate signing key request |
| `signature` | `str` | Optional | Assinatura dos dados de pagamento. Verifica se a origem da mensagem é o Google. Corresponde ao signature do token Google. |
| `signed_message` | `str` | Optional | - |
| `merchant_identifier` | `str` | Optional | - |

## Example

```python
from pagarmeapisdk.models.create_google_pay_request import CreateGooglePayRequest

create_google_pay_request = CreateGooglePayRequest(
    version='version0',
    data='data4',
    intermediate_signing_key=None,
    signature='signature2',
    signed_message='signed_message0'
)
```

