class Task:
    def __init__(self, description, deadline, status=False):
        self.description = description  # Описание задачи
        self.deadline = deadline  # Срок выполнения
        self.status = status  # Статус (False - не выполнено, True - выполнено)


tasks = []  # Список для хранения всех задач


def add_task(description, deadline):
    """Добавляет новую задачу в список"""
    new_task = Task(description, deadline)
    tasks.append(new_task)
    print(f'Добавлена: "{description}" (до {deadline})')


def complete_task(task_index):
    """Отмечает задачу как выполненную по индексу"""
    if 0 <= task_index < len(tasks):
        tasks[task_index].status = True
        print(f'Выполнено: "{tasks[task_index].description}"')
    else:
        print("Ошибка: неверный индекс задачи")


def show_current_tasks():
    """Показывает список невыполненных задач с их индексами"""
    current_tasks = [t for t in tasks if not t.status]

    if not current_tasks:
        print("Все задачи выполнены!")
        return

    print("\nТекущие задачи:")
    for i, task in enumerate(current_tasks):
        print(f"{i}. {task.description} (до {task.deadline})")


# Пример использования
add_task("помолиться", "2024-01-01")
add_task("идти в спортзал", "2024-01-02")

complete_task(0)  # Отмечаем первую задачу как выполненную

show_current_tasks()