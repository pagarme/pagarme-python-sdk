
# List Payables Response

Response object for listing payable objects

## Structure

`ListPayablesResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `data` | [`List[GetPayableResponse]`](../../doc/models/get-payable-response.md) | Optional | The payable object |
| `paging` | [`CursorPagingResponse`](../../doc/models/cursor-paging-response.md) | Required | Cursor paging response |

## Example

```python
import dateutil.parser

from pagarmeapisdk.models.cursor_paging_response import CursorPagingResponse
from pagarmeapisdk.models.get_payable_response import GetPayableResponse
from pagarmeapisdk.models.list_payables_response import ListPayablesResponse

list_payables_response = ListPayablesResponse(
    paging=CursorPagingResponse(
        forward_cursor='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYWxhcGlDdXJzb3IiOiJleUpoYkdjaU9pSklVekkxTmlJc0luUjVjQ0k2SWtwWFZDSjkuZXlKcFlYUWlPaUl4TnpnMU9UTXpNVGN6SWl3aVpYaHdJam94TnpnMU9UTTJOemN6TENKcFpDSTZJalF6TWpVeU1ETXhOREFpZlEuTmtrUk85Slg3eC1YMVFLZ0ZIYkw3VGw4ZVV0NkR1ZWVQVlk5a0pHNXhxNCIsImlhdCI6MTc4NTkzMzE3MywiZXhwIjoxNzg1OTM2NzczfQ.5qM-BQbArZKXbfen5NnEXq6gbhyP-DrgsG1SMrpF4Y4'
    ),
    data=[
        GetPayableResponse(
            id='5b71f2a8b472ef521b224b75fd13c14e09d37822fd100f2cd425ef5aea02f5bf',
            status='paid',
            amount=1100,
            gateway_id=None,
            charge_id='ch_123',
            split_id=None,
            bulk_anticipation_id=None,
            recipient_id='re_cixm61j7e00doin6de8ocgttb',
            originator_model='ownership_assignment',
            originator_model_id=None,
            original_payment_date=dateutil.parser.parse('2025-08-21T03:00:00Z'),
            payment_method='credit_card',
            created_at=dateutil.parser.parse('2025-08-20T10:30:00Z'),
            settlement_id='03002e00-edde-6d4c-dd9e-ffaaafac08de',
            payment_profile_id='pp_03gd2e0o5kj37ujs38zgw9s9v',
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
    ]
)
```

