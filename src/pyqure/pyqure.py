from dataclasses import dataclass
from typing import TypeVar, Generic, Type, Any, Callable, cast

T = TypeVar("T")


@dataclass(frozen=True, eq=True)
class Key(Generic[T]):
    name: str
    type: type[Any]

PyqureMemory = dict[Key[Any], Any]

def pyqure(memory: PyqureMemory) -> tuple[Callable[[Key[Any], Any], None], Callable[[Key[Any]], Any]]:
    def provide(key: Key[T], value: T) -> None:
        if not isinstance(value, key.type):
            raise TypeError(f"Expected {key.type}, got {type(value)}")

        memory[key] = value

    def inject(key: Key[T]) -> T:
        return cast(T, memory[key])

    return provide, inject
