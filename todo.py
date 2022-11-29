# DVA128 Case 2
# Grupp 6:
#   Sinan Pasic,
#   Jasmine Pedersen,
#   Karl Sorsell
#   Karam Al-Saudi

import os
import json
from jsonschema import validate

FLAG_EXIT = False

todos = []

def validate_json_format(file_handle: str) -> bool:


def validate_file_by_schema(file_handle: str) -> bool:
    try:
        validate(instance = file_handle, schema = )
    
    except jsonschema.exceptions.ValidationError:
        print("Provided .json file did not follow format enforcement by the schema.\nSee schema.json for correct format.")
        return False

    return True

while FLAG_EXIT == False:
    os.system("cls" if os.name == "nt" else "clear")

    print(
        " ─────────────────────────────────────\n",
        "\t\tTodoify\t\n",
        "─────────────────────────────────────\n",
        "list  \t│ List todos\n",
        "add   \t│ Add todo\n",
        "check \t│ Check todo\n",
        "delete\t│ Delete todo\n",
        "exit  \t│ Exit the application\n",
        "─────────────────────────────────────\n",
        "save\t│ Save todos to .json file\n",
        "load\t│ Load todos from .json file\n",
        "─────────────────────────────────────\n"
        )

    user_input: str = input("Selection > ")

    match (user_input):
        case "exit":
            FLAG_EXIT = True

        case "list":
            """
            Prints each dictionary object in the todo list as [index | status description]
            """
            if not todos:
                print("Nothing in the list!")
                input("Press anything to continue.")
                continue

            for todo in todos:
                print("[X]" if todo["checked"] else "[ ]", todo["description"])
            input("Press anything to continue.")
        
        case "add":
            todo_description = input("Todo description > ")
            todos.append({
                "description": todo_description,
                "checked": False
            })

            input("Press anything to continue.")
        
        case "check":
            """
            Overview: Applies boolean negation of a todo dictionary object's 'checked' attribute.
            Edge case: Negative values behave as normally when indexing.
            """
            if not todos:
                print("Nothing in the list!")
                input("Press anything to continue.")
                continue
                
            for index, todo in enumerate(todos):
                print(f"{index} | {'[X]' if todo['checked'] else '[ ]'} {todo['description']}")

            try:
                todos_idx = int(input("Todo index > "))
                todos[todos_idx]["checked"] = not todos[todos_idx]["checked"]

            except ValueError:
                print("Invalid input type provided as index to todo-list.")
                input("Press anything to continue")

            except IndexError:
                print("Out of range index value provided as argument to todo-list.")
                input("Press anything to continue")

            else:
                print(f"Success: {'Unchecked → checked' if todos[todos_idx]['checked'] else 'Checked → Unchecked'}")
                input("Press anything to continue.")

        case "delete":
            """
            Overview: Deletes a dictionary object in todos list by given index.
            Edge cases: Negative values behave as normally when indexing.
            Return: Return which index was deleted and its description attribute.
            """
            if not todos:
                print("Nothing in the list!")
                input("Press anything to continue")
                continue

            for index, todo in enumerate(todos):
                print(f"{index} | {'[X]' if todo['checked'] else '[ ]'} {todo['description']}")

            try:
                todos_idx = int(input("Todo index > "))

                # Pop() deletes by index, while remove() deletes by value.
                # Pop() also returns the item which was deleted at the given index, which here is represented by a
                # dictionary object which can be indexed to access object attributes.
                deleted_desc = todos.pop(todos_idx)['description']

            except ValueError:
                print("Invalid input type provided as idex to todo-list.")
                input("Press anything to continue")

            except IndexError:
                print("Out of range index value provided as argument to todo-list.")
                input("Press anything to continue")

            else:
                print(f"Index {index} removed from list.\nDescription: {deleted_desc}")
                input("Press anything to continue")

        case "save":
            """
            Saves the dictionary objects in todos to a .json file.
            """

            # Doesn't require error-checking. If the tasks were imported from a .json file
            # then they've already been validated, and if they were generated through program functions
            # then they're already in the correct format for exportation.
            with open('todo_data.json', 'w') as file_handle:
                for todo in todos:
                    json.dump(todo, file_handle)

            print("Tasks successfully saved to 'todo_data.json'")
            input("Press anything to continue.")

        case "load":
            """
            Reads a .json file of dictionary objects with attributes 'description: str' and 'checked: bool'
            into the todos list structure.
            Given a file of incorrect format or extension, an error is raised.
            Format:
                {"description": "", "checked": Boolean}
            """
            pass

        case _:
            print(f"Invalid option '{user_input}' selected.")
            input("Press anything to continue.")
