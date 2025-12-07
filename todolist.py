import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry("400x500")
        root.configure(bg="blue")

        self.tasks = []

        # Heading
        self.title_label = tk.Label(root, text="To-Do List", font=("Arial", 18, "bold"))
        self.title_label.pack(pady=10)

        # Task Entry
        self.task_entry = tk.Entry(root, font=("Arial", 14))
        self.task_entry.pack(pady=10, padx=20, fill=tk.X)

        # Buttons Frame
        self.btn_frame = tk.Frame(root)
        self.btn_frame.pack(pady=5)

        self.add_btn = tk.Button(self.btn_frame, text="Add Task", command=self.add_task, width=12,bg="black",fg="white")
        self.add_btn.grid(row=0, column=0, padx=5)

        self.delete_btn = tk.Button(self.btn_frame, text="Delete Task", command=self.delete_task, width=12,bg="black",fg="white")
        self.delete_btn.grid(row=0, column=1, padx=5)

        self.clear_btn = tk.Button(self.btn_frame, text="Clear All", command=self.clear_tasks, width=12,bg="black",fg="white")
        self.clear_btn.grid(row=0, column=2, padx=5)

        # Listbox
        self.task_listbox = tk.Listbox(root, font=("Arial", 14), selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append(task)
            self.update_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task")

    def delete_task(self):
        try:
            selected_task = self.task_listbox.curselection()[0]
            self.tasks.pop(selected_task)
            self.update_listbox()
        except:
            messagebox.showwarning("Warning", "Please select a task to delete")

    def clear_tasks(self):
        self.tasks.clear()
        self.update_listbox()

    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)


if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
