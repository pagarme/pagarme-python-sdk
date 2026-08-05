
# Get Invoice Item Response

Response object for getting an invoice item

## Structure

`GetInvoiceItemResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | `int` | Optional | - |
| `description` | `str` | Optional | - |
| `pricing_scheme` | [`GetPricingSchemeResponse`](../../doc/models/get-pricing-scheme-response.md) | Optional | - |
| `price_bracket` | [`GetPriceBracketResponse`](../../doc/models/get-price-bracket-response.md) | Optional | - |
| `quantity` | `int` | Optional | - |
| `name` | `str` | Optional | - |
| `subscription_item_id` | `str` | Optional | Subscription Item Id |

## Example

```python
from pagarmeapisdk.models.get_invoice_item_response import GetInvoiceItemResponse

get_invoice_item_response = GetInvoiceItemResponse(
    amount=30,
    description='description2',
    pricing_scheme=None,
    price_bracket=None,
    quantity=144
)
```

