## the firsr method is to go from the sun.
## if the sun in the right, which means EAST, we go from right to left
## if the sun in the left, which means WEST, we go from left to right

## O(N) time | 0(N) Space because we may store all the buildings
def sunsetViews(buildings, direction):
    # Write your code here.
    maxbuilding = []
    if direction == "EAST":
        for buildingidx in range(len(buildings)-1, -1, -1):
            print(buildingidx,len(buildings), maxbuilding)
            if buildingidx == len(buildings)-1:
                maxbuilding.append(buildingidx)
                continue
            if buildings[maxbuilding[-1]] < buildings[buildingidx]:
                maxbuilding.append(buildingidx)
    elif direction == "WEST":
        for buildingidx in range(len(buildings)):
            print(buildingidx,len(buildings), maxbuilding)
            if buildingidx == 0:
                maxbuilding.append(buildingidx)
                continue
            if buildings[maxbuilding[-1]] < buildings[buildingidx]:
                maxbuilding.append(buildingidx)
    return sorted(maxbuilding)


# O(N) time | O(N) space
## using Stack
def sunsetViews(buildings, direction):
    candidateBuildingStack = []

    startIdx = 0 if direction == "EAST" else len(buildings) -1
    step = 1 if direction == "EAST" else -1

    idx = startIdx
    while idx >= 0 and idx < len(buildings):
        buildingHeight = buildings[idx]

        while len(candidateBuildingStack)>0 and  buildingHeight >= buildings[candidateBuildingStack[-1]]:
            candidateBuildingStack.pop()

        candidateBuildingStack.append(idx)
        idx += step

    if direction == "WEST":
        return candidateBuildingStack[::-1]

    return candidateBuildingStack



buildings = [3,5,4,4,3,1,3,2]
direction = "EAST"

print(sunsetViews(buildings, direction))


# {"buildings": [3, 5, 4, 4, 3, 1, 3, 2], "direction": "EAST"}
# [1, 3, 6, 7]


# {"buildings": [3, 5, 4, 4, 3, 1, 3, 2], "direction": "WEST"}
# [0, 1]
