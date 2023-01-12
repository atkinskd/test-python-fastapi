# appsec-ken-test-api

A test FastAPI Project

# Project Setup

Install all dependencies from Pipfile.lock

`$ pipenv sync --dev`

Install the pre-commit hooks

`$ pipenv run pre-commit install`

# Local Development
```
appsec-ken-test-api$ pipenv shell
appsec-ken-test-api$ pyenv run app
```

# Other commands

**Update package versions and lock them**

`$ pipenv install --dev`

**Install a new package**

`$ pipenv install <package>`

**Install a new package for development**

`$ pipenv install <package> --dev`

**Load virtual environment**

`$ pipenv shell`

**Run tests**

`$ pipenv run test`

**Run tests with coverage**

`pipenv run test:cov`

**Run pylint**

`$ pipenv run lint:all`

**Sort imports**

`$ pipenv run isort:all`

**Format code with Black**

`$ pipenv run format:all`


# Other Pipenv commands

Locate the virtualenv

```bash
$ pipenv --venv
/home/user/.local/share/virtualenvs/test-2_TgoNaQ
```

Locate the Python interpreter

```bash
$ pipenv --py
/home/gets/.local/share/virtualenvs/test-UfpKvvps/bin/python
```

Remove the virtualenv

```bash
$ pipenv --rm
Removing virtualenv (/home/gets/.local/share/virtualenvs/test-UfpKvvps)...
```