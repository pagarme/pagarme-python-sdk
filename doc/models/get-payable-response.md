
# Get Payable Response

Response object for getting an payable

## Structure

`GetPayableResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Required | Payable Identifier |
| `status` | `str` | Required | Payable status |
| `amount` | `int` | Required | Payable amount in cents |
| `fee` | `int` | Optional | Payable fee amount in cents |
| `anticipation_fee` | `int` | Optional | Antecipation fee amount in cents |
| `fraud_coverage_fee` | `int` | Optional | Fraud coverage fee amount in cents |
| `installment` | `int` | Optional | Number of installment |
| `gateway_id` | `str` | Required | Payment gateway identifier<br><br>**Default**: `"null"` |
| `charge_id` | `str` | Required | Charge identifier<br><br>**Default**: `"null"` |
| `split_id` | `str` | Required | **Default**: `"null"` |
| `bulk_anticipation_id` | `str` | Required | **Default**: `"null"` |
| `anticipation_id` | `str` | Optional | - |
| `recipient_id` | `str` | Required | Recipient identifier |
| `originator_model` | `str` | Required | **Default**: `"null"` |
| `originator_model_id` | `str` | Required | Originator model identifier<br><br>**Default**: `"null"` |
| `payment_date` | `datetime` | Optional | Payment Date |
| `original_payment_date` | `datetime` | Required | Original Payment Date |
| `mtype` | `str` | Optional | Type of payable |
| `payment_method` | `str` | Required | Payment method of transaction<br><br>**Default**: `"null"` |
| `accrual_at` | `datetime` | Optional | Date issuer identify payment |
| `created_at` | `datetime` | Required | Creation date |
| `liquidation_arrangement_id` | `str` | Optional | **Default**: `"null"` |
| `settlement_id` | `str` | Required | Settlement identifier  (new in v7.x)<br><br>**Default**: `"null"` |
| `payment_profile_id` | `str` | Required | Operational identifier of merchant inside of payment platform (new in v7.x)<br><br>**Default**: `"null"` |

## Example

```python
import dateutil.parser

from pagarmeapisdk.models.get_payable_response import GetPayableResponse

get_payable_response = GetPayableResponse(
    id='5b71f2a8b472ef521b224b75fd13c14e09d37822fd100f2cd425ef5aea02f5bf',
    status='paid',
    amount=1100,
    gateway_id=None,
    charge_id='ch_123',
    split_id=None,
    bulk_anticipation_id=None,
    recipient_id='re_abcde123fghijk789',
    originator_model='ownership_assignment',
    originator_model_id=None,
    original_payment_date=dateutil.parser.parse('2025-08-21T03:00:00Z'),
    payment_method='credit_card',
    created_at=dateutil.parser.parse('2025-08-20T10:30:00Z'),
    settlement_id='03002e00-edde-6d4c-dd9e-ffaaafac08de',
    payment_profile_id='pp_abcde123fghijk789',
    fee=0,
    anticipation_fee=0,
    fraud_coverage_fee=0,
    installment=44,
    anticipation_id='anticipation_id0',
    payment_date=dateutil.parser.parse('2025-08-18T03:00:00Z'),
    mtype='credit',
    accrual_at=dateutil.parser.parse('2023-08-21T12:51:28Z'),
    liquidation_arrangement_id=None
)
```

