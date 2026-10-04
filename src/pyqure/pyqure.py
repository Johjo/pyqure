from dataclasses import dataclass
from typing import TypeVar, Generic, Any, Protocol, cast, runtime_checkable

T = TypeVar("T")


@dataclass(frozen=True, eq=True)
class Key(Generic[T]):
    name: str
    type: type[Any]


PyqureMemory = dict[Key[Any], Any]


@runtime_checkable
class Provide(Protocol):
    def __call__(self, key: Key[T], value: T) -> None: ...


@runtime_checkable
class Inject(Protocol):
    def __call__(self, key: Key[T]) -> T: ...


def pyqure(memory: PyqureMemory) -> tuple[Provide, Inject]:
    def provide(key: Key[T], value: T) -> None:
        if not isinstance(value, key.type):
            raise TypeError(f"Expected {key.type}, got {type(value)}")

        memory[key] = value

    def inject(key: Key[T]) -> T:
        return cast(T, memory[key])

    return provide, inject
