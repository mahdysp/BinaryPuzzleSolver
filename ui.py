# ui.py
import tkinter as tk
from solver import BinaryPuzzleSolver

class BinaryPuzzleUI:
    """
    Tkinter UI for Binary Puzzle Solver
    """
    def __init__(self, root):
        self.root = root
        self.root.title("Binary Puzzle Solver")
        self.root.geometry("500x500")
        self.theme = "light"
        self.grid_cells = []
        self.n = None
        self.snake_text = "by jarvis"
        self.snake_index = 0
        self.build_ui()
        self.apply_theme()
        self.root.after(5000, self.start_snake)

    # --- UI Building ---
    def build_ui(self):
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(pady=10)
        tk.Label(self.main_frame, text="Grid Size").pack()
        self.size_var = tk.StringVar()
        self.size_entry = tk.Entry(self.main_frame, textvariable=self.size_var, width=10)
        self.size_entry.pack(pady=5)
        tk.Button(self.main_frame, text="Create Grid", command=self.create_grid).pack()
        tk.Button(self.main_frame, text="Solve", command=self.solve).pack(pady=5)
        tk.Button(self.main_frame, text="UI: Light / Dark", command=self.toggle_theme).pack(pady=5)
        self.status_frame = None
        self.grid_frame = tk.Frame(self.root)
        self.grid_frame.pack(pady=10)

    def show_status(self, main_text, sub_text=None, color="red"):
        if self.status_frame:
            self.status_frame.destroy()
        self.status_frame = tk.Frame(self.main_frame, bg=self.bg_color)
        self.status_frame.pack(pady=5)
        tk.Label(self.status_frame, text=main_text, fg=color, bg=self.bg_color, font=("Arial", 14, "bold")).pack()
        if sub_text:
            tk.Label(self.status_frame, text=sub_text, fg=color, bg=self.bg_color, font=("Arial", 9)).pack()
        self.root.after(2000, lambda: self.status_frame.destroy() if self.status_frame else None)

    def create_grid(self):
        try:
            self.n = int(self.size_var.get())
        except:
            self.show_status("Invalid Number!")
            return
        if self.n <= 0 or self.n % 2 != 0:
            self.show_status("Invalid Number!", "Grid size must be positive and even")
            return
        for w in self.grid_frame.winfo_children():
            w.destroy()
        self.grid_cells = []
        for r in range(self.n):
            row = []
            for c in range(self.n):
                e = tk.Entry(self.grid_frame, width=2, justify="center", font=("Arial", 12))
                e.grid(row=r, column=c, padx=2, pady=2)
                row.append(e)
            self.grid_cells.append(row)
        self.show_status("Grid Created", color="green")

    def solve(self):
        if not self.n or self.n <= 0 or self.n % 2 != 0:
            self.show_status("Invalid Number!")
            return
        grid = []
        for r in range(self.n):
            row = []
            for c in range(self.n):
                val = self.grid_cells[r][c].get().strip()
                if val == '':
                    row.append('-')
                elif val in ('0','1'):
                    row.append(val)
                else:
                    self.show_status("Invalid Input")
                    return
            grid.append(row)
        solver = BinaryPuzzleSolver(self.n, grid)
        if solver.solve():
            for r in range(self.n):
                for c in range(self.n):
                    self.grid_cells[r][c].delete(0, tk.END)
                    self.grid_cells[r][c].insert(0, solver.grid[r][c])
            self.show_status("Solved", color="green")
        else:
            self.show_status("Unsolvable", color="red")

    # --- Theme ---
    def toggle_theme(self):
        self.theme = "dark" if self.theme == "light" else "light"
        self.apply_theme()

    def apply_theme(self):
        if self.theme == "light":
            self.bg_color, self.fg_color, self.btn_color, self.entry_bg = "#ffffff", "#000000", "#e0e0e0", "#ffffff"
        else:
            self.bg_color, self.fg_color, self.btn_color, self.entry_bg = "#1e1e1e", "#ffffff", "#333333", "#2b2b2b"
        self.root.configure(bg=self.bg_color)
        self.main_frame.configure(bg=self.bg_color)
        self.grid_frame.configure(bg=self.bg_color)
        for widget in self.main_frame.winfo_children():
            if isinstance(widget, tk.Button):
                widget.configure(bg=self.btn_color, fg=self.fg_color)
            elif isinstance(widget, tk.Label):
                widget.configure(bg=self.bg_color, fg=self.fg_color)
            elif isinstance(widget, tk.Entry):
                widget.configure(bg=self.entry_bg, fg=self.fg_color, insertbackground=self.fg_color)
        for row in self.grid_cells:
            for cell in row:
                cell.configure(bg=self.entry_bg, fg=self.fg_color, insertbackground=self.fg_color)

    # --- Snake Message ---
    def start_snake(self):
        self.snake_label = tk.Label(self.root, text=self.snake_text, font=("Arial", 12, "bold"), fg="blue", bg=self.bg_color)
        self.snake_label.place(x=0, y=self.root.winfo_height() - 30)
        self.snake_index = 0
        self.move_snake_once()

    def move_snake_once(self):
        width = self.root.winfo_width()
        if self.snake_index <= width:
            self.snake_label.place(x=self.snake_index, y=self.root.winfo_height() - 30)
            self.snake_index += 5
            self.root.after(50, self.move_snake_once)
        else:
            self.snake_label.destroy()
