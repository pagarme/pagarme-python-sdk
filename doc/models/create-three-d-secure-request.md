
# Create Three D Secure Request

Creates a 3D-S authentication payment

## Structure

`CreateThreeDSecureRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mpi` | `string` | Required | The MPI Vendor (MerchantPlugin) |
| `cavv` | `string` | Optional | The Cardholder Authentication Verification value |
| `eci` | `string` | Optional | The Electronic Commerce Indicator value |
| `transaction_id` | `string` | Optional | The TransactionId value (XID) |
| `success_url` | `string` | Optional | The success URL after the authentication |
| `ds_transaction_id` | `string` | Optional | Directory Service Transaction Identifier |
| `version` | `string` | Optional | ThreeDSecure Version |

## Example (as JSON)

```json
{
  "mpi": "mpi2",
  "cavv": null,
  "eci": null,
  "transaction_id": null,
  "success_url": null,
  "ds_transaction_id": null,
  "version": null
}
```

