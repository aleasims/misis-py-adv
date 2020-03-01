class Task:
    default_priority = 0

    def __init__(self, task: str, time: int, priority: int = default_priority):
        raise NotImplementedError

    def __str__(self):
        raise NotImplementedError


class Timetable:
    def __init__(self):
        raise NotImplementedError

    def __len__(self):
        raise NotImplementedError

    def __str__(self):
        raise NotImplementedError

    def __repr__(self):
        raise NotImplementedError

    def __iter__(self):
        raise NotImplementedError

    def add(self, task: Task) -> int:
        raise NotImplementedError

    def get(self, task_id: int) -> Task:
        raise NotImplementedError

    def remove(self, task_id: int):
        raise NotImplementedError

    def arrange_by_priority(self):
        raise NotImplementedError

    def arrange_by_time(self, desc: bool = True):
        raise NotImplementedError


def test():
    t = Timetable()
    i = t.add(Task('task_A', 10))
    assert repr(t) == 'Timetable:\n1. task_A (10 h, 0 priority)'
    t.add(Task('task_B', 5, 2))
    assert [task.task for task in t.arrange_by_time()] == ['task_A', 'task_B']
    assert [task.task for task in t.arrange_by_time(desc=False)] == \
        ['task_B', 'task_A']
    assert [task.task for task in t.arrange_by_priority()] == \
        ['task_B', 'task_A']
    t.remove(i)
    assert len(t) == 1


if __name__ == "__main__":
    test()
