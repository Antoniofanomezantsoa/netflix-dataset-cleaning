#!/usr/bin/env bash
set -euo pipefail
uv run kaggle datasets download -d shivamb/netflix-shows -p data/raw --unzip
