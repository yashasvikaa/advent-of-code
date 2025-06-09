import numpy as np

def reader():
    with open("day6_part1_input.txt", "r") as file:
        grid = [list(line.strip()) for line in file]
    return np.array(grid)

def main():
    grid = reader()
    directions = ["^", ">", "V", "<"]
    moves = {"^": (-1, 0), ">": (0, 1), "V": (1, 0), "<": (0, -1)}

    row, col = np.argwhere(grid == "^")[0]
    direction = "^"
    visited = set()
    visited.add((row, col))

    while True:
        moved = False
        for _ in range(4):
            dr, dc = moves[direction]
            new_r, new_c = row + dr, col + dc

            # If next step is outside the grid, guard leaves
            if not (0 <= new_r < len(grid)) or not (0 <= new_c < len(grid[0])):
                # Mark current position as visited and stop
                print(len(visited))
                return

            # If next step is free space, move
            if grid[new_r][new_c] != "#":
                row, col = new_r, new_c
                visited.add((row, col))
                moved = True
                break
            else:
                # blocked, turn right
                i = directions.index(direction)
                direction = directions[(i + 1) % 4]

        if not moved:
            # no moves possible; trapped
            print(len(visited))
            return

if __name__ == "__main__":
    main()