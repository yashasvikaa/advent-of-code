from day2_part1 import reader, isDecreasing, isIncreasing

def check(row):
    for i in range(len(row)):
        new_row = row[:i] + row[i+1:]  
        if isDecreasing(new_row) or isIncreasing(new_row):
            return True
    return False
        

def main():
    grid = reader()
    report = []
    for row in grid:
        if isDecreasing(row) or isIncreasing(row) or check(row):
            report.append("Safe")
        else:
            report.append("Unsafe")
    print(report.count("Safe"))
    
if __name__ == "__main__":
    main()