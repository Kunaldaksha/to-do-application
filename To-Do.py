import os

# File to store tasks
TASK_FILE = "todo.txt"

# Load tasks from file
def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, "r") as file:
        lines = file.readlines()
    tasks = []
    for line in lines:
        task, status = line.strip().split(" | ")
        tasks.append({"task": task, "done": status == "Done"})
    return tasks

# Save tasks to file
def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        for t in tasks:
            file.write(f"{t['task']} | {'Done' if t['done'] else 'Pending'}\n")

# Display all tasks
def view_tasks(tasks):
    if not tasks:
        print("\n✅ No tasks found!")
        return
    print("\n📝 To-Do List:")
    print("----------------------")
    for i, t in enumerate(tasks, start=1):
        status = "✔️" if t["done"] else "❌"
        print(f"{i}. {t['task']} [{status}]")

# Add a new task
def add_task(tasks):
    task = input("\nEnter new task: ").strip()
    if task:
        tasks.append({"task": task, "done": False})
        save_tasks(tasks)
        print("✅ Task added successfully!")
    else:
        print("⚠️ Task cannot be empty!")

# Mark a task as done
def mark_done(tasks):
    view_tasks(tasks)
    try:
        num = int(input("\nEnter task number to mark as done: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["done"] = True
            save_tasks(tasks)
            print("✅ Task marked as done!")
        else:
            print("⚠️ Invalid task number!")
    except ValueError:
        print("⚠️ Please enter a valid number!")

# Update a task
def update_task(tasks):
    view_tasks(tasks)
    try:
        num = int(input("\nEnter task number to update: "))
        if 1 <= num <= len(tasks):
            new_text = input("Enter updated task: ").strip()
            if new_text:
                tasks[num - 1]["task"] = new_text
                save_tasks(tasks)
                print("✅ Task updated successfully!")
            else:
                print("⚠️ Task cannot be empty!")
        else:
            print("⚠️ Invalid task number!")
    except ValueError:
        print("⚠️ Please enter a valid number!")

# Delete a task
def delete_task(tasks):
    view_tasks(tasks)
    try:
        num = int(input("\nEnter task number to delete: "))
        if 1 <= num <= len(tasks):
            deleted = tasks.pop(num - 1)
            save_tasks(tasks)
            print(f"🗑️ Deleted task: '{deleted['task']}'")
        else:
            print("⚠️ Invalid task number!")
    except ValueError:
        print("⚠️ Please enter a valid number!")

# Main Menu
def main():
    tasks = load_tasks()
    while True:
        print("\n========== TO-DO LIST ==========")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Update Task")
        print("5. Delete Task")
        print("6. Exit")
        print("================================")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            update_task(tasks)
        elif choice == "5":
            delete_task(tasks)
        elif choice == "6":
            print("\n👋 Exiting... Have a productive day!")
            break
        else:
            print("⚠️ Invalid choice! Please enter 1–6.")

if __name__ == "__main__":
    main()
