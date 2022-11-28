def draw_gui():
    print(
        " ─────────────────────────────────────\n",
        "\t\tTodoify\t\n",
        "─────────────────────────────────────\n",
        "list  \t│ List todos\n",
        "add   \t│ Add todo\n",
        "check \t│ Check todo\n",
        "delete\t│ Delete todo\n",
        "exit  \t│ Exit the application\n",
        "───────────────────────────────────\n",
        "save\t│ Save todos to file\n",
        "load\t│ Load todos from file\n",
        "────────────────────────────────────\n"
    )

todos = [
    {
        'description': '',
        'checked': False
    }
]

for todo in todos:
    if todo['checked'] == True:
        print("[X]", todo['description'])
    else:
        print("[ ]", todo['description'])

while (user_input := input("Selection > ")).casefold() != "exit":
    match (user_input):
        case "list":
            for todo in todos:
                print(todo)
