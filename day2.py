# Functions
def getScore(data):
    # Define scores
    score = {
        "X": 1,
        "Y": 2,
        "Z": 3,
    }
    return score[data[1]]

def isWin(data):
    # Define win and draw conditions
    opponent_move = data[0]
    your_move = data[1]
    # Move to numbers
    opponent_move_num = {
        "A": 0,
        "B": 1,
        "C": 2,
    }
    your_move_num = {
        "X": 0,
        "Y": 1,
        "Z": 2,
    }
    diff = (your_move_num[your_move] - opponent_move_num[opponent_move]) % 3
    if diff == 0:
        return 3
    elif diff == 1:
        return 6
    elif diff == 2:
        return 0

def getMove(data):
    opponent_move = data[0]
    win_result = data[1]
    # Move to numbers
    opponent_move_num = {
        "A": 0,
        "B": 1,
        "C": 2,
    }
    your_move_num = {
        0: "A",
        1: "B",
        2: "C",
    }
    if win_result == "Y":
        return your_move_num[opponent_move_num[opponent_move]]
    elif win_result == "X":
        return your_move_num[(opponent_move_num[opponent_move]+2) % 3]
    elif win_result == "Z":
        return your_move_num[(opponent_move_num[opponent_move]+1) % 3]

def getScorePart2(move):
    score = {
        "A": 1,
        "B": 2,
        "C": 3,
    }
    return score[move]


def isWinPart2(data):
    win_result = data[1]
    if win_result == "X":
        return 0
    elif win_result == "Y":
        return 3
    elif win_result == "Z":
        return 6


def main():
    # Get input
    with open("day2/input.txt", 'r') as f:
        nums = [line for line in f.readlines()]

    # Split up data
    split_data = [num.strip('\n').split(' ') for num in nums]

    # Part 1
    scores = [getScore(data)+isWin(data) for data in split_data]
    print("Part 1: %i" % sum(scores))

    # Part 2
    moves = [getMove(data) for data in split_data]
    scores = [getScorePart2(move)+isWinPart2(data) for move, data in zip(moves, split_data)]
    print("Part 2: %i" % sum(scores))

if __name__ == '__main__':
    main()