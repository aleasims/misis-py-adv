class Task:
    default_priority = 0

    def __init__(self, task: str, time: int, priority: int = default_priority):
        self.task = task
        self.time = time
        self.priority = priority

    def __str__(self):
        if self.priority != self.default_priority:
            return '{task} ({time} h, {priority} priority)'.format(
                task=self.task,
                time=self.time,
                priority=self.priority)
        else:
            return '{task} ({time} h)'.format(
                task=self.task,
                time=self.time)


class Timetable:
    def __init__(self):
        self.tasks = []

    def __len__(self):
        return len(self.tasks)

    def __str__(self):
        return '<Timetable ({} tasks)>'.format(len(self))

    def __repr__(self):
        tmp = ['Timetable:']
        tmp += ['{}. {}'.format(i, task)
                for i, task in enumerate(self.tasks, start=1)]
        return '\n'.join(tmp)

    def __iter__(self):
        yield from self.tasks

    def add(self, task: Task) -> int:
        self.tasks.append(task)
        return len(self)

    def get(self, task_id):
        if task_id > 0:
            try:
                return self.tasks[task_id - 1]
            except IndexError:
                pass

    def remove(self, task_id):
        if task_id > 0:
            try:
                self.tasks.pop(task_id - 1)
            except IndexError:
                pass

    def arrange_by_priority(self):
        yield from sorted(self, key=lambda task: task.priority, reverse=True)

    def arrange_by_time(self, desc=True):
        yield from sorted(self, key=lambda task: task.time, reverse=desc)


def test():
    t = Timetable()
    i = t.add(Task('task_A', 10))
    assert repr(t) == 'Timetable:\n1. task_A (10 h)'

    t.add(Task('task_B', 5, 2))
    assert repr(t) == 'Timetable:\n' + \
        '1. task_A (10 h)\n2. task_B (5 h, 2 priority)'

    assert t.get(1).task == 'task_A'

    assert [task.task for task in t.arrange_by_time()] == ['task_A', 'task_B']
    assert [task.task for task in t.arrange_by_time(desc=False)] == \
        ['task_B', 'task_A']
    assert [task.task for task in t.arrange_by_priority()] == \
        ['task_B', 'task_A']

    t.remove(i)
    assert len(t) == 1


if __name__ == "__main__":
    test()
