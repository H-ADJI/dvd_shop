# DVD Shop

## Project Setup

### Requirements

- Linux based OS, Ubuntu 22.04.2 LTS x86_64 is the one used for dev.
- Python version 3.x the version used for dev environment is 3.10.6
- add your python alias to the Makefile for ease of use
- **Optional** : Docker runtime with the new CLI >= 1.13.

```sh
py=python
```

or

```sh
py=python3
```

### Dependencies

The dependencies used are :

- Typer : Library for building intuitive CLIs in python.
- Pytest : framework makes it easy to write small, readable tests.

#### Using your local python VM environment

- Make sure you're inside the project folder
- Create a virtual env to isolate dependencies from conflicting with other project using :

```sh
python -m venv venv
```

- Install dependencies using :

```sh
pip install -r requirements.txt
```

- Running the project

```sh
make local_cli
```

- Running the tests

```sh
make local_test
```

#### Using Docker runtine environment

- Running the project

```sh
make container_cli
```

- Running the tests

```sh
make container_test
```
