# Options Dashboard

A Streamlit-based dashboard for visualizing options trading data and analytics. This project uses modern Python tooling including `uv` for package management, `ruff` for linting/formatting, and `pytest` for testing.

## Features

- Interactive Streamlit dashboard
- Data analysis with pandas and numpy
- Visualization with matplotlib
- Statistical analysis with scipy
- Modern Python development tooling

## Prerequisites

- Python 3.9 or higher
- [uv](https://github.com/astral-sh/uv) package manager

## Installation

1. Clone the repository:
```bash
cd options_dashboard
```

2. Install dependencies:
```bash
uv sync
```

This will create a virtual environment and install all required dependencies.

## Usage

### Running the Dashboard

```bash
uv run streamlit run src/options_dashboard/app.py
```

The dashboard will open in your default web browser at `http://localhost:8501`.

### Running Tests

```bash
uv run pytest
```

### Code Quality

Format code with ruff:
```bash
uv run ruff format .
```

Lint code:
```bash
uv run ruff check .
```

Fix linting issues automatically:
```bash
uv run ruff check --fix .
```

Type checking with mypy:
```bash
uv run mypy src/
```

## Project Structure

```
options_dashboard/
├── src/
│   └── options_dashboard/
│       ├── __init__.py
│       └── app.py           # Main Streamlit application
├── tests/
│   ├── __init__.py
│   └── test_app.py          # Test files
├── docs/                     # Documentation
├── .vscode/                  # VSCode settings
│   └── settings.json
├── pyproject.toml           # Project configuration and dependencies
├── .gitignore
└── README.md
```

## Development

### Adding New Dependencies

Runtime dependencies:
```bash
uv add package-name
```

Development dependencies:
```bash
uv add --dev package-name
```

### VSCode Setup

The project includes VSCode settings for:
- Automatic formatting on save with ruff
- Python interpreter configuration
- Test discovery with pytest

Install the recommended VSCode extension:
- [Ruff](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff)

## Next Steps

1. Add your matplotlib chart prototypes to the dashboard
2. Create data loading and processing functions
3. Build interactive components for data exploration
4. Add unit tests for your analysis functions

## License

Add your license information here.
