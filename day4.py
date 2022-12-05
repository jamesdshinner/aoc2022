# Functions
def expandRangeString(rangeString):
    min_max = rangeString.split('-')
    minRange, maxRange = int(min_max[0]), int(min_max[1])
    expandedRangeList = []
    for i in range(minRange, maxRange + 1):
        expandedRangeList.append(i)
    return expandedRangeList

def isFullyContains(rangeString1, rangeString2):
    if set(rangeString1) <= set(rangeString2):
        return True
    elif set(rangeString2) <= set(rangeString1):
        return True
    else:
        return False

def isOverlap(rangeString1, rangeString2):
    # Order strings
    if rangeString1[0] < rangeString2[0]:
        lowerString = rangeString1
        higherString = rangeString2
    elif rangeString2[0] < rangeString1[0]:
        lowerString = rangeString2
        higherString = rangeString1
    else:
        return True
    # Check endpoints
    if lowerString[-1] >= higherString[0]:
        return True
    else:
        return False

def main():
    # Get input
    with open("day4/input.txt", 'r') as f:
        nums = [line for line in f.readlines()]

    nums = [num.strip() for num in nums]

    # Part 1
    nums_1 = [num.split(",") for num in nums]
    expanded_nums_1 = [[expandRangeString(num) for num in nums_pair] for nums_pair in nums_1]
    fully_contains_nums_1 = [isFullyContains(nums_pair[0], nums_pair[1]) for nums_pair in expanded_nums_1]
    print("Part 1: %i" % sum(fully_contains_nums_1))

    # Part 2
    nums_2 = [num.split(",") for num in nums]
    expanded_nums_2 = [[expandRangeString(num) for num in nums_pair] for nums_pair in nums_2]
    overlaps_nums_2 = [isOverlap(nums_pair[0], nums_pair[1]) for nums_pair in expanded_nums_2]
    print("Part 2: %i" % sum(overlaps_nums_2))

if __name__ == '__main__':
    main()