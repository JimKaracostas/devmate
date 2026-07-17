import argparse
import sys
import os
from rich.console import Console
from rich.table import Table
import questionary
from .templates import generate_template, TEMPLATES_INFO
from .git_manager import init_git

console = Console()

def main():
    parser = argparse.ArgumentParser(description="Devmate: Developer Workflow Automation CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # 'new' command
    new_parser = subparsers.add_parser("new", help="Create a new project from a template")
    new_parser.add_argument("project_name", nargs="?", help="Name of the project directory")
    new_parser.add_argument("--template", choices=list(TEMPLATES_INFO.keys()), help="Template to use")
    new_parser.add_argument("--git", action="store_true", help="Initialize a git repository after creation")
    
    # 'git-init' command
    git_parser = subparsers.add_parser("git-init", help="Initialize git repository and make initial commit")
    git_parser.add_argument("project_path", nargs="?", default=".", help="Path to the project (default: current directory)")
    git_parser.add_argument("--remote", help="URL of the remote repository to add")
    
    # 'list' command
    list_parser = subparsers.add_parser("list", help="List all available templates")
    
    args = parser.parse_args()
    
    if args.command == "new" or args.command is None:
        # If no args were passed at all, or if "new" was passed without required args
        project_name = args.project_name if hasattr(args, 'project_name') else None
        template = args.template if hasattr(args, 'template') else None
        git_init = args.git if hasattr(args, 'git') else False
        
        if not project_name:
            project_name = questionary.text("What is your project named?").ask()
            if not project_name:
                console.print("[red]Project name is required. Exiting.[/red]")
                sys.exit(1)
                
        if not template:
            template = questionary.select(
                "Which template would you like to use?",
                choices=list(TEMPLATES_INFO.keys())
            ).ask()
            if not template:
                console.print("[red]Template is required. Exiting.[/red]")
                sys.exit(1)
                
        if not hasattr(args, 'project_name') or not args.project_name:
            # If we're fully interactive, ask about git too
            git_init = questionary.confirm("Would you like to initialize a Git repository?", default=False).ask()

        console.print(f"[bold green]Creating new {template} project:[/bold green] [cyan]{project_name}[/cyan]")
        generate_template(project_name, template)
        
        if git_init:
            init_git(project_name)
            
    elif args.command == "git-init":
        init_git(args.project_path, args.remote)
        
    elif args.command == "list":
        table = Table(title="Available Devmate Templates")
        table.add_column("Template", style="cyan", no_wrap=True)
        table.add_column("Description", style="white")

        for name, desc in TEMPLATES_INFO.items():
            table.add_row(name, desc)
            
        console.print(table)
        
    else:
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()
