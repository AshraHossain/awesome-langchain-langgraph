import sys
from pathlib import Path

# Make scripts/ importable (lib, validate, generate_readme) without packaging.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
