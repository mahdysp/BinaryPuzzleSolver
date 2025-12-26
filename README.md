# Binary Puzzle Solver

**Binary Puzzle Solver** is a Python application with a **Tkinter GUI** that allows users to create, edit, and automatically solve binary puzzles. The solver uses advanced techniques from Constraint Satisfaction Problems (CSP) including **backtracking, MRV, LCV, and forward checking** to efficiently solve puzzles of various sizes.

---

## Table of Contents

- [Features](#features)  
- [Installation](#installation)  
- [Usage](#usage)  
- [How it Works](#how-it-works)  
- [User Interface](#user-interface)  
- [Examples](#examples)  
- [Creating an Executable](#creating-an-executable)  
- [Screenshots](#screenshots)  
- [License](#license)  

---

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

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/BinaryPuzzleSolver.git
cd BinaryPuzzleSolver
