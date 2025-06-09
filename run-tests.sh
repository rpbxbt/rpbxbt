#!/bin/bash
set -e
pip install -r requirements.txt
export PYTHONPATH=.
pytest -v
mkdir -p build
cp -r data build/
