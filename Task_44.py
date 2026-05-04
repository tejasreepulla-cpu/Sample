# import csv

# class TodoList:
#     def __init__(self):
#         self.tasks = []
#         self.file_name = "tasks.csv"
#         self.load_tasks()   # Load tasks when object is created

#     def add_task(self, task):
#         self.tasks.append({"task": task, "completed": False})
#         print("Task added successfully!")

#     def remove_task(self, task):
#         for t in self.tasks:
#             if t["task"] == task:
#                 self.tasks.remove(t)
#                 print("Task removed successfully!")
#                 return
#         print("Task not found in the list.")

#     def mark_completed(self, task):
#         for t in self.tasks:
#             if t["task"] == task:
#                 t["completed"] = True
#                 print("Task marked as completed!")
#                 return
#         print("Task not found in the list.")

#     def display_tasks(self):
#         if self.tasks:
#             print("Tasks:")
#             for i, t in enumerate(self.tasks, start=1):
#                 status = "Completed" if t["completed"] else "Not Completed"
#                 print(f"{i}. {t['task']} - {status}")
#         else:
#             print("No tasks in the list.")

#     # ✅ SAVE TASKS TO CSV
#     def save_tasks(self):
#         with open(self.file_name, mode='w', newline='') as file:
#             writer = csv.writer(file)
#             writer.writerow(["task", "status"])  # header

#             for t in self.tasks:
#                 writer.writerow([t["task"], t["completed"]])

#         print("Tasks saved to CSV successfully!")

#     # ✅ LOAD TASKS FROM CSV
#     def load_tasks(self):
#         try:
#             with open(self.file_name, mode='r') as file:
#                 reader = csv.DictReader(file)
#                 self.tasks = []

#                 for row in reader:
#                     self.tasks.append({
#                         "task": row["task"],
#                         "completed": row["status"] == 'True'
#                     })

#             print("Tasks loaded from CSV successfully!")

#         except FileNotFoundError:
#             print("No existing file found. Starting fresh.")


# def main():
#     todo_list = TodoList()

#     while True:
#         print("\nTODO LIST MENU:")
#         print("1. Add a task")
#         print("2. Remove a task")
#         print("3. Mark a task as completed")
#         print("4. Display tasks")
#         print("5. Save tasks")
#         print("6. Exit")

#         choice = input("Enter your choice (1-6): ")

#         if choice == '1':
#             task = input("Enter task to add: ")
#             todo_list.add_task(task)

#         elif choice == '2':
#             task = input("Enter task to remove: ")
#             todo_list.remove_task(task)

#         elif choice == '3':
#             task = input("Enter task to mark as completed: ")
#             todo_list.mark_completed(task)

#         elif choice == '4':
#             todo_list.display_tasks()

#         elif choice == '5':
#             todo_list.save_tasks()

#         elif choice == '6':
#             todo_list.save_tasks()  # auto-save before exit
#             print("Exiting...")
#             break

#         else:
#             print("Invalid choice. Please enter a valid option.")


# main()

"""Due Dates for Tasks
“Add an option to set a due date for each task using a date picker (Calendar widget) and display it beside the task in the list.”"""


# import csv
# from tkinter import *
# from tkcalendar import Calendar

# class TodoList:
#     def __init__(self):
#         self.tasks = []
#         self.file_name = "tasks.csv"
#         self.load_tasks()

#     def add_task(self, task, due_date):
#         self.tasks.append({
#             "task": task,
#             "completed": False,
#             "due_date": due_date
#         })
#         print("Task added successfully!")

#     def remove_task(self, task):
#         for t in self.tasks:
#             if t["task"] == task:
#                 self.tasks.remove(t)
#                 print("Task removed successfully!")
#                 return
#         print("Task not found.")

#     def mark_completed(self, task):
#         for t in self.tasks:
#             if t["task"] == task:
#                 t["completed"] = True
#                 print("Task marked as completed!")
#                 return
#         print("Task not found.")

#     def display_tasks(self):
#         if self.tasks:
#             print("\nTasks:")
#             for i, t in enumerate(self.tasks, start=1):
#                 status = "Completed" if t["completed"] else "Not Completed"
#                 print(f"{i}. {t['task']} | {status} | Due: {t['due_date']}")
#         else:
#             print("No tasks.")

#     def save_tasks(self):
#         with open(self.file_name, mode='w', newline='') as file:
#             writer = csv.writer(file)
#             writer.writerow(["task", "status", "due_date"])

#             for t in self.tasks:
#                 writer.writerow([t["task"], t["completed"], t["due_date"]])

#     def load_tasks(self):
#         try:
#             with open(self.file_name, mode='r') as file:
#                 reader = csv.DictReader(file)
#                 self.tasks = []

#                 for row in reader:
#                     self.tasks.append({
#                         "task": row["task"],
#                         "completed": row["status"] == 'True',
#                         "due_date": row["due_date"]
#                     })
#         except FileNotFoundError:
#             pass


# # 🎯 Calendar Picker Function
# def pick_date(todo_list):
#     def get_date():
#         selected_date = cal.get_date()
#         task = entry.get()

#         if task:
#             todo_list.add_task(task, selected_date)
#             top.destroy()
#         else:
#             print("Enter a task first!")

#     top = Toplevel()
#     top.title("Select Due Date")

#     cal = Calendar(top, selectmode='day')
#     cal.pack(pady=10)

#     Button(top, text="Confirm Date", command=get_date).pack(pady=10)


# # 🎯 Main Program
# def main():
#     todo_list = TodoList()

#     root = Tk()
#     root.title("Todo List")

#     global entry
#     entry = Entry(root, width=40)
#     entry.pack(pady=10)

#     Button(root, text="Add Task with Due Date",
#            command=lambda: pick_date(todo_list)).pack()

#     Button(root, text="Display Tasks",
#            command=todo_list.display_tasks).pack()

#     Button(root, text="Save Tasks",
#            command=todo_list.save_tasks).pack()

#     Button(root, text="Exit",
#            command=lambda: (todo_list.save_tasks(), root.destroy())).pack()

#     root.mainloop()


# main()

"""Time Reminder / Notifications
“Add a reminder feature that pops up a messagebox when a task’s due time is reached.”"""

# import csv
# from tkinter import *
# from tkinter import messagebox
# from tkcalendar import Calendar
# from datetime import datetime

# class TodoList:
#     def __init__(self):
#         self.tasks = []
#         self.file_name = "tasks.csv"
#         self.load_tasks()

#     def add_task(self, task, due_datetime):
#         self.tasks.append({
#             "task": task,
#             "completed": False,
#             "due_datetime": due_datetime
#         })
#         print("Task added successfully!")

#     def remove_task(self, task):
#         for t in self.tasks:
#             if t["task"] == task:
#                 self.tasks.remove(t)
#                 print("Task removed successfully!")
#                 return
#         print("Task not found.")

#     def mark_completed(self, task):
#         for t in self.tasks:
#             if t["task"] == task:
#                 t["completed"] = True
#                 print("Task marked as completed!")
#                 return
#         print("Task not found.")

#     def display_tasks(self):
#         if self.tasks:
#             print("\nTasks:")
#             for i, t in enumerate(self.tasks, start=1):
#                 status = "Completed" if t["completed"] else "Not Completed"
#                 print(f"{i}. {t['task']} | {status} | Due: {t['due_datetime']}")
#         else:
#             print("No tasks.")

#     def save_tasks(self):
#         with open(self.file_name, mode='w', newline='') as file:
#             writer = csv.writer(file)
#             writer.writerow(["task", "status", "due_datetime"])

#             for t in self.tasks:
#                 writer.writerow([t["task"], t["completed"], t["due_datetime"]])

#     def load_tasks(self):
#         try:
#             with open(self.file_name, mode='r') as file:
#                 reader = csv.DictReader(file)
#                 self.tasks = []

#                 for row in reader:
#                     # ✅ FIX: handle both old and new CSV formats
#                     due = row.get("due_datetime") or row.get("due_date") or ""

#                     self.tasks.append({
#                         "task": row.get("task", ""),
#                         "completed": row.get("status", "False") == 'True',
#                         "due_datetime": due
#                     })
#         except FileNotFoundError:
#             pass


# # 🎯 Calendar + Time Picker
# def pick_date(todo_list):
#     def get_date():
#         selected_date = cal.get_date()
#         task = entry.get()
#         time_str = time_entry.get()

#         try:
#             due_datetime = datetime.strptime(
#                 selected_date + " " + time_str, "%m/%d/%y %H:%M"
#             )

#             if task:
#                 todo_list.add_task(task, due_datetime.strftime("%Y-%m-%d %H:%M"))
#                 top.destroy()
#             else:
#                 messagebox.showwarning("Warning", "Enter a task first!")

#         except ValueError:
#             messagebox.showerror("Error", "Enter time in HH:MM format (24-hour)")

#     top = Toplevel()
#     top.title("Select Due Date")

#     cal = Calendar(top, selectmode='day')
#     cal.pack(pady=10)

#     Button(top, text="Confirm Date", command=get_date).pack(pady=10)


# # 🎯 Reminder Checker
# def check_reminders(todo_list, root):
#     now = datetime.now().strftime("%Y-%m-%d %H:%M")

#     for task in todo_list.tasks:
#         if not task["completed"] and task["due_datetime"] == now:
#             messagebox.showinfo("Reminder", f"⏰ Task Due: {task['task']}")
#             task["completed"] = True  # prevent repeat popup

#     root.after(60000, check_reminders, todo_list, root)


# # 🎯 Main GUI
# def main():
#     global entry, time_entry

#     todo_list = TodoList()

#     root = Tk()
#     root.title("Todo List with Reminder")
#     root.geometry("350x300")

#     Label(root, text="Enter Task").pack(pady=5)
#     entry = Entry(root, width=40)
#     entry.pack(pady=5)

#     Label(root, text="Enter Time (HH:MM)").pack(pady=5)
#     time_entry = Entry(root, width=20)
#     time_entry.pack(pady=5)
#     time_entry.insert(0, "HH:MM")

#     Button(root, text="Add Task with Due Date",
#            command=lambda: pick_date(todo_list)).pack(pady=5)

#     Button(root, text="Display Tasks",
#            command=todo_list.display_tasks).pack(pady=5)

#     Button(root, text="Save Tasks",
#            command=todo_list.save_tasks).pack(pady=5)

#     Button(root, text="Exit",
#            command=lambda: (todo_list.save_tasks(), root.destroy())).pack(pady=10)

#     # Start reminder system
#     check_reminders(todo_list, root)

#     root.mainloop()


# main()

"""Task Categories
“Add a dropdown menu to select a category (like Work, Study, Personal) when adding a task, and show it beside each task.”"""

# import csv
# from tkinter import *
# from tkinter import messagebox
# from tkcalendar import Calendar
# from datetime import datetime

# class TodoList:
#     def __init__(self):
#         self.tasks = []
#         self.file_name = "tasks.csv"
#         self.load_tasks()

#     def add_task(self, task, due_datetime):
#         self.tasks.append({
#             "task": task,
#             "completed": False,
#             "due_datetime": due_datetime
#         })

#     def remove_task(self, index):
#         if 0 <= index < len(self.tasks):
#             del self.tasks[index]

#     def mark_completed(self, index):
#         if 0 <= index < len(self.tasks):
#             self.tasks[index]["completed"] = True

#     def save_tasks(self):
#         with open(self.file_name, mode='w', newline='') as file:
#             writer = csv.writer(file)
#             writer.writerow(["task", "status", "due_datetime"])

#             for t in self.tasks:
#                 writer.writerow([t["task"], t["completed"], t["due_datetime"]])

#     def load_tasks(self):
#         try:
#             with open(self.file_name, mode='r') as file:
#                 reader = csv.DictReader(file)
#                 self.tasks = []

#                 for row in reader:
#                     due = row.get("due_datetime") or row.get("due_date") or ""

#                     self.tasks.append({
#                         "task": row.get("task", ""),
#                         "completed": row.get("status", "False") == 'True',
#                         "due_datetime": due
#                     })
#         except FileNotFoundError:
#             pass


# # 📅 Calendar Picker
# def pick_date(todo_list):
#     def get_date():
#         selected_date = cal.get_date()
#         task = entry.get()
#         time_str = time_entry.get()

#         try:
#             due_datetime = datetime.strptime(
#                 selected_date + " " + time_str, "%m/%d/%y %H:%M"
#             )

#             if task:
#                 todo_list.add_task(task, due_datetime.strftime("%Y-%m-%d %H:%M"))
#                 update_listbox(todo_list)
#                 top.destroy()
#             else:
#                 messagebox.showwarning("Warning", "Enter a task first!")

#         except ValueError:
#             messagebox.showerror("Error", "Enter time in HH:MM format")

#     top = Toplevel()
#     cal = Calendar(top, selectmode='day')
#     cal.pack(pady=10)

#     Button(top, text="Confirm", command=get_date).pack()


# # 🔄 Update Listbox
# def update_listbox(todo_list):
#     listbox.delete(0, END)

#     for i, t in enumerate(todo_list.tasks):
#         status = "✔" if t["completed"] else "✘"
#         listbox.insert(END, f"{i+1}. {t['task']} [{status}] ({t['due_datetime']})")


# # ❌ Delete Task
# def delete_task(todo_list):
#     selected = listbox.curselection()
#     if selected:
#         todo_list.remove_task(selected[0])
#         update_listbox(todo_list)


# # ✅ Mark Complete
# def complete_task(todo_list):
#     selected = listbox.curselection()
#     if selected:
#         todo_list.mark_completed(selected[0])
#         update_listbox(todo_list)


# # 🔔 Reminder
# def check_reminders(todo_list, root):
#     now = datetime.now().strftime("%Y-%m-%d %H:%M")

#     for task in todo_list.tasks:
#         if not task["completed"] and task["due_datetime"] == now:
#             messagebox.showinfo("Reminder", f"⏰ Task Due: {task['task']}")
#             task["completed"] = True

#     root.after(60000, check_reminders, todo_list, root)


# # 🎯 Main GUI
# def main():
#     global entry, time_entry, listbox

#     todo_list = TodoList()

#     root = Tk()
#     root.title("Todo App")
#     root.geometry("500x400")

#     entry = Entry(root, width=40)
#     entry.pack(pady=5)

#     time_entry = Entry(root, width=20)
#     time_entry.pack()
#     time_entry.insert(0, "HH:MM")

#     Button(root, text="Add Task", command=lambda: pick_date(todo_list)).pack(pady=5)

#     listbox = Listbox(root, width=60, height=10)
#     listbox.pack(pady=10)

#     Button(root, text="Mark Completed", command=lambda: complete_task(todo_list)).pack(pady=2)
#     Button(root, text="Delete Task", command=lambda: delete_task(todo_list)).pack(pady=2)

#     Button(root, text="Save", command=todo_list.save_tasks).pack(pady=5)

#     update_listbox(todo_list)
#     check_reminders(todo_list, root)

#     root.mainloop()


# main()

"""Edit Task Feature
“Add an Edit Task button that allows updating the text of a selected task.”"""

# import csv
# from tkinter import *
# from tkinter import messagebox
# from tkcalendar import Calendar
# from datetime import datetime

# class TodoList:
#     def __init__(self):
#         self.tasks = []
#         self.file_name = "tasks.csv"
#         self.load_tasks()

#     def add_task(self, task, due_datetime):
#         self.tasks.append({
#             "task": task,
#             "completed": False,
#             "due_datetime": due_datetime
#         })

#     def remove_task(self, index):
#         if 0 <= index < len(self.tasks):
#             del self.tasks[index]

#     def mark_completed(self, index):
#         if 0 <= index < len(self.tasks):
#             self.tasks[index]["completed"] = True

#     def edit_task(self, index, new_task):
#         if 0 <= index < len(self.tasks):
#             self.tasks[index]["task"] = new_task

#     def save_tasks(self):
#         with open(self.file_name, mode='w', newline='') as file:
#             writer = csv.writer(file)
#             writer.writerow(["task", "status", "due_datetime"])

#             for t in self.tasks:
#                 writer.writerow([t["task"], t["completed"], t["due_datetime"]])

#     def load_tasks(self):
#         try:
#             with open(self.file_name, mode='r') as file:
#                 reader = csv.DictReader(file)
#                 self.tasks = []

#                 for row in reader:
#                     due = row.get("due_datetime") or row.get("due_date") or ""

#                     self.tasks.append({
#                         "task": row.get("task", ""),
#                         "completed": row.get("status", "False") == 'True',
#                         "due_datetime": due
#                     })
#         except FileNotFoundError:
#             pass


# # 📅 Calendar Picker
# def pick_date(todo_list):
#     def get_date():
#         selected_date = cal.get_date()
#         task = entry.get()
#         time_str = time_entry.get()

#         try:
#             due_datetime = datetime.strptime(
#                 selected_date + " " + time_str, "%m/%d/%y %H:%M"
#             )

#             if task:
#                 todo_list.add_task(task, due_datetime.strftime("%Y-%m-%d %H:%M"))
#                 update_listbox(todo_list)
#                 top.destroy()
#             else:
#                 messagebox.showwarning("Warning", "Enter a task first!")

#         except ValueError:
#             messagebox.showerror("Error", "Enter time in HH:MM format")

#     top = Toplevel()
#     top.title("Select Due Date")

#     cal = Calendar(top, selectmode='day')
#     cal.pack(pady=10)

#     Button(top, text="Confirm", command=get_date).pack(pady=10)


# # 🔄 Update Listbox
# def update_listbox(todo_list):
#     listbox.delete(0, END)

#     for i, t in enumerate(todo_list.tasks):
#         status = "✔" if t["completed"] else "✘"
#         listbox.insert(END, f"{i+1}. {t['task']} [{status}] ({t['due_datetime']})")


# # ❌ Delete Task
# def delete_task(todo_list):
#     selected = listbox.curselection()
#     if selected:
#         todo_list.remove_task(selected[0])
#         update_listbox(todo_list)
#     else:
#         messagebox.showwarning("Warning", "Select a task to delete")


# # ✅ Mark Complete
# def complete_task(todo_list):
#     selected = listbox.curselection()
#     if selected:
#         todo_list.mark_completed(selected[0])
#         update_listbox(todo_list)
#     else:
#         messagebox.showwarning("Warning", "Select a task")


# # ✏️ Edit Task (NEW FEATURE)
# def edit_task_ui(todo_list):
#     selected = listbox.curselection()

#     if not selected:
#         messagebox.showwarning("Warning", "Select a task to edit")
#         return

#     index = selected[0]

#     edit_window = Toplevel()
#     edit_window.title("Edit Task")

#     Label(edit_window, text="Edit Task:").pack(pady=5)

#     edit_entry = Entry(edit_window, width=40)
#     edit_entry.pack(pady=5)
#     edit_entry.insert(0, todo_list.tasks[index]["task"])

#     def save_edit():
#         new_text = edit_entry.get()

#         if new_text:
#             todo_list.edit_task(index, new_text)
#             update_listbox(todo_list)
#             edit_window.destroy()
#         else:
#             messagebox.showwarning("Warning", "Task cannot be empty")

#     Button(edit_window, text="Save Changes", command=save_edit).pack(pady=10)


# # 🔔 Reminder System
# def check_reminders(todo_list, root):
#     now = datetime.now().strftime("%Y-%m-%d %H:%M")

#     for task in todo_list.tasks:
#         if not task["completed"] and task["due_datetime"] == now:
#             messagebox.showinfo("Reminder", f"⏰ Task Due: {task['task']}")
#             task["completed"] = True

#     root.after(60000, check_reminders, todo_list, root)


# # 🎯 Main GUI
# def main():
#     global entry, time_entry, listbox

#     todo_list = TodoList()

#     root = Tk()
#     root.title("Todo App with Reminder")
#     root.geometry("500x450")

#     Label(root, text="Enter Task").pack(pady=5)
#     entry = Entry(root, width=40)
#     entry.pack(pady=5)

#     Label(root, text="Enter Time (HH:MM)").pack(pady=5)
#     time_entry = Entry(root, width=20)
#     time_entry.pack(pady=5)
#     time_entry.insert(0, "HH:MM")

#     Button(root, text="Add Task",
#            command=lambda: pick_date(todo_list)).pack(pady=5)

#     listbox = Listbox(root, width=60, height=12)
#     listbox.pack(pady=10)

#     Button(root, text="Mark Completed",
#            command=lambda: complete_task(todo_list)).pack(pady=2)

#     Button(root, text="Delete Task",
#            command=lambda: delete_task(todo_list)).pack(pady=2)

#     Button(root, text="Edit Task",
#            command=lambda: edit_task_ui(todo_list)).pack(pady=2)

#     Button(root, text="Save Tasks",
#            command=todo_list.save_tasks).pack(pady=5)

#     Button(root, text="Exit",
#            command=lambda: (todo_list.save_tasks(), root.destroy())).pack(pady=10)

#     update_listbox(todo_list)
#     check_reminders(todo_list, root)

#     root.mainloop()


# main()

"""Auto-Save and Restore
“Ensure all tasks are automatically saved when modified and reloaded when the app restarts (persistent data).”"""

# import csv
# from tkinter import *
# from tkinter import messagebox
# from tkcalendar import Calendar
# from datetime import datetime

# class TodoList:
#     def __init__(self):
#         self.tasks = []
#         self.file_name = "tasks.csv"
#         self.load_tasks()

#     def add_task(self, task, due_datetime):
#         self.tasks.append({
#             "task": task,
#             "completed": False,
#             "due_datetime": due_datetime
#         })
#         self.save_tasks()   # ✅ Auto-save

#     def remove_task(self, index):
#         if 0 <= index < len(self.tasks):
#             del self.tasks[index]
#             self.save_tasks()   # ✅ Auto-save

#     def mark_completed(self, index):
#         if 0 <= index < len(self.tasks):
#             self.tasks[index]["completed"] = True
#             self.save_tasks()   # ✅ Auto-save

#     def edit_task(self, index, new_task):
#         if 0 <= index < len(self.tasks):
#             self.tasks[index]["task"] = new_task
#             self.save_tasks()   # ✅ Auto-save

#     def save_tasks(self):
#         with open(self.file_name, mode='w', newline='') as file:
#             writer = csv.writer(file)
#             writer.writerow(["task", "status", "due_datetime"])

#             for t in self.tasks:
#                 writer.writerow([t["task"], t["completed"], t["due_datetime"]])

#     def load_tasks(self):
#         try:
#             with open(self.file_name, mode='r') as file:
#                 reader = csv.DictReader(file)
#                 self.tasks = []

#                 for row in reader:
#                     due = row.get("due_datetime") or row.get("due_date") or ""

#                     self.tasks.append({
#                         "task": row.get("task", ""),
#                         "completed": row.get("status", "False") == 'True',
#                         "due_datetime": due
#                     })
#         except FileNotFoundError:
#             pass


# # 📅 Calendar Picker
# def pick_date(todo_list):
#     def get_date():
#         selected_date = cal.get_date()
#         task = entry.get()
#         time_str = time_entry.get()

#         try:
#             due_datetime = datetime.strptime(
#                 selected_date + " " + time_str, "%m/%d/%y %H:%M"
#             )

#             if task:
#                 todo_list.add_task(task, due_datetime.strftime("%Y-%m-%d %H:%M"))
#                 update_listbox(todo_list)
#                 top.destroy()
#             else:
#                 messagebox.showwarning("Warning", "Enter a task first!")

#         except ValueError:
#             messagebox.showerror("Error", "Enter time in HH:MM format")

#     top = Toplevel()
#     top.title("Select Due Date")

#     cal = Calendar(top, selectmode='day')
#     cal.pack(pady=10)

#     Button(top, text="Confirm", command=get_date).pack(pady=10)


# # 🔄 Update Listbox
# def update_listbox(todo_list):
#     listbox.delete(0, END)

#     for i, t in enumerate(todo_list.tasks):
#         status = "✔" if t["completed"] else "✘"
#         listbox.insert(END, f"{i+1}. {t['task']} [{status}] ({t['due_datetime']})")


# # ❌ Delete Task
# def delete_task(todo_list):
#     selected = listbox.curselection()
#     if selected:
#         todo_list.remove_task(selected[0])
#         update_listbox(todo_list)
#     else:
#         messagebox.showwarning("Warning", "Select a task to delete")


# # ✅ Mark Complete
# def complete_task(todo_list):
#     selected = listbox.curselection()
#     if selected:
#         todo_list.mark_completed(selected[0])
#         update_listbox(todo_list)
#     else:
#         messagebox.showwarning("Warning", "Select a task")


# # ✏️ Edit Task
# def edit_task_ui(todo_list):
#     selected = listbox.curselection()

#     if not selected:
#         messagebox.showwarning("Warning", "Select a task to edit")
#         return

#     index = selected[0]

#     edit_window = Toplevel()
#     edit_window.title("Edit Task")

#     Label(edit_window, text="Edit Task:").pack(pady=5)

#     edit_entry = Entry(edit_window, width=40)
#     edit_entry.pack(pady=5)
#     edit_entry.insert(0, todo_list.tasks[index]["task"])

#     def save_edit():
#         new_text = edit_entry.get()

#         if new_text:
#             todo_list.edit_task(index, new_text)
#             update_listbox(todo_list)
#             edit_window.destroy()
#         else:
#             messagebox.showwarning("Warning", "Task cannot be empty")

#     Button(edit_window, text="Save Changes", command=save_edit).pack(pady=10)


# # 🔔 Reminder System
# def check_reminders(todo_list, root):
#     now = datetime.now().strftime("%Y-%m-%d %H:%M")

#     for task in todo_list.tasks:
#         if not task["completed"] and task["due_datetime"] == now:
#             messagebox.showinfo("Reminder", f"⏰ Task Due: {task['task']}")
#             task["completed"] = True
#             todo_list.save_tasks()   # ✅ Auto-save after reminder

#     root.after(60000, check_reminders, todo_list, root)


# # 🎯 Main GUI
# def main():
#     global entry, time_entry, listbox

#     todo_list = TodoList()

#     root = Tk()
#     root.title("Todo App with Auto-Save")
#     root.geometry("500x450")

#     Label(root, text="Enter Task").pack(pady=5)
#     entry = Entry(root, width=40)
#     entry.pack(pady=5)

#     Label(root, text="Enter Time (HH:MM)").pack(pady=5)
#     time_entry = Entry(root, width=20)
#     time_entry.pack(pady=5)
#     time_entry.insert(0, "HH:MM")

#     Button(root, text="Add Task",
#            command=lambda: pick_date(todo_list)).pack(pady=5)

#     listbox = Listbox(root, width=60, height=12)
#     listbox.pack(pady=10)

#     Button(root, text="Mark Completed",
#            command=lambda: complete_task(todo_list)).pack(pady=2)

#     Button(root, text="Delete Task",
#            command=lambda: delete_task(todo_list)).pack(pady=2)

#     Button(root, text="Edit Task",
#            command=lambda: edit_task_ui(todo_list)).pack(pady=2)

#     Button(root, text="Exit",
#            command=root.destroy).pack(pady=10)

#     update_listbox(todo_list)
#     check_reminders(todo_list, root)

#     root.mainloop()


# main()

"""
Clear All Tasks
“Add a ‘Clear All Tasks’ button that asks for confirmation before deleting all tasks.”"""

# import csv
# from tkinter import *
# from tkinter import messagebox
# from tkcalendar import Calendar
# from datetime import datetime

# class TodoList:
#     def __init__(self):
#         self.tasks = []
#         self.file_name = "tasks.csv"
#         self.load_tasks()

#     def add_task(self, task, due_datetime):
#         self.tasks.append({
#             "task": task,
#             "completed": False,
#             "due_datetime": due_datetime
#         })
#         self.save_tasks()

#     def remove_task(self, index):
#         if 0 <= index < len(self.tasks):
#             del self.tasks[index]
#             self.save_tasks()

#     def mark_completed(self, index):
#         if 0 <= index < len(self.tasks):
#             self.tasks[index]["completed"] = True
#             self.save_tasks()

#     def edit_task(self, index, new_task):
#         if 0 <= index < len(self.tasks):
#             self.tasks[index]["task"] = new_task
#             self.save_tasks()

#     def clear_all_tasks(self):
#         self.tasks.clear()
#         self.save_tasks()

#     def save_tasks(self):
#         with open(self.file_name, mode='w', newline='') as file:
#             writer = csv.writer(file)
#             writer.writerow(["task", "status", "due_datetime"])

#             for t in self.tasks:
#                 writer.writerow([t["task"], t["completed"], t["due_datetime"]])

#     def load_tasks(self):
#         try:
#             with open(self.file_name, mode='r') as file:
#                 reader = csv.DictReader(file)
#                 self.tasks = []

#                 for row in reader:
#                     due = row.get("due_datetime") or row.get("due_date") or ""

#                     self.tasks.append({
#                         "task": row.get("task", ""),
#                         "completed": row.get("status", "False") == 'True',
#                         "due_datetime": due
#                     })
#         except FileNotFoundError:
#             pass


# # 📅 Calendar Picker
# def pick_date(todo_list):
#     def get_date():
#         selected_date = cal.get_date()
#         task = entry.get()
#         time_str = time_entry.get()

#         try:
#             due_datetime = datetime.strptime(
#                 selected_date + " " + time_str, "%m/%d/%y %H:%M"
#             )

#             if task:
#                 todo_list.add_task(task, due_datetime.strftime("%Y-%m-%d %H:%M"))
#                 update_listbox(todo_list)
#                 top.destroy()
#             else:
#                 messagebox.showwarning("Warning", "Enter a task first!")

#         except ValueError:
#             messagebox.showerror("Error", "Enter time in HH:MM format")

#     top = Toplevel()
#     top.title("Select Due Date")

#     cal = Calendar(top, selectmode='day')
#     cal.pack(pady=10)

#     Button(top, text="Confirm", command=get_date).pack(pady=10)


# # 🔄 Update Listbox
# def update_listbox(todo_list):
#     listbox.delete(0, END)

#     for i, t in enumerate(todo_list.tasks):
#         status = "✔" if t["completed"] else "✘"
#         listbox.insert(END, f"{i+1}. {t['task']} [{status}] ({t['due_datetime']})")


# # ❌ Delete Task
# def delete_task(todo_list):
#     selected = listbox.curselection()
#     if selected:
#         todo_list.remove_task(selected[0])
#         update_listbox(todo_list)
#     else:
#         messagebox.showwarning("Warning", "Select a task to delete")


# # ✅ Mark Complete
# def complete_task(todo_list):
#     selected = listbox.curselection()
#     if selected:
#         todo_list.mark_completed(selected[0])
#         update_listbox(todo_list)
#     else:
#         messagebox.showwarning("Warning", "Select a task")


# # ✏️ Edit Task
# def edit_task_ui(todo_list):
#     selected = listbox.curselection()

#     if not selected:
#         messagebox.showwarning("Warning", "Select a task to edit")
#         return

#     index = selected[0]

#     edit_window = Toplevel()
#     edit_window.title("Edit Task")

#     Label(edit_window, text="Edit Task:").pack(pady=5)

#     edit_entry = Entry(edit_window, width=40)
#     edit_entry.pack(pady=5)
#     edit_entry.insert(0, todo_list.tasks[index]["task"])

#     def save_edit():
#         new_text = edit_entry.get()

#         if new_text:
#             todo_list.edit_task(index, new_text)
#             update_listbox(todo_list)
#             edit_window.destroy()
#         else:
#             messagebox.showwarning("Warning", "Task cannot be empty")

#     Button(edit_window, text="Save Changes", command=save_edit).pack(pady=10)


# # 🗑️ Clear All Tasks
# def clear_all_ui(todo_list):
#     confirm = messagebox.askyesno("Confirm", "Are you sure you want to delete ALL tasks?")

#     if confirm:
#         todo_list.clear_all_tasks()
#         update_listbox(todo_list)


# # 🔔 Reminder System
# def check_reminders(todo_list, root):
#     now = datetime.now().strftime("%Y-%m-%d %H:%M")

#     for task in todo_list.tasks:
#         if not task["completed"] and task["due_datetime"] == now:
#             messagebox.showinfo("Reminder", f"⏰ Task Due: {task['task']}")
#             task["completed"] = True
#             todo_list.save_tasks()

#     root.after(60000, check_reminders, todo_list, root)


# # 🎯 Main GUI
# def main():
#     global entry, time_entry, listbox

#     todo_list = TodoList()

#     root = Tk()
#     root.title("Todo App (Final Version)")
#     root.geometry("500x480")

#     Label(root, text="Enter Task").pack(pady=5)
#     entry = Entry(root, width=40)
#     entry.pack(pady=5)

#     Label(root, text="Enter Time (HH:MM)").pack(pady=5)
#     time_entry = Entry(root, width=20)
#     time_entry.pack(pady=5)
#     time_entry.insert(0, "HH:MM")

#     Button(root, text="Add Task",
#            command=lambda: pick_date(todo_list)).pack(pady=5)

#     listbox = Listbox(root, width=60, height=12)
#     listbox.pack(pady=10)

#     Button(root, text="Mark Completed",
#            command=lambda: complete_task(todo_list)).pack(pady=2)

#     Button(root, text="Delete Task",
#            command=lambda: delete_task(todo_list)).pack(pady=2)

#     Button(root, text="Edit Task",
#            command=lambda: edit_task_ui(todo_list)).pack(pady=2)

#     Button(root, text="Clear All Tasks",
#            command=lambda: clear_all_ui(todo_list)).pack(pady=5)

#     Button(root, text="Exit",
#            command=root.destroy).pack(pady=10)

#     update_listbox(todo_list)
#     check_reminders(todo_list, root)

#     root.mainloop()

# main()

"""Train Project"""

# import random

# # We start by importing the random module, which we'll use to generate random PNRs for the tickets later on.


# class Train():
#     def __init__(self, train_num, source, destination, seats,):
#         self.train_num = train_num
#         self.source = source
#         self.destination = destination
#         self.seats = seats

# #     We define the Train class, which takes in four parameter a train number, source, destination, and number of available seats. The __init__() method is called when a new Train object is created and initializes these attributes.

#     def display_info(self):
#         print(f"Train number: {self.train_num}")
#         print(f"Source: {self.source}")
#         print(f"Destination: {self.destination}")
#         print(f"Available seats: {self.seats}")
#         print()  # line break for each train information is displayed

# #     We define a display_info() method for the Train class, which displays the train number, source, destination, and number of available seats for a given train object.

#     def book_tickets(self, num_tickets):
#         if num_tickets > self.seats:
#             return None
#         else:
#             pnr_list = []
#             for i in range(num_tickets):
#                 pnr_list.append(random.randint(100000, 999999))
#             self.seats -= num_tickets
#             return pnr_list

# #     We define a book_tickets() method for the Train class, which takes a number of tickets as input and attempts to book that many tickets on the train. If there are enough available seats, the method generates a list of random PNRs equal to the number of tickets being booked, updates the number of available seats, and returns the list of PNRs. Otherwise, the method returns None to indicate that the booking failed.
# # The book_tickets method takes in the number of tickets to be booked and returns a list of PNR numbers for the tickets if they are available, or None if there are not enough seats.


# class Passenger:
#     def __init__(self, name, age, gender, phone):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.phone = phone
# # The Passenger class is defined, which takes in four parameters - name, age, gender, and phone. These parameters are used to initialize the attributes of the Passenger object.

#     def display_info(self):
#         print(f"Name: {self.name}")
#         print(f"Age: {self.age}")
#         print(f"Gender: {self.gender}")
#         print(f"Phone Number: {self.phone}")
# # The Passenger class has a method called display_info, which prints out the name, age, gender, and phone number of the passenger.


# class Ticket:
#     def __init__(self, train, source, destination, passengers, pnr):
#         self.train = train
#         self.source = source
#         self.destination = destination
#         self.passengers = passengers
#         self.pnr = pnr
# # The Ticket class is defined, which takes in five parameters - train, source, destination, passengers, and pnr. These parameters are used to initialize the attributes of the Ticket object.

#     def display_info(self):
#         print(f"Train Number: {self.train.train_num}")
#         print(f"Source: {self.source}")
#         print(f"Destination: {self.destination}")
#         print(f"PNR: {self.pnr}")
#         for passenger in self.passengers:
#             passenger.display_info()
#         print()
# # The Ticket class has a method called display_info, which prints out the train number, source, destination, PNR number, and the information of each passenger.


# class Account:

#     def __init__(self, username, password):
#         self.username = username
#         self.password = password

#     def check_password(self, password):
#         return self.password == password


# # Class called Account is defined with a constructor that takes two arguments: username and password. These arguments are used to initialize instance variables with the same names. The class also defines a method called check_password which takes a single argument password and returns a boolean indicating whether the input password matches the stored password.

# accounts = [
#     Account("user1", "password1"),
#     Account("user2", "password2")
# ]

# # A list called accounts is initialized with two Account objects already in it, with the usernames "user1" and "user2" and passwords "password1" and "password2" respectively.

# logged_in_account = None
# # A variable called logged_in_account is initialized to None. This variable will be used later to keep track of the currently logged-in account.

# while True:  # A while loop is started that will run indefinitely until the user logs in successfully and is presented with the available train details.
#     print("\n1. Create an account\n2. Login\n")
#     choice = input("Enter choice: ")
#     if choice == "1":
#         username = input("Enter username: ")
#         password = input("Enter password: ")
#         accounts.append(Account(username, password))
# # If the user chooses to create an account (choice == "1"), they are prompted to enter a username and password. The inputted username and password are then used to create a new Account object, which is appended to the accounts list.
#         print("Account created successfully!")
# # Inside the loop, the user is presented with two options: either to create an account or to login. The user's choice is stored in a variable called choice.
#     elif choice == "2":
#         username = input("Enter username: ")
#         password = input("Enter password: ")
#         for account in accounts:
#             if account.username == username and account.check_password(password):
#                 logged_in_account = account
#                 break
#         if logged_in_account is None:
#             print("Invalid username or password.")
# # If the user chooses to login (choice == "2"), they are prompted to enter a username and password. The program then iterates through the accounts list and checks if any of the stored accounts match the inputted username and password. If a match is found, the corresponding Account object is assigned to the logged_in_account variable and the loop is broken. Otherwise, an error message is printed.
#         else:
#             print(
#                 f"\nLogged in as {logged_in_account.username}\n\n-----Availabe Train details-----\n")

#             break
#     else:
#         print("Invalid choice.")

# if logged_in_account is not None:
#     trains = [
#         Train("12737", "Tadepalligudem", "Secunderabad", 40),
#         Train("12728", "Tadepalligudem", "Visakhapatnam", 50),
#         Train("22863", "Vijayawada", "Bangalore", 1),

        
#     ]
# # The program creates a list of Train objects, with each train having a unique train number, source, destination, and the number of seats available.

# # Display available trains
# for train in trains:
#     train.display_info()
# # If the logged_in_account variable is not None, it means that the user has successfully logged in. A message is printed confirming the login, and then a list of available train details is printed.


# # Get user input for booking
# while True:
#     try:
#         train_num = input("Enter Train Number: ")
#         num_tickets = int(input("Enter Number of Tickets: "))
#         if num_tickets <= 0:
#             raise ValueError("Number of tickets should be greater than 0")
#         for train in trains:
#             if train.train_num == train_num:
#                 if num_tickets > train.seats:
#                     raise ValueError(
#                         "Selected more tickets than available seats")  # If the number of tickets entered is more than the available seats, it will raise a ValueError with the message "Selected more tickets than available seats".
#                 break
#         else:
#             raise ValueError("Invalid Train Number.")
#         break
#     except ValueError as e:
#         print(f"Invalid Input: {e}")
# # The program asks the user to enter the train number and the number of tickets they want to book.

# train = None
# for t in trains:
#     if t.train_num == train_num:
#         train = t
#         break
# # The program then searches for the Train object with the corresponding train number entered by the user.

# if train is None:
#     print("Invalid Train Number.")
# # If the train number is invalid, the program prints "Invalid Train Number." and exits.

# else:
#     passengers = []
#     for i in range(num_tickets):
#         print(f"\nEnter details for Passenger {i + 1}:")
#         while True:
#             try:
#                 name = input("Name: ")
#                 if not name:
#                     raise ValueError("Name cannot be empty")
#                 age = int(input("Age: "))
#                 if age <= 0 or age > 120:
#                     raise ValueError("Invalid Age")
#                 gender = input("Gender: ")
#                 phone = input("Phone Number: ")
#                 if not phone or len(phone) != 10 or not phone.isdigit():
#                     raise ValueError("Invalid Phone Number")
#                 passenger = Passenger(name, age, gender, phone)
#                 passengers.append(passenger)
#                 break
#             except ValueError as e:
#                 print(f"Invalid Input: {e}")
# # If the train number is valid, the program prompts the user to enter the details of each passenger.
# # For each passenger, the program creates a Passenger object with the name, age, gender, and phone number entered by the user and appends it to a list of passengers.

#     pnr_list = train.book_tickets(num_tickets)
#     if pnr_list is None:
#         print("Tickets not available.")
# # The program then calls the book_tickets method of the Train object to book the tickets. If there are enough seats available, the book_tickets method returns a list of PNR numbers for the tickets, which the program saves in a list called pnr_list.
# # If there are not enough seats available, the book_tickets method returns None, and the program prints "Tickets not available." and exits.
#     else:
#         print("\n--------------Booking Successful!------------\n\nYour Ticket Details: \n")

#         for i in range(num_tickets):
#             ticket = Ticket(train, train.source, train.destination, [
#                             passengers[i]], pnr_list[i])
#             ticket.display_info()
#             print("\n--------Thank You------- \n-------Safe Journey------")

"""1. Berth Allocation:Add a feature to assign random berths (Lower, Middle, Upper) for each confirmed passenger."""

# import random


# class Train():
#     def __init__(self, train_num, source, destination, seats):
#         self.train_num = train_num
#         self.source = source
#         self.destination = destination
#         self.seats = seats

#     def display_info(self):
#         print(f"Train number: {self.train_num}")
#         print(f"Source: {self.source}")
#         print(f"Destination: {self.destination}")
#         print(f"Available seats: {self.seats}")
#         print()

#     def book_tickets(self, num_tickets):
#         if num_tickets > self.seats:
#             return None
#         else:
#             pnr_list = []
#             for i in range(num_tickets):
#                 pnr_list.append(random.randint(100000, 999999))
#             self.seats -= num_tickets
#             return pnr_list


# class Passenger:
#     def __init__(self, name, age, gender, phone, berth=None):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.phone = phone
#         self.berth = berth  # NEW

#     def display_info(self):
#         print(f"Name: {self.name}")
#         print(f"Age: {self.age}")
#         print(f"Gender: {self.gender}")
#         print(f"Phone Number: {self.phone}")
#         print(f"Berth: {self.berth}")  # NEW


# class Ticket:
#     def __init__(self, train, source, destination, passengers, pnr):
#         self.train = train
#         self.source = source
#         self.destination = destination
#         self.passengers = passengers
#         self.pnr = pnr

#     def display_info(self):
#         print(f"Train Number: {self.train.train_num}")
#         print(f"Source: {self.source}")
#         print(f"Destination: {self.destination}")
#         print(f"PNR: {self.pnr}")
#         for passenger in self.passengers:
#             passenger.display_info()
#         print()


# class Account:
#     def __init__(self, username, password):
#         self.username = username
#         self.password = password

#     def check_password(self, password):
#         return self.password == password


# accounts = [
#     Account("user1", "password1"),
#     Account("user2", "password2")
# ]

# logged_in_account = None

# # LOGIN / SIGNUP LOOP
# while True:
#     print("\n1. Create an account\n2. Login\n")
#     choice = input("Enter choice: ")

#     if choice == "1":
#         username = input("Enter username: ")
#         password = input("Enter password: ")
#         accounts.append(Account(username, password))
#         print("Account created successfully!")

#     elif choice == "2":
#         username = input("Enter username: ")
#         password = input("Enter password: ")

#         for account in accounts:
#             if account.username == username and account.check_password(password):
#                 logged_in_account = account
#                 break

#         if logged_in_account is None:
#             print("Invalid username or password.")
#         else:
#             print(f"\nLogged in as {logged_in_account.username}")
#             print("\n-----Available Train details-----\n")
#             break
#     else:
#         print("Invalid choice.")


# if logged_in_account is not None:
#     trains = [
#         Train("12737", "Tadepalligudem", "Secunderabad", 40),
#         Train("12728", "Tadepalligudem", "Visakhapatnam", 50),
#         Train("22863", "Vijayawada", "Bangalore", 1),
#     ]


# # DISPLAY TRAINS
# for train in trains:
#     train.display_info()


# # BOOKING INPUT
# while True:
#     try:
#         train_num = input("Enter Train Number: ")
#         num_tickets = int(input("Enter Number of Tickets: "))

#         if num_tickets <= 0:
#             raise ValueError("Number of tickets should be greater than 0")

#         for train in trains:
#             if train.train_num == train_num:
#                 if num_tickets > train.seats:
#                     raise ValueError("Selected more tickets than available seats")
#                 break
#         else:
#             raise ValueError("Invalid Train Number.")

#         break

#     except ValueError as e:
#         print(f"Invalid Input: {e}")


# # FIND TRAIN
# train = None
# for t in trains:
#     if t.train_num == train_num:
#         train = t
#         break

# if train is None:
#     print("Invalid Train Number.")

# else:
#     passengers = []
#     berths = ["Lower", "Middle", "Upper"]  # NEW

#     for i in range(num_tickets):
#         print(f"\nEnter details for Passenger {i + 1}:")
#         while True:
#             try:
#                 name = input("Name: ")
#                 if not name:
#                     raise ValueError("Name cannot be empty")

#                 age = int(input("Age: "))
#                 if age <= 0 or age > 120:
#                     raise ValueError("Invalid Age")

#                 gender = input("Gender: ")

#                 phone = input("Phone Number: ")
#                 if not phone or len(phone) != 10 or not phone.isdigit():
#                     raise ValueError("Invalid Phone Number")

#                 # ASSIGN RANDOM BERTH
#                 berth = random.choice(berths)

#                 passenger = Passenger(name, age, gender, phone, berth)
#                 passengers.append(passenger)
#                 break

#             except ValueError as e:
#                 print(f"Invalid Input: {e}")


#     pnr_list = train.book_tickets(num_tickets)

#     if pnr_list is None:
#         print("Tickets not available.")

#     else:
#         print("\n--------------Booking Successful!------------")
#         print("\nYour Ticket Details:\n")

#         for i in range(num_tickets):
#             ticket = Ticket(
#                 train,
#                 train.source,
#                 train.destination,
#                 [passengers[i]],
#                 pnr_list[i]
#             )
#             ticket.display_info()

#         print("--------Thank You-------")
#         print("-------Safe Journey------")

"""Create a waiting list that stores the PNR of passengers when seats are full.
Each waiting ticket should show status as ‘Waiting’.”"""

# import random


# class Train():
#     def __init__(self, train_num, source, destination, seats):
#         self.train_num = train_num
#         self.source = source
#         self.destination = destination
#         self.seats = seats
#         self.waiting_list = []   # NEW

#     def display_info(self):
#         print(f"Train number: {self.train_num}")
#         print(f"Source: {self.source}")
#         print(f"Destination: {self.destination}")
#         print(f"Available seats: {self.seats}")
#         print()

#     def book_tickets(self, num_tickets):
#         pnr_list = []
#         status_list = []

#         for _ in range(num_tickets):
#             pnr = random.randint(100000, 999999)

#             if self.seats > 0:
#                 self.seats -= 1
#                 status_list.append("Confirmed")
#             else:
#                 self.waiting_list.append(pnr)   # ADD TO WAITING
#                 status_list.append("Waiting")

#             pnr_list.append(pnr)

#         return pnr_list, status_list


# class Passenger:
#     def __init__(self, name, age, gender, phone, berth=None):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.phone = phone
#         self.berth = berth

#     def display_info(self):
#         print(f"Name: {self.name}")
#         print(f"Age: {self.age}")
#         print(f"Gender: {self.gender}")
#         print(f"Phone Number: {self.phone}")
#         print(f"Berth: {self.berth}")


# class Ticket:
#     def __init__(self, train, source, destination, passengers, pnr, status):
#         self.train = train
#         self.source = source
#         self.destination = destination
#         self.passengers = passengers
#         self.pnr = pnr
#         self.status = status   # NEW

#     def display_info(self):
#         print(f"Train Number: {self.train.train_num}")
#         print(f"Source: {self.source}")
#         print(f"Destination: {self.destination}")
#         print(f"PNR: {self.pnr}")
#         print(f"Status: {self.status}")   # NEW
#         for passenger in self.passengers:
#             passenger.display_info()
#         print()


# class Account:
#     def __init__(self, username, password):
#         self.username = username
#         self.password = password

#     def check_password(self, password):
#         return self.password == password


# accounts = [
#     Account("user1", "password1"),
#     Account("user2", "password2")
# ]

# logged_in_account = None

# # LOGIN / SIGNUP
# while True:
#     print("\n1. Create an account\n2. Login\n")
#     choice = input("Enter choice: ")

#     if choice == "1":
#         username = input("Enter username: ")
#         password = input("Enter password: ")
#         accounts.append(Account(username, password))
#         print("Account created successfully!")

#     elif choice == "2":
#         username = input("Enter username: ")
#         password = input("Enter password: ")

#         for account in accounts:
#             if account.username == username and account.check_password(password):
#                 logged_in_account = account
#                 break

#         if logged_in_account is None:
#             print("Invalid username or password.")
#         else:
#             print(f"\nLogged in as {logged_in_account.username}")
#             print("\n-----Available Train details-----\n")
#             break
#     else:
#         print("Invalid choice.")


# if logged_in_account is not None:
#     trains = [
#         Train("12737", "Tadepalligudem", "Secunderabad", 2),
#         Train("12728", "Tadepalligudem", "Visakhapatnam", 2),
#         Train("22863", "Vijayawada", "Bangalore", 1),
#     ]


# # DISPLAY TRAINS
# for train in trains:
#     train.display_info()


# # BOOKING INPUT
# while True:
#     try:
#         train_num = input("Enter Train Number: ")
#         num_tickets = int(input("Enter Number of Tickets: "))

#         if num_tickets <= 0:
#             raise ValueError("Number of tickets should be greater than 0")

#         for train in trains:
#             if train.train_num == train_num:
#                 break
#         else:
#             raise ValueError("Invalid Train Number.")

#         break

#     except ValueError as e:
#         print(f"Invalid Input: {e}")


# # FIND TRAIN
# train = None
# for t in trains:
#     if t.train_num == train_num:
#         train = t
#         break

# if train is None:
#     print("Invalid Train Number.")

# else:
#     passengers = []
#     berths = ["Lower", "Middle", "Upper"]

#     for i in range(num_tickets):
#         print(f"\nEnter details for Passenger {i + 1}:")
#         while True:
#             try:
#                 name = input("Name: ")
#                 if not name:
#                     raise ValueError("Name cannot be empty")

#                 age = int(input("Age: "))
#                 if age <= 0 or age > 120:
#                     raise ValueError("Invalid Age")

#                 gender = input("Gender: ")

#                 phone = input("Phone Number: ")
#                 if not phone or len(phone) != 10 or not phone.isdigit():
#                     raise ValueError("Invalid Phone Number")

#                 berth = random.choice(berths)

#                 passenger = Passenger(name, age, gender, phone, berth)
#                 passengers.append(passenger)
#                 break

#             except ValueError as e:
#                 print(f"Invalid Input: {e}")


#     # BOOK TICKETS (UPDATED)
#     pnr_list, status_list = train.book_tickets(num_tickets)

#     print("\n--------------Booking Result------------")
#     print("\nYour Ticket Details:\n")

#     for i in range(num_tickets):
#         ticket = Ticket(
#             train,
#             train.source,
#             train.destination,
#             [passengers[i]],
#             pnr_list[i],
#             status_list[i]
#         )
#         ticket.display_info()

#     print("--------Thank You-------")
#     print("-------Safe Journey------")

"""Modify your code to take journey date and time from the user."""

# import random


# class Train():
#     def __init__(self, train_num, source, destination, seats):
#         self.train_num = train_num
#         self.source = source
#         self.destination = destination
#         self.seats = seats
#         self.waiting_list = []

#     def display_info(self):
#         print(f"Train number: {self.train_num}")
#         print(f"Source: {self.source}")
#         print(f"Destination: {self.destination}")
#         print(f"Available seats: {self.seats}")
#         print()

#     def book_tickets(self, num_tickets):
#         pnr_list = []
#         status_list = []

#         for _ in range(num_tickets):
#             pnr = random.randint(100000, 999999)

#             if self.seats > 0:
#                 self.seats -= 1
#                 status_list.append("Confirmed")
#             else:
#                 self.waiting_list.append(pnr)
#                 status_list.append("Waiting")

#             pnr_list.append(pnr)

#         return pnr_list, status_list


# class Passenger:
#     def __init__(self, name, age, gender, phone, berth=None):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.phone = phone
#         self.berth = berth

#     def display_info(self):
#         print(f"Name: {self.name}")
#         print(f"Age: {self.age}")
#         print(f"Gender: {self.gender}")
#         print(f"Phone Number: {self.phone}")
#         print(f"Berth: {self.berth}")


# class Ticket:
#     def __init__(self, train, source, destination, passengers, pnr, status, journey_date, journey_time):
#         self.train = train
#         self.source = source
#         self.destination = destination
#         self.passengers = passengers
#         self.pnr = pnr
#         self.status = status
#         self.journey_date = journey_date
#         self.journey_time = journey_time

#     def display_info(self):
#         print(f"Train Number: {self.train.train_num}")
#         print(f"Source: {self.source}")
#         print(f"Destination: {self.destination}")
#         print(f"Journey Date: {self.journey_date}")
#         print(f"Journey Time: {self.journey_time}")
#         print(f"PNR: {self.pnr}")
#         print(f"Status: {self.status}")
#         for passenger in self.passengers:
#             passenger.display_info()
#         print()


# class Account:
#     def __init__(self, username, password):
#         self.username = username
#         self.password = password

#     def check_password(self, password):
#         return self.password == password


# accounts = [
#     Account("user1", "password1"),
#     Account("user2", "password2")
# ]

# logged_in_account = None

# # LOGIN / SIGNUP
# while True:
#     print("\n1. Create an account\n2. Login\n")
#     choice = input("Enter choice: ")

#     if choice == "1":
#         username = input("Enter username: ")
#         password = input("Enter password: ")
#         accounts.append(Account(username, password))
#         print("Account created successfully!")

#     elif choice == "2":
#         username = input("Enter username: ")
#         password = input("Enter password: ")

#         for account in accounts:
#             if account.username == username and account.check_password(password):
#                 logged_in_account = account
#                 break

#         if logged_in_account is None:
#             print("Invalid username or password.")
#         else:
#             print(f"\nLogged in as {logged_in_account.username}")
#             print("\n-----Available Train details-----\n")
#             break
#     else:
#         print("Invalid choice.")


# if logged_in_account is not None:
#     trains = [
#         Train("12737", "Tadepalligudem", "Secunderabad", 2),
#         Train("12728", "Tadepalligudem", "Visakhapatnam", 2),
#         Train("22863", "Vijayawada", "Bangalore", 1),
#     ]


# # DISPLAY TRAINS
# for train in trains:
#     train.display_info()


# # BOOKING INPUT
# while True:
#     try:
#         train_num = input("Enter Train Number: ")
#         num_tickets = int(input("Enter Number of Tickets: "))

#         if num_tickets <= 0:
#             raise ValueError("Number of tickets should be greater than 0")

#         for train in trains:
#             if train.train_num == train_num:
#                 break
#         else:
#             raise ValueError("Invalid Train Number.")

#         break

#     except ValueError as e:
#         print(f"Invalid Input: {e}")


# # JOURNEY DATE & TIME INPUT (NEW)
# while True:
#     try:
#         journey_date = input("Enter Journey Date (DD-MM-YYYY): ")
#         journey_time = input("Enter Journey Time (HH:MM): ")

#         if not journey_date or not journey_time:
#             raise ValueError("Date and Time cannot be empty")

#         break
#     except ValueError as e:
#         print(f"Invalid Input: {e}")


# # FIND TRAIN
# train = None
# for t in trains:
#     if t.train_num == train_num:
#         train = t
#         break

# if train is None:
#     print("Invalid Train Number.")

# else:
#     passengers = []
#     berths = ["Lower", "Middle", "Upper"]

#     for i in range(num_tickets):
#         print(f"\nEnter details for Passenger {i + 1}:")
#         while True:
#             try:
#                 name = input("Name: ")
#                 if not name:
#                     raise ValueError("Name cannot be empty")

#                 age = int(input("Age: "))
#                 if age <= 0 or age > 120:
#                     raise ValueError("Invalid Age")

#                 gender = input("Gender: ")

#                 phone = input("Phone Number: ")
#                 if not phone or len(phone) != 10 or not phone.isdigit():
#                     raise ValueError("Invalid Phone Number")

#                 berth = random.choice(berths)

#                 passenger = Passenger(name, age, gender, phone, berth)
#                 passengers.append(passenger)
#                 break

#             except ValueError as e:
#                 print(f"Invalid Input: {e}")


#     # BOOK TICKETS
#     pnr_list, status_list = train.book_tickets(num_tickets)

#     print("\n--------------Booking Result------------")
#     print("\nYour Ticket Details:\n")

#     for i in range(num_tickets):
#         ticket = Ticket(
#             train,
#             train.source,
#             train.destination,
#             [passengers[i]],
#             pnr_list[i],
#             status_list[i],
#             journey_date,
#             journey_time
#         )
#         ticket.display_info()

#     print("--------Thank You-------")
#     print("-------Safe Journey------")

"""Bank Project"""

# class Account:
#     def __init__(self, username, password, balance=0,):

#         self.username = username
#         self.password = password
#         self.balance = balance
# # the Account class is defined with three instance variables - username, password, and balance. The __init__ method initializes these variables with the arguments passed while creating an object of this class. The class also contains four methods - deposit, withdraw, get_balance, and get_mini_statement.

#     def deposit(self, amount):

#         self.balance += amount
#         print(f"\nAmount deposited: {amount}\nTotal Balance: {self.balance}")
# # The deposit method takes an argument amount and adds it to the balance variable. It then prints a message showing the deposited amount and the updated balance.

#     def withdraw(self, amount):
#         if self.balance >= amount:
#             self.balance -= amount
#             print(
#                 f"\nAmount withdrawn: {amount}\nRemaing Balance: {self.balance}")
#         else:
#             print("Insufficient balance")
# # The withdraw method takes an argument amount and checks if the balance is greater than or equal to the amount to be withdrawn. If it is, it deducts the withdrawn amount from the balance and prints a message showing the withdrawn amount and the updated balance. If not, it prints a message saying that there is insufficient balance.

#     def get_balance(self):
#         return self.balance
# # The get_balance method simply returns the current balance.

#     def get_mini_statement(self):
#         print("Mini statement:")
#         print(f"Username: {self.username}")
#         print(f"Current balance: {self.balance}")
# # The get_mini_statement method prints the username and current balance of the account.


# class BankingSystem:
#     def __init__(self):
#         self.accounts = {}
# # the BankingSystem class is defined. It has one instance variable - accounts - which is a dictionary that stores the username as key and the Account object as value.

#     def create_account(self, username, password):
#         if username in self.accounts:
#             print("Username already exists")
#         else:
#             self.accounts[username] = Account(username, password)
#             print("\nAccount created successfully")
#             print("-------Welcome to PYTHON Bank-------")
# # The create_account method takes two arguments - username and password. It checks if the username already exists in the accounts dictionary. If it does, it prints a message saying that the username already exists. If it does not, it creates a new Account object with the given username and password and adds it to the accounts dictionary. It then prints a message saying that the account was created successfully.

#     def login(self, username, password):
#         if username in self.accounts:
#             account = self.accounts[username]
#             if account.password == password:
#                 print("Login Sucess....")
#                 return account
#             else:
#                 print("Invalid password")
#         else:
#             print("Invalid username")
#         return None
# # The login method takes two arguments - username and password. It checks if the given username exists in the accounts dictionary. If it does, it retrieves the corresponding Account object and checks if the given password matches the password of that account. If it does, it prints a message saying that the login was successful and returns the Account object. If it does not, it prints a message saying that the password is invalid. If the given username is not found in the accounts dictionary, it prints a message saying that the username is invalid.


# bank = BankingSystem()

# while True:
#     print("\n")
#     print("1. Create account")
#     print("2. Login")
#     print("3. Exit")
#     choice = input("Enter your choice (1-3): ")
# # the main program loop is defined inside the if __name__ == '__main__': block. It creates a new BankingSystem object and presents a menu of options to the user - create an account, login, or exit.
#     if choice == '1':
#         username = input("Enter username: ")
#         password = input("Enter password: ")
#         bank.create_account(username, password)
# # If the user chooses to create an account, the program prompts the user to enter a username and password. It then calls the create_account method of the BankingSystem object with these arguments.

#     elif choice == '2':
#         username = input("Enter username: ")
#         password = input("Enter password: ")
#         account = bank.login(username, password)
#         if account is not None:
#             while True:
#                 print("\n-----Welcome to PYTHON Bank-----")
#                 print("1. Deposit")
#                 print("2. Withdraw")
#                 print("3. Check balance")
#                 print("4. Mini statement")
#                 print("5. Logout\n")
#                 choice = input("Enter your choice (1-5): ")
# # If the user chooses to login, the program prompts the user to enter their username and password. It then calls the login method of the BankingSystem object with these arguments. If the login is successful, it presents the user with a menu of options - deposit, withdraw, check balance, print mini-statement, or logout.

#                 if choice == '1':
#                     amount = int(input("Enter amount to deposit: "))
#                     account.deposit(amount)

#                 elif choice == '2':
#                     amount = int(input("Enter amount to withdraw: "))
#                     account.withdraw(amount)
# # If the user chooses to deposit or withdraw, the program prompts the user to enter the amount to deposit or withdraw. It then calls the corresponding method of the Account object.

#                 elif choice == '3':
#                     print(f"Current balance: {account.get_balance()}")
# # If the user chooses to check their balance, the program calls the get_balance method of the Account object and prints the current balance.

#                 elif choice == '4':
#                     account.get_mini_statement()
# # If the user chooses to print a mini-statement, the program calls the get_mini_statement method of the Account object and prints the username and current balance.

#                 elif choice == '5':
#                     print("\n--------THANK YOU VISIT AGAIN--------")
#                     break
# # If the user chooses to logout, break out of the inner WHILE loop and display a message saying "THANK YOU VISIT AGAIN".
#                 else:
#                     print("Invalid choice")
#     elif choice == '3':
#         print("\n------THANK YOU------")
#         break
# # If the user selects option 3, a message is printed indicating that they have exited the program, and the break statement is used to exit the outer while loop that displays the main menu.

#     else:
#         print("Invalid choice")


"""Add a feature to store all account details(username, password, balance, and transaction history) in a CSV file so that data is not lost when the app closes."""

# import csv
# import os


# class Account:
#     def __init__(self, username, password, balance=0, transactions=None):
#         self.username = username
#         self.password = password
#         self.balance = balance
#         self.transactions = transactions if transactions else []

#     def deposit(self, amount):
#         self.balance += amount
#         self.transactions.append(f"Deposit:{amount}")
#         print(f"\nAmount deposited: {amount}\nTotal Balance: {self.balance}")

#     def withdraw(self, amount):
#         if self.balance >= amount:
#             self.balance -= amount
#             self.transactions.append(f"Withdraw:{amount}")
#             print(f"\nAmount withdrawn: {amount}\nRemaining Balance: {self.balance}")
#         else:
#             print("Insufficient balance")

#     def get_balance(self):
#         return self.balance

#     def get_mini_statement(self):
#         print("\nMini statement:")
#         print(f"Username: {self.username}")
#         print(f"Current balance: {self.balance}")
#         print("Transactions:")
#         for t in self.transactions:
#             print(f" - {t}")


# class BankingSystem:
#     def __init__(self):
#         self.accounts = {}
#         self.file_name = "accounts.csv"
#         self.load_accounts()   # LOAD DATA ON START

#     # SAVE ALL ACCOUNTS
#     def save_accounts(self):
#         with open(self.file_name, mode='w', newline='') as file:
#             writer = csv.writer(file)
#             writer.writerow(["username", "password", "balance", "transactions"])

#             for acc in self.accounts.values():
#                 transactions_str = "|".join(acc.transactions)
#                 writer.writerow([acc.username, acc.password, acc.balance, transactions_str])

#     # LOAD ALL ACCOUNTS
#     def load_accounts(self):
#         if not os.path.exists(self.file_name):
#             return

#         with open(self.file_name, mode='r') as file:
#             reader = csv.DictReader(file)
#             for row in reader:
#                 transactions = row["transactions"].split("|") if row["transactions"] else []
#                 account = Account(
#                     row["username"],
#                     row["password"],
#                     int(row["balance"]),
#                     transactions
#                 )
#                 self.accounts[row["username"]] = account

#     def create_account(self, username, password):
#         if username in self.accounts:
#             print("Username already exists")
#         else:
#             self.accounts[username] = Account(username, password)
#             self.save_accounts()   # SAVE
#             print("\nAccount created successfully")
#             print("-------Welcome to PYTHON Bank-------")

#     def login(self, username, password):
#         if username in self.accounts:
#             account = self.accounts[username]
#             if account.password == password:
#                 print("Login Success....")
#                 return account
#             else:
#                 print("Invalid password")
#         else:
#             print("Invalid username")
#         return None


# bank = BankingSystem()

# while True:
#     print("\n1. Create account")
#     print("2. Login")
#     print("3. Exit")
#     choice = input("Enter your choice (1-3): ")

#     if choice == '1':
#         username = input("Enter username: ")
#         password = input("Enter password: ")
#         bank.create_account(username, password)

#     elif choice == '2':
#         username = input("Enter username: ")
#         password = input("Enter password: ")
#         account = bank.login(username, password)

#         if account is not None:
#             while True:
#                 print("\n-----Welcome to PYTHON Bank-----")
#                 print("1. Deposit")
#                 print("2. Withdraw")
#                 print("3. Check balance")
#                 print("4. Mini statement")
#                 print("5. Logout\n")

#                 choice = input("Enter your choice (1-5): ")

#                 if choice == '1':
#                     amount = int(input("Enter amount to deposit: "))
#                     account.deposit(amount)
#                     bank.save_accounts()   # SAVE AFTER CHANGE

#                 elif choice == '2':
#                     amount = int(input("Enter amount to withdraw: "))
#                     account.withdraw(amount)
#                     bank.save_accounts()   # SAVE AFTER CHANGE

#                 elif choice == '3':
#                     print(f"Current balance: {account.get_balance()}")

#                 elif choice == '4':
#                     account.get_mini_statement()

#                 elif choice == '5':
#                     print("\n--------THANK YOU VISIT AGAIN--------")
#                     break

#                 else:
#                     print("Invalid choice")

#     elif choice == '3':
#         print("\n------THANK YOU------")
#         break

#     else:
#         print("Invalid choice")


"""Make sure multiple users can log in, perform transactions, and view only their own mini statements."""
"""Add a checkbox on the login screen to toggle password visibility (show/hide password)."""

# import csv
# import os
# import tkinter as tk
# from tkinter import messagebox


# # ---------------- ACCOUNT CLASS ----------------
# class Account:
#     def __init__(self, username, password, balance=0, transactions=None):
#         self.username = username
#         self.password = password
#         self.balance = balance
#         self.transactions = transactions if transactions else []

#     def deposit(self, amount):
#         self.balance += amount
#         self.transactions.append(f"Deposit:{amount}")

#     def withdraw(self, amount):
#         if self.balance >= amount:
#             self.balance -= amount
#             self.transactions.append(f"Withdraw:{amount}")
#         else:
#             raise ValueError("Insufficient balance")


# # ---------------- BANKING SYSTEM ----------------
# class BankingSystem:
#     def __init__(self):
#         self.accounts = {}
#         self.file_name = "accounts.csv"
#         self.load_accounts()

#     def save_accounts(self):
#         with open(self.file_name, mode='w', newline='') as file:
#             writer = csv.writer(file)
#             writer.writerow(["username", "password", "balance", "transactions"])

#             for acc in self.accounts.values():
#                 transactions_str = "|".join(acc.transactions)
#                 writer.writerow([acc.username, acc.password, acc.balance, transactions_str])

#     def load_accounts(self):
#         if not os.path.exists(self.file_name):
#             return

#         with open(self.file_name, mode='r') as file:
#             reader = csv.DictReader(file)
#             for row in reader:
#                 transactions = row["transactions"].split("|") if row["transactions"] else []
#                 account = Account(
#                     row["username"],
#                     row["password"],
#                     int(row["balance"]),
#                     transactions
#                 )
#                 self.accounts[row["username"]] = account

#     def create_account(self, username, password):
#         if username in self.accounts:
#             return False
#         self.accounts[username] = Account(username, password)
#         self.save_accounts()
#         return True

#     def login(self, username, password):
#         if username in self.accounts:
#             acc = self.accounts[username]
#             if acc.password == password:
#                 return acc   # IMPORTANT: return specific user object
#         return None


# bank = BankingSystem()


# # ---------------- GUI ----------------
# def toggle_password():
#     entry_password.config(show="" if show_var.get() else "*")


# def login():
#     username = entry_username.get()
#     password = entry_password.get()

#     account = bank.login(username, password)

#     if account:
#         messagebox.showinfo("Success", f"Welcome {username}")
#         open_dashboard(account)   # PASS USER OBJECT
#     else:
#         messagebox.showerror("Error", "Invalid Username or Password")


# def create_account():
#     username = entry_username.get()
#     password = entry_password.get()

#     if bank.create_account(username, password):
#         messagebox.showinfo("Success", "Account Created Successfully")
#     else:
#         messagebox.showerror("Error", "Username already exists")


# # ---------------- DASHBOARD ----------------
# def open_dashboard(account):
#     dash = tk.Toplevel(root)
#     dash.title(f"{account.username} Dashboard")
#     dash.geometry("320x320")

#     def deposit():
#         try:
#             amt = int(entry_amount.get())
#             account.deposit(amt)
#             bank.save_accounts()
#             messagebox.showinfo("Success", f"Deposited {amt}")
#         except:
#             messagebox.showerror("Error", "Invalid amount")

#     def withdraw():
#         try:
#             amt = int(entry_amount.get())
#             account.withdraw(amt)
#             bank.save_accounts()
#             messagebox.showinfo("Success", f"Withdrawn {amt}")
#         except Exception as e:
#             messagebox.showerror("Error", str(e))

#     def show_balance():
#         messagebox.showinfo("Balance", f"Balance: {account.balance}")

#     def mini_statement():
#         if account.transactions:
#             statement = "\n".join(account.transactions)
#         else:
#             statement = "No transactions yet"
#         messagebox.showinfo(f"{account.username} Statement", statement)

#     def logout():
#         dash.destroy()

#     tk.Label(dash, text=f"Welcome {account.username}", font=("Arial", 12)).pack(pady=10)

#     entry_amount = tk.Entry(dash)
#     entry_amount.pack(pady=5)

#     tk.Button(dash, text="Deposit", command=deposit).pack(pady=5)
#     tk.Button(dash, text="Withdraw", command=withdraw).pack(pady=5)
#     tk.Button(dash, text="Check Balance", command=show_balance).pack(pady=5)
#     tk.Button(dash, text="Mini Statement", command=mini_statement).pack(pady=5)
#     tk.Button(dash, text="Logout", command=logout).pack(pady=10)


# # ---------------- LOGIN WINDOW ----------------
# root = tk.Tk()
# root.title("Python Bank Login")
# root.geometry("300x250")

# tk.Label(root, text="Username").pack()
# entry_username = tk.Entry(root)
# entry_username.pack()

# tk.Label(root, text="Password").pack()
# entry_password = tk.Entry(root, show="*")
# entry_password.pack()

# show_var = tk.BooleanVar()
# tk.Checkbutton(root, text="Show Password", variable=show_var, command=toggle_password).pack()

# tk.Button(root, text="Login", command=login).pack(pady=5)
# tk.Button(root, text="Create Account", command=create_account).pack()

# root.mainloop()

"""“Add a feature to calculate and show interest (e.g., 5% annual rate) based on the current balance.”"""

import csv
import os
import tkinter as tk
from tkinter import messagebox


# ---------------- ACCOUNT CLASS ----------------
class Account:
    def __init__(self, username, password, balance=0, transactions=None):
        self.username = username
        self.password = password
        self.balance = balance
        self.transactions = transactions if transactions else []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposit:{amount}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transactions.append(f"Withdraw:{amount}")
        else:
            raise ValueError("Insufficient balance")

    def calculate_interest(self, rate=5, time=1):
        return (self.balance * rate * time) / 100

    def add_interest(self, rate=5, time=1):
        interest = self.calculate_interest(rate, time)
        self.balance += interest
        self.transactions.append(f"Interest Added:{interest}")
        return interest


# ---------------- BANKING SYSTEM ----------------
class BankingSystem:
    def __init__(self):
        self.accounts = {}
        self.file_name = "accounts.csv"
        self.load_accounts()

    def save_accounts(self):
        with open(self.file_name, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["username", "password", "balance", "transactions"])

            for acc in self.accounts.values():
                transactions_str = "|".join(acc.transactions)
                writer.writerow([acc.username, acc.password, acc.balance, transactions_str])

    def load_accounts(self):
        if not os.path.exists(self.file_name):
            return

        with open(self.file_name, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                transactions = row["transactions"].split("|") if row["transactions"] else []
                account = Account(
                    row["username"],
                    row["password"],
                    float(row["balance"]),
                    transactions
                )
                self.accounts[row["username"]] = account

    def create_account(self, username, password):
        if username in self.accounts:
            return False
        self.accounts[username] = Account(username, password)
        self.save_accounts()
        return True

    def login(self, username, password):
        if username in self.accounts:
            acc = self.accounts[username]
            if acc.password == password:
                return acc
        return None


bank = BankingSystem()


# ---------------- GUI FUNCTIONS ----------------
def toggle_password():
    entry_password.config(show="" if show_var.get() else "*")


def login():
    username = entry_username.get()
    password = entry_password.get()

    account = bank.login(username, password)
    if account:
        messagebox.showinfo("Success", f"Welcome {username}")
        open_dashboard(account)
    else:
        messagebox.showerror("Error", "Invalid Username or Password")


def create_account():
    username = entry_username.get()
    password = entry_password.get()

    if bank.create_account(username, password):
        messagebox.showinfo("Success", "Account Created Successfully")
    else:
        messagebox.showerror("Error", "Username already exists")


# ---------------- DASHBOARD ----------------
def open_dashboard(account):
    dash = tk.Toplevel(root)
    dash.title(f"{account.username} Dashboard")
    dash.geometry("350x400")

    def deposit():
        try:
            amt = float(entry_amount.get())
            account.deposit(amt)
            bank.save_accounts()
            messagebox.showinfo("Success", f"Deposited ₹{amt}")
        except:
            messagebox.showerror("Error", "Invalid amount")

    def withdraw():
        try:
            amt = float(entry_amount.get())
            account.withdraw(amt)
            bank.save_accounts()
            messagebox.showinfo("Success", f"Withdrawn ₹{amt}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def show_balance():
        messagebox.showinfo("Balance", f"Balance: ₹{account.balance}")

    def mini_statement():
        if account.transactions:
            statement = "\n".join(account.transactions)
        else:
            statement = "No transactions yet"
        messagebox.showinfo("Mini Statement", statement)

    def show_interest():
        interest = account.calculate_interest()
        messagebox.showinfo("Interest", f"Interest (5% yearly): ₹{interest}")

    def apply_interest():
        interest = account.add_interest()
        bank.save_accounts()
        messagebox.showinfo("Success", f"₹{interest} added as interest")

    def logout():
        dash.destroy()

    tk.Label(dash, text=f"Welcome {account.username}", font=("Arial", 12)).pack(pady=10)

    entry_amount = tk.Entry(dash)
    entry_amount.pack(pady=5)

    tk.Button(dash, text="Deposit", command=deposit).pack(pady=5)
    tk.Button(dash, text="Withdraw", command=withdraw).pack(pady=5)
    tk.Button(dash, text="Check Balance", command=show_balance).pack(pady=5)
    tk.Button(dash, text="Mini Statement", command=mini_statement).pack(pady=5)

    # NEW INTEREST FEATURES
    tk.Button(dash, text="Calculate Interest", command=show_interest).pack(pady=5)
    tk.Button(dash, text="Add Interest to Balance", command=apply_interest).pack(pady=5)

    tk.Button(dash, text="Logout", command=logout).pack(pady=10)


# ---------------- LOGIN WINDOW ----------------
root = tk.Tk()
root.title("Python Bank Login")
root.geometry("300x250")

tk.Label(root, text="Username").pack()
entry_username = tk.Entry(root)
entry_username.pack()

tk.Label(root, text="Password").pack()
entry_password = tk.Entry(root, show="*")
entry_password.pack()

show_var = tk.BooleanVar()
tk.Checkbutton(root, text="Show Password", variable=show_var, command=toggle_password).pack()

tk.Button(root, text="Login", command=login).pack(pady=5)
tk.Button(root, text="Create Account", command=create_account).pack()

root.mainloop()
