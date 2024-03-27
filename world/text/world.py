import sys
import import_helper

# global obs, values
values = "obs"
obs = import_helper.dynamic_import("maze.obstacles")
# values = "obs"
    
if "text" in sys.argv and len(sys.argv) == 3:
    values = sys.argv[len(sys.argv)-1]
    obs = import_helper.dynamic_import("maze."+values)


def obs_import():
    """
        function returns module
    """
    global obs

    return obs


def printing_obstacles(robot_name):
    """
        print all obstacles
    """
    global obs, values

    print(''+robot_name+': Loaded obstacles.')

    obstacles_list = obs.get_obstacles()

    if len(obstacles_list) > 0:
        print("There are some obstacles:")
        for obstacle in obstacles_list:
            print("- At position {},{} (to {},{})".format(obstacle[0], obstacle[1], obstacle[0]+4, obstacle[1]+4))


def show_position(robot_name, position_x, position_y):
    """
        prints current position of toy
    """
    print(' > '+robot_name+' now at position ('+str(position_x)+','+str(position_y)+').')


def is_position_allowed(new_x, new_y, position_x, position_y):
    """
        Checks if the new position will still fall within the max area limit
        :param new_x: the new/proposed x position
        :param new_y: the new/proposed y position
        :return: True if allowed, i.e. it falls in the allowed area, else False
    """
    global obs
    
    # area limit vars
    min_y, max_y = -200, 200
    min_x, max_x = -100, 100

    return min_x <= new_x <= max_x and min_y <= new_y <= max_y, obs.is_path_blocked(position_x,position_y, new_x, new_y)


def update_position(steps, position_x, position_y, current_direction_index):
    """
        Update the current x and y positions given the current direction, and specific nr of steps
        :param steps:
        :return: True if the position was updated, else False
    """

    directions = ['forward', 'right', 'back', 'left']

    new_x = position_x
    new_y = position_y

    if directions[current_direction_index] == 'forward':
        new_y = new_y + steps
    elif directions[current_direction_index] == 'right':
        new_x = new_x + steps
    elif directions[current_direction_index] == 'back':
        new_y = new_y - steps
    elif directions[current_direction_index] == 'left':
        new_x = new_x - steps

    area, obst_ = is_position_allowed(new_x, new_y, position_x, position_y)
    if area and not obst_:
        return area, obst_, new_x, new_y
    return area, obst_, position_x, position_y