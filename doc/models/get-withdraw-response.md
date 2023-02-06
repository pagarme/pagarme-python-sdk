
# Get Withdraw Response

## Structure

`GetWithdrawResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Optional | - |
| `gateway_id` | `string` | Optional | - |
| `amount` | `int` | Optional | - |
| `status` | `string` | Optional | - |
| `created_at` | `datetime` | Optional | - |
| `updated_at` | `datetime` | Optional | - |
| `metadata` | `List of string` | Optional | - |
| `fee` | `int` | Optional | - |
| `funding_date` | `datetime` | Optional | - |
| `funding_estimated_date` | `datetime` | Optional | - |
| `mtype` | `string` | Optional | - |
| `source` | [`GetWithdrawSourceResponse`](../../doc/models/get-withdraw-source-response.md) | Optional | - |
| `target` | [`GetWithdrawTargetResponse`](../../doc/models/get-withdraw-target-response.md) | Optional | - |

## Example (as JSON)

```json
{
  "id": null,
  "gateway_id": null,
  "amount": null,
  "status": null,
  "created_at": null,
  "updated_at": null,
  "metadata": null,
  "fee": null,
  "funding_date": null,
  "funding_estimated_date": null,
  "type": null,
  "source": null,
  "target": null
}
```

