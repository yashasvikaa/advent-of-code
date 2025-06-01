def reader():
    grid1 = []
    grid2 = []
    with open("day1_part1_input.txt", "r") as file:
        for line in file: 
            parts = line.strip().split()
            grid1.append(int(parts[0]))
            grid2.append(int(parts[1]))
    grid1.sort()
    grid2.sort()
    return grid1, grid2

def main():
    grid1, grid2 = reader()
    sum = 0
    for i in range(0, len(grid1)):
        sum += abs(grid1[i] - grid2[i])
    print(sum)

if __name__ == "__main__":
    main()
