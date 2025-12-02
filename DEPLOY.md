# Deployment Guide

This repository uses **manual deployment** to GitHub Pages (like your friend's setup).

## Quick Start

### Windows
```bash
deploy.bat
```

### Linux/Mac
```bash
chmod +x deploy.sh
./deploy.sh
```

### Or use Python directly
```bash
python deploy.py
```

## What the script does

1. **Checks/installs ghp-import** - Tool for pushing to gh-pages branch
2. **Builds the book** - Runs `jupyter-book build book`
3. **Deploys to GitHub Pages** - Pushes built files to `gh-pages` branch

## Prerequisites

- Python 3.x installed
- Jupyter Book installed: `pip install -r book/requirements.txt`
- Git configured with access to push to the repository

## Manual Steps (if script doesn't work)

If you prefer to do it manually:

```bash
# 1. Build the book
jupyter-book build book

# 2. Install ghp-import (if not installed)
pip install ghp-import

# 3. Deploy to gh-pages
ghp-import -n -p -f -m "Update book" book/_build/html
```

## GitHub Pages Setup

Make sure GitHub Pages is configured:

1. Go to your repository on GitHub
2. Settings → Pages
3. Source: **Deploy from a branch**
4. Branch: **gh-pages** / **/(root)**
5. Save

Your book will be live at: `https://jehiku.github.io/culanggo-jb/`

## Troubleshooting

- **"ghp-import not found"**: The script will auto-install it
- **"Build failed"**: Check that all dependencies are installed
- **"Permission denied"**: Make sure you have push access to the repository
- **Pages not updating**: Wait a few minutes, GitHub Pages can take 1-5 minutes to update

