## 📋 Description

<!-- Clearly describe the changes made and their purpose -->

## 🎯 Type of change

<!-- Check the appropriate boxes with [x] -->

- [ ] 🐛 Bug fix (fixes an issue)
- [ ] ✨ New feature (adds functionality)
- [ ] 🔨 Refactoring (code improvement without changing behavior)
- [ ] 📝 Documentation
- [ ] 🎨 UI/UX (visual or user experience changes)
- [ ] ⚡ Performance
- [ ] 🔒 Security
- [ ] 🌐 Translation

## 🔗 Related tasks

<!-- Reference related task IDs -->

Task: [Task ID](link_to_task)

## 📦 Affected module(s)

<!-- List the affected Odoo modules -->

- `module_name`
- `other_module`

## 🧪 Tests performed

<!-- Describe how you tested these changes -->

- [ ] Manual tests performed
- [ ] Unit tests added/updated
- [ ] Tested on different browsers (if applicable)
- [ ] Tested with production data (staging environment)

## 🔄 Migration / Update

<!-- If applicable, describe necessary migration steps -->

- [ ] Requires a migration script
- [ ] Requires a database update
- [ ] Requires a manual module update
- [ ] Requires manual actions (describe below)

### Required actions

<!-- SQL commands, Python scripts, configurations, etc. -->

```python
# Migration code example if needed
```

## ⚙️ Configuration

<!-- Are there new system parameters or configurations to define? -->

- [ ] New Python dependencies (see `requirements.txt`)
- [ ] New npm/JavaScript dependencies
- [ ] Manual configurations to be done (Describe below)

## 📚 Documentation

- [ ] Code is commented, especially in complex areas
- [ ] Technical documentation has been updated
- [ ] User documentation has been updated (if applicable)
- [ ] Python docstrings are up to date

## ✅ Checklist

<!-- Verify that you have followed Odoo standards -->

### Python Code
- [ ] PEP 8 compliance
- [ ] No `print()` or `pdb` left in the code
- [ ] Appropriate use of `self.env`, `sudo()`, `with_context()`
- [ ] Correct access rights management (`ir.model.access`, `ir.rule`)
- [ ] Translated messages with `_()` from `odoo.tools.translate`

### XML/QWeb Views
- [ ] No `noupdate="1"` without valid reason
- [ ] No inappropriate use of `<xpath expr="..." position="replace">`
- [ ] External IDs properly named (`module_name.view_model_form`)
- [ ] View inheritance correctly implemented with `inherit_id`

### JavaScript/OWL
- [ ] ES6+ code (const, let, arrow functions)
- [ ] No `console.log()` left in the code
- [ ] Well-structured OWL components
- [ ] Appropriate use of hooks (`useState`, `useRef`, etc.)

### Security
- [ ] User input validation
- [ ] No raw SQL queries (use the ORM)
- [ ] Protection against XSS injections in QWeb
- [ ] Appropriate access rights verification

### Performance
- [ ] No loops on `search()` (prefer `read()` or `search_read()`)
- [ ] Use of `prefetch` when necessary
- [ ] No N+1 queries
- [ ] Database indexes added if necessary

## 💬 Additional notes

<!-- Add any relevant information for reviewers -->

## 👥 Suggested reviewers

<!-- Mention people who should review this PR -->

@username