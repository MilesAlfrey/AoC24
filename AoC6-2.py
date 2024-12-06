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
startPosOfGuard = (0, 0)
obstacles = set()
yLines = []
for line in f1:
    yLines.append(line[:-1])

for Yi in range(len(yLines)):
    for Xi in range(len(yLines[Yi])):
        if yLines[Yi][Xi] == "#":
            obstacles.add((Xi, Yi))
        elif yLines[Yi][Xi] == "^":
            startPosOfGuard = (Xi, Yi)
circles = 0
exit = False
visited = set()
maxStep = len(yLines) * len(yLines[0]) + 1
totalSteps = 0
direction = (0, -1)
for Yi in range(len(yLines)):
    for Xi in range(len(yLines[Yi])):
        newObstacles = obstacles.copy()
        newObstacles.add((Xi, Yi))
        direction = (0, -1)
        posOfGuard = startPosOfGuard
        totalSteps = 0
        visited = set()
        exit = False
        while exit == False:
            visited.add(posOfGuard)
            nextStep = (posOfGuard[0] + direction[0],
                        posOfGuard[1] + direction[1])
            while nextStep in newObstacles:
                direction = direction_change(direction)
                nextStep = (posOfGuard[0] + direction[0],
                            posOfGuard[1] + direction[1])
            if posOfGuard[0] >= len(yLines[0]) or posOfGuard[0] < 0 or posOfGuard[1] >= len(yLines) or posOfGuard[1] < 0:
                exit = True
            posOfGuard = nextStep
            totalSteps += 1
            if totalSteps > maxStep:
                circles += 1
                break


print(circles)
