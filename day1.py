import numpy as np

def main():
    # Get input
    with open("day1/input.txt", 'r') as f:
        nums = [line for line in f.readlines()]

    # Part 1
    count = 0
    counts = []
    for i, entry in enumerate(nums):
        if entry == '\n':
            counts.append(count)
            count = 0
        else:
            count += int(entry.strip('\n'))
        if i == len(nums)-1:
            counts.append(count)

    print("Part 1: %i" % max(counts))

    # Part 2
    totalCals = 0
    for i in range(3):
        totalCals += max(counts)
        counts.pop(np.argmax(counts))

    print("Part 2: %i" % totalCals)

if __name__ == '__main__':
    main()
