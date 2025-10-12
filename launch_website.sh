#!/bin/bash

echo "============================================================"
echo "🚀 BITS PILANI ACADEMIC WEBSITE LAUNCHER"
echo "============================================================"
echo

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    if ! command -v python &> /dev/null; then
        echo "❌ ERROR: Python is not installed"
        echo "Please install Python 3.x from https://python.org"
        echo
        exit 1
    else
        PYTHON_CMD="python"
    fi
else
    PYTHON_CMD="python3"
fi

echo "✅ Python found: $($PYTHON_CMD --version)"
echo

# Make the script executable
chmod +x "$0"

# Launch the Python server
$PYTHON_CMD launch_website.py
