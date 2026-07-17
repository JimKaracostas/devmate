<h1 align="center">
  Devmate 🛠️
</h1>

<p align="center">
  <strong>A developer workflow automation CLI tool designed to simplify setting up new projects and managing Git repositories.</strong>
</p>

<p align="center">
  <img alt="Python Version" src="https://img.shields.io/badge/python-3.8%2B-blue">
  <img alt="License" src="https://img.shields.io/badge/license-MIT-green">
  <img alt="PRs Welcome" src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg">
</p>

<hr>

Instead of manually creating boilerplate files and running the same git initialization commands every time you start a project, **Devmate** automates the process for you. Say goodbye to repetitive boilerplate!

## 📑 Table of Contents

- [Features](#-features)
- [Installation](#-installation)
- [Usage Guide](#-usage-guide)
  - [1. Scaffold a New Project](#1-scaffold-a-new-project)
  - [2. Initialize Git Repository](#2-initialize-git-repository)
  - [3. List Available Templates](#3-list-available-templates)
- [Extending Devmate](#-extending-devmate)
- [Contributing](#-contributing)
- [License](#-license)

---

## ✨ Features

- **Blazing Fast Setup**: Generate fully-functional boilerplates in milliseconds.
- **Multi-language Support**: Built-in templates for Python, Node.js, React, and Vanilla Web.
- **Git Automation**: Initialize repositories, create `.gitignore` files, and add remotes in one command.
- **Highly Extensible**: Easily add your own custom project templates.

---

## 🚀 Installation

### Recommended (Using pipx)

Since Devmate is a global CLI tool, the safest and cleanest way to install it on modern Linux distributions is via `pipx` (which manages isolated virtual environments for you):

```bash
pipx install .
```

### Alternative (Editable Mode for Developers)

If you are modifying the source code and want changes to be reflected immediately, you can install it using pip in editable mode:

```bash
pip install -e . --break-system-packages
```

---

## 📖 Usage Guide

Devmate currently supports the following commands:

### 1. Scaffold a New Project

**`devmate new`**

Creates a new project directory and populates it with boilerplate code for a specific language or framework.

**Syntax:**

```bash
devmate new <project_name> --template <template_type> [--git]
```

**Templates Available:**

- `python`: Creates a Python project with a virtual environment (`venv`), `main.py`, `requirements.txt`, and a `.gitignore` file.
- `web`: Creates a basic vanilla web project with `index.html`, `style.css`, and `script.js`.
- `node`: Creates a basic Node.js + Express project structure.
- `react`: Creates a basic React (Vite-like) project structure.

**Example:**
Create a new Python project named `my-api` and immediately initialize a git repository for it:

```bash
devmate new my-api --template python --git
```

### 2. Initialize Git Repository

**`devmate git-init`**

Initializes a git repository, creates a default `.gitignore` (if one doesn't exist), stages all files, makes an initial commit, and optionally links it to a remote repository.

**Syntax:**

```bash
devmate git-init [project_path] [--remote <url>]
```

**Example:**
Initialize a repository in your current directory and link it to GitHub:

```bash
devmate git-init . --remote https://github.com/your-name/your-repo.git
```

### 3. List Available Templates

**`devmate list`**

Lists all currently available templates and their descriptions.

**Syntax:**

```bash
devmate list
```

---

## 🛠️ Extending Devmate

Want to add your own templates? You can easily extend Devmate to fit your personal workflow!

1. Open `devmate/templates.py`.
2. Create a new function for your template (e.g., `create_go_template`).
3. Update the `generate_template` function to route to your new template.
4. Add the new template description to the `TEMPLATES_INFO` dictionary.
5. Update `devmate/cli.py` if necessary (the template will be automatically picked up by the `list` command if added to `TEMPLATES_INFO`).

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

Feel free to check out the [issues page](https://github.com/JimKaracostas/devmate/issues) if you want to contribute.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.
