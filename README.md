# Sudoku Solver

A Sudoku solver implemented using the **backtracking search** algorithm. This project solves standard 9x9 Sudoku puzzles efficiently by filling in the empty cells through backtracking search.

## Features

- Solves any valid 9x9 Sudoku puzzle.
- Implements a backtracking search algorithm for solution.
- Handles partially filled puzzles.

## Usage

### Prerequisites

Make sure you have Python installed (version 3.x recommended).

### Running the Solver

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/sudoku-solver.git
   cd sudoku-solver
   ```

2. Run the solver script:

   ```bash
   python sudoku_solver.py
   ```

### Example Input

```python
[5, 3, 0, 0, 7, 0, 0, 0, 0]
[6, 0, 0, 1, 9, 5, 0, 0, 0]
[0, 9, 8, 0, 0, 0, 0, 6, 0]
[8, 0, 0, 0, 6, 0, 0, 0, 3]
[4, 0, 0, 8, 0, 3, 0, 0, 1]
[7, 0, 0, 0, 2, 0, 0, 0, 6]
[0, 6, 0, 0, 0, 0, 2, 8, 0]
[0, 0, 0, 4, 1, 9, 0, 0, 5]
[0, 0, 0, 0, 8, 0, 0, 7, 9]
```

### Example Output

```python
[5, 3, 4, 6, 7, 8, 9, 1, 2]
[6, 7, 2, 1, 9, 5, 3, 4, 8]
[1, 9, 8, 3, 4, 2, 5, 6, 7]
[8, 5, 9, 7, 6, 1, 4, 2, 3]
[4, 2, 6, 8, 5, 3, 7, 9, 1]
[7, 1, 3, 9, 2, 4, 8, 5, 6]
[9, 6, 1, 5, 3, 7, 2, 8, 4]
[2, 8, 7, 4, 1, 9, 6, 3, 5]
[3, 4, 5, 2, 8, 6, 1, 7, 9]
```

## Project Structure

```
.
├── sudoku_solver.py      # Main solver script
└── README.md             # Project documentation
```

