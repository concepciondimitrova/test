import os

TASKS_FILE = "for_tasks.txt"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r", encoding="utf-8") as file:
        tasks = [line.strip() for line in file.readlines()]
    return tasks

def save_tasks(tasks):
    with open(TASKS_FILE, "w", encoding="utf-8") as file:
        for task in tasks:
            file.write(f"{task}\n")

def show_tasks(tasks):
    if not tasks:
        print("\nСписок задач пуст.\n")
    else:
        print("\nТекущие задачи:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    print()

def add_task(tasks):
    task = input("Введите новую задачу: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print(f"Задача \"{task}\" добавлена!\n")
    else:
        print("Задача не может быть пустой.\n")

def delete_task(tasks):
    show_tasks(tasks)
    try:
        task_num = int(input("Введите номер задачи для удаления: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f"Задача \"{removed_task}\" удалена!\n")
        else:
            print("Неверный номер задачи.\n")
    except ValueError:
        print("Введите корректный номер задачи.\n")

def main():
    tasks = load_tasks()
    while True:
        print("Меню:")
        print("1. Показать задачи")
        print("2. Добавить задачу")
        print("3. Удалить задачу")
        print("4. Выйти")

        choice = input("Выберите действие (1-4): ").strip()
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("До свидания!")
            break
        else:
            print("Неверный ввод. Попробуйте снова.\n")

if __name__ == "__main__":
    main()
