import os
import subprocess
from pathlib import Path

def create_gitignore_if_missing(project_path: str):
    path = Path(project_path)
    gitignore_file = path / ".gitignore"
    if not gitignore_file.exists():
        with open(gitignore_file, "w") as f:
            f.write("# Default devmate gitignore\n.DS_Store\nnode_modules/\nvenv/\n__pycache__/\n*.pyc\n.env\n")
        print("Created default .gitignore")

def init_git(project_path: str, remote_url: str = None):
    try:
        # Initialize git
        print("Initializing git repository...")
        subprocess.run(["git", "init"], cwd=project_path, check=True, capture_output=True)
        
        # Ensure .gitignore exists
        create_gitignore_if_missing(project_path)
        
        # Add files
        subprocess.run(["git", "add", "."], cwd=project_path, check=True, capture_output=True)
        
        # Initial commit
        subprocess.run(["git", "commit", "-m", "Initial commit from devmate"], cwd=project_path, check=True, capture_output=True)
        print("Created initial commit.")
        
        # Add remote if provided
        if remote_url:
            subprocess.run(["git", "remote", "add", "origin", remote_url], cwd=project_path, check=True, capture_output=True)
            print(f"Added remote origin: {remote_url}")
            
        print("Git initialization complete!")
    except subprocess.CalledProcessError as e:
        print(f"Error during git operations: {e}")
        if e.stderr:
            print(e.stderr.decode('utf-8'))
    except FileNotFoundError:
        print("Error: 'git' command not found. Please ensure git is installed.")
