import random

global obsatcles_list
obsatcles_list = []

def get_obstacles():
    """
        Function Randomly generates a maze(maze_world)
        returns list with obstacles (x,y)
    """
    y_coordinate = -200
    for y in range(0,20):
        x_coordinate = -100
        for x in range(0,10):
            if not (y_coordinate in range(-20,20) and x_coordinate in range(-20,20)):
                list_obst = populate_pixels_obstacles(x_coordinate,y_coordinate)
            x_coordinate += 20
        y_coordinate += 20

    return list_obst

def populate_pixels_obstacles(x_coordinate,y_coordinate):
    """
        Function randomly populates a 20 by 20 pixel of obstacles.
        parameter x_coordinate, y_coordinate: start coordinates
        returns list with randomly populated obstacles
    """
    global obsatcles_list

    for y in range(0,4):
        for x in range(0,4):
            if random.randint(1,20) % 4 == 0:
                obsatcles_list.append((x_coordinate,y_coordinate))
            x_coordinate += 5
        x_coordinate -= 20
        y_coordinate += 5

    return obsatcles_list

def compare_values(value_1, value_2):
    """
        returns smallest value first
    """
    if value_1 > value_2:
        return value_2, value_1

    return value_1, value_2
    
def is_position_blocked(x,y):
    """
        function checks if given position is blocked with an obstacle
        returns false if position is not blocked, true if it is
    """
    global obsatcles_list

    for obstacle in obsatcles_list:
        if x in range(obstacle[0], obstacle[0]+5) and y in range(obstacle[1], obstacle[1]+5):
            return True

    return False

def is_path_blocked(x1,y1, x2, y2):
    """ 
        returns true if path is blocked, false if not blocked
    """
    if y1 == y2:
        x1, x2 = compare_values(x1, x2)
        for x in range(x1, x2):
            if is_position_blocked(x, y1):
                return True
    else:
        y1, y2 = compare_values(y1, y2)
        for y in range(y1, y2):
            if is_position_blocked(x1, y):
                return True
                
    return False