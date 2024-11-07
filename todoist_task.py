from dataclasses import dataclass
from datetime import date
from typing import Optional

@dataclass
class TodoistTask:
    task: str = 'task'
    name: str
    description: str = ''
    priority: int
    due_date: Optional[date] = None
    
    def __post_init__(self):
        # Initialize priority through the setter to enforce limits
        self.priority = self.priority
    
    @property
    def priority(self) -> int:
        return self._priority
    
    @priority.setter
    def priority(self, value: int) -> None:
        self._priority = min( max(value, 1), 4 )