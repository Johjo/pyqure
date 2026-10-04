# pyqure

Minimal dependency injection for Python — values are identified by **typed keys**, not by name alone.

## Why pyqure?

Most DI containers wire dependencies by name or by type hints. pyqure keeps it simple: a `Key` is a pair `(name, type)`, and the container guarantees that what you provide is what you inject.

- **Typed keys** — `Key("db_host", str)` and `Key("db_host", int)` are two different dependencies
- **Runtime type safety** — providing a value of the wrong type raises `TypeError`
- **Static type safety (opt-in)** — subscript a key (`Key[int]("port", int)`) and mypy checks every `provide`/`inject` call site
- **Zero dependencies** — pure standard library
- **Fully typed** — `py.typed` marker, checked with mypy in strict mode

## Quick start

```python
from pyqure import Key, pyqure

provide, inject = pyqure({})

provide(Key("db_host", str), "localhost")
provide(Key("db_port", int), 5432)

host = inject(Key("db_host", str))  # "localhost"
port = inject(Key("db_port", int))  # 5432
```

### Error handling

```python
provide(Key("db_host", str), 5432)       # TypeError: expected str
inject(Key("unknown", str))              # KeyError: no value provided
```

### Static typing

`provide` and `inject` are generic protocols. Subscript a key and the value type is checked statically at every call site:

```python
port = inject(Key[int]("db_port", int))      # mypy knows: int
provide(Key[int]("db_port", int), "5432")    # mypy error
```

Abstract classes work as keys without tripping mypy's `type-abstract` check — a common DI pattern:

```python
provide(Key[AbstractConnection]("db", AbstractConnection), PostgresConnection())
```

Bare keys (`Key("db", AbstractConnection)`) are also fine: the type is then enforced at runtime only.

### Sharing a container

`pyqure` returns closures over the memory you pass in. Call it again with the same memory to get another handle on the same container:

```python
memory = {}
provide, _ = pyqure(memory)
provide(Key("greeting", str), "hello")

_, inject = pyqure(memory)
inject(Key("greeting", str))  # "hello"
```

## Installation

The package is not yet published on PyPI. Install from the repository:

```bash
pip install git+https://github.com/Johjo/pyqure.git
```

Or, for development:

```bash
git clone https://github.com/Johjo/pyqure.git
cd pyqure
uv sync
```

## Development

```bash
uv run pytest   # run tests
uv run mypy .   # type-check (strict)
```

## License

[MIT](LICENSE)

## Acknowledgments

pyqure is inspired by [piqure](https://github.com/Gnuk/piqure) by Anthony Rey, a dependency injection system in JavaScript (MIT licensed).
