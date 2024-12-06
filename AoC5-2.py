def checkUpdate(rules, update):
    beforePages = []
    incorrectPages = []
    for newPage in update:
        for page in beforePages:
            for rule in rules:
                if rule[0] == newPage and rule[1] == page:
                    incorrectPages.append(newPage)
                    incorrectPages.append(page)
        beforePages.append(newPage)
    if len(incorrectPages) > 0:
        return False, incorrectPages
    return True, incorrectPages


def updateFixer(rules, update):
    incorrect = False
    while incorrect == False:
        incorrect = False
        for newPageI in range(len(update)):
            for pageI in range(len(update)):
                for rule in rules:
                    if rule[0] == update[newPageI] and rule[1] == update[pageI]:
                        newVal = update[newPageI]
                        update[newPageI] = update[pageI]
                        update[pageI] = newVal
                        incorrect = True
    return update


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
    check, incorrectPages = checkUpdate(filters, update)
    if not check:
        updateFixer(filters, update)
        middleIndex = (len(update)-1) // 2
        total += (update[middleIndex])

print(total)
