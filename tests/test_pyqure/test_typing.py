import subprocess
import sys
from pathlib import Path

from pyqure import Key, Provide, Inject, pyqure

TYPING_PROOF = '''\
from pyqure import Key, pyqure

provide, inject = pyqure({})
reveal_type(inject(Key("host", str)))
provide(Key("host", str), "localhost")
provide(Key("port", int), 5432)
provide(Key("host", str), 5432)
inject(Key("port", int)) + "text"
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

    assert (
        f'{proof}:7: error: Cannot infer value of type parameter "T" of "__call__" of "Provide"  [misc]'
        in result.stdout
    )
    assert (
        f'{proof}:8: error: Unsupported operand types for + ("int" and "str")'
        in result.stdout
    )
    assert 'Revealed type is "str"' in result.stdout
    assert result.stdout.count("error:") == 2
