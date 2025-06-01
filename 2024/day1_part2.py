from day1_part1 import reader
from collections import Counter

def main():
    grid1, grid2 = reader()
    freq = Counter(grid2)
    total = sum(num * freq[num] for num in grid1)
    print(total)

if __name__ == "__main__":
    main()