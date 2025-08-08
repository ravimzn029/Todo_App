# 📝 To-Do App (Python CLI)

A simple **Command-Line To-Do List** application built in Python using **file handling**.
This app lets you **add**, **view**, and **delete** tasks from your to-do list, all stored in a local file (`todo.txt`).

---

## 📌 Features

* **View Tasks** – Displays all saved tasks with numbering.
* **Add Task** – Lets you add a new task to the list.
* **Delete Task** – Removes a task by its number.
* **Data Persistence** – Tasks are stored in `todo.txt` so they remain after closing the app.

---

## 🛠️ Technologies Used

* Python 3
* File Handling (`open`, `readlines`, `writelines`)

---

## 📂 Project Structure

```
.
├── todo.py      # Main application script
├── todo.txt     # Stores the list of tasks (auto-created if missing)
└── README.md    # Project documentation
```

---

## ▶️ How to Run

1. **Clone this repository**

   ```bash
   git clone https://github.com/your-username/todo-app.git
   cd todo-app
   ```

2. **Run the script**

   ```bash
   python todo.py
   ```

---

## 📋 Usage

When you run the program, you'll see this menu:

```
====== TO-DO APP ======
1. View Tasks
2. Add Task
3. Delete Task
4. Exit
```

**Example:**

```
Enter your choice (1-4): 2
Enter new task: Buy groceries
Task added successfully!
```

---

## 🗑️ Delete Tasks

When deleting, enter the task number shown in the list:

```
1. Buy groceries
2. Finish homework
Enter task number to delete: 1
Task 'Buy groceries' deleted!
```

---

## 📌 Notes

* The file `todo.txt` will be automatically created when you add your first task.
* Make sure you run the app in the same folder where `todo.txt` is located.

---

## 📜 License

This project is open-source and free to use.


