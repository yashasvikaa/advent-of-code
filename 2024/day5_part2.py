from day5_part1 import reader, is_valid

def correct(rules, order):
    final = order[:]  
    changed = True
    while changed:
        changed = False
        for i in range(len(final)):
            for j in range(i + 1, len(final)):
                if (final[j], final[i]) in rules:  
                    final[i], final[j] = final[j], final[i]
                    changed = True
    return final

def main():
    rules, updates = reader()
    incorrect = []
    final = []
    sum = 0
    for update in updates:
        if not is_valid(rules, update):
            incorrect.append(update)
    for order in incorrect:
        final.append(correct(rules, order))
    for list in final:
        sum += list[len(list)//2]
    print(sum)

if __name__ == "__main__":
    main()