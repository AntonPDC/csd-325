import tkinter as tk
from tkinter import Menu
import tkinter.messagebox as msg


class ToDo(tk.Tk):
    def __init__(self, tasks=None):
        super().__init__()

        # Initialize the task list
        if not tasks:
            self.tasks = []
        else:
            self.tasks = tasks

        # Define alternating color schemes
        self.colour_schemes = [
            {"bg": "lightblue", "fg": "darkblue"},
            {"bg": "darkblue", "fg": "lightblue"}
        ]

        # Set up the main window
        self.title("DeCesare To-Do")
        self.geometry("300x400")

        # Add a visible File menu inside the window
        self.menu_frame = tk.Frame(self, bg="lightgrey", height=30)
        self.menu_frame.pack(side=tk.TOP, fill=tk.X)

        self.file_button = tk.Menubutton(self.menu_frame, text="File", bg="lightgrey", fg="black", relief=tk.RAISED)
        self.file_menu = tk.Menu(self.file_button, tearoff=0, bg="white", fg="black")
        self.file_menu.add_command(label="Exit", command=self.exit_program)
        self.file_button["menu"] = self.file_menu
        self.file_button.pack(side=tk.LEFT, padx=5)

        # Set up the canvas and frames for tasks
        self.tasks_canvas = tk.Canvas(self)
        self.tasks_frame = tk.Frame(self.tasks_canvas)
        self.text_frame = tk.Frame(self)
        self.scrollbar = tk.Scrollbar(self.tasks_canvas, orient="vertical", command=self.tasks_canvas.yview)

        self.tasks_canvas.configure(yscrollcommand=self.scrollbar.set)

        # Task input text box
        self.task_create = tk.Text(self.text_frame, height=3, bg="white", fg="black")

        self.tasks_canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas_frame = self.tasks_canvas.create_window((0, 0), window=self.tasks_frame, anchor="n")

        self.task_create.pack(side=tk.BOTTOM, fill=tk.X)
        self.text_frame.pack(side=tk.BOTTOM, fill=tk.X)
        self.task_create.focus_set()

        # Instructions label
        todo1 = tk.Label(
            self.tasks_frame,
            text="--- Add Items Here (Right-click to delete) ---",
            bg="lightgrey",
            fg="black",
            pady=10
        )
        todo1.bind("<Button-3>", self.remove_task)  # Right-click for Windows/Linux
        todo1.bind("<Button-2>", self.remove_task)  # Right-click for macOS

        self.tasks.append(todo1)
        todo1.pack(side=tk.TOP, fill=tk.X)

        # Bind events
        self.bind("<Return>", self.add_task)
        self.bind("<Configure>", self.on_frame_configure)
        self.bind_all("<MouseWheel>", self.mouse_scroll)
        self.bind_all("<Button-4>", self.mouse_scroll)
        self.bind_all("<Button-5>", self.mouse_scroll)
        self.tasks_canvas.bind("<Configure>", self.task_width)

    # Applies alternating colors to tasks and binds removal events
    def apply_alternate_color(self, task, idx):
        color_scheme = self.colour_schemes[idx % 2]
        task.config(bg=color_scheme["bg"], fg=color_scheme["fg"])
        task.bind("<Button-3>", self.remove_task)  # Right-click for Windows/Linux
        task.bind("<Button-2>", self.remove_task)  # Right-click for macOS

    # Add a new task to the task list
    def add_task(self, event=None):
        task_text = self.task_create.get(1.0, tk.END).strip()
        if task_text:
            new_task = tk.Label(self.tasks_frame, text=task_text, pady=10)
            self.apply_alternate_color(new_task, len(self.tasks))  # Apply alternating colors
            self.tasks.append(new_task)
            new_task.pack(side=tk.TOP, fill=tk.X)
        self.task_create.delete(1.0, tk.END)

    # Remove a task
    def remove_task(self, event):
        task = event.widget
        if task in self.tasks:
            self.tasks.remove(task)
            task.destroy()

            # Reapply alternating colors after task removal
            for idx, task in enumerate(self.tasks):
                self.apply_alternate_color(task, idx)

    # Update the scroll region of the canvas
    def on_frame_configure(self, event=None):
        self.tasks_canvas.configure(scrollregion=self.tasks_canvas.bbox("all"))

    # Enable scrolling in the canvas
    def mouse_scroll(self, event):
        if event.delta:
            self.tasks_canvas.yview_scroll(-1 * (event.delta // 120), "units")
        elif event.num == 4:
            self.tasks_canvas.yview_scroll(-1, "units")
        elif event.num == 5:
            self.tasks_canvas.yview_scroll(1, "units")

    # Adjust the task width when the canvas is resized
    def task_width(self, event):
        canvas_width = event.width
        self.tasks_canvas.itemconfig(self.canvas_frame, width=canvas_width)

    # Handle exiting the program with a confirmation dialog
    def exit_program(self):
        if msg.askyesno("Exit Confirmation", "Are you sure you want to exit?"):
            self.destroy()  # Close the application


if __name__ == "__main__":
    app = ToDo()
    app.mainloop()
