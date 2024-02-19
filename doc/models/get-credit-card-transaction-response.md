
# Get Credit Card Transaction Response

Response object for getting a credit card transaction

## Structure

`GetCreditCardTransactionResponse`

## Inherits From

[`GetTransactionResponse`](../../doc/models/get-transaction-response.md)

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `statement_descriptor` | `str` | Optional | Text that will appear on the credit card's statement |
| `acquirer_name` | `str` | Optional | Acquirer name |
| `acquirer_affiliation_code` | `str` | Optional | Aquirer affiliation code |
| `acquirer_tid` | `str` | Optional | Acquirer TID |
| `acquirer_nsu` | `str` | Optional | Acquirer NSU |
| `acquirer_auth_code` | `str` | Optional | Acquirer authorization code |
| `operation_type` | `str` | Optional | Operation type |
| `card` | [`GetCardResponse`](../../doc/models/get-card-response.md) | Optional | Card data |
| `acquirer_message` | `str` | Optional | Acquirer message |
| `acquirer_return_code` | `str` | Optional | Acquirer Return Code |
| `installments` | `int` | Optional | Number of installments |
| `threed_authentication_url` | `str` | Optional | 3D-S authentication Url |
| `funding_source` | `str` | Optional | Identify when a card is prepaid, credit or debit. |
| `retry_info` | [`GetRetryTransactionInformationResponse`](../../doc/models/get-retry-transaction-information-response.md) | Optional | Retry transaction information |

## Example (as JSON)

```json
{
  "gateway_id": "gateway_id8",
  "amount": 40,
  "status": "status6",
  "success": false,
  "created_at": "2016-03-13T12:52:32.123Z",
  "statement_descriptor": "statement_descriptor2",
  "acquirer_name": "acquirer_name6",
  "acquirer_affiliation_code": "acquirer_affiliation_code6",
  "acquirer_tid": "acquirer_tid8",
  "acquirer_nsu": "acquirer_nsu8"
}
```

