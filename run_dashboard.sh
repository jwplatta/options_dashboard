#!/bin/bash
# Script to run the Streamlit dashboard

export PATH="$HOME/.local/bin:$PATH"
uv run streamlit run src/options_dashboard/app.py
