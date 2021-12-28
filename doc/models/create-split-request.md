
# Create Split Request

Split

## Structure

`CreateSplitRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | `string` | Required | Split type |
| `amount` | `int` | Required | Amount |
| `recipient_id` | `string` | Required | Recipient id |
| `options` | [`CreateSplitOptionsRequest`](/doc/models/create-split-options-request.md) | Optional | The split options request |

## Example (as JSON)

```json
{
  "type": "type0",
  "amount": 46,
  "recipient_id": "recipient_id0",
  "options": null
}
```

