"""Entrada independente da versão 1 do desafio."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from cash import main

if __name__ == "__main__":
    main()
