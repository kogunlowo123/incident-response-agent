#!/bin/bash
set -euo pipefail
echo "Setting up Incident Response Agent..."
pip install -e ".[dev]"
echo "Setup complete!"
