# ==== Difficulty config ====
# ===========================

import json
from pathlib import Path

path = Path("data/difficulties.json")

with path.open() as file:
    difficulties = json.load(file)
