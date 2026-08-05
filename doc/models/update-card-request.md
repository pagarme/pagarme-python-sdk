
# Update Card Request

Request for updating a card

## Structure

`UpdateCardRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `holder_name` | `str` | Required | Holder name |
| `exp_month` | `int` | Required | Expiration month |
| `exp_year` | `int` | Required | Expiration year |
| `billing_address_id` | `str` | Optional | Id of the address to be used as billing address |
| `billing_address` | [`CreateAddressRequest`](../../doc/models/create-address-request.md) | Required | Billing address |
| `metadata` | `Dict[str, str]` | Required | Metadata |
| `label` | `str` | Required | - |

## Example

```python
from pagarmeapisdk.models.create_address_request import CreateAddressRequest
from pagarmeapisdk.models.update_card_request import UpdateCardRequest

update_card_request = UpdateCardRequest(
    holder_name='holder_name0',
    exp_month=102,
    exp_year=142,
    billing_address=CreateAddressRequest(
        street=None,
        number=None,
        zip_code=None,
        neighborhood=None,
        city=None,
        state=None,
        country=None,
        complement=None,
        line_1=None,
        line_2=None
    ),
    metadata={
        'key0': 'metadata1',
        'key1': 'metadata0'
    },
    label='label4',
    billing_address_id='billing_address_id0'
)
```

