# Contributing to Roadmap Personal Blog

First off, thank you for considering contributing to Roadmap Personal Blog! It's people like you that make it a great tool for everyone.

## Code of Conduct

By participating in this project, you are expected to uphold our Code of Conduct:

- Use welcoming and inclusive language
- Be respectful of differing viewpoints and experiences
- Gracefully accept constructive criticism
- Focus on what is best for the community
- Show empathy towards other community members

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the existing issues as you might find out that you don't need to create one. When you are creating a bug report, please include as many details as possible:

* **Use a clear and descriptive title** for the issue
* **Describe the exact steps to reproduce the problem**
* **Provide specific examples** to demonstrate the steps
* **Describe the behavior you observed after following the steps**
* **Explain which behavior you expected to see instead and why**
* **Include screenshots or animated GIFs** if possible
* **Include your environment details** (OS, Python version, etc.)

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, please include:

* **Use a clear and descriptive title** for the issue
* **Provide a step-by-step description of the suggested enhancement**
* **Provide specific examples to demonstrate the steps**
* **Describe the current behavior** and **explain which behavior you expected to see instead**
* **Explain why this enhancement would be useful**
* **List some other applications where this enhancement exists**, if applicable

### Pull Requests

1. Fork the repository and create your branch from `main`
2. If you've added code that should be tested, add tests
3. If you've changed APIs, update the documentation
4. Ensure the test suite passes
5. Make sure your code follows the existing style
6. Issue that pull request!

## Development Process

1. Clone the repository:
   ```bash
   git clone https://github.com/P-Nelly/roadmap-personal-blog.git
   cd roadmap-personal-blog
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Create a branch for your feature:
   ```bash
   git checkout -b feature/your-feature-name
   ```

4. Make your changes and commit them:
   ```bash
   git add .
   git commit -m "Add your commit message"
   ```

5. Push to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

## Style Guide

### Python Style Guide

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- Use meaningful variable names
- Add docstrings to functions and classes
- Keep functions focused and small
- Use type hints where appropriate

### Git Commit Messages

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters or less
- Reference issues and pull requests liberally after the first line

### Testing

- Write unit tests for new features
- Ensure all tests pass before submitting a pull request
- Aim for high test coverage
- Run tests using:
  ```bash
  python -m pytest
  ```

## Project Structure

When adding new features, please maintain the existing project structure:

```
roadmap-personal-blog/
├── app/                    # Application package
│   ├── articles/          # Article storage
│   ├── static/            # Static files (CSS, JS)
│   ├── templates/         # HTML templates
│   ├── __init__.py       # App initialization
│   ├── auth.py           # Authentication logic
│   └── routes.py         # Route handlers
├── tests/                 # Test suite
└── requirements.txt       # Project dependencies
```

## Documentation

- Update the README.md if you change functionality
- Comment your code where necessary
- Update docstrings for any modified functions
- Add new sections to documentation for new features

## Questions?

Feel free to open an issue with the tag "question" if you have any questions about contributing.

## License

By contributing, you agree that your contributions will be licensed under the MIT License. 