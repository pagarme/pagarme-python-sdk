
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
  "type": null,
  "amount": null,
  "recipient": null,
  "gateway_id": null,
  "options": null,
  "id": null
}
```

