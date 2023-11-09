
# Create Checkout Bank Transfer Request

Checkout bank transfer payment request

## Structure

`CreateCheckoutBankTransferRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `bank` | `List[str]` | Required | Bank |
| `retries` | `int` | Required | Number of retries for processing |

## Example (as JSON)

```json
{
  "bank": [
    "bank7",
    "bank8",
    "bank9"
  ],
  "retries": 56
}
```

