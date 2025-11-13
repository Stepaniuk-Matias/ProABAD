from dataclasses import dataclass

from datetime import datetime

@dataclass
class Process:
    id: UUID
    name: str
    description: str
    status: ProcessStatus
    tasks: list[Task]
    resources: list[Resource]
    responsible: User
    created_at: datetime
    updated_at: datetime

    def add_task(self, task: Task):
        if any(t.name == task.name for t in self.tasks):
            raise ValueError("Duplicate task name")
        self.tasks.append(task)

    def mark_complete(self):
        if not all(t.is_complete for t in self.tasks):
            raise ValueError("Cannot complete process with pending tasks")
        self.status = ProcessStatus.COMPLETED
