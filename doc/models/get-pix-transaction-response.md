
# Get Pix Transaction Response

Response object when getting a pix transaction

## Structure

`GetPixTransactionResponse`

## Inherits From

[`GetTransactionResponse`](../../doc/models/get-transaction-response.md)

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `qr_code` | `string` | Optional | - |
| `qr_code_url` | `string` | Optional | - |
| `expires_at` | `datetime` | Optional | - |
| `additional_information` | [`List of PixAdditionalInformation`](../../doc/models/pix-additional-information.md) | Optional | - |
| `end_to_end_id` | `string` | Optional | - |
| `payer` | [`GetPixPayerResponse`](../../doc/models/get-pix-payer-response.md) | Optional | - |

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
  "transaction_type": "pix",
  "id": null,
  "gateway_response": null,
  "antifraud_response": null,
  "metadata": null,
  "split": null,
  "interest": null,
  "fine": null,
  "max_days_to_pay_past_due": null,
  "qr_code": null,
  "qr_code_url": null,
  "expires_at": null,
  "additional_information": null,
  "end_to_end_id": null,
  "payer": null
}
```

