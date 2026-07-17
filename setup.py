from setuptools import setup, find_packages

setup(
    name="devmate",
    version="0.2.0-beta",
    packages=find_packages(),
    install_requires=[
        "rich",
        "questionary"
    ],
    entry_points={
        "console_scripts": [
            "devmate=devmate.cli:main",
        ],
    },
    author="dev",
    description="A developer workflow automation CLI",
    python_requires=">=3.6",
)
