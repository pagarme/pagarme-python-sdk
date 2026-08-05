
# Get Checkout Bank Transfer Payment Response

Bank transfer checkout response

## Structure

`GetCheckoutBankTransferPaymentResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `bank` | `List[str]` | Optional | bank list response |

## Example

```python
from pagarmeapisdk.models.get_checkout_bank_transfer_payment_response import GetCheckoutBankTransferPaymentResponse

get_checkout_bank_transfer_payment_response = GetCheckoutBankTransferPaymentResponse(
    bank=[
        'bank9',
        'bank0',
        'bank1'
    ]
)
```

