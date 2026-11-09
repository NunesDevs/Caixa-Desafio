from decimal import Decimal
import unittest
import subprocess
import sys
from pathlib import Path
from cash import DENOMINATIONS, money, plan_withdrawal


class CashTests(unittest.TestCase):
    def test_all_cli_entrypoints_and_eof(self):
        root = Path(__file__).resolve().parents[1]
        for version in (1, 2, 3):
            script = str(root / f'Caixa-{version}' / 'program.py')
            process = subprocess.run([sys.executable, '-X', 'utf8', script], input='abc\n6\n', text=True, encoding='utf-8', capture_output=True, timeout=5)
            self.assertEqual(process.returncode, 0, process.stderr)
            self.assertIn('Total entregue: R$ 6.00', process.stdout)
            self.assertIn('Valor não entregue: R$ 0.00', process.stdout)
            eof = subprocess.run([sys.executable, '-X', 'utf8', script], input='', text=True, encoding='utf-8', capture_output=True, timeout=5)
            self.assertEqual(eof.returncode, 0, eof.stderr)
            self.assertIn('Encerrando', eof.stdout)

    def test_decimal_money_and_actual_debit(self):
        result = plan_withdrawal("175,45", "200,00")
        self.assertEqual(result.dispensed, Decimal("175.00"))
        self.assertEqual(result.remainder, Decimal("0.45"))
        self.assertEqual(result.balance, Decimal("25.00"))
        self.assertEqual(sum(note * count for note, count in result.notes.items()), 175)

    def test_exact_change_instead_of_greedy_remainder(self):
        self.assertEqual(plan_withdrawal(6).notes, {2: 3})
        self.assertEqual(plan_withdrawal(8).notes, {2: 4})
        self.assertEqual(plan_withdrawal(101).remainder, Decimal(0))
        self.assertEqual(plan_withdrawal(3).dispensed, Decimal(2))
        self.assertEqual(plan_withdrawal(1).dispensed, Decimal(0))
        self.assertEqual(plan_withdrawal(3, include_one=True).dispensed, Decimal(3))

    def test_optimal_note_count_matches_reference_for_small_amounts(self):
        reference = [0] + [float("inf")] * 600
        for subtotal in range(1, len(reference)):
            reference[subtotal] = min((reference[subtotal - d] + 1 for d in DENOMINATIONS if d <= subtotal), default=float("inf"))
            if reference[subtotal] != float("inf"):
                result = plan_withdrawal(subtotal)
                self.assertEqual(result.remainder, 0)
                self.assertEqual(sum(result.notes.values()), reference[subtotal], subtotal)

    def test_invalid_amounts_and_insufficient_balance(self):
        for value in ("abc", "NaN", "Infinity", "-1", "1.001", "1.000.000", "1000000001"):
            with self.assertRaises(ValueError):
                money(value)
        for value in (0, "-2"):
            with self.assertRaises(ValueError):
                plan_withdrawal(value)
        with self.assertRaisesRegex(ValueError, "Saldo insuficiente"):
            plan_withdrawal(201, 200)
        self.assertEqual(plan_withdrawal(200, 200).balance, Decimal(0))
        self.assertEqual(money("20"), Decimal("20.00"))


if __name__ == "__main__":
    unittest.main()
