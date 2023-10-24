
# Create Split Request

Split

## Structure

`CreateSplitRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | `str` | Required | Split type |
| `amount` | `int` | Required | Amount |
| `recipient_id` | `str` | Required | Recipient id |
| `options` | [`CreateSplitOptionsRequest`](../../doc/models/create-split-options-request.md) | Optional | The split options request |
| `split_rule_id` | `str` | Optional | Rule code used in cancellation. |

## Example (as JSON)

```json
{
  "type": "type6",
  "amount": 100,
  "recipient_id": "recipient_id6",
  "options": {
    "liable": false,
    "charge_processing_fee": false,
    "charge_remainder_fee": false
  },
  "split_rule_id": "split_rule_id8"
}
```

