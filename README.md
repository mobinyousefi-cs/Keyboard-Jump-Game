# Keyboard Jump Game (Python / Pygame)

A fast‑paced typing game built with **Pygame**. Type the letters shown on screen before they hit the ground. Miss or press a wrong key and it’s game over. Designed for clean architecture, testability, and a modern Python project layout.

---

## Features
- Smooth 60 FPS gameplay with incremental difficulty
- Clean separation of concerns: config, assets, core loop, UI layer, and generators
- Sound effects (optional) and polished HUD
- `src/` layout with `pyproject.toml` (PEP 621)
- CI: GitHub Actions running Ruff, Black, and Pytest

## Demo
Run locally and play with your keyboard. Score increases for each correct key.

## Installation
```bash
# create & activate a virtual environment (recommended)
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# install via pyproject
pip install -e .
```

Alternatively, without editable install:
```bash
pip install pygame>=2.5
```

## Usage
```bash
python -m keyboard_jump
```

### Controls
- Type the **displayed letter** to score.
- Any **wrong key** ends the game.
- Press **ESC** to quit at any time.

## Project Structure
```
keyboard-jump/
├─ .editorconfig
├─ .gitignore
├─ LICENSE
├─ pyproject.toml
├─ README.md
├─ .github/
│  └─ workflows/
│     └─ ci.yml
├─ src/
│  └─ keyboard_jump/
│     ├─ __init__.py
│     ├─ main.py
│     ├─ config.py
│     ├─ assets.py
│     ├─ ui.py
│     ├─ wordstream.py
│     └─ core.py
└─ tests/
   └─ test_wordstream.py
```

## Development
```bash
# lint
ruff check .

# format
black .

# tests
pytest -q
```

## Notes
- Requires Python 3.9+
- If Pygame cannot initialize audio on your system, the game will continue without sound.

## Author
**Mobin Yousefi** — [github.com/mobinyousefi-cs](https://github.com/mobinyousefi-cs)

## License
MIT — see [LICENSE](LICENSE).

