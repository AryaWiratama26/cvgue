# Contributing to CVGue

Thank you for considering contributing to CVGue! This document provides guidelines and instructions for contributing to this project.

## Getting Started

### Prerequisites

- Python 3.10 or higher
- Git
- Virtual environment (recommended)

### Setting Up Development Environment

1. **Fork and clone the repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/cvgue.git
   cd cvgue
   ```

2. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt  # Development dependencies
   ```

4. **Install the package in editable mode:**
   ```bash
   pip install -e .
   ```

## Running Tests

Before submitting a pull request, make sure all tests pass:

```bash
# Run all tests
pytest testing/test.py -v

# Run tests with coverage
pytest testing/test.py --cov=cvgue --cov-report=html
```

## Code Style Guidelines

### Python Code Style

- Follow [PEP 8](https://pep8.org/) style guide
- Use meaningful variable and function names
- Add docstrings to all public functions and classes
- Keep functions small and focused on a single task

### Code Formatting

We use **Black** for code formatting:

```bash
# Format all Python files
black cvgue/ testing/

# Check formatting without making changes
black --check cvgue/ testing/
```

### Type Hints

Add type hints to function signatures:

```python
def create_cv(data: dict, template_type: str = "ats", output_path: str = "cv.pdf") -> None:
    """Generate CV PDF from data."""
    pass
```

## Template Contributions

### Adding a New Template

If you want to contribute a new CV template:

1. Create a new directory under `cvgue/templates/your_template_name/`
2. Include these files:
   - `template.html` - Jinja2 template
   - `styles.css` - Template-specific styles
3. Update `cvgue/engine.py` to support the new template
4. Add example output to `example/` directory
5. Update README.md with template documentation

### Template Design Guidelines

- **ATS-Friendly**: Ensure proper HTML structure for parsing
- **Print-Optimized**: Use `@page` rules and proper page-break handling
- **Responsive**: Test with various data lengths
- **Accessible**: Use semantic HTML and proper contrast ratios

## Bug Reports

When filing a bug report, please include:

1. **CVGue version** (`pip show cvgue`)
2. **Python version** (`python --version`)
3. **Operating System**
4. **Minimal reproducible example**
5. **Expected behavior**
6. **Actual behavior**
7. **Error messages or screenshots** (if applicable)

## Feature Requests

For feature requests:

1. Check if the feature has already been requested in [Issues](https://github.com/AryaWiratama26/cvgue/issues)
2. Clearly describe the feature and its use case
3. Provide examples of how it would work
4. Explain why this feature would be useful to other users

## Pull Request Process

1. **Create a new branch** for your feature or bugfix:
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/your-bugfix-name
   ```

2. **Make your changes** following the code style guidelines

3. **Add or update tests** for your changes

4. **Update documentation** if needed (README.md, docstrings, etc.)

5. **Commit your changes** with clear commit messages:
   ```bash
   git commit -m "feat: add new modern CV template"
   git commit -m "fix: resolve page break issue in creative template"
   git commit -m "docs: update installation instructions"
   ```

6. **Push to your fork:**
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Open a Pull Request** with:
   - Clear title and description
   - Reference to related issues (if any)
   - Screenshots (for UI/template changes)
   - Test results

### Commit Message Convention

We follow [Conventional Commits](https://www.conventionalcommits.org/):

- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation changes
- `style:` - Code style changes (formatting, no code change)
- `refactor:` - Code refactoring
- `test:` - Adding or updating tests
- `chore:` - Maintenance tasks

## Documentation

- Update README.md if you change functionality
- Add docstrings to new functions/classes
- Update examples if you add new features
- Keep CHANGELOG.md updated

## Code of Conduct

Please note that this project follows a Code of Conduct. By participating, you are expected to uphold this code. Please report unacceptable behavior to [aryawiratama2401@gmail.com](mailto:aryawiratama2401@gmail.com).

## Questions?

If you have questions about contributing, feel free to:

- Open a [Discussion](https://github.com/AryaWiratama26/cvgue/discussions)
- Open an [Issue](https://github.com/AryaWiratama26/cvgue/issues)
- Contact the maintainer at [aryawiratama2401@gmail.com](mailto:aryawiratama2401@gmail.com)

## Recognition

Contributors will be recognized in:
- README.md contributors section
- Release notes
- Project documentation

Thank you for contributing to CVGue!
