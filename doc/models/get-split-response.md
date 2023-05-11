
# Get Split Response

Split response

## Structure

`GetSplitResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | `string` | Optional | Type |
| `amount` | `int` | Optional | Amount |
| `recipient` | [`GetRecipientResponse`](../../doc/models/get-recipient-response.md) | Optional | Recipient |
| `gateway_id` | `string` | Optional | The split rule gateway id |
| `options` | [`GetSplitOptionsResponse`](../../doc/models/get-split-options-response.md) | Optional | - |
| `id` | `string` | Optional | - |

## Example (as JSON)

```json
{
  "type": "type0",
  "amount": 46,
  "recipient": {
    "id": "id8",
    "name": "name8",
    "email": "email8",
    "document": "document8",
    "description": "description2"
  },
  "gateway_id": "gateway_id0",
  "options": {
    "liable": false,
    "charge_processing_fee": false,
    "charge_remainder_fee": "charge_remainder_fee0"
  }
}
```

