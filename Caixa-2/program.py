"""Entrada independente da versão 2 do desafio."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from cash import main
from random import randint

if __name__ == "__main__":
    main(balance=randint(20000, 1000000) / 100)
