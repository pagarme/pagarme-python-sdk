
# Getting Started with PagarmeApiSDK

## Introduction

Pagarme API

## Building

You must have Python `3 >=3.7, <= 3.11` installed on your system to install and run this SDK. This SDK package depends on other Python packages like pytest, jsonpickle etc. These dependencies are defined in the `requirements.txt` file that comes with the SDK. To resolve these dependencies, you can use the PIP Dependency manager. Install it by following steps at [https://pip.pypa.io/en/stable/installing/](https://pip.pypa.io/en/stable/installing/).

Python and PIP executables should be defined in your PATH. Open command prompt and type `pip --version`. This should display the version of the PIP Dependency Manager installed if your installation was successful and the paths are properly defined.

* Using command line, navigate to the directory containing the generated files (including `requirements.txt`) for the SDK.
* Run the command `pip install -r requirements.txt`. This should install all the required dependencies.

![Building SDK - Step 1](https://apidocs.io/illustration/python?workspaceFolder=Pagarmeapisdk-Python&step=installDependencies)

## Installation

The following section explains how to use the pagarmeapisdk library in a new project.

### 1. Open Project in an IDE

Open up a Python IDE like PyCharm. The basic workflow presented here is also applicable if you prefer using a different editor or IDE.

![Open project in PyCharm - Step 1](https://apidocs.io/illustration/python?workspaceFolder=Pagarmeapisdk-Python&step=pyCharm)

Click on `Open` in PyCharm to browse to your generated SDK directory and then click `OK`.

![Open project in PyCharm - Step 2](https://apidocs.io/illustration/python?workspaceFolder=Pagarmeapisdk-Python&step=openProject0)

The project files will be displayed in the side bar as follows:

![Open project in PyCharm - Step 3](https://apidocs.io/illustration/python?workspaceFolder=Pagarmeapisdk-Python&projectName=pagarmeapisdk&step=openProject1)

### 2. Add a new Test Project

Create a new directory by right clicking on the solution name as shown below:

![Add a new project in PyCharm - Step 1](https://apidocs.io/illustration/python?workspaceFolder=Pagarmeapisdk-Python&projectName=pagarmeapisdk&step=createDirectory)

Name the directory as "test".

![Add a new project in PyCharm - Step 2](https://apidocs.io/illustration/python?workspaceFolder=Pagarmeapisdk-Python&step=nameDirectory)

Add a python file to this project.

![Add a new project in PyCharm - Step 3](https://apidocs.io/illustration/python?workspaceFolder=Pagarmeapisdk-Python&projectName=pagarmeapisdk&step=createFile)

Name it "testSDK".

![Add a new project in PyCharm - Step 4](https://apidocs.io/illustration/python?workspaceFolder=Pagarmeapisdk-Python&projectName=pagarmeapisdk&step=nameFile)

In your python file you will be required to import the generated python library using the following code lines

```python
from pagarmeapisdk.pagarmeapisdk_client import PagarmeapisdkClient
```

![Add a new project in PyCharm - Step 5](https://apidocs.io/illustration/python?workspaceFolder=Pagarmeapisdk-Python&projectName=pagarmeapisdk&libraryName=pagarmeapisdk.pagarmeapisdk_client&className=PagarmeapisdkClient&step=projectFiles)

After this you can write code to instantiate an API client object, get a controller object and  make API calls. Sample code is given in the subsequent sections.

### 3. Run the Test Project

To run the file within your test project, right click on your Python file inside your Test project and click on `Run`

![Run Test Project - Step 1](https://apidocs.io/illustration/python?workspaceFolder=Pagarmeapisdk-Python&projectName=pagarmeapisdk&libraryName=pagarmeapisdk.pagarmeapisdk_client&className=PagarmeapisdkClient&step=runProject)

## Initialize the API Client

**_Note:_** Documentation for the client can be found [here.](https://www.github.com/pagarme/pagarme-python-sdk/tree/6.8.3/doc/client.md)

The following parameters are configurable for the API Client:

| Parameter | Type | Description |
|  --- | --- | --- |
| `service_referer_name` | `str` |  |
| `http_client_instance` | `HttpClient` | The Http Client passed from the sdk user for making requests |
| `override_http_client_configuration` | `bool` | The value which determines to override properties of the passed Http Client from the sdk user |
| `http_call_back` | `HttpCallBack` | The callback value that is invoked before and after an HTTP call is made to an endpoint |
| `timeout` | `float` | The value to use for connection timeout. <br> **Default: 60** |
| `max_retries` | `int` | The number of times to retry an endpoint call if it fails. <br> **Default: 0** |
| `backoff_factor` | `float` | A backoff factor to apply between attempts after the second try. <br> **Default: 2** |
| `retry_statuses` | `Array of int` | The http statuses on which retry is to be done. <br> **Default: [408, 413, 429, 500, 502, 503, 504, 521, 522, 524]** |
| `retry_methods` | `Array of string` | The http methods on which retry is to be done. <br> **Default: ['GET', 'PUT']** |
| `basic_auth_user_name` | `str` | The username to use with basic authentication |
| `basic_auth_password` | `str` | The password to use with basic authentication |

The API client can be initialized as follows:

```python
from pagarmeapisdk.pagarmeapisdk_client import PagarmeapisdkClient
from pagarmeapisdk.configuration import Environment

client = PagarmeapisdkClient(
    service_referer_name='ServiceRefererName',
    basic_auth_user_name='BasicAuthUserName',
    basic_auth_password='BasicAuthPassword',
    environment=Environment.PRODUCTION
)
```

## Authorization

This API uses `Basic Authentication`.

## API Errors

Here is the list of errors that the API might throw.

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Invalid request | [`ErrorException`](https://www.github.com/pagarme/pagarme-python-sdk/tree/6.8.3/doc/models/error-exception.md) |
| 401 | Invalid API key | [`ErrorException`](https://www.github.com/pagarme/pagarme-python-sdk/tree/6.8.3/doc/models/error-exception.md) |
| 404 | An informed resource was not found | [`ErrorException`](https://www.github.com/pagarme/pagarme-python-sdk/tree/6.8.3/doc/models/error-exception.md) |
| 412 | Business validation error | [`ErrorException`](https://www.github.com/pagarme/pagarme-python-sdk/tree/6.8.3/doc/models/error-exception.md) |
| 422 | Contract validation error | [`ErrorException`](https://www.github.com/pagarme/pagarme-python-sdk/tree/6.8.3/doc/models/error-exception.md) |
| 500 | Internal server error | [`ErrorException`](https://www.github.com/pagarme/pagarme-python-sdk/tree/6.8.3/doc/models/error-exception.md) |

## List of APIs

* [Subscriptions](https://www.github.com/pagarme/pagarme-python-sdk/tree/6.8.3/doc/controllers/subscriptions.md)
* [Orders](https://www.github.com/pagarme/pagarme-python-sdk/tree/6.8.3/doc/controllers/orders.md)
* [Plans](https://www.github.com/pagarme/pagarme-python-sdk/tree/6.8.3/doc/controllers/plans.md)
* [Invoices](https://www.github.com/pagarme/pagarme-python-sdk/tree/6.8.3/doc/controllers/invoices.md)
* [Customers](https://www.github.com/pagarme/pagarme-python-sdk/tree/6.8.3/doc/controllers/customers.md)
* [Charges](https://www.github.com/pagarme/pagarme-python-sdk/tree/6.8.3/doc/controllers/charges.md)
* [Recipients](https://www.github.com/pagarme/pagarme-python-sdk/tree/6.8.3/doc/controllers/recipients.md)
* [Tokens](https://www.github.com/pagarme/pagarme-python-sdk/tree/6.8.3/doc/controllers/tokens.md)
* [Transactions](https://www.github.com/pagarme/pagarme-python-sdk/tree/6.8.3/doc/controllers/transactions.md)
* [Transfers](https://www.github.com/pagarme/pagarme-python-sdk/tree/6.8.3/doc/controllers/transfers.md)
* [Payables](https://www.github.com/pagarme/pagarme-python-sdk/tree/6.8.3/doc/controllers/payables.md)
* [Balance Operations](https://www.github.com/pagarme/pagarme-python-sdk/tree/6.8.3/doc/controllers/balance-operations.md)

## Classes Documentation

* [Utility Classes](https://www.github.com/pagarme/pagarme-python-sdk/tree/6.8.3/doc/utility-classes.md)
* [HttpResponse](https://www.github.com/pagarme/pagarme-python-sdk/tree/6.8.3/doc/http-response.md)
* [HttpRequest](https://www.github.com/pagarme/pagarme-python-sdk/tree/6.8.3/doc/http-request.md)

