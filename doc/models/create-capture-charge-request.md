
# Create Capture Charge Request

Request for capturing a charge

## Structure

`CreateCaptureChargeRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `code` | `string` | Required | Code for the charge. Sending this field will update the code send on the charge and order creation. |
| `amount` | `int` | Optional | The amount that will be captured |
| `split` | [`List of CreateSplitRequest`](../../doc/models/create-split-request.md) | Optional | Splits |
| `operation_reference` | `string` | Required | - |

## Example (as JSON)

```json
{
  "code": "code8",
  "amount": null,
  "split": null,
  "operation_reference": "operation_reference0"
}
```

