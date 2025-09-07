# Contributing to the Project

First off, thank you for considering contributing to this project! Any contributions you make are **greatly appreciated**.

## Code of Conduct

This project and everyone participating in it is governed by the [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

## How Can I Contribute?

### Reporting Bugs

- **Ensure the bug was not already reported** by searching on GitHub under [Issues](https://github.com/burusan123/dev_template_python/issues).
- If you're unable to find an open issue addressing the problem, [open a new one](https://github.com/burusan123/dev_template_python/issues/new). Be sure to include a **title and clear description**, as much relevant information as possible, and a **code sample** or an **executable test case** demonstrating the expected behavior that is not occurring.

### Suggesting Enhancements

- Open a new issue with your suggestion. Please provide a clear description of the enhancement and its potential benefits.

### Pull Requests

1.  Fork the repository and create your branch from `main`.
2.  Set up your local development environment by following the instructions in the [README.md](README.md).
3.  Make your changes. Please add tests for any new functionality.
4.  Ensure all tests pass and the code is formatted and linted correctly.
    ```bash
    # Run all checks
    pytest
    ruff check . --fix
    ruff format .
    mypy .
    ```
5.  Commit your changes using a descriptive commit message.
6.  Push your branch and open a pull request.

## Development Workflow

- We use `pre-commit` to ensure code quality before commits. Please make sure it's installed by running `pre-commit install`.
- All pull requests must pass the CI checks defined in `.github/workflows/ci.yml`.

## Styleguides

- We use `Ruff` for formatting and linting.
- We use `Mypy` for static type checking.
- All code should include type hints.

Thank you for your contribution!
