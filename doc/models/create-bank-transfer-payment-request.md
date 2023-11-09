
# Create Bank Transfer Payment Request

Request for creating a bank transfer payment

## Structure

`CreateBankTransferPaymentRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `bank` | `str` | Required | Bank |
| `retries` | `int` | Required | Number of retries |

## Example (as JSON)

```json
{
  "bank": "bank4",
  "retries": 188
}
```

