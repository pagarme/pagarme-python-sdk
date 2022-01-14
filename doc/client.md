
# Client Class Documentation

The following parameters are configurable for the API Client:

| Parameter | Type | Description |
|  --- | --- | --- |
| `http_client_instance` | `HttpClient` | The Http Client passed from the sdk user for making requests |
| `override_http_client_configuration` | `bool` | The value which determines to override properties of the passed Http Client from the sdk user |
| `timeout` | `float` | The value to use for connection timeout. <br> **Default: 60** |
| `max_retries` | `int` | The number of times to retry an endpoint call if it fails. <br> **Default: 0** |
| `backoff_factor` | `float` | A backoff factor to apply between attempts after the second try. <br> **Default: 2** |
| `retry_statuses` | `Array of int` | The http statuses on which retry is to be done. <br> **Default: [408, 413, 429, 500, 502, 503, 504, 521, 522, 524]** |
| `retry_methods` | `Array of string` | The http methods on which retry is to be done. <br> **Default: ['GET', 'PUT']** |

The API client can be initialized as follows:

```python
from pagarmeapisdk.pagarmeapisdk_client import PagarmeapisdkClient
from pagarmeapisdk.configuration import Environment

client = PagarmeapisdkClient(
    environment=Environment.PRODUCTION,)
```

## PagarmeApiSDK Client

The gateway for the SDK. This class acts as a factory for the Controllers and also holds the configuration of the SDK.

## Controllers

| Name | Description |
|  --- | --- |
| plans | Gets PlansController |
| subscriptions | Gets SubscriptionsController |
| invoices | Gets InvoicesController |
| orders | Gets OrdersController |
| customers | Gets CustomersController |
| recipients | Gets RecipientsController |
| charges | Gets ChargesController |
| transfers | Gets TransfersController |
| tokens | Gets TokensController |
| transactions | Gets TransactionsController |

