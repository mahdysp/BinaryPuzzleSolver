## Functions Overview
**Binary Puzzle Solver** is a Python application with a **Tkinter GUI** that allows users to create, edit, and automatically solve binary puzzles. The solver uses advanced techniques from Constraint Satisfaction Problems (CSP) including **backtracking, MRV, LCV, and forward checking** to efficiently solve puzzles of various sizes.
## Features

- Create a square grid of **any even size**.  
- Fill cells with `0`, `1` or leave empty for the solver to fill.  
- Solve the puzzle using:
  - **MRV (Minimum Remaining Values)** for selecting variables  
  - **LCV (Least Constraining Value)** for ordering values  
  - **Forward Checking** to prune inconsistent assignments early  
- Light and Dark UI themes for better user experience.  
- One-time “snake-style” animated message for fun.  
- Shows **status messages** for invalid input, unsolvable puzzles, and success.  

---

This section explains the key functions used in the **BinaryPuzzleSolver** and **BinaryPuzzleUI** classes, including their purpose, inputs, outputs, and behavior.

---

### Solver Functions (`BinaryPuzzleSolver`)

#### `__init__(self, n, grid)`
- **Purpose:** Initialize the solver with a grid.
- **Inputs:**
  - `n`: Grid size (number of rows/columns, must be even)
  - `grid`: 2D list containing `0`, `1`, or `'-'` for empty cells
- **Behavior:**  
  - Sets up `self.domains` for all empty cells with possible values `{0, 1}`.  
  - Converts filled cells from string to integer.
- **Output:** None (initializes internal state)

---

#### `is_complete(self)`
- **Purpose:** Check if the puzzle is fully solved.
- **Inputs:** None
- **Behavior:** Returns `True` if `self.domains` is empty (no unassigned cells remain).
- **Output:** `bool`

---

#### `valid_count(self, line)`
- **Purpose:** Ensure a line (row or column) does not exceed allowed number of 0s or 1s.
- **Inputs:** 
  - `line`: List of numbers or `'-'` for empty cells
- **Behavior:** Counts 0s and 1s; returns `False` if either exceeds `n/2`.
- **Output:** `bool`

---

#### `valid_triplet(self, line)`
- **Purpose:** Check that no three identical numbers appear consecutively in a line.
- **Inputs:** 
  - `line`: List of numbers or `'-'`
- **Behavior:** Iterates over the line and checks for consecutive triplets of 0s or 1s.
- **Output:** `bool`

---

#### `valid_uniqueness(self)`
- **Purpose:** Ensure all completed rows and columns are unique.
- **Inputs:** None
- **Behavior:** Compares all filled rows and columns; returns `False` if duplicates exist.
- **Output:** `bool`

---

#### `is_consistent(self, r, c)`
- **Purpose:** Check whether the current assignment at `(r, c)` is consistent.
- **Inputs:** 
  - `r`, `c`: Row and column indices
- **Behavior:**  
  - Checks `valid_count` and `valid_triplet` for the row and column.  
  - If row/column is complete, checks uniqueness.
- **Output:** `bool`

---

#### `select_variable_mrv(self)`
- **Purpose:** Choose the next cell to assign using **MRV (Minimum Remaining Values)**.
- **Inputs:** None
- **Behavior:** Selects the variable with the fewest remaining possible values.
- **Output:** Tuple `(row, column)`

---

#### `order_values_lcv(self, var)`
- **Purpose:** Order possible values for a variable using **LCV (Least Constraining Value)** heuristic.
- **Inputs:** 
  - `var`: Tuple `(row, column)`
- **Behavior:**  
  - Simulates each value and counts conflicts it causes in related cells.  
  - Returns values in ascending order of conflicts.
- **Output:** List of values `[0,1]` sorted by least impact

---

#### `forward_checking(self, var)`
- **Purpose:** Eliminate inconsistent values from neighboring variables.
- **Inputs:** 
  - `var`: Tuple `(row, column)` just assigned
- **Behavior:**  
  - For each variable in the same row or column, removes values that violate constraints.  
  - Returns `False` if any variable has no possible values left.
- **Output:** `bool`

---

#### `backtrack(self)`
- **Purpose:** Solve the puzzle recursively using **backtracking**.
- **Inputs:** None
- **Behavior:**  
  - Checks if the puzzle is complete.  
  - Selects the next variable (MRV), orders values (LCV), assigns, forward-checks, and recurses.  
  - Backtracks if necessary.
- **Output:** `bool` indicating whether a solution was found

---

#### `solve(self)`
- **Purpose:** Entry point to start solving the puzzle.
- **Inputs:** None
- **Behavior:** Calls `backtrack`.
- **Output:** `bool` (solution found or not)

---

### UI Functions (`BinaryPuzzleUI`)

#### `__init__(self, root)`
- **Purpose:** Initialize the Tkinter GUI.
- **Inputs:** `root` (Tkinter root window)
- **Behavior:**  
  - Sets up variables, builds the UI, applies theme, starts snake message.
- **Output:** None

---

#### `build_ui(self)`
- **Purpose:** Create widgets (buttons, entries, labels) for the interface.
- **Inputs:** None
- **Behavior:** Adds grid size input, buttons for grid creation, solving, theme toggle, and grid frame.
- **Output:** None

---

#### `create_grid(self)`
- **Purpose:** Generate a new empty grid of Entry widgets.
- **Inputs:** None
- **Behavior:**  
  - Reads `self.size_var`, validates size.  
  - Creates `n x n` Entry widgets.  
  - Stores them in `self.grid_cells`.
- **Output:** None

---

#### `solve(self)`
- **Purpose:** Read grid, solve it, and update UI.
- **Inputs:** None
- **Behavior:**  
  - Converts Entry values into solver input.  
  - Calls `BinaryPuzzleSolver.solve()`.  
  - Updates entries with solution or shows error.
- **Output:** None

---

#### `toggle_theme(self)` & `apply_theme(self)`
- **Purpose:** Switch between Light and Dark mode.
- **Inputs:** None
- **Behavior:** Changes colors of root, buttons, labels, and entries.
- **Output:** None

---

#### `show_status(self, main_text, sub_text=None, color="red")`
- **Purpose:** Display temporary messages in the UI.
- **Inputs:**  
  - `main_text`: Main message string  
  - `sub_text`: Optional secondary text  
  - `color`: Text color
- **Behavior:** Displays a label, then destroys it after 2 seconds.
- **Output:** None

---

#### Snake Animation Functions
- **`start_snake(self)`**: Starts the one-time left-to-right message animation.
- **`move_snake_once(self)`**: Moves the snake label by incrementing `x` until it exits the window.
- **Inputs:** None
- **Output:** None

---

These explanations can be added as a **“Functions Overview”** section in your README to make it clear how your solver and UI work internally.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/BinaryPuzzleSolver.git
cd BinaryPuzzleSolver
```
---

by M. Mahdy Sobhany Poor
📟
