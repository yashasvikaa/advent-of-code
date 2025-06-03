def reader():
    with open("day5_part1_input.txt", "r") as file:
        rules_sec, updates_sec = file.read(). strip(). split("\n\n")

    rules = rules_sec.strip().splitlines()
    updates = updates_sec.strip().splitlines()
    list_of_rules = []
    for line in rules:
        x, y = map(int, line.split("|"))
        list_of_rules.append((x,y))

    list_of_updates = [list(map(int, line.split(","))) for line in updates]
    return list_of_rules, list_of_updates

def is_valid(rules, update):
    position = {num: index for index, num in enumerate(update)}
    for (a, b) in rules:
        if a in position and b in position:
            if position[a] >= position[b]:
                return False
    return True

def main():
    rules, updates = reader()
    total = 0
    for update in updates:
        if is_valid(rules, update):
            total += update[len(update)//2]

    print(total)

if __name__ == "__main__":
    main()