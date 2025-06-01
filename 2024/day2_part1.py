def reader():
    grid = []
    a = 0
    with open("day2_part1_input.txt", "r") as file:
        for line in file:
            parts = line.strip().split()
            row = [int(x) for x in parts]
            grid.append(row)
    return grid

def isDecreasing(row):
    for i in range(1, len(row)):
        if not row[i] < row [i-1] or not abs(row[i] - row[i-1]) < 4:
            return False
    return True
            
            
def isIncreasing(row):
    for i in range(1, len(row)):
        if not row[i] > row [i-1] or not abs(row[i] - row[i-1]) < 4:
            return False
    return True

def main():
    grid = reader()
    report = []
    for row in grid:
        if isDecreasing(row) or isIncreasing(row):
            report.append("Safe")
        else:
            report.append("Unsafe")
    print(report.count("Safe"))

if __name__ == "__main__":
    main()