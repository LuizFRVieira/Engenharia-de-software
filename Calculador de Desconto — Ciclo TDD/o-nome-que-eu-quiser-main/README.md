# Calculador de Desconto — Ciclo TDD

Atividade prática de TDD (Test-Driven Development) com o ciclo Vermelho-Verde-Refatorar,
aplicando o padrão de projeto Strategy em Python.

## Problema

Implementação de um calculador de desconto com três políticas:

- **Sem desconto** — retorna o valor original
- **Desconto percentual** — aplica um percentual fixo (ex.: 10%)
- **Desconto por cupom** — subtrai um valor fixo (ex.: R$ 20,00), nunca resultando em valor negativo

## Ciclo TDD

| Fase | Arquivo | Commit |
|------|---------|--------|
| 🔴 Red | `test_discount.py` | `red: testes iniciais` |
| 🟢 Green | `discount_green.py` | `green: implementação mínima` |
| 🔵 Refactor | `discount_refactor.py` | `refactor: padrão Strategy aplicado` |

## Padrão aplicado

Na fase de refatoração foi aplicado o padrão **Strategy**:
cada política de desconto virou uma classe independente (`NoDiscount`, `PercentageDiscount`, `CouponDiscount`)
com uma interface comum. A `DiscountCalculator` delega o cálculo para a estratégia correta,
sem precisar saber como cada uma funciona internamente.

## Links

- 🔗 Repositório: https://github.com/LuizFRVieira/o-nome-que-eu-quiser
- 🤖 Interação com IA (Claude): https://claude.ai/share/60b49aec-aef7-48cd-9d5d-a900aa87f9e6
- 🤖 Interação com IA (ChatGPT): https://chatgpt.com/share/69fe3f56-ff54-83e9-a4b9-44b6331cc170
