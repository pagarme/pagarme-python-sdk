
# Create Checkout Boleto Payment Request

## Structure

`CreateCheckoutBoletoPaymentRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `bank` | `str` | Required | Bank identifier |
| `instructions` | `str` | Required | Instructions |
| `due_at` | `datetime` | Required | Due date |

## Example (as JSON)

```json
{
  "bank": "bank4",
  "instructions": "instructions4",
  "due_at": "2016-03-13T12:52:32.123Z"
}
```

