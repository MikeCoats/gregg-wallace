# What is Gregg Wallace doing?

[what-is-gregg-wallace-doing.mikecoats.xyz](https://what-is-gregg-wallace-doing.mikecoats.xyz)

A web app

## For developers

### Install the required packages

```sh
python -m venv .venv --prompt gregg
source .venv/bin/activate
pip install -r dev-requirements.txt
git config core.hooksPath .githooks
```

### Debug with Visual Studio Code

Install Microsoft's
[Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python),
if you haven't already. Then launch vscode from within the project's activated
virtualenv.

```sh
$ source .venv/bin/activate
$ code .
```

Add the following snippet to your `.vscode/launch.json`'s `.configuration`
array.

```json
{
    "name": "Debug Gregg Wallace",
    "type": "python",
    "request": "launch",
    "module": "uvicorn",
    "args": [
        "main:app",
        "--reload",
        "--host", "0.0.0.0",
        "--port", "8002"
    ],
    "jinja": true,
    "justMyCode": true
}
```

### Linting the project

Linting is automatically run by the pre-commit git hook, but to manually lint the
project run the `.githooks/pre-commit` script.
