import os
import subprocess
from pathlib import Path
from rich.console import Console

console = Console()

def create_gitignore_if_missing(project_path: str):
    path = Path(project_path)
    gitignore_file = path / ".gitignore"
    if not gitignore_file.exists():
        with open(gitignore_file, "w") as f:
            f.write("# Default devmate gitignore\n.DS_Store\nnode_modules/\nvenv/\n__pycache__/\n*.pyc\n.env\n")
        console.print("[dim]Created default .gitignore[/dim]")

def init_git(project_path: str, remote_url: str = None):
    try:
        # Initialize git
        with console.status("[bold cyan]Initializing git repository...[/bold cyan]", spinner="dots"):
            subprocess.run(["git", "init"], cwd=project_path, check=True, capture_output=True)
            
            # Ensure .gitignore exists
            create_gitignore_if_missing(project_path)
            
            # Add files
            subprocess.run(["git", "add", "."], cwd=project_path, check=True, capture_output=True)
            
            # Initial commit
            subprocess.run(["git", "commit", "-m", "Initial commit from devmate"], cwd=project_path, check=True, capture_output=True)
            
            # Add remote if provided
            if remote_url:
                subprocess.run(["git", "remote", "add", "origin", remote_url], cwd=project_path, check=True, capture_output=True)
                
        console.print("[bold green]Created initial commit.[/bold green]")
        if remote_url:
            console.print(f"[bold green]Added remote origin:[/bold green] [cyan]{remote_url}[/cyan]")
            
        console.print("[bold green]Git initialization complete![/bold green]")
    except subprocess.CalledProcessError as e:
        console.print(f"[bold red]Error during git operations:[/bold red] {e}")
        if e.stderr:
            console.print(f"[red]{e.stderr.decode('utf-8')}[/red]")
    except FileNotFoundError:
        console.print("[bold red]Error: 'git' command not found. Please ensure git is installed.[/bold red]")
