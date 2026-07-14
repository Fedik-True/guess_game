# ==== Difficulty config ====
# ===========================

import json
from pathlib import Path

path = Path("data/difficulties.json")

with path.open() as file:
    difficulties = json.load(file)


difficulty_map = {
    1: "easy",
    2: "medium",
    3: "hard",
    4: "extreme",
    5: "nightmare",
}
