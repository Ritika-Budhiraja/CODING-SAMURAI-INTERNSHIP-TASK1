import json

class Task:
    def __init__(self, description):
        self.description = description

    def to_dict(self):
        return {"description": self.description}

    @classmethod
    def from_dict(cls, data):
        return cls(description=data["description"])

class TaskList:
    def __init__(self, filename="tasks.json"):
        self.tasks = []
        self.filename = filename
        self.load_tasks()

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)
        self.save_tasks()

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            self.save_tasks()

    def save_tasks(self):
        with open(self.filename, "w") as f:
            json.dump([task.to_dict() for task in self.tasks], f, indent=4)

    def load_tasks(self):
        try:
            with open(self.filename, "r") as f:
                tasks_data = json.load(f)
                self.tasks = [Task.from_dict(task_data) for task_data in tasks_data]
        except FileNotFoundError:
            self.tasks = []

    def list_tasks(self):
        for i, task in enumerate(self.tasks):
            print(f"{i + 1}. {task.description}")


def main():
    task_list = TaskList()

    while True:
        print("\nTo-Do List:")
        task_list.list_tasks()
        print("\nOptions:")
        print("1. Add task")
        print("2. Remove task")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            description = input("Enter task description: ")
            task_list.add_task(description)
        elif choice == "2":
            try:
                index = int(input("Enter task number to remove: ")) - 1
                task_list.remove_task(index)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == "3":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
