def direction_change(direction):
    match direction:
        case (0, -1):
            return (1, 0)
        case (1, 0):
            return (0, 1)
        case (0, 1):
            return (-1, 0)
        case (-1, 0):
            return (0, -1)


f1 = open("AoC/AoC6.txt")
posOfGuard = (0, 0)
obstacles = set()
yLines = []
for line in f1:
    yLines.append(line[:-1])

for Yi in range(len(yLines)):
    for Xi in range(len(yLines[Yi])):
        if yLines[Yi][Xi] == "#":
            obstacles.add((Xi, Yi))
        elif yLines[Yi][Xi] == "^":
            posOfGuard = (Xi, Yi)
exit = False
visited = set()
direction = (0, -1)
while exit == False:
    visited.add(posOfGuard)
    nextStep = (posOfGuard[0] + direction[0], posOfGuard[1] + direction[1])
    while nextStep in obstacles:
        direction = direction_change(direction)
        nextStep = (posOfGuard[0] + direction[0], posOfGuard[1] + direction[1])
    if posOfGuard[0] >= len(yLines[0]) or posOfGuard[0] < 0 or posOfGuard[1] >= len(yLines) or posOfGuard[1] < 0:
        exit = True
    posOfGuard = nextStep

print(len(visited)-1)
