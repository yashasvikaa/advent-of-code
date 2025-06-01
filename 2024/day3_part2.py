def reader():
    do = True
    grid = []
    with open("day3_part1_input.txt", "r") as file:
        content = file.read()
    i = 0  
    while i < len(content):
        if content[i: i+7] == "don't()":
            do = False
            index = content.find("do()", i+7) 
            if index == -1:
                break
            i = index
            do = True
        if do and content[i:i+4] == "mul(":
            index1 = content.find(")", i+7, i+12)
            index2 = content.find(",",i+5, i+8)
            str_1 = content[i+4:index2]
            str_2 = content[index2 + 1: index1]
            if str_1.isdigit() and str_2.isdigit():
                row = [int(str_1), int(str_2)]
                grid.append(row)
        i += 1
        
    return grid

def main():
    grid = reader()
    sum_of_products = 0
    for row in grid:
        sum_of_products += row[0]*row[1]
    print(sum_of_products)

if __name__ == "__main__":
    main()