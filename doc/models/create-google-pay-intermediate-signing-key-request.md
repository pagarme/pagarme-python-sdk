
# Create Google Pay Intermediate Signing Key Request

The GooglePay Intermediate Signing Key Request

## Structure

`CreateGooglePayIntermediateSigningKeyRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `signed_key` | `str` | Optional | Uma mensagem codificada em Base64 com a descrição de pagamento da chave. |
| `signatures` | `List[str]` | Optional | Verifica se a origem da chave de assinatura intermediária é o Google. É codificada em Base64 e criada usando o ECDSA. |

## Example

```python
from pagarmeapisdk.models.create_google_pay_intermediate_signing_key_request import CreateGooglePayIntermediateSigningKeyRequest

create_google_pay_intermediate_signing_key_request = CreateGooglePayIntermediateSigningKeyRequest(
    signed_key='signed_key8',
    signatures=[
        'signatures4',
        'signatures5',
        'signatures6'
    ]
)
```

