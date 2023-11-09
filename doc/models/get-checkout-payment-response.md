
# Get Checkout Payment Response

Resposta das configurações de pagamento do checkout

## Structure

`GetCheckoutPaymentResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | - |
| `amount` | `int` | Optional | Valor em centavos |
| `default_payment_method` | `str` | Optional | Meio de pagamento padrão no checkout |
| `success_url` | `str` | Optional | Url de redirecionamento de sucesso após o checkou |
| `payment_url` | `str` | Optional | Url para pagamento usando o checkout |
| `gateway_affiliation_id` | `str` | Optional | Código da afiliação onde o pagamento será processado no gateway |
| `accepted_payment_methods` | `List[str]` | Optional | Meios de pagamento aceitos no checkout |
| `status` | `str` | Optional | Status do checkout |
| `skip_checkout_success_page` | `bool` | Optional | Pular tela de sucesso pós-pagamento? |
| `created_at` | `datetime` | Optional | Data de criação |
| `updated_at` | `datetime` | Optional | Data de atualização |
| `canceled_at` | `datetime` | Optional | Data de cancelamento |
| `customer_editable` | `bool` | Optional | Torna o objeto customer editável |
| `customer` | [`GetCustomerResponse`](../../doc/models/get-customer-response.md) | Optional | Dados do comprador |
| `billingaddress` | [`GetAddressResponse`](../../doc/models/get-address-response.md) | Optional | Dados do endereço de cobrança |
| `credit_card` | [`GetCheckoutCreditCardPaymentResponse`](../../doc/models/get-checkout-credit-card-payment-response.md) | Optional | Configurações de cartão de crédito |
| `boleto` | [`GetCheckoutBoletoPaymentResponse`](../../doc/models/get-checkout-boleto-payment-response.md) | Optional | Configurações de boleto |
| `billing_address_editable` | `bool` | Optional | Indica se o billing address poderá ser editado |
| `shipping` | [`GetShippingResponse`](../../doc/models/get-shipping-response.md) | Optional | Configurações  de entrega |
| `shippable` | `bool` | Optional | Indica se possui entrega |
| `closed_at` | `datetime` | Optional | Data de fechamento |
| `expires_at` | `datetime` | Optional | Data de expiração |
| `currency` | `str` | Optional | Moeda |
| `debit_card` | [`GetCheckoutDebitCardPaymentResponse`](../../doc/models/get-checkout-debit-card-payment-response.md) | Optional | Configurações de cartão de débito |
| `bank_transfer` | [`GetCheckoutBankTransferPaymentResponse`](../../doc/models/get-checkout-bank-transfer-payment-response.md) | Optional | Bank transfer payment response |
| `accepted_brands` | `List[str]` | Optional | Accepted Brands |
| `pix` | [`GetCheckoutPixPaymentResponse`](../../doc/models/get-checkout-pix-payment-response.md) | Optional | Pix payment response |

## Example (as JSON)

```json
{
  "id": "id6",
  "amount": 148,
  "default_payment_method": "default_payment_method6",
  "success_url": "success_url8",
  "payment_url": "payment_url0"
}
```

