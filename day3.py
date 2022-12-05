# Functions
def getMatchingChar(first_compartment, second_compartment):
    # Convert chars to numbers
    first_compartment = [ord(char)-96 if 97 <= ord(char) <= 122 else ord(char)-38 for char in first_compartment]
    second_compartment = [ord(char)-96 if 97 <= ord(char) <= 122 else ord(char)-38 for char in second_compartment]
    matching_char = [x for x in first_compartment if (x in second_compartment)]
    return matching_char[0]

def getMatchingCharPart2(first_rucksack, second_rucksack, third_rucksack):
    # Convert chars to numbers
    set_of_chars = first_rucksack + second_rucksack + third_rucksack
    first_rucksack = [ord(char)-96 if 97 <= ord(char) <= 122 else ord(char)-38 for char in first_rucksack]
    second_rucksack = [ord(char)-96 if 97 <= ord(char) <= 122 else ord(char)-38 for char in second_rucksack]
    third_rucksack = [ord(char)-96 if 97 <= ord(char) <= 122 else ord(char)-38 for char in third_rucksack]
    set_of_chars = [ord(char)-96 if 97 <= ord(char) <= 122 else ord(char)-38 for char in set_of_chars]
    matching_char = [x for x in set_of_chars if (x in first_rucksack and x in second_rucksack and x in third_rucksack)]
    return matching_char[0]


def main():
    # Get input
    with open("day3/input.txt", 'r') as f:
        nums = [line for line in f.readlines()]

    nums = [num.strip() for num in nums]

    # Part 1
    count = 0
    for i in range(len(nums)):
        len_num = int(len(nums[i]) / 2)
        first_compartment = nums[i][:len_num]
        second_compartment = nums[i][len_num:]
        matching_val = getMatchingChar(first_compartment, second_compartment)
        count += matching_val

    print("Part 1: %i" % count)

    # Part 2
    count = 0
    for i in range(len(nums)):
        if i % 3 == 2:
            first_rucksack = nums[i-2]
            second_rucksack = nums[i-1]
            third_rucksack = nums[i]
            matching_val = getMatchingCharPart2(first_rucksack, second_rucksack, third_rucksack)
            count += matching_val

    print("Part 2: %i" % count)

if __name__ == '__main__':
    main()