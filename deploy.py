#!/usr/bin/env python3
"""
Deploy Jupyter Book to GitHub Pages
Builds the book and pushes to gh-pages branch
"""

import subprocess
import sys
import os
from pathlib import Path

def run_command(cmd, check=True, shell=None):
    """Run a command and return the result"""
    if shell is None:
        shell = isinstance(cmd, str) or sys.platform == "win32"
    
    print(f"Running: {' '.join(cmd) if isinstance(cmd, list) else cmd}")
    try:
        if isinstance(cmd, str):
            result = subprocess.run(cmd, shell=True, check=check)
        else:
            result = subprocess.run(cmd, check=check, shell=shell)
        return result.returncode == 0
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return False
    except FileNotFoundError as e:
        print(f"Command not found: {e}")
        return False

def check_command_exists(cmd):
    """Check if a command exists"""
    try:
        subprocess.run([cmd, "--version"], capture_output=True, check=True, shell=sys.platform == "win32")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def main():
    print("=" * 60)
    print("Jupyter Book Deployment Script")
    print("=" * 60)
    
    # Check if we're in the right directory
    if not Path("book/_config.yml").exists():
        print("ERROR: book/_config.yml not found!")
        print("Please run this script from the repository root.")
        sys.exit(1)
    
    # Step 1: Check/install ghp-import
    print("\n[1/3] Checking ghp-import...")
    if not check_command_exists("ghp-import"):
        print("ghp-import not found. Installing...")
        if not run_command([sys.executable, "-m", "pip", "install", "ghp-import"]):
            print("ERROR: Failed to install ghp-import")
            sys.exit(1)
    print("✓ ghp-import is available")
    
    # Step 2: Build the book
    print("\n[2/3] Building Jupyter Book...")
    # Try jupyter-book command first, fallback to python -m jupyterbook
    build_cmd = ["jupyter-book", "build", "book"]
    if not check_command_exists("jupyter-book"):
        print("jupyter-book command not found, trying python -m jupyterbook...")
        build_cmd = [sys.executable, "-m", "jupyterbook", "build", "book"]
    
    if not run_command(build_cmd):
        print("ERROR: Build failed!")
        print("Make sure Jupyter Book is installed: pip install -r book/requirements.txt")
        sys.exit(1)
    
    # Verify build output
    build_output = Path("book/_build/html")
    if not build_output.exists():
        print("ERROR: Build output not found at book/_build/html")
        sys.exit(1)
    
    if not (build_output / "index.html").exists():
        print("ERROR: index.html not found in build output")
        sys.exit(1)
    
    print("✓ Build completed successfully")
    
    # Step 3: Deploy to gh-pages
    print("\n[3/3] Deploying to GitHub Pages...")
    print("Pushing to gh-pages branch...")
    
    # Use ghp-import to push
    # -n: don't push if there are no changes
    # -p: push to origin
    # -f: force push (needed for gh-pages)
    # -m: commit message
    deploy_cmd = [
        "ghp-import",
        "-n",  # Don't push if no changes
        "-p",  # Push to origin
        "-f",  # Force push
        "-m", "Update book",
        str(build_output)
    ]
    
    if not run_command(deploy_cmd):
        print("ERROR: Deployment failed!")
        sys.exit(1)
    
    print("\n" + "=" * 60)
    print("✓ Deployment successful!")
    print("=" * 60)
    print("\nYour book should be live at:")
    print("https://jehiku.github.io/culanggo-jb/")
    print("\nNote: It may take a few minutes for GitHub Pages to update.")
    print("=" * 60)

if __name__ == "__main__":
    main()

