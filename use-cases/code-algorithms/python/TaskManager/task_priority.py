from datetime import datetime
from typing import List, Optional, Any
from models import TaskStatus, TaskPriority

def calculate_task_score(task: Any) -> int:
    """Calculate a priority score for a task based on multiple factors.

    Evaluates a task's priority, due date proximity, current status, metadata 
    tags, and recent update activity to compute a composite numerical score 
    representing its overall urgency and importance.

    Args:
        task (Any): An object representing the task. Expected attributes include:
            - priority (TaskPriority): The base priority level.
            - due_date (datetime, optional): The task deadline.
            - status (TaskStatus): The current lifecycle state of the task.
            - tags (iterable of str, optional): Associated labels or keywords.
            - updated_at (datetime): Timestamp of the last modification.

    Returns:
        int: The calculated priority score. Higher scores indicate greater 
            urgency and importance. Negative scores are possible for completed tasks.

    Raises:
        AttributeError: If the provided `task` object lacks any required 
            attributes (`priority`, `status`, `tags`, `updated_at`).
        TypeError: If datetime comparisons encounter incompatible timezone-aware 
            and timezone-naive objects.

    Example:
        >>> task = Task(
        ...     priority=TaskPriority.HIGH,
        ...     due_date=datetime(2026, 6, 10),
        ...     status=TaskStatus.TODO,
        ...     tags=["critical"],
        ...     updated_at=datetime.now()
        ... )
        >>> score = calculate_task_score(task)
        >>> print(score)
        53

    Note:
        - Relies on system time via `datetime.now()` for deadline calculations.
        - Overdue tasks receive a significant boost (+35 points), while 
          completed tasks receive a severe penalty (-50 points).
    """
    # Base priority weights
    priority_weights = {
        TaskPriority.LOW: 1,
        TaskPriority.MEDIUM: 2,
        TaskPriority.HIGH: 4,
        TaskPriority.URGENT: 6
    }

    # Calculate base score from priority
    score = priority_weights.get(task.priority, 0) * 10

    # Add due date factor (higher score for tasks due sooner)
    if task.due_date:
        days_until_due = (task.due_date - datetime.now()).days
        if days_until_due < 0:  # Overdue tasks
            score += 35
        elif days_until_due == 0:  # Due today
            score += 20
        elif days_until_due <= 2:  # Due in next 2 days
            score += 15
        elif days_until_due <= 7:  # Due in next week
            score += 10

    # Reduce score for tasks that are completed or in review
    if task.status == TaskStatus.DONE:
        score -= 50
    elif task.status == TaskStatus.REVIEW:
        score -= 15

    # Boost score for tasks with certain tags (safely handle empty/None tags)
    if task.tags and any(tag in ["blocker", "critical", "urgent"] for tag in task.tags):
        score += 8

    # Boost score for recently updated tasks
    days_since_update = (datetime.now() - task.updated_at).days
    if days_since_update < 1:
        score += 5

    return score

def sort_tasks_by_importance(tasks: List[Any]) -> List[Any]:
    """Sort tasks by calculated importance score (highest first).

    Pre-computes scores for each task to avoid redundant execution inside the 
    sorting algorithm, then orders the collection in descending sequence.

    Args:
        tasks (List[Any]): A collection of task objects to be sorted.

    Returns:
        List[Any]: A new list containing the tasks ordered from highest priority 
            score to lowest priority score.

    Example:
        >>> sorted_backlog = sort_tasks_by_importance(my_tasks)
    """
    # Pair each task with its score upfront to prevent recalculating inside sort()
    task_scores = [(calculate_task_score(task), task) for task in tasks]
    
    # Sort descending (reverse=True) using the score (index 0) as the sorting key
    sorted_tasks = [task for _, task in sorted(task_scores, key=lambda x: x[0], reverse=True)]
    return sorted_tasks

def get_top_priority_tasks(tasks: List[Any], limit: int = 5) -> List[Any]:
    """Return the top N priority tasks.

    Evaluates and sorts an entire collection of tasks, slicing the result 
    to return only the top-tier items requiring immediate action.

    Args:
        tasks (List[Any]): A collection of task objects to evaluate.
        limit (int, optional): The maximum number of top tasks to return. 
            Defaults to 5.

    Returns:
        List[Any]: A list containing up to `limit` highest-priority tasks.

    Example:
        >>> immediate_focus = get_top_priority_tasks(my_tasks, limit=3)
    """
    sorted_tasks = sort_tasks_by_importance(tasks)
    return sorted_tasks[:limit]