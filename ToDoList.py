"""
Simple To-Do List Application with Tkinter GUI
A desktop application for managing daily tasks with persistent storage.
"""

import tkinter as tk
from tkinter import messagebox, scrolledtext
import json
import os
from datetime import datetime


class ToDoApp:
    """Main To-Do List application class"""

    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Manager")
        self.root.geometry("500x700+300+50")
        self.root.resizable(False, False)
        
        # Configure style
        self.root.config(bg="#f0f0f0")
        
        self.task_list = []
        self.tasks_file = "tasks.json"
        
        self.setup_ui()
        self.load_tasks()

    def setup_ui(self):
        """Setup the user interface"""
        # Header
        header_frame = tk.Frame(self.root, bg="#4f46e5", height=80)
        header_frame.pack(fill=tk.X)
        header_frame.pack_propagate(False)
        
        title_label = tk.Label(
            header_frame, 
            text="My Tasks", 
            font=("Arial", 24, "bold"),
            fg="white",
            bg="#4f46e5"
        )
        title_label.pack(pady=15)
        
        subtitle_label = tk.Label(
            header_frame,
            text="Stay organized and productive",
            font=("Arial", 10),
            fg="rgba(255,255,255,0.8)",
            bg="#4f46e5"
        )
        subtitle_label.pack()
        
        # Input frame
        input_frame = tk.Frame(self.root, bg="white")
        input_frame.pack(fill=tk.X, padx=10, pady=10)
        
        self.task_entry = tk.Entry(
            input_frame,
            font=("Arial", 12),
            width=35,
            relief=tk.FLAT,
            bd=1
        )
        self.task_entry.pack(side=tk.LEFT, padx=5, pady=5, ipady=8)
        self.task_entry.bind("<Return>", lambda e: self.add_task())
        
        add_btn = tk.Button(
            input_frame,
            text="Add",
            font=("Arial", 11, "bold"),
            bg="#4f46e5",
            fg="white",
            relief=tk.FLAT,
            width=8,
            command=self.add_task
        )
        add_btn.pack(side=tk.LEFT, padx=5, pady=5)
        
        # Stats frame
        stats_frame = tk.Frame(self.root, bg="#f3f4f6")
        stats_frame.pack(fill=tk.X, padx=10, pady=5)
        
        tk.Label(stats_frame, text="Total:", bg="#f3f4f6", font=("Arial", 10)).pack(side=tk.LEFT, padx=10, pady=8)
        self.total_label = tk.Label(stats_frame, text="0", bg="#f3f4f6", font=("Arial", 10, "bold"), fg="#4f46e5")
        self.total_label.pack(side=tk.LEFT, padx=5)
        
        tk.Label(stats_frame, text="|", bg="#f3f4f6").pack(side=tk.LEFT, padx=5)
        
        tk.Label(stats_frame, text="Completed:", bg="#f3f4f6", font=("Arial", 10)).pack(side=tk.LEFT, padx=10)
        self.completed_label = tk.Label(stats_frame, text="0", bg="#f3f4f6", font=("Arial", 10, "bold"), fg="#10b981")
        self.completed_label.pack(side=tk.LEFT, padx=5)
        
        tk.Label(stats_frame, text="|", bg="#f3f4f6").pack(side=tk.LEFT, padx=5)
        
        tk.Label(stats_frame, text="Pending:", bg="#f3f4f6", font=("Arial", 10)).pack(side=tk.LEFT, padx=10)
        self.pending_label = tk.Label(stats_frame, text="0", bg="#f3f4f6", font=("Arial", 10, "bold"), fg="#ef4444")
        self.pending_label.pack(side=tk.LEFT, padx=5)
        
        # Listbox frame
        listbox_frame = tk.Frame(self.root, bg="white")
        listbox_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        scrollbar = tk.Scrollbar(listbox_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.listbox = tk.Listbox(
            listbox_frame,
            font=("Arial", 11),
            relief=tk.FLAT,
            bd=0,
            yscrollcommand=scrollbar.set,
            bg="white",
            fg="#1f2937",
            selectmode=tk.SINGLE
        )
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.listbox.bind("<Delete>", lambda e: self.delete_task())
        self.listbox.bind("<Double-Button-1>", lambda e: self.toggle_task())
        
        scrollbar.config(command=self.listbox.yview)
        
        # Button frame
        btn_frame = tk.Frame(self.root, bg="#f0f0f0")
        btn_frame.pack(fill=tk.X, padx=10, pady=10)
        
        delete_btn = tk.Button(
            btn_frame,
            text="Delete Selected",
            font=("Arial", 10),
            bg="#ef4444",
            fg="white",
            relief=tk.FLAT,
            command=self.delete_task
        )
        delete_btn.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        
        clear_btn = tk.Button(
            btn_frame,
            text="Clear Completed",
            font=("Arial", 10),
            bg="#10b981",
            fg="white",
            relief=tk.FLAT,
            command=self.clear_completed
        )
        clear_btn.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)

    def add_task(self):
        """Add a new task"""
        task_text = self.task_entry.get().strip()
        
        if not task_text:
            messagebox.showwarning("Warning", "Please enter a task!")
            self.task_entry.focus()
            return
        
        task = {
            "id": len(self.task_list),
            "text": task_text,
            "completed": False,
            "created_at": datetime.now().isoformat()
        }
        
        self.task_list.append(task)
        self.task_entry.delete(0, tk.END)
        self.task_entry.focus()
        
        self.save_tasks()
        self.update_listbox()
        self.update_stats()

    def delete_task(self):
        """Delete selected task"""
        selection = self.listbox.curselection()
        if not selection:
            messagebox.showwarning("Warning", "Please select a task to delete!")
            return
        
        if messagebox.askyesno("Confirm", "Delete this task?"):
            idx = selection[0]
            self.task_list.pop(idx)
            self.save_tasks()
            self.update_listbox()
            self.update_stats()

    def toggle_task(self):
        """Toggle task completion (double-click)"""
        selection = self.listbox.curselection()
        if selection:
            idx = selection[0]
            self.task_list[idx]["completed"] = not self.task_list[idx]["completed"]
            self.save_tasks()
            self.update_listbox()
            self.update_stats()

    def clear_completed(self):
        """Remove all completed tasks"""
        completed = [t for t in self.task_list if t["completed"]]
        if not completed:
            messagebox.showinfo("Info", "No completed tasks!")
            return
        
        if messagebox.askyesno("Confirm", f"Delete {len(completed)} completed task(s)?"):
            self.task_list = [t for t in self.task_list if not t["completed"]]
            self.save_tasks()
            self.update_listbox()
            self.update_stats()

    def update_listbox(self):
        """Update the task listbox display"""
        self.listbox.delete(0, tk.END)
        for task in self.task_list:
            status = "✓ " if task["completed"] else "○ "
            display_text = status + task["text"]
            self.listbox.insert(tk.END, display_text)

    def update_stats(self):
        """Update statistics display"""
        total = len(self.task_list)
        completed = sum(1 for t in self.task_list if t["completed"])
        pending = total - completed
        
        self.total_label.config(text=str(total))
        self.completed_label.config(text=str(completed))
        self.pending_label.config(text=str(pending))

    def save_tasks(self):
        """Save tasks to JSON file"""
        try:
            with open(self.tasks_file, "w") as f:
                json.dump(self.task_list, f, indent=2)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save tasks: {str(e)}")

    def load_tasks(self):
        """Load tasks from JSON file"""
        if os.path.exists(self.tasks_file):
            try:
                with open(self.tasks_file, "r") as f:
                    self.task_list = json.load(f)
                self.update_listbox()
                self.update_stats()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load tasks: {str(e)}")


def main():
    """Main application entry point"""
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()

