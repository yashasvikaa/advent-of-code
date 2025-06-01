def reader():
    grid = []
    with open("day3_part1_input.txt", "r") as file:
        for line in file:
            for i in range(0, len(line)):
                if line[i:i+4] == "mul(":
                    index1 = line.find(")", i+7, i+12)
                    index2 = line.find(",",i+5, i+8)
                    str_1 = line[i+4:index2]
                    str_2 = line[index2 + 1: index1]
                    if str_1.isdigit() and str_2.isdigit():
                        row = [int(str_1), int(str_2)]
                        grid.append(row)
    return grid
             

def main():
    grid = reader()
    sum_of_products = 0
    for row in grid:
        sum_of_products += row[0]*row[1]
    print(sum_of_products)

if __name__ == "__main__":
    main()