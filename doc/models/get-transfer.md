
# Get Transfer

## Structure

`GetTransfer`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Required | - |
| `gateway_id` | `str` | Required | - |
| `amount` | `int` | Required | - |
| `status` | `str` | Required | - |
| `created_at` | `datetime` | Required | - |
| `updated_at` | `datetime` | Required | - |
| `metadata` | `Dict[str, str]` | Optional | - |
| `fee` | `int` | Optional | - |
| `funding_date` | `datetime` | Optional | - |
| `funding_estimated_date` | `datetime` | Optional | - |
| `mtype` | `str` | Required | - |
| `source` | [`GetTransferSourceResponse`](../../doc/models/get-transfer-source-response.md) | Required | - |
| `target` | [`GetTransferTargetResponse`](../../doc/models/get-transfer-target-response.md) | Required | - |

## Example

```python
import dateutil.parser

from pagarmeapisdk.models.get_transfer import GetTransfer
from pagarmeapisdk.models.get_transfer_source_response import GetTransferSourceResponse
from pagarmeapisdk.models.get_transfer_target_response import GetTransferTargetResponse

get_transfer = GetTransfer(
    id='id4',
    gateway_id='gateway_id6',
    amount=172,
    status='status4',
    created_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    updated_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    mtype='type6',
    source=GetTransferSourceResponse(),
    target=GetTransferTargetResponse(),
    metadata={
        'key0': 'metadata9',
        'key1': 'metadata0',
        'key2': 'metadata1'
    },
    fee=130,
    funding_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    funding_estimated_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
)
```

