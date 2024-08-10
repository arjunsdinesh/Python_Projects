# Creating a to-do list

# Created a list named tasks
tasks = []

# To add your tasks
def add_task(task):
    tasks.append({'task': task, 'done': False})
    print("Task added...")

# To mark task as done
def mark_done(task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index]['done'] = True
        print("Task marked as done...")
    else:
        print("Invalid task number")

# To delete your task
def delete_task(task_index):
    if 0 <= task_index < len(tasks):
        tasks.pop(task_index)
        print("Task Deleted...")
    else:
        print("Invalid task number")

# To show all tasks and the status of the tasks
def show_task():
    for i, task in enumerate(tasks):
        status = "done" if task["done"] else "not done"
        print("Tasks:\n")
        print(f"{i}. {task['task']} - {status}")

def main():
    while True:
        print("\nTo-Do List Application")
        print("1. Add Your Task \n2. Mark Your Task As Done \n3. Delete Task \n4. Show The Tasks \n5. Exit")

        choice = int(input("Enter Your Choice: "))

        if choice == 1:
            task = input('Enter Your Task: ')
            add_task(task)

        elif choice == 2:
            task_index = int(input("Enter the Task index to mark it as done: "))
            mark_done(task_index)

        elif choice == 3:
            task_index = int(input("Enter the task index to delete: "))
            delete_task(task_index)

        elif choice == 4:
            show_task()

        elif choice == 5:
            break
        
        else:
            print("Enter a valid option")

main()  # To call the main function
