// http://www.geeksforgeeks.org/backtracking-set-7-suduku/

import Glibc

let unassigned = 0

func solvePuzzle(inout grid: [[Int]]) -> Bool {
    let result = findUnassignedLocation(grid)

    if !result.unassigned {
        return true
    }

    for i in 1...9 {
        if(isSafe(grid, result.row, result.column, i)) {
            grid[result.row][result.column] = i
            if solvePuzzle(&grid) {
                return true
            }
            grid[result.row][result.column] = unassigned
        }
    }

    return false
}

func isSafe(grid: [[Int]], _ row: Int, _ column: Int, _ number: Int) -> Bool {
    return !usedInRow(grid, row, number) && !usedInColumn(grid, column, number)
            && !usedInBox(grid, row - row % 3, column - column % 3, number)
}

func usedInRow(grid: [[Int]], _ row: Int, _ number: Int) -> Bool {
    for column in 0..<9 {
        if grid[row][column] == number {
            return true
        }
    }
    return false
}

func usedInColumn(grid: [[Int]], _ column: Int, _ number: Int) -> Bool {
    for row in 0..<9 {
        if grid[row][column] == number {
            return true
        }
    }
    return false
}

func usedInBox(grid: [[Int]], _ boxRow: Int, _ boxColumn: Int, _ number: Int) -> Bool {
    for row in 0..<3 {
        for column in 0..<3 {
            if grid[row + boxRow][column + boxColumn] == number {
                return true
            }
        }
    }
    return false
}

func findUnassignedLocation(grid: [[Int]]) -> (row: Int, column: Int, unassigned: Bool) {
    for row in 0..<9 {
        for column in 0..<9 {
            if grid[row][column] == unassigned {
                return (row, column, true)
            }
        }
    }
    return (8, 8, false)
}


var grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
            [5, 2, 0, 0, 0, 0, 0, 0, 0],
            [0, 8, 7, 0, 0, 0, 0, 3, 1],
            [0, 0, 3, 0, 1, 0, 0, 8, 0],
            [9, 0, 0, 8, 6, 3, 0, 0, 5],
            [0, 5, 0, 0, 9, 0, 6, 0, 0],
            [1, 3, 0, 0, 0, 0, 2, 5, 0],
            [0, 0, 0, 0, 0, 0, 0, 7, 4],
            [0, 0, 5, 2, 0, 6, 3, 0, 0]]

if solvePuzzle(&grid) {
    print("Puzzle was solved!")
    for row in grid {
        print(row)
    }
} else {
    print("Puzzle cannot be solved.")
}