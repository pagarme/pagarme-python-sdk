
# Get Subscription Split Response

## Structure

`GetSubscriptionSplitResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enabled` | `bool` | Required | Defines if the split is enabled |
| `rules` | [`List of GetSplitResponse`](../../doc/models/get-split-response.md) | Required | Split |

## Example (as JSON)

```json
{
  "enabled": false,
  "rules": [
    {
      "type": "type6",
      "amount": 210,
      "recipient": null,
      "gateway_id": "gateway_id6",
      "options": null,
      "id": "id4"
    }
  ]
}
```

