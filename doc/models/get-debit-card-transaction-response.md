
# Get Debit Card Transaction Response

Response object for getting a debit card transaction

## Structure

`GetDebitCardTransactionResponse`

## Inherits From

[`GetTransactionResponse`](../../doc/models/get-transaction-response.md)

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `statement_descriptor` | `string` | Optional | Text that will appear on the debit card's statement |
| `acquirer_name` | `string` | Optional | Acquirer name |
| `acquirer_affiliation_code` | `string` | Optional | Aquirer affiliation code |
| `acquirer_tid` | `string` | Optional | Acquirer TID |
| `acquirer_nsu` | `string` | Optional | Acquirer NSU |
| `acquirer_auth_code` | `string` | Optional | Acquirer authorization code |
| `operation_type` | `string` | Optional | Operation type |
| `card` | [`GetCardResponse`](../../doc/models/get-card-response.md) | Optional | Card data |
| `acquirer_message` | `string` | Optional | Acquirer message |
| `acquirer_return_code` | `string` | Optional | Acquirer Return Code |
| `mpi` | `string` | Optional | Merchant Plugin |
| `eci` | `string` | Optional | Electronic Commerce Indicator (ECI) |
| `authentication_type` | `string` | Optional | Authentication type |
| `threed_authentication_url` | `string` | Optional | 3D-S Authentication Url |
| `funding_source` | `string` | Optional | Identify when a card is prepaid, credit or debit. |

## Example (as JSON)

```json
{
  "gateway_id": null,
  "amount": null,
  "status": null,
  "success": null,
  "created_at": null,
  "updated_at": null,
  "attempt_count": null,
  "max_attempts": null,
  "splits": null,
  "next_attempt": null,
  "transaction_type": "debit_card",
  "id": null,
  "gateway_response": null,
  "antifraud_response": null,
  "metadata": null,
  "split": null,
  "interest": null,
  "fine": null,
  "max_days_to_pay_past_due": null,
  "statement_descriptor": null,
  "acquirer_name": null,
  "acquirer_affiliation_code": null,
  "acquirer_tid": null,
  "acquirer_nsu": null,
  "acquirer_auth_code": null,
  "operation_type": null,
  "card": null,
  "acquirer_message": null,
  "acquirer_return_code": null,
  "mpi": null,
  "eci": null,
  "authentication_type": null,
  "threed_authentication_url": null,
  "funding_source": null
}
```

