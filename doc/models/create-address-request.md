
# Create Address Request

Request for creating a new Address

## Structure

`CreateAddressRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `street` | `str` | Required | Street |
| `number` | `str` | Required | Number |
| `zip_code` | `str` | Required | The zip code containing only numbers. No special characters or spaces. |
| `neighborhood` | `str` | Required | Neighborhood |
| `city` | `str` | Required | City |
| `state` | `str` | Required | State |
| `country` | `str` | Required | Country. Must be entered using ISO 3166-1 alpha-2 format. See https://pt.wikipedia.org/wiki/ISO_3166-1_alfa-2 |
| `complement` | `str` | Required | Complement |
| `metadata` | `Dict[str, str]` | Optional | Metadata |
| `line_1` | `str` | Required | Line 1 for address |
| `line_2` | `str` | Required | Line 2 for address |

## Example

```python
from pagarmeapisdk.models.create_address_request import CreateAddressRequest

create_address_request = CreateAddressRequest(
    street='street8',
    number='number6',
    zip_code='zip_code2',
    neighborhood='neighborhood4',
    city='city8',
    state='state4',
    country='country2',
    complement='complement4',
    line_1='line_12',
    line_2='line_26',
    metadata={
        'key0': 'metadata5',
        'key1': 'metadata4'
    }
)
```

