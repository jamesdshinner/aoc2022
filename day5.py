import numpy as np

# Functions
def build_diagram(nums):
    split_point = np.where(np.array(nums) == "\n")[0][0]

    diagram = nums[:split_point]

    num_lists = int(diagram[-1][-3])

    diagram_dict = {}

    # Create dict to hold stacks
    for i in range(1, num_lists + 1):
        diagram_dict[i] = []

    # Get the boxes in each stack
    for i in range(split_point-1):
        # Visualisation aid
        row = nums[i].replace(' ','_').strip('\n')[:(4*num_lists - 1)]
        for j in range(num_lists):
            box = row[4*j+1]
            if box != '_':
                diagram_dict[j+1].append(box)

    # Reverse stacks
    for i in range(1, num_lists + 1):
        diagram_dict[i].reverse()

    return diagram_dict

def get_commands(nums):
    split_point = np.where(np.array(nums) == "\n")[0][0]
    return nums[split_point+1:]


def move_boxes_part1(diagram_dict, num_boxes, original_loc, new_loc):
    # Pop and re-add boxes
    for i in range(num_boxes):
        moveable = diagram_dict[original_loc].pop()
        diagram_dict[new_loc].append(moveable)

def move_boxes_part2(diagram_dict, num_boxes, original_loc, new_loc):
    moveables = []
    #Pop boxes
    for i in range(num_boxes):
        moveable = diagram_dict[original_loc].pop()
        moveables.append(moveable)
    # Preserve order
    moveables.reverse()
    # 
    for moveable_new in moveables:
        diagram_dict[new_loc].append(moveable_new)

def main():
    # Get input
    with open("day5/input.txt", 'r') as f:
        nums = [line for line in f.readlines()]

    # Part 1
    # Separate diagram from commands
    diagram_dict = build_diagram(nums)
    commands = get_commands(nums)

    # Execute commands
    for command in commands:
        command_list = command.replace('move ', '').replace('from ', '').replace('to ', '').strip('\n').split(' ')
        num_boxes = int(command_list[0])
        original_loc = int(command_list[1])
        new_loc = int(command_list[2])
        move_boxes_part1(diagram_dict, num_boxes, original_loc, new_loc)

    # Get top crates
    message = ''
    for i in range(1, len(diagram_dict)+1):
        message += diagram_dict[i][-1]
    print("Part 1: %s" % message)

    # Part 2
    # Get fresh diagram
    diagram_dict_2 = build_diagram(nums)

    # Execute commands
    for command in commands:
        command_list = command.replace('move ', '').replace('from ', '').replace('to ', '').strip('\n').split(' ')
        num_boxes = int(command_list[0])
        original_loc = int(command_list[1])
        new_loc = int(command_list[2])
        move_boxes_part2(diagram_dict_2, num_boxes, original_loc, new_loc)

    # Get top crates
    message = ''
    for i in range(1, len(diagram_dict_2)+1):
        message += diagram_dict_2[i][-1]
    print("Part 2: %s" % message)

if __name__ == '__main__':
    main()
