import os
import subprocess
import json
from pathlib import Path
from rich.console import Console

console = Console()

TEMPLATES_INFO = {
    "python": "Creates a Python project with a virtual environment (venv), main.py, and requirements.txt.",
    "web": "Creates a basic vanilla web project with index.html, style.css, and script.js.",
    "node": "Creates a basic Node.js + Express project structure.",
    "react": "Creates a basic React (Vite-like) project structure."
}

def create_python_template(project_path: str):
    path = Path(project_path)
    path.mkdir(parents=True, exist_ok=True)
    
    # Create main.py
    with open(path / "main.py", "w") as f:
        f.write('def main():\n    print("Hello, Devmate!")\n\nif __name__ == "__main__":\n    main()\n')
        
    # Create requirements.txt
    with open(path / "requirements.txt", "w") as f:
        f.write("# Add your dependencies here\n")
        
    # Create venv
    # Create venv
    console.print("[dim]Creating virtual environment...[/dim]")
    try:
        with console.status("[bold cyan]Running python3 -m venv...[/bold cyan]", spinner="dots"):
            subprocess.run(["python3", "-m", "venv", "venv"], cwd=path, check=True, capture_output=True)
    except subprocess.CalledProcessError as e:
        console.print("[yellow]Warning: Failed to create virtual environment (ensure python3-venv is installed).[/yellow]")
    except FileNotFoundError:
        console.print("[yellow]Warning: python3 not found, skipping virtual environment creation.[/yellow]")
        
    # Create .gitignore
    with open(path / ".gitignore", "w") as f:
        f.write("venv/\n__pycache__/\n*.pyc\n.env\n")
        
    console.print(f"[bold green]Python template created successfully in[/bold green] [cyan]{project_path}[/cyan]")

def create_web_template(project_path: str):
    path = Path(project_path)
    path.mkdir(parents=True, exist_ok=True)
    
    # Create index.html
    with open(path / "index.html", "w") as f:
        f.write('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Devmate Web Project</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>Hello, Devmate!</h1>
    <script src="script.js"></script>
</body>
</html>''')
        
    # Create style.css
    with open(path / "style.css", "w") as f:
        f.write('body {\n    font-family: sans-serif;\n    margin: 2rem;\n}\n')
        
    # Create script.js
    with open(path / "script.js", "w") as f:
        f.write('console.log("Hello, Devmate!");\n')
        
    console.print(f"[bold green]Web template created successfully in[/bold green] [cyan]{project_path}[/cyan]")

def create_node_template(project_path: str):
    path = Path(project_path)
    path.mkdir(parents=True, exist_ok=True)

    # Create package.json
    package_json = {
        "name": path.name,
        "version": "1.0.0",
        "description": "Node.js project created by devmate",
        "main": "index.js",
        "scripts": {
            "start": "node index.js",
            "dev": "node index.js"
        },
        "dependencies": {
            "express": "^4.18.2"
        }
    }
    with open(path / "package.json", "w") as f:
        json.dump(package_json, f, indent=2)

    # Create index.js
    with open(path / "index.js", "w") as f:
        f.write('''const express = require('express');
const app = express();
const port = process.env.PORT || 3000;

app.get('/', (req, res) => {
  res.send('Hello, Devmate!');
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
''')

    # Create .gitignore
    with open(path / ".gitignore", "w") as f:
        f.write("node_modules/\n.env\n")

    console.print(f"[bold green]Node.js template created successfully in[/bold green] [cyan]{project_path}[/cyan]")
    console.print("[dim]Run 'npm install' or 'npm install express' to install dependencies.[/dim]")

def create_react_template(project_path: str):
    path = Path(project_path)
    path.mkdir(parents=True, exist_ok=True)

    # Create package.json
    package_json = {
        "name": path.name,
        "private": True,
        "version": "0.0.0",
        "type": "module",
        "scripts": {
            "dev": "vite",
            "build": "vite build",
            "lint": "eslint . --ext js,jsx --report-unused-disable-directives --max-warnings 0",
            "preview": "vite preview"
        },
        "dependencies": {
            "react": "^18.2.0",
            "react-dom": "^18.2.0"
        },
        "devDependencies": {
            "@types/react": "^18.2.15",
            "@types/react-dom": "^18.2.7",
            "@vitejs/plugin-react": "^4.0.3",
            "eslint": "^8.45.0",
            "vite": "^4.4.5"
        }
    }
    with open(path / "package.json", "w") as f:
        json.dump(package_json, f, indent=2)

    # Create index.html
    with open(path / "index.html", "w") as f:
        f.write('''<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Devmate React Project</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.jsx"></script>
  </body>
</html>
''')

    # Create vite.config.js
    with open(path / "vite.config.js", "w") as f:
        f.write('''import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
})
''')

    # Create src directory
    src_path = path / "src"
    src_path.mkdir(exist_ok=True)

    # Create src/main.jsx
    with open(src_path / "main.jsx", "w") as f:
        f.write('''import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)
''')

    # Create src/App.jsx
    with open(src_path / "App.jsx", "w") as f:
        f.write('''function App() {
  return (
    <div>
      <h1>Hello, Devmate React!</h1>
    </div>
  )
}

export default App
''')

    # Create .gitignore
    with open(path / ".gitignore", "w") as f:
        f.write("node_modules/\ndist/\ndist-ssr/\n*.local\n.env\n")

    console.print(f"[bold green]React template created successfully in[/bold green] [cyan]{project_path}[/cyan]")
    console.print("[dim]Run 'npm install' and 'npm run dev' to start the project.[/dim]")

def generate_template(project_name: str, template_type: str):
    if template_type == "python":
        create_python_template(project_name)
    elif template_type == "web":
        create_web_template(project_name)
    elif template_type == "node":
        create_node_template(project_name)
    elif template_type == "react":
        create_react_template(project_name)
    else:
        console.print(f"[bold red]Unknown template:[/bold red] {template_type}")
