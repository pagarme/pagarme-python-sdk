
# Get Withdraw Response

## Structure

`GetWithdrawResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Required | - |
| `gateway_id` | `string` | Required | - |
| `amount` | `int` | Required | - |
| `status` | `string` | Required | - |
| `created_at` | `datetime` | Required | - |
| `updated_at` | `datetime` | Required | - |
| `metadata` | `List of string` | Optional | - |
| `fee` | `int` | Optional | - |
| `funding_date` | `datetime` | Optional | - |
| `funding_estimated_date` | `datetime` | Optional | - |
| `mtype` | `string` | Required | - |
| `source` | [`GetWithdrawSourceResponse`](../../doc/models/get-withdraw-source-response.md) | Required | - |
| `target` | [`GetWithdrawTargetResponse`](../../doc/models/get-withdraw-target-response.md) | Required | - |

## Example (as JSON)

```json
{
  "id": "id0",
  "gateway_id": "gateway_id0",
  "amount": 46,
  "status": "status8",
  "created_at": "2016-03-13T12:52:32.123Z",
  "updated_at": "2016-03-13T12:52:32.123Z",
  "metadata": null,
  "fee": null,
  "funding_date": null,
  "funding_estimated_date": null,
  "type": "type0",
  "source": {
    "source_id": "source_id8",
    "type": "type6"
  },
  "target": {
    "target_id": "target_id2",
    "type": "type8"
  }
}
```

