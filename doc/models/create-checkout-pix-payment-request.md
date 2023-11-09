
# Create Checkout Pix Payment Request

Checkout pix payment request

## Structure

`CreateCheckoutPixPaymentRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `expires_at` | `datetime` | Optional | Expires at |
| `expires_in` | `int` | Optional | Expires in |
| `additional_information` | [`List[PixAdditionalInformation]`](../../doc/models/pix-additional-information.md) | Optional | Additional information |

## Example (as JSON)

```json
{
  "expires_at": "2016-03-13T12:52:32.123Z",
  "expires_in": 4,
  "additional_information": [
    {
      "Name": "Name0",
      "Value": "Value2"
    }
  ]
}
```

