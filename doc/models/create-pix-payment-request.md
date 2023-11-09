
# Create Pix Payment Request

Contains information to create a pix payment

## Structure

`CreatePixPaymentRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `expires_at` | `datetime` | Optional | Datetime when pix payment will expire |
| `expires_in` | `int` | Optional | Seconds until pix payment expires |
| `additional_information` | [`List[PixAdditionalInformation]`](../../doc/models/pix-additional-information.md) | Optional | Pix additional information |

## Example (as JSON)

```json
{
  "expires_at": "2016-03-13T12:52:32.123Z",
  "expires_in": 216,
  "additional_information": [
    {
      "Name": "Name0",
      "Value": "Value2"
    },
    {
      "Name": "Name0",
      "Value": "Value2"
    }
  ]
}
```

