#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
echo "Starting TENPHASE VILLAIN client pitch server..."
exec python3 serve.py
