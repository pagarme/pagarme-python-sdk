
# Get Bank Transfer Transaction Response

Response object for getting a bank transfer transaction

## Structure

`GetBankTransferTransactionResponse`

## Inherits From

[`GetTransactionResponse`](../../doc/models/get-transaction-response.md)

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `url` | `string` | Optional | Payment url |
| `bank_tid` | `string` | Optional | Transaction identifier for the bank |
| `bank` | `string` | Optional | Bank |
| `paid_at` | `datetime` | Optional | Payment date |
| `paid_amount` | `int` | Optional | Paid amount |

## Example (as JSON)

```json
{
  "gateway_id": "gateway_id2",
  "amount": 244,
  "status": "status0",
  "success": false,
  "created_at": "2016-03-13T12:52:32.123Z",
  "transaction_type": "bank_transfer",
  "url": "url4",
  "bank_tid": "bank_tid4",
  "bank": "bank8",
  "paid_at": "2016-03-13T12:52:32.123Z",
  "paid_amount": 210
}
```

