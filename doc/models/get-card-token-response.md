
# Get Card Token Response

Card token data

## Structure

`GetCardTokenResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `last_four_digits` | `str` | Optional | - |
| `holder_name` | `str` | Optional | - |
| `holder_document` | `str` | Optional | - |
| `exp_month` | `int` | Optional | - |
| `exp_year` | `int` | Optional | - |
| `brand` | `str` | Optional | - |
| `mtype` | `str` | Optional | - |
| `label` | `str` | Optional | - |

## Example

```python
from pagarmeapisdk.models.get_card_token_response import GetCardTokenResponse

get_card_token_response = GetCardTokenResponse(
    last_four_digits='last_four_digits8',
    holder_name='holder_name8',
    holder_document='holder_document4',
    exp_month=32,
    exp_year=8
)
```

