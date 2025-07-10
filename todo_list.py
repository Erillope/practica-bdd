from typing import List

class Task:
    def __init__(self, name: str) -> None :
        self.name = name
        self.completed = False
    
    def complete(self) -> None:
        self.completed = True

class TodoList:
    def __init__(self) -> None:
        self.tasks: List[Task] = []
    
    def add_task(self, task: str) -> None:
        self.tasks.append(Task(task))
    
    def complete_task(self, task: str) -> None:
        for t in self.tasks:
            if t.name == task:
                t.complete()
                return
        raise ValueError("Task not found in the list")