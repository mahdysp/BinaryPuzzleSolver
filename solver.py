# solver.py
import copy

class BinaryPuzzleSolver:
    """
    A solver for Binary Puzzles using Backtracking with MRV, LCV and Forward Checking.
    """
    def __init__(self, n: int, grid: list):
        self.n = n
        self.grid = grid
        self.domains = {}

        for r in range(n):
            for c in range(n):
                if grid[r][c] == '-':
                    self.domains[(r, c)] = {0, 1}
                else:
                    grid[r][c] = int(grid[r][c])

    def is_complete(self) -> bool:
        return len(self.domains) == 0

    def valid_count(self, line: list) -> bool:
        return line.count(0) <= self.n // 2 and line.count(1) <= self.n // 2

    def valid_triplet(self, line: list) -> bool:
        for i in range(len(line) - 2):
            if line[i] == line[i+1] == line[i+2] != '-':
                return False
        return True

    def valid_uniqueness(self) -> bool:
        rows, cols = [], []
        for r in range(self.n):
            if '-' not in self.grid[r]:
                rows.append(tuple(self.grid[r]))
        for c in range(self.n):
            col = [self.grid[r][c] for r in range(self.n)]
            if '-' not in col:
                cols.append(tuple(col))
        return len(rows) == len(set(rows)) and len(cols) == len(set(cols))

    def is_consistent(self, r: int, c: int) -> bool:
        row = self.grid[r]
        col = [self.grid[i][c] for i in range(self.n)]
        if not self.valid_count(row) or not self.valid_count(col):
            return False
        if not self.valid_triplet(row) or not self.valid_triplet(col):
            return False
        if '-' not in row or '-' not in col:
            return self.valid_uniqueness()
        return True

    def select_variable_mrv(self):
        return min(self.domains, key=lambda v: len(self.domains[v]))

    def order_values_lcv(self, var):
        r, c = var
        def conflicts(val):
            count = 0
            self.grid[r][c] = val
            for (rr, cc) in self.domains:
                if (rr, cc) != var and (rr == r or cc == c):
                    if not self.is_consistent(rr, cc):
                        count += 1
            self.grid[r][c] = '-'
            return count
        return sorted(self.domains[var], key=conflicts)

    def forward_checking(self, var):
        r, c = var
        for (rr, cc) in list(self.domains):
            if (rr, cc) == var:
                continue
            if rr == r or cc == c:
                for val in self.domains[(rr, cc)].copy():
                    self.grid[rr][cc] = val
                    if not self.is_consistent(rr, cc):
                        self.domains[(rr, cc)].remove(val)
                    self.grid[rr][cc] = '-'
                if not self.domains[(rr, cc)]:
                    return False
        return True

    def backtrack(self) -> bool:
        if self.is_complete():
            return True
        var = self.select_variable_mrv()
        for value in self.order_values_lcv(var):
            r, c = var
            self.grid[r][c] = value
            if self.is_consistent(r, c):
                saved_domains = copy.deepcopy(self.domains)
                del self.domains[var]
                if self.forward_checking(var) and self.backtrack():
                    return True
                self.domains = saved_domains
            self.grid[r][c] = '-'
        return False

    def solve(self) -> bool:
        return self.backtrack()
