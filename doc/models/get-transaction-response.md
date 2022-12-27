
# Get Transaction Response

Generic response object for getting a transaction.

## Structure

`GetTransactionResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `gateway_id` | `string` | Required | Gateway transaction id |
| `amount` | `int` | Required | Amount in cents |
| `status` | `string` | Required | Transaction status |
| `success` | `bool` | Required | Indicates if the transaction ocurred successfuly |
| `created_at` | `datetime` | Required | Creation date |
| `updated_at` | `datetime` | Required | Last update date |
| `attempt_count` | `int` | Required | Number of attempts tried |
| `max_attempts` | `int` | Required | Max attempts |
| `splits` | [`List of GetSplitResponse`](../../doc/models/get-split-response.md) | Required | Splits |
| `next_attempt` | `datetime` | Optional | Date and time of the next attempt |
| `transaction_type` | `string` | Optional | - |
| `id` | `string` | Required | Código da transação |
| `gateway_response` | [`GetGatewayResponseResponse`](../../doc/models/get-gateway-response-response.md) | Required | The Gateway Response |
| `antifraud_response` | [`GetAntifraudResponse`](../../doc/models/get-antifraud-response.md) | Required | - |
| `metadata` | `dict` | Optional | - |
| `split` | [`List of GetSplitResponse`](../../doc/models/get-split-response.md) | Required | - |
| `interest` | [`GetInterestResponse`](../../doc/models/get-interest-response.md) | Optional | - |
| `fine` | [`GetFineResponse`](../../doc/models/get-fine-response.md) | Optional | - |
| `max_days_to_pay_past_due` | `int` | Optional | - |

## Example (as JSON)

```json
{
  "gateway_id": "gateway_id0",
  "amount": 46,
  "status": "status8",
  "success": false,
  "created_at": "2016-03-13T12:52:32.123Z",
  "updated_at": "2016-03-13T12:52:32.123Z",
  "attempt_count": 70,
  "max_attempts": 174,
  "splits": [
    {
      "type": "type4",
      "amount": 62,
      "recipient": null,
      "gateway_id": "gateway_id4",
      "options": null,
      "id": "id6"
    },
    {
      "type": "type3",
      "amount": 63,
      "recipient": null,
      "gateway_id": "gateway_id3",
      "options": null,
      "id": "id7"
    }
  ],
  "next_attempt": null,
  "transaction_type": null,
  "id": "id0",
  "gateway_response": {
    "code": "code6",
    "errors": [
      {
        "message": "message3"
      },
      {
        "message": "message4"
      },
      {
        "message": "message5"
      }
    ]
  },
  "antifraud_response": {
    "status": "status0",
    "return_code": "return_code8",
    "return_message": "return_message4",
    "provider_name": "provider_name4",
    "score": "score8"
  },
  "metadata": null,
  "split": [
    {
      "type": "type6",
      "amount": 28,
      "recipient": null,
      "gateway_id": "gateway_id6",
      "options": null,
      "id": "id4"
    },
    {
      "type": "type5",
      "amount": 27,
      "recipient": null,
      "gateway_id": "gateway_id5",
      "options": null,
      "id": "id5"
    },
    {
      "type": "type4",
      "amount": 26,
      "recipient": null,
      "gateway_id": "gateway_id4",
      "options": null,
      "id": "id6"
    }
  ],
  "interest": null,
  "fine": null,
  "max_days_to_pay_past_due": null
}
```

