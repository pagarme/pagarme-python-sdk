
# Create Usage Request

Request for creating a usage

## Structure

`CreateUsageRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `quantity` | `int` | Required | - |
| `description` | `str` | Required | - |
| `used_at` | `datetime` | Required | - |
| `code` | `str` | Optional | Identification code in the client system |
| `group` | `str` | Optional | identification group in the client system |
| `amount` | `int` | Optional | Field used in item scheme type 'Percent' |

## Example

```python
import dateutil.parser

from pagarmeapisdk.models.create_usage_request import CreateUsageRequest

create_usage_request = CreateUsageRequest(
    quantity=222,
    description='description2',
    used_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    code='code0',
    group='group0',
    amount=108
)
```

