# Functions
def isDistinct(candidate_marker_string):
    # Check if all the characters in a string are distinct
    candidate_marker_set = set(candidate_marker_string)
    if len(candidate_marker_set) == len(candidate_marker_string):
        return True
    else:
        return False

def getDistinctMarker(input_string, num_distinct):
    # Loop through the string to slice out candidates and check distinct characters
    marker_point = 0
    for i in range(len(input_string)):
        candidate_marker_string = input_string[i: i + num_distinct]
        if isDistinct(candidate_marker_string):
            marker_point = i + num_distinct
            break
    if marker_point == 0:
        raise Exception("No distinct marker found")
    return marker_point

def main():
    # Get input
    with open("day6/input.txt", 'r') as f:
        nums = [line for line in f.readlines()]

    # Parse input
    nums = nums[0].strip()

    # Part 1
    marker_point_1 = getDistinctMarker(input_string=nums, num_distinct=4)
    print("Part 1: %i" % marker_point_1)

    # Part 2
    marker_point_2 = getDistinctMarker(input_string=nums, num_distinct=14)
    print("Part 2: %i" % marker_point_2)


if __name__ == '__main__':
    main()