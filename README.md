# Caixa — desafio de cédulas

Três entradas de console para simular saques. Não movimenta dinheiro real nem se conecta a banco.

```sh
python Caixa-1/program.py
python Caixa-2/program.py
python Caixa-3/program.py
python -m unittest discover -s tests -v
```

- **Caixa 1:** calcula notas de R$ 100, 50, 20, 10, 5 e 2.
- **Caixa 2:** usa essas cédulas e um saldo inicial simulado entre R$ 200 e R$ 10.000; rejeita pedidos acima do saldo.
- **Caixa 3:** inclui também a cédula de R$ 1 como exercício.

Valores aceitam vírgula ou ponto e até duas casas decimais. O resultado distingue o total entregue, a parte não entregue e o saldo restante. Apenas a quantia efetivamente entregue é debitada. Frações de real não são pagas em moedas.

## Lógica e validação

`cash.py` concentra a conversão para `Decimal`, a validação de valor/saldo e o planejamento de cédulas. Os três `program.py` são entradas pequenas e não iniciam interação ao serem importados.

Uma busca limitada para o restante evita a armadilha de um algoritmo guloso simples: R$ 6 são entregues com três notas de R$ 2; R$ 101 também podem ser entregues integralmente. A quantidade de notas é conferida por uma referência exaustiva para os valores representáveis de R$ 1 a R$ 600. Os cinco testes também cobrem centavos, débito efetivo, saldo insuficiente, valores inválidos e os três programas de console com EOF.

```python
from cash import plan_withdrawal
result = plan_withdrawal("175,45", "200,00")
assert result.dispensed == 175
assert result.remainder == result.requested - result.dispensed
assert result.balance == 25
```

O simulador considera estoque ilimitado de cada cédula e limita os valores de entrada a R$ 1 bilhão. Quando a quantia inteira não é representável, entrega o maior valor possível e informa o restante. Python 3.10 ou superior; somente biblioteca padrão. Licença MIT em `LICENSE`.

Memória técnica: `docs/ai-context/QUALITY_REFRESH.md`.
