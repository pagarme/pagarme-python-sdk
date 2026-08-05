
# Create Card Token Request

Card token data

## Structure

`CreateCardTokenRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `number` | `str` | Required | Credit card number |
| `holder_name` | `str` | Required | Holder name, as written on the card |
| `exp_month` | `int` | Required | The expiration month |
| `exp_year` | `int` | Required | The expiration year, that can be informed with 2 or 4 digits |
| `cvv` | `str` | Required | The card's security code |
| `brand` | `str` | Required | Card brand |
| `label` | `str` | Required | - |

## Example

```python
from pagarmeapisdk.models.create_card_token_request import CreateCardTokenRequest

create_card_token_request = CreateCardTokenRequest(
    number='number2',
    holder_name='holder_name6',
    exp_month=186,
    exp_year=110,
    cvv='cvv8',
    brand='brand4',
    label='label0'
)
```

