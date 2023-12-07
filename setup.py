from setuptools import setup, find_packages

setup(
    author="Carlos David Sandoval Vargas",
    license="MIT",
    name="password-generator",
    version="0.1",
    description="A simple password generator and tester.",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "pass = password_generator.main:main",
        ]
    },
)