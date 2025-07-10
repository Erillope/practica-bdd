Feature: Manage tasks in ToDo List

  Scenario: Add a task to the to-do list
    Given the to-do list is empty
    When the user adds a task "Buy groceries"
    Then the to-do list should contain "Buy groceries"

  Scenario: List all tasks in the to-do list
    Given the to-do list contains tasks:
      | Task         |
      | Buy groceries|
      | Pay bills    |
    When the user lists all tasks
    Then the output should contain:
      | Task         |
      | Buy groceries|
      | Pay bills    |

  Scenario: Mark a task as completed
    Given the to-do list contains tasks with status:
      | Task         | Status  |
      | Buy groceries| Pending |
    When the user marks task "Buy groceries" as completed
    Then the to-do list should show task "Buy groceries" as completed

  Scenario: Clear the entire to-do list
    Given the to-do list contains tasks:
      | Task         |
      | Buy groceries|
      | Pay bills    |
    When the user clears the to-do list
    Then the to-do list should be empty

  Scenario: Try to mark a task that does not exist
    Given the to-do list is empty
    When the user marks task "Go running" as completed
    Then the to-do list should still be empty

  Scenario: Add multiple tasks and list them
    Given the to-do list is empty
    When the user adds the following tasks:
      | Task          |
      | Buy milk      |
      | Walk the dog  |
    Then the to-do list should contain:
      | Task          |
      | Buy milk      |
      | Walk the dog  |
