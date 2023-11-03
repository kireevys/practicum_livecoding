import pytest


class NotFound(Exception):
    """Задача не обнаружена в вашем списке"""


class AlreadyDone(Exception):
    """Задача уже выполнена"""


class TodoList:
    def __init__(self, storage: dict):
        self._storage: dict[int, dict[str, str]] = storage
        self._last_task_number = 0

    def add(self, task: str):
        self._last_task_number += 1
        self._storage[self._last_task_number] = {"task": task, "status": "NEW"}

    def done(self, task_number: int):
        for k, v in self._storage.items():
            if k == task_number:
                if v["status"] == "DONE":
                    raise AlreadyDone
                v["status"] = "DONE"
                return
        raise NotFound

    def ls(self):
        if len(self._storage) == 0:
            return "Empty now!"

        result = []
        for k, v in self._storage.items():
            result.append(f"{k} - {v['task']} - {v['status']}")
        return "\n".join(result)

    def delete(self, task_number: int):
        for k, v in self._storage.items():
            if k == task_number:
                v["status"] = "DELETED"
                return
        raise NotFound


def test_add_first():
    sut = TodoList({})

    sut.add("some_task")

    assert sut._storage[1] == {"task": "some_task", "status": "NEW"}


def test_add_second_task():
    sut = TodoList({})

    sut.add("first")
    sut.add("second")

    assert sut._storage[2] == {"task": "second", "status": "NEW"}


def test_ls_empty():
    sut = TodoList({})

    assert sut.ls() == "Empty now!"


def test_ls_just_one():
    sut = TodoList({})

    sut.add("some")

    assert sut.ls() == "1 - some - NEW"


def test_ls_many():
    sut = TodoList(
        {
            1: {"task": "first", "status": "NEW"},
            2: {"task": "second", "status": "NEW"},
        }
    )

    assert sut.ls() == "1 - first - NEW\n2 - second - NEW"


def test_done_not_exists():
    sut = TodoList({})

    with pytest.raises(NotFound):
        sut.done(1)


def test_done():
    sut = TodoList(
        {1: {"task": "some", "status": "NEW"}, 2: {"task": "some", "status": "NEW"}}
    )

    sut.done(1)

    assert sut._storage[1] == {"task": "some", "status": "DONE"}
    assert sut._storage[2] == {"task": "some", "status": "NEW"}


def test_already_done():
    sut = TodoList({1: {"task": "some", "status": "DONE"}})

    with pytest.raises(AlreadyDone):
        sut.done(1)


def test_delete_not_exists():
    sut = TodoList({})

    with pytest.raises(NotFound):
        sut.delete(1)


def test_delete():
    sut = TodoList({1: {"task": "some", "status": "DONE"}})

    sut.delete(1)

    assert sut._storage[1] == {"task": "some", "status": "DELETED"}
