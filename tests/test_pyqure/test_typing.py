import subprocess
import sys
from pathlib import Path

from pyqure import Key, Provide, Inject, pyqure

TYPING_PROOF = '''\
from abc import ABC, abstractmethod

from pyqure import Key, pyqure


class Abstract(ABC):
    @abstractmethod
    def m(self) -> None: ...


class Concrete(Abstract):
    def m(self) -> None: ...


provide, inject = pyqure({})
reveal_type(inject(Key[str]("host", str)))
provide(Key[str]("host", str), "localhost")
provide(Key[int]("port", int), 5432)
provide(Key[str]("host", str), 5432)
inject(Key[int]("port", int)) + "text"
reveal_type(inject(Key[Abstract]("db", Abstract)))
provide(Key[Abstract]("db", Abstract), Concrete())
provide(Key("bare", str), "no subscript, no static typing, no error")
'''


def test_pyqure_returns_protocol_conformants() -> None:
    (provide, inject) = pyqure({})

    assert isinstance(provide, Provide)
    assert isinstance(inject, Inject)


def test_call_site_typing_is_preserved(tmp_path: Path) -> None:
    proof = tmp_path / "typing_proof.py"
    proof.write_text(TYPING_PROOF)
    project_root = Path(__file__).parents[2]

    result = subprocess.run(
        [sys.executable, "-m", "mypy", "--no-incremental", str(proof)],
        cwd=project_root,
        capture_output=True,
        text=True,
    )

    assert result.returncode != 0, "mypy should report the two type errors"

    assert 'Revealed type is "str"' in result.stdout
    assert (
        f'{proof}:19: error: Cannot infer value of type parameter "T" of "__call__" of "Provide"  [misc]'
        in result.stdout
    )
    assert (
        f'{proof}:20: error: Unsupported operand types for + ("int" and "str")'
        in result.stdout
    )
    assert 'Revealed type is "typing_proof.Abstract"' in result.stdout
    assert result.stdout.count("error:") == 2, (
        "the abstract-key pattern (lines 20-21) and bare keys (line 22) "
        "must not produce static errors"
    )
