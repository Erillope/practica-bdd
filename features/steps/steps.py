from behave import given, when, then #type: ignore
import sys
import os
from typing import Any

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from todo_list import TodoList

@given('the To-Do list is empty')
def step_given_empty_list(context: Any):
    context.todo_list = TodoList()

@when('the user adds a task "{task_name}"')
def step_when_add_task(context: Any, task_name: str):
    
    context.todo_list.add_task(task_name)

@then('the to-do list should contain "{task_name}"')
def step_then_check_task(context: Any, task_name: str):
    assert any(task.name == task_name for task in context.todo_list.tasks), f"Task '{task_name}' not found in the list"


@given('the to-do list contains tasks')
def step_given_list_contains_tasks(context):
    context.todo_list = TodoList()
    for row in context.table:
        context.todo_list.add_task(row['Task'])


@given('the to-do list contains tasks with status')
def step_given_tasks_with_status(context):
    context.todo_list = TodoList()
    for row in context.table:
        context.todo_list.add_task(row['Task'])
        if row['Status'].lower() == 'completed':
            context.todo_list.complete_task(row['Task'])


@when('the user adds the following tasks')
def step_when_add_multiple_tasks(context):
    for row in context.table:
        context.todo_list.add_task(row['Task'])


@when('the user lists all tasks')
def step_when_list_tasks(context):
    context.listed_tasks = [task.name for task in context.todo_list.tasks]


@when('the user marks task "{task_name}" as completed')
def step_when_mark_task_completed(context, task_name):
    try:
        context.todo_list.complete_task(task_name)
    except ValueError:
        pass


@when('the user clears the to-do list')
def step_when_clear_list(context):
    context.todo_list.tasks.clear()


@then('the output should contain')
def step_then_output_should_contain(context):
    expected = [row['Task'] for row in context.table]
    actual = context.listed_tasks
    for task in expected:
        assert task in actual, f"Expected task '{task}' not in output"


@then('the to-do list should show task "{task_name}" as completed')
def step_then_task_should_be_completed(context, task_name):
    for task in context.todo_list.tasks:
        if task.name == task_name:
            assert task.completed, f"Task '{task_name}' is not completed"
            return
    raise AssertionError(f"Task '{task_name}' not found")


@then('the to-do list should be empty')
def step_then_list_should_be_empty(context):
    assert len(context.todo_list.tasks) == 0, "The to-do list is not empty"


@then('the to-do list should contain')
def step_then_list_should_contain(context):
    expected_tasks = [row['Task'] for row in context.table]
    actual_tasks = [task.name for task in context.todo_list.tasks]
    for task in expected_tasks:
        assert task in actual_tasks, f"Task '{task}' not found in to-do list"
    assert len(actual_tasks) == len(expected_tasks), "Unexpected number of tasks"


@then('the to-do list should still be empty')
def step_impl(context):
    assert len(context.todo_list.tasks) == 0, "Expected to-do list to be empty"