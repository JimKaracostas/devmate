from setuptools import setup, find_packages

setup(
    name="devmate",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "devmate=devmate.cli:main",
        ],
    },
    author="dev",
    description="A developer workflow automation CLI",
    python_requires=">=3.6",
)
