
# Create Cancel Charge Split Rules Request

Creates a refund with split rules

## Structure

`CreateCancelChargeSplitRulesRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Required | The split rule gateway id |
| `amount` | `int` | Required | The split rule amount |
| `mtype` | `str` | Required | The amount type (flat ou percentage) |

## Example

```python
from pagarmeapisdk.models.create_cancel_charge_split_rules_request import CreateCancelChargeSplitRulesRequest

create_cancel_charge_split_rules_request = CreateCancelChargeSplitRulesRequest(
    id='id6',
    amount=158,
    mtype='type4'
)
```

