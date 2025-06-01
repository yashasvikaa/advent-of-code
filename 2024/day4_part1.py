def reader():
    grid = []
    with open("day4_part1_input.txt", "r") as file:
        for line in file:
            new_line = line.strip()
            row = list(new_line)
            grid.append(row)
    return grid

def up_and_down(grid):
    sum = 0
    for i in range(0, len(grid)-3):
        for j in range(0, len(grid)):
            word = (grid[i][j] + grid[i+1][j] + grid[i+2][j] + grid[i+3][j])
            if word == "XMAS" or word == "SAMX":
                sum+=1
    return sum

def right_and_left(grid):
    sum = 0
    for i in range(0, len(grid)):
        for j in range(0, len(grid)-3):
            word = (grid[i][j] + grid[i][j+1] + grid[i][j+2] + grid[i][j+3])
            if word == "XMAS" or word == "SAMX":
                sum += 1
    return sum

def diagonal_left(grid):
    sum = 0
    for i in range(0, len(grid)-3):
        for j in range(0, len(grid) - 3):
            word = (grid[i][j] + grid[i+1][j+1]+ grid[i+2][j+2] + grid[i+3][j+3])
            if word == "XMAS" or word == "SAMX":
                sum += 1
    return sum

def diagonal_right(grid):
    sum = 0
    for i in range(3, len(grid)):
        for j in range(0, len(grid) - 3):
            word = (grid[i][j] + grid[i-1][j+1] + grid[i-2][j+2] + grid[i-3][j+3])
            if word == "XMAS" or word == "SAMX":
                sum+=1
    return sum 


def main():
    grid = reader()
    print(up_and_down(grid)+ right_and_left(grid) + diagonal_left(grid) + diagonal_right(grid))

if __name__ == "__main__":
    main()