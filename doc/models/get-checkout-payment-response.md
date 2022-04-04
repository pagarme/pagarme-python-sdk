
# Get Checkout Payment Response

Resposta das configurações de pagamento do checkout

## Structure

`GetCheckoutPaymentResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Required | - |
| `amount` | `int` | Optional | Valor em centavos |
| `default_payment_method` | `string` | Required | Meio de pagamento padrão no checkout |
| `success_url` | `string` | Required | Url de redirecionamento de sucesso após o checkou |
| `payment_url` | `string` | Required | Url para pagamento usando o checkout |
| `gateway_affiliation_id` | `string` | Required | Código da afiliação onde o pagamento será processado no gateway |
| `accepted_payment_methods` | `List of string` | Required | Meios de pagamento aceitos no checkout |
| `status` | `string` | Required | Status do checkout |
| `skip_checkout_success_page` | `bool` | Required | Pular tela de sucesso pós-pagamento? |
| `created_at` | `datetime` | Required | Data de criação |
| `updated_at` | `datetime` | Required | Data de atualização |
| `canceled_at` | `datetime` | Optional | Data de cancelamento |
| `customer_editable` | `bool` | Required | Torna o objeto customer editável |
| `customer` | [`GetCustomerResponse`](../../doc/models/get-customer-response.md) | Optional | Dados do comprador |
| `billingaddress` | [`GetAddressResponse`](../../doc/models/get-address-response.md) | Required | Dados do endereço de cobrança |
| `credit_card` | [`GetCheckoutCreditCardPaymentResponse`](../../doc/models/get-checkout-credit-card-payment-response.md) | Required | Configurações de cartão de crédito |
| `boleto` | [`GetCheckoutBoletoPaymentResponse`](../../doc/models/get-checkout-boleto-payment-response.md) | Required | Configurações de boleto |
| `billing_address_editable` | `bool` | Required | Indica se o billing address poderá ser editado |
| `shipping` | [`GetShippingResponse`](../../doc/models/get-shipping-response.md) | Required | Configurações  de entrega |
| `shippable` | `bool` | Required | Indica se possui entrega |
| `closed_at` | `datetime` | Optional | Data de fechamento |
| `expires_at` | `datetime` | Optional | Data de expiração |
| `currency` | `string` | Required | Moeda |
| `debit_card` | [`GetCheckoutDebitCardPaymentResponse`](../../doc/models/get-checkout-debit-card-payment-response.md) | Optional | Configurações de cartão de débito |
| `bank_transfer` | [`GetCheckoutBankTransferPaymentResponse`](../../doc/models/get-checkout-bank-transfer-payment-response.md) | Optional | Bank transfer payment response |
| `accepted_brands` | `List of string` | Required | Accepted Brands |
| `pix` | [`GetCheckoutPixPaymentResponse`](../../doc/models/get-checkout-pix-payment-response.md) | Optional | Pix payment response |

## Example (as JSON)

```json
{
  "id": "id0",
  "amount": null,
  "default_payment_method": "default_payment_method0",
  "success_url": "success_url2",
  "payment_url": "payment_url6",
  "gateway_affiliation_id": "gateway_affiliation_id4",
  "accepted_payment_methods": [
    "accepted_payment_methods3",
    "accepted_payment_methods4",
    "accepted_payment_methods5"
  ],
  "status": "status8",
  "skip_checkout_success_page": false,
  "created_at": "2016-03-13T12:52:32.123Z",
  "updated_at": "2016-03-13T12:52:32.123Z",
  "canceled_at": null,
  "customer_editable": false,
  "customer": null,
  "billingaddress": {
    "id": "id8",
    "street": "street8",
    "number": "number6",
    "complement": "complement4",
    "zip_code": "zip_code2",
    "neighborhood": "neighborhood4",
    "city": "city8",
    "state": "state4",
    "country": "country2",
    "status": "status0",
    "created_at": "2016-03-13T12:52:32.123Z",
    "updated_at": "2016-03-13T12:52:32.123Z",
    "customer": null,
    "metadata": {
      "key0": "metadata5"
    },
    "line_1": "line_18",
    "line_2": "line_26",
    "deleted_at": null
  },
  "credit_card": {
    "statementDescriptor": "statementDescriptor4",
    "installments": [
      {
        "number": "number1",
        "total": 167
      }
    ],
    "authentication": {
      "type": "type0",
      "threed_secure": {
        "mpi": "mpi0",
        "eci": "eci2",
        "cavv": "cavv8",
        "transaction_Id": "transaction_Id2",
        "success_url": "success_url4"
      }
    }
  },
  "boleto": {
    "due_at": "2016-03-13T12:52:32.123Z",
    "instructions": "instructions2"
  },
  "billing_address_editable": false,
  "shipping": {
    "amount": 52,
    "description": "description6",
    "recipient_name": "recipient_name2",
    "recipient_phone": "recipient_phone6",
    "address": {
      "id": "id0",
      "street": "street0",
      "number": "number8",
      "complement": "complement6",
      "zip_code": "zip_code4",
      "neighborhood": "neighborhood6",
      "city": "city0",
      "state": "state6",
      "country": "country4",
      "status": "status2",
      "created_at": "2016-03-13T12:52:32.123Z",
      "updated_at": "2016-03-13T12:52:32.123Z",
      "customer": null,
      "metadata": {
        "key0": "metadata7"
      },
      "line_1": "line_14",
      "line_2": "line_28",
      "deleted_at": null
    },
    "max_delivery_date": null,
    "estimated_delivery_date": null,
    "type": "type6"
  },
  "shippable": false,
  "closed_at": null,
  "expires_at": null,
  "currency": "currency0",
  "debit_card": null,
  "bank_transfer": null,
  "accepted_brands": [
    "accepted_brands8",
    "accepted_brands9"
  ],
  "pix": null
}
```

