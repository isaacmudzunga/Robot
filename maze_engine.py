from collections import deque

def convert_instructions(instruction, output_list):
    """
        function convert instructions to a shorter list
        parameter instruction is a list with instructions that need to be converted
        output_list is a list with converted instructions
    """

    while True:
        if len(instruction) == 1:
            break

        count = 0
        command = instruction[0]
        while command == instruction[0]:
            count += 5
            command = instruction.pop(0)

        output_list.append((command, count))

    return output_list

def edge_finder(direction, obst_import):
    """
        function finds a valid point at the edge and return points in 
        tuple form
    """
 
    direction_dict = {"U": (-60,200), "D": (-60,-200), \
                        "R": (100,-90), "L": (-100,-90)}
    x, y  = direction_dict[direction]

    if direction == "U" or direction == "D":
        while obst_import.is_position_blocked(x,y):
            x += 5
    else:
        while obst_import.is_position_blocked(x,y):
            y += 5   
             
    return (x, y)

def search_route(direction, start_x, start_y, edge_x, edge_y, obst_import):
    """
        function use breath first search method
        parameter direction is a robot command, move robot to where user wants
        obst_import import maze module
    """
    
    first = deque()
    dic_solution = dict()
    visited = list()

    x = edge_x
    y = edge_y    

    first.append((x, y))
    dic_solution[x,y] = x,y

    while len(first) > 0:
        x, y = first.popleft()

        for i in ["U", "R", "D", "L"]:
            block = x_y(x, y, i, 5)
            if not obst_import.is_path_blocked(x,y, block[0], block[1]) and (-101 <= block[0] <= 101 and -201 <= block[1] <= 201) and block not in visited:
                dic_solution[block] = x, y   
                first.append(block)
                visited.append(block)

    return dic_solution

def convert_coordinates(value1, value2, positive, negative):
    """
        function also convert coordinates to instructions
    """
    
    if value1 < value2:
        return positive
    else:
        return negative


def instruct_(cord_list, instruction):
    """
        function converts coordinates to cord_list into instructions
        parameter cord_list is a list with coordinates from start point to end point
    """

    for i in range(0, len(cord_list)-1):

        if cord_list[i][0] == cord_list[i+1][0]:
            instruction.append(convert_coordinates(cord_list[i][1],\
                                    cord_list[i+1][1],"U","D"))
        else:
            instruction.append(convert_coordinates(cord_list[i][0],\
                                    cord_list[i+1][0],"R","L"))

    instruction.append("")

    return convert_instructions(instruction, [])


def back_path(dic_solution, edge_x, edge_y, x, y):
    """
        function finds back path
        parameter dic_solution is a dictionary with solution to maze
        x,y are the starting point
        edge_x, edge_y the coordinates of the edge
    """

    cord_list = [(x,y)]

    while (x, y) != (edge_x, edge_y):
        x, y = dic_solution[x, y] 
        cord_list.append((x,y))

    return instruct_(cord_list, [])


def x_y(x, y, todo, step):
    """
        function returns dictionary of direction
    """
    
    direction_dict = {"U": (x,y+step), "D": (x,y-step), \
                        "R": (x+step,y), "L": (x-step,y)}
    
    return direction_dict[todo]


