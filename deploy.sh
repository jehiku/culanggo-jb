#!/bin/bash
# Deploy Jupyter Book to GitHub Pages (Linux/Mac)

set -e  # Exit on error

echo "============================================================"
echo "Jupyter Book Deployment Script"
echo "============================================================"
echo ""

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    exit 1
fi

# Run the Python deployment script
python3 deploy.py

echo ""
echo "Done!"

