import os
import sys
todo_list = []


def load_todos(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            for line in f:
                todo_list.append(line.strip())
    else:
        print("No existing todo file found, starting fresh.")


def save_todos(file_path):
    with open(file_path, 'w') as f:
        for todo in todo_list:
            f.write(todo + '\n')


def add_todo():
    todo = input("Enter a new todo: ")
    todo_list.append(todo)
    print("Todo added.")


def list_todos():
    if len(todo_list) == 0:
        print("No todos yet!")
    else:
        for i in range(len(todo_list)):
            print(f"{i + 1}. {todo_list[i]}")


def remove_todo():
    list_todos()
    idx = input("Enter the number of the todo to remove: ")
    todo_list.pop(int(idx) - 1)
    print("Todo removed.")


def main():
    file_path = 'todos.txt'
    load_todos(file_path)
    while True:
        print("\nTodo Manager")
        print("1. List todos")
        print("2. Add todo")
        print("3. Remove todo")
        print("4. Save and Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            list_todos()
        elif choice == '2':
            add_todo()
        elif choice == '3':
            remove_todo()
        elif choice == '4':
            save_todos(file_path)
            print("Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice, try again.")


if __name__ == '__main__':
    main()

