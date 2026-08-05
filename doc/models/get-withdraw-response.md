
# Get Withdraw Response

## Structure

`GetWithdrawResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | - |
| `gateway_id` | `str` | Optional | - |
| `amount` | `int` | Optional | - |
| `status` | `str` | Optional | - |
| `created_at` | `datetime` | Optional | - |
| `updated_at` | `datetime` | Optional | - |
| `metadata` | `List[str]` | Optional | - |
| `fee` | `int` | Optional | - |
| `funding_date` | `datetime` | Optional | - |
| `funding_estimated_date` | `datetime` | Optional | - |
| `mtype` | `str` | Optional | - |
| `source` | [`GetWithdrawSourceResponse`](../../doc/models/get-withdraw-source-response.md) | Optional | - |
| `target` | [`GetWithdrawTargetResponse`](../../doc/models/get-withdraw-target-response.md) | Optional | - |

## Example

```python
import dateutil.parser

from pagarmeapisdk.models.get_withdraw_response import GetWithdrawResponse

get_withdraw_response = GetWithdrawResponse(
    id='id8',
    gateway_id='gateway_id2',
    amount=4,
    status='status0',
    created_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
)
```

