def checkUpdate(rules, update):
    beforePages = []
    for newPage in update:
        for page in beforePages:
            for rule in rules:
                if rule[0] == newPage and rule[1] == page:
                    return False
        beforePages.append(newPage)
    return True


f1 = open("AoC/AoC5-1.txt")
filters = []
for line in f1:
    filt = line.split("|")

    filters.append((int(filt[0]), int(filt[1])))

f2 = open("AoC/AoC5-2.txt")
updates = []
for line in f2:
    update = line.split(",")
    newUpdate = []
    for page in update:
        newUpdate.append(int(page))
    updates.append(newUpdate)

total = 0

for update in updates:
    if checkUpdate(filters, update):
        middleIndex = (len(update)-1) // 2
        total += (update[middleIndex])

print(total)
