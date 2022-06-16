"""
Author: Noa Kirschbaum
Assignment / Part: HW4 - Q1
Date due: 2022-06-21
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

def initialize_world(in_filepath):
    # use error handling to deal with case where there is no input file
    # if error, return an empty world and do not allow anything else to happen
    try:
        file = open(in_filepath, 'r')
    except FileNotFoundError:
        return []
    row_list = [line.strip() for line in file]
    file.close()
    return row_list


def count_neighbors(world, position):
    # position is a row and column
    # count number of living neighbors next to the position

    if position[0] == 0:  # if row is the first row
        if position[1] == 0:  # if column is the leftmost (first) column
            neighbor_list = [world[position[0]][position[1] + 1], world[position[0] + 1][position[1]], world[position[0] + 1][position[1] + 1]]
        elif position[1] == len(world[position[0]]) - 1:  # column is rightmost (last) column
            neighbor_list = [world[position[0]][position[1] - 1], world[position[0] + 1][position[1]], world[position[0] + 1][position[1] - 1]]
        else:  # any column in the middle
            neighbor_list_nextTo = [world[position[0]][position[1] - 1], world[position[0]][position[1] + 1]]
            neighbor_list_below = [world[position[0] + 1][position[1] - 1], world[position[0] + 1][position[1]], world[position[0] + 1][position[1] + 1]]
            neighbor_list = neighbor_list_nextTo + neighbor_list_below
    elif position[0] == len(world)-1:  # if row is the last row
        if position[1] == 0:  # if column is the leftmost (first) column
            neighbor_list = [world[position[0]][position[1] + 1], world[position[0] - 1][position[1]], world[position[0] - 1][position[1] + 1]]
        elif position[1] == len(world[position[0]]) - 1:  # column is rightmost (last) column
            neighbor_list = [world[position[0]][position[1] - 1], world[position[0] - 1][position[1]], world[position[0] - 1][position[1] - 1]]
        else:  # any column in the middle
            neighbor_list_nextTo = [world[position[0]][position[1] - 1], world[position[0]][position[1] + 1]]
            neighbor_list_above = [world[position[0] - 1][position[1] - 1], world[position[0] - 1][position[1]], world[position[0] - 1][position[1] + 1]]
            neighbor_list = neighbor_list_nextTo + neighbor_list_above
    else:  # any row in the middle
        if position[1] == 0:  # leftmost column
            neighbor_list_above = [world[position[0] - 1][position[1]], world[position[0] - 1][position[1] + 1]]
            neighbor_list_nextTo = [world[position[0]][position[1] + 1]]
            neighbor_list_below = [world[position[0] + 1][position[1]], world[position[0] + 1][position[1] + 1]]
            neighbor_list = neighbor_list_above + neighbor_list_nextTo + neighbor_list_below
        elif position[1] == len(world[position[0]]) - 1:  # rightmost
            neighbor_list_above = [world[position[0] - 1][position[1]]]
            neighbor_list_nextTo = [world[position[0]][position[1] - 1]]
            neighbor_list_below = [world[position[0] + 1][position[1]]]
            neighbor_list = neighbor_list_above + neighbor_list_nextTo + neighbor_list_below
        else:  # middle columns
            neighbor_list_above = [world[position[0] - 1][position[1] - 1], world[position[0] - 1][position[1]], world[position[0] - 1][position[1] + 1]]
            neighbor_list_nextTo = [world[position[0]][position[1] - 1], world[position[0]][position[1] + 1]]
            neighbor_list_below = [world[position[0] + 1][position[1] - 1], world[position[0] + 1][position[1]], world[position[0] + 1][position[1] + 1]]
            neighbor_list = neighbor_list_above + neighbor_list_nextTo + neighbor_list_below

    living_neighbors = 0
    for item in neighbor_list:
        if item == "*":
            living_neighbors += 1

    return living_neighbors


def compute_next_generation(start_gen):
    # call count_neighbors in here
    # dashes are dead, asterisks are alive
    for row in range(len(start_gen)):
        current_row = start_gen[row]
        for column in range(len(current_row)):
            living_neighbors = count_neighbors(start_gen, (row, column))
            print(row, column, living_neighbors)

    return []



#def display_world(world):
    # print representation of world to the screen, looks like input file



def main():
    # print original and then 10 generations after
    first_world = initialize_world("life.txt")
    print("first world:", first_world)
    next_world = compute_next_generation(first_world)
    print(next_world)


if __name__ == "__main__":
    main()













