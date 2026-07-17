import argparse
import sys
import os
from .templates import generate_template, TEMPLATES_INFO
from .git_manager import init_git

def main():
    parser = argparse.ArgumentParser(description="Devmate: Developer Workflow Automation CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # 'new' command
    new_parser = subparsers.add_parser("new", help="Create a new project from a template")
    new_parser.add_argument("project_name", help="Name of the project directory")
    new_parser.add_argument("--template", choices=list(TEMPLATES_INFO.keys()), required=True, help="Template to use")
    new_parser.add_argument("--git", action="store_true", help="Initialize a git repository after creation")
    
    # 'git-init' command
    git_parser = subparsers.add_parser("git-init", help="Initialize git repository and make initial commit")
    git_parser.add_argument("project_path", nargs="?", default=".", help="Path to the project (default: current directory)")
    git_parser.add_argument("--remote", help="URL of the remote repository to add")
    
    # 'list' command
    list_parser = subparsers.add_parser("list", help="List all available templates")
    
    args = parser.parse_args()
    
    if args.command == "new":
        print(f"Creating new {args.template} project: {args.project_name}")
        generate_template(args.project_name, args.template)
        
        if args.git:
            # Need to pass absolute path or relative path carefully
            # project_name is relative to current dir
            init_git(args.project_name)
            
    elif args.command == "git-init":
        init_git(args.project_path, args.remote)
        
    elif args.command == "list":
        print("Available Devmate Templates:")
        for name, desc in TEMPLATES_INFO.items():
            print(f"  {name.ljust(10)} - {desc}")
        
    else:
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()
