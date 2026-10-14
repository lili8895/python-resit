import tkinter as tk
from datetime import date, datetime
from pathlib import Path

FILE = Path(__file__).with_name("tasks.txt")

def load_tasks():
    if not FILE.exists():
        return []
    result = []
    for line in FILE.read_text(encoding="utf-8").splitlines():
        if "|" in line:
            title, due = line.split("|", 1)
            result.append((title.strip(), due.strip()))
    return result

def save_tasks(tasks):
    text = "\n".join(f"{title}|{due}" for title, due in tasks)
    FILE.write_text(text, encoding="utf-8")

def task_color(due):
    today = date.today()
    task_date = datetime.strptime(due, "%Y-%m-%d").date()
    if task_date < today:
        return "red"
    if task_date == today:
        return "orange"
    return "green"

def refresh():
    for widget in listbox.winfo_children():
        widget.destroy()

    for index, (title, due) in enumerate(tasks):
        row = tk.Frame(listbox)
        row.pack(fill="x", padx=5, pady=3)

        label = tk.Label(
            row,
            text=f"{title} — до {due}",
            anchor="w",
            fg=task_color(due),
            font=("Arial", 11)
        )
        label.pack(side="left", fill="x", expand=True)

        button = tk.Button(row, text="Удалить", command=lambda i=index: delete_task(i))
        button.pack(side="right")

def add_task():
    title = title_entry.get().strip()
    due = date_entry.get().strip()

    try:
        datetime.strptime(due, "%Y-%m-%d")
    except ValueError:
        status.config(text="Дата должна быть в формате ГГГГ-ММ-ДД")
        return

    if not title:
        status.config(text="Введите название задачи")
        return

    tasks.append((title, due))
    save_tasks(tasks)
    title_entry.delete(0, tk.END)
    date_entry.delete(0, tk.END)
    refresh()
    status.config(text="Задача добавлена")

def delete_task(index):
    tasks.pop(index)
    save_tasks(tasks)
    refresh()

root = tk.Tk()
root.title("Напоминалка — ToDo")
root.geometry("650x450")

tk.Label(root, text="Название задачи:").pack(pady=(10, 2))
title_entry = tk.Entry(root, width=60)
title_entry.pack()

tk.Label(root, text="Срок (ГГГГ-ММ-ДД):").pack(pady=(8, 2))
date_entry = tk.Entry(root, width=60)
date_entry.pack()

tk.Button(root, text="Добавить задачу", command=add_task).pack(pady=10)

status = tk.Label(root, text="")
status.pack()

listbox = tk.Frame(root)
listbox.pack(fill="both", expand=True, padx=10, pady=10)

tasks = load_tasks()
refresh()
root.mainloop()
