"""Simulação educacional: dinheiro em centavos e cédulas sem estoque limitado."""
from dataclasses import dataclass
from decimal import Decimal, InvalidOperation

DENOMINATIONS = (100, 50, 20, 10, 5, 2)


def money(value):
    try:
        amount = Decimal(str(value).strip().replace(",", "."))
    except InvalidOperation as error:
        raise ValueError("Informe um valor monetário válido") from error
    if not amount.is_finite() or amount < 0 or amount > Decimal("1000000000"):
        raise ValueError("Valor monetário fora do limite")
    if amount != amount.quantize(Decimal("0.01")):
        raise ValueError("Use no máximo duas casas decimais")
    return amount.quantize(Decimal("0.01"))


@dataclass(frozen=True)
class Withdrawal:
    requested: Decimal
    notes: dict
    dispensed: Decimal
    remainder: Decimal
    balance: Decimal | None


def plan_withdrawal(value, balance=None, include_one=False):
    requested = money(value)
    if requested <= 0:
        raise ValueError("O saque deve ser maior que zero")
    available = money(balance) if balance is not None else None
    if available is not None and requested > available:
        raise ValueError("Saldo insuficiente")
    units = int(requested)
    denominations = DENOMINATIONS + ((1,) if include_one else ())
    # Reserve one R$100 note for a bounded exact-change search. This avoids the
    # greedy trap R$6 -> R$5 + remainder R$1 (three R$2 notes dispense all R$6).
    hundreds = max(0, units // 100 - 1)
    target = units - hundreds * 100
    cost = [0] + [float("inf")] * target
    previous = [None] * (target + 1)
    for subtotal in range(1, target + 1):
        for note in denominations:
            if note <= subtotal and cost[subtotal - note] + 1 < cost[subtotal]:
                cost[subtotal] = cost[subtotal - note] + 1
                previous[subtotal] = note
    actual = target
    while actual > 0 and previous[actual] is None:
        actual -= 1
    notes = {note: 0 for note in denominations}
    notes[100] = hundreds
    remaining = actual
    while remaining:
        note = previous[remaining]
        notes[note] += 1
        remaining -= note
    dispensed = Decimal(hundreds * 100 + actual).quantize(Decimal("0.01"))
    return Withdrawal(requested, {k: v for k, v in notes.items() if v}, dispensed,
                      requested - dispensed, available - dispensed if available is not None else None)


def main(balance=None, include_one=False):
    print("Caixa eletrônico — simulação, sem movimentação bancária")
    if balance is not None:
        print(f"Saldo simulado: R$ {money(balance):.2f}")
    while True:
        try:
            result = plan_withdrawal(input("Valor que deseja sacar: R$ "), balance, include_one)
        except ValueError as error:
            print(error)
            continue
        except (EOFError, KeyboardInterrupt):
            print("\nEncerrando...")
            return
        for note, count in result.notes.items():
            print(f"{count} notas de R$ {note},00")
        print(f"Total entregue: R$ {result.dispensed:.2f}")
        print(f"Valor não entregue: R$ {result.remainder:.2f}")
        if result.balance is not None:
            print(f"Saldo disponível: R$ {result.balance:.2f}")
        return
