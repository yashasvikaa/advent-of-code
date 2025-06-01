from day4_part1 import reader

def check(grid):
    sum = 0
    for i in range(1, len(grid)-1):
         for j in range(1, len(grid)-1):
             if grid[i][j] == "A":
                 if (grid[i-1][j-1] == "S" and grid[i+1][j+1] == "M") or (grid[i-1][j-1] == "M" and grid[i+1][j+1] == "S"):
                     if (grid[i-1][j+1] == "S" and grid[i+1][j-1] == "M") or (grid[i-1][j+1] == "M" and grid[i+1][j-1] == "S"):
                         sum += 1
    return sum

def main():
    grid = reader()
    print(check(grid))

if __name__ == "__main__":
    main()