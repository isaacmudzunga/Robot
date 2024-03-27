import random

global obstacles_list
obstacles_list = []

def random_obstacles():
    """
        Generate random list of obstacles.
    """
    global obstacles_list

    obstacles_list = [(random.randint(-100,100),random.randint(-200,200)) for i in range(0,random.randint(1,10))]

    return obstacles_list

def get_obstacles():
    """
        returns random obstacles
    """
    return random_obstacles()

def check_value(value_1, value_2):
    """
        check smallest value 
    """
    if value_1 > value_2:
        return value_2, value_1

    return value_1, value_2

def is_position_blocked(x, y):
    """
        Checks position of the obstacle and the coordinates inside the obstacles.
    """
 
    global obstacles_list

    for obstacles in obstacles_list:
        if x in range(obstacles[0], obstacles[0]+5) and y in range(obstacles[1], obstacles[1]+5):
            return True

    return False

    
def is_path_blocked(x1, y1, x2, y2):
    """
        Responsible for the path in which the robot will be going 
        and block it so it doesn't collide with an obstacle.
        return true if path is blocked
        return false if path is not blocked
    """
    if y1 == y2:
        x1, x2 = check_value(x1, x2)
        for x in range(x1, x2):
            if is_position_blocked(x, y1):
                return True
    else:
        y1, y2 = check_value(y1, y2)
        for y in range(y1, y2):
            if is_position_blocked(x1, y):
                return True
    return False
