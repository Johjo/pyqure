from abc import ABC, abstractmethod
from typing import Any

import pytest

from pyqure import Key, pyqure, PyqureMemory


class SomeClass:
    pass


class AnotherClass:
    pass


class SomeSubClass(SomeClass):
    pass

class AnAbstractClass(ABC):
    @abstractmethod
    def any_method(self) -> None:
        pass

class AConcreteClass(AnAbstractClass):
    def any_method(self) -> None:
        pass


@pytest.mark.parametrize("key,expected", [
    [Key("string key", str), "Injected"],
    [Key("string key", int), 42],
    [Key("string key", SomeClass), SomeClass()],
    [Key("string key", SomeClass), SomeSubClass()],
    [Key("string key", AnAbstractClass), AConcreteClass()],
])
def test_provide_dependency_for_key(key: Key[Any], expected: Any) -> None:
    memory : PyqureMemory = {}
    (provide, inject) = pyqure(memory)
    provide(key, expected)

    injected = inject(key)

    assert injected == expected


def test_tell_error_when_key_not_found() -> None:
    (_, inject) = pyqure({})

    with pytest.raises(KeyError):
        inject(Key("unknown key", str))

@pytest.mark.parametrize("title,key,injected", [
    ["standard type", Key("string key", int), "Injected"],
    ["subtype type", Key("string key", SomeClass), AnotherClass()],
    ["abstract type", Key("string key", AnAbstractClass), AnotherClass()],
])
def test_tell_error_when_type_not_match(title: str, key: Key[Any], injected: Any) -> None:
    (provide, _) = pyqure({})
    with pytest.raises(TypeError):
        provide(key, injected)


def test_provide_many_keys() -> None:
    (provide, inject) = pyqure({})
    provide(Key("string key", str), "Injected")
    provide(Key("int key", int), 42)
    provide(Key("float key", float), 3.14)

    assert inject(Key("string key", str)) == "Injected"
    assert inject(Key("int key", int)) == 42
    assert inject(Key("float key", float)) == 3.14


def test_override_key() -> None:
    (provide, inject) = pyqure({})
    provide(Key("string key", str), "Injected")
    provide(Key("string key", str), "Override")

    assert inject(Key("string key", str)) == "Override"


def test_dont_remove_key_when_multiple_provide() -> None:

    memory: PyqureMemory = {}
    (first_provide, _) = pyqure(memory)
    first_provide(Key("First key", str), "Injected")

    (second_provide, inject) = pyqure(memory)
    second_provide(Key("Second key", str), "Injected")

    assert inject(Key("First key", str)) == "Injected"
    assert inject(Key("Second key", str)) == "Injected"
