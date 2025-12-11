# .github Repository

## 📋 Overview

This repository serves as a **centralized configuration hub** for GitHub workflows and quality control scripts used across all E3K Odoo projects. By maintaining these configurations in a single location, we ensure consistency, maintainability, and easy updates across multiple repositories.

## 🎯 Purpose

The `.github` repository provides:

- **Reusable GitHub Actions workflows** for continuous integration
- **Quality control scripts** that enforce E3K coding standards
- **Standardized pull request templates** for better collaboration
- **Centralized configuration** accessible to all project repositories

## 📁 Repository Structure

```
.github/
├── README.md
├── pull_request_template.md
├── scripts/
│   ├── check-field-prefix.py
│   ├── check_author.py
│   ├── check_manifest_version.py
│   ├── run_pylint_if_compatible.py
│   └── utils.py
└── workflows/
    └── quality-control.yml
```

## 🔄 GitHub Workflows

### Quality Control Workflow

**File:** `.github/workflows/quality-control.yml`

This reusable workflow performs automated code quality checks on Python code. It can be called from any repository using:

```yaml
jobs:
  quality-checks:
    uses: E3KCO/.github/.github/workflows/quality-control.yml@main
    with:
      python-version: '3.11'
```

#### Workflow Jobs

The quality control workflow consists of **5 independent jobs** that run in parallel:

---

##### 1. 🔍 **Flake8** - Code Style Linter

**What it does:**
- Checks Python code against PEP 8 style guidelines
- Detects common programming errors and code smells
- Enforces consistent code formatting

**Configuration:**
- Maximum line length: 88 characters
- Excludes `__init__.py` files from checks

**Command:**
```bash
flake8 --max-line-length=88 --exclude=__init__.py .
```

---

##### 2. 🐍 **Pylint** - Advanced Code Analysis

**What it does:**
- Performs comprehensive static code analysis
- Uses `pylint-odoo` plugin for Odoo-specific checks
- Checks code quality score and error severity

**Key features:**
- Only runs on Python ≤ 3.11
- Minimum required score: 7.5/10
- Uses centralized `.pylintrc.ini` configuration
- Excludes virtual environments and `.github-central/` directories

**Command:**
```bash
python run_pylint_if_compatible.py --rcfile=.github-central/.pylintrc.ini $(find . -name "*.py" ...)
```

---

##### 3. ✍️ **Check Author** - Manifest Validation

**What it does:**
- Validates that all `__manifest__.py` files have the correct author
- Ensures consistency across E3K modules

**Script:** `scripts/check_author.py`

**Requirements:**
- All E3K modules must have `"author": "e3k"` in their manifest
- Fails if author is missing or incorrect

**Example validation:**
```python
# ✅ Valid
{
    "name": "Custom Module",
    "author": "e3k",
    ...
}

# ❌ Invalid
{
    "name": "Custom Module",
    "author": "John Doe",  # Wrong author
    ...
}
```

---

##### 4. 🏷️ **Check Field Prefix** - Odoo Field Naming

**What it does:**
- Ensures all custom fields in inherited Odoo models use the `e3k_` prefix
- Prevents naming conflicts with standard Odoo fields
- Only checks E3K modules (ignores third-party code)

**Script:** `scripts/check-field-prefix.py`

**Rules:**
- Custom fields in inherited models **must** start with `e3k_`
- Use `# no-check` comment to bypass validation on specific lines
- Internal fields (starting with `_`) are automatically ignored

**Example:**
```python
class ResPartner(models.Model):
    _inherit = 'res.partner'

    # ✅ Valid
    e3k_custom_field = fields.Char("Custom Field")

    # ❌ Invalid - missing e3k_ prefix
    custom_field = fields.Char("Custom Field")

    # ✅ Valid - bypassed with comment
    special_field = fields.Char("Special")  # no-check
```

---

##### 5. 📌 **Check Version Format** - Semantic Versioning

**What it does:**
- Validates that module versions follow semantic versioning (x.y.z)
- Ensures consistency in version numbering across all modules

**Script:** `scripts/check_manifest_version.py`

**Requirements:**
- Version must match the pattern: `\d+\.\d+\.\d+`
- Examples: `1.0.0`, `2.3.5`, `10.15.3` ✅
- Invalid: `1.0`, `v1.0.0`, `1.0.0-beta` ❌

**Example validation:**
```python
# ✅ Valid versions
"version": "1.0.0"
"version": "2.15.3"

# ❌ Invalid versions
"version": "1.0"      # Missing patch number
"version": "v1.0.0"   # Has 'v' prefix
"version": "1.0.0-rc" # Has suffix
```

---

## 🛠️ Utility Scripts

### `utils.py`

Provides shared utility functions used across all validation scripts:

- **`is_e3k_module(file_path)`**: Determines if a file belongs to an E3K module
- **`find_manifest_files()`**: Locates all `__manifest__.py` files in the project
- Other helper functions for file parsing and validation

## 📝 Pull Request Template

The `pull_request_template.md` provides a standardized structure for pull requests, ensuring that all necessary information is included:

- Description of changes
- Type of change (bugfix, feature, refactor, etc.)
- Testing checklist
- Related issues/tickets

## 🚀 Usage in Projects

To use these workflows and scripts in your Odoo project:

1. **Add workflow to your repository:**
   ```yaml
   # .github/workflows/ci.yml
   name: CI

   on: [push, pull_request]

   jobs:
     quality-control:
       uses: E3KCO/.github/.github/workflows/quality-control.yml@main
       with:
         python-version: '3.11'
   ```

2. **Scripts are automatically fetched** during workflow execution
3. **No local installation required** - everything runs in GitHub Actions

## 🔧 Development Guidelines

When modifying this repository:

1. **Test changes locally** before committing
2. **Update this README** if adding new scripts or workflows
3. **Maintain backward compatibility** - many repositories depend on this
4. **Use semantic versioning** for major changes
5. **Document new validation rules** clearly

## ⚙️ Configuration Files

- **`.pylintrc.ini`**: Pylint configuration with Odoo-specific rules
- **Python version**: 3.11 (specified in workflow inputs)
- **Line length standard**: 88 characters (Black/Flake8 compatibility)

## 🤝 Contributing

To contribute improvements to shared workflows:

1. Create a feature branch
2. Test changes with at least one dependent repository
3. Submit a pull request with clear documentation
4. Ensure all quality checks pass

## 📚 Additional Resources

- [GitHub Actions - Reusing Workflows](https://docs.github.com/en/actions/using-workflows/reusing-workflows)
- [Odoo Development Guidelines](https://www.odoo.com/documentation/)
- [PEP 8 - Python Style Guide](https://peps.python.org/pep-0008/)
- [Semantic Versioning](https://semver.org/)

---

**Maintained by:** E3K Development Team
**Last updated:** December 2025
