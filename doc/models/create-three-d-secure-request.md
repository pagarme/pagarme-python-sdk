
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
  "cavv": "cavv4",
  "eci": "eci0",
  "transaction_id": "transaction_id8",
  "success_url": "success_url2",
  "ds_transaction_id": "ds_transaction_id8",
  "version": "version4"
}
```

