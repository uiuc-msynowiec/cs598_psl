# CS 598 PSL

## Environment Setup with uv

### Install uv
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Initialize a new project
```bash
uv init my-project    # creates pyproject.toml, hello.py, .python-version
cd my-project
```

Or in an existing directory:
```bash
uv init               # adds pyproject.toml to current folder
```

### Create a virtual environment
```bash
uv venv               # creates .venv using the project's Python version
source .venv/bin/activate
```

### Add / install packages
```bash
uv add scikit-learn        # installs + adds to pyproject.toml dependencies
uv add numpy matplotlib    # multiple at once

uv pip install ucimlrepo   # install without tracking in pyproject.toml
```

### Remove a package
```bash
uv remove scikit-learn
```

### Sync environment to pyproject.toml
```bash
uv sync                    # installs all declared dependencies
```

### Run a script without activating
```bash
uv run python script.py    # uses the project's .venv automatically
```

### Key difference from pip
- `uv add` — installs + records in `pyproject.toml` (like `npm install`)
- `uv pip install` — installs only, no tracking (like plain `pip install`)
