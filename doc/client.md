
# Client Class Documentation

The following parameters are configurable for the API Client:

| Parameter | Type | Description |
|  --- | --- | --- |
| service_referer_name | `str` |  |
| http_client_instance | `Union[Session, HttpClientProvider]` | The Http Client passed from the sdk user for making requests |
| override_http_client_configuration | `bool` | The value which determines to override properties of the passed Http Client from the sdk user |
| http_call_back | `HttpCallBack` | The callback value that is invoked before and after an HTTP call is made to an endpoint |
| timeout | `float` | The value to use for connection timeout. <br> **Default: 60** |
| max_retries | `int` | The number of times to retry an endpoint call if it fails. <br> **Default: 0** |
| backoff_factor | `float` | A backoff factor to apply between attempts after the second try. <br> **Default: 2** |
| retry_statuses | `Array of int` | The http statuses on which retry is to be done. <br> **Default: [408, 413, 429, 500, 502, 503, 504, 521, 522, 524]** |
| retry_methods | `Array of string` | The http methods on which retry is to be done. <br> **Default: ["GET", "PUT"]** |
| proxy_settings | [`ProxySettings`](../doc/proxy-settings.md) | Optional proxy configuration to route HTTP requests through a proxy server. |
| basic_auth_credentials | [`BasicAuthCredentials`](auth/basic-authentication.md) | The credential object for Basic Authentication |

The API client can be initialized as follows:

## Code-Based Client Initialization

```python
from pagarmeapisdk.configuration import Environment
from pagarmeapisdk.http.auth.basic_auth import BasicAuthCredentials
from pagarmeapisdk.pagarmeapisdk_client import PagarmeapisdkClient

client = PagarmeapisdkClient(
    service_referer_name='ServiceRefererName',
    basic_auth_credentials=BasicAuthCredentials(
        username='BasicAuthUserName',
        password='BasicAuthPassword'
    ),
    environment=Environment.PRODUCTION
)
```

## Environment-Based Client Initialization

```python
from pagarmeapisdk.pagarmeapisdk_client import PagarmeapisdkClient

# Specify the path to your .env file if it’s located outside the project’s root directory.
client = PagarmeapisdkClient.from_environment(dotenv_path='/path/to/.env')
```

See the [Environment-Based Client Initialization](../doc/environment-based-client-initialization.md) section for details.

## PagarmeApiSDK Client

The gateway for the SDK. This class acts as a factory for the Controllers and also holds the configuration of the SDK.

## Controllers

| Name | Description |
|  --- | --- |
| subscriptions | Gets SubscriptionsController |
| orders | Gets OrdersController |
| plans | Gets PlansController |
| invoices | Gets InvoicesController |
| customers | Gets CustomersController |
| charges | Gets ChargesController |
| recipients | Gets RecipientsController |
| tokens | Gets TokensController |
| transactions | Gets TransactionsController |
| transfers | Gets TransfersController |
| payables | Gets PayablesController |

