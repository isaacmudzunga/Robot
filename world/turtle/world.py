import turtle as toy
import sys
import import_helper

global obs

def obs_import():
    """
        function returns module
    """
    global obs

    return obs

def constraits_box():
    """
        function draws the robots constraints box 
    """
    toy.goto(-100,200)
    toy.pencolor("black")
    toy.pensize(3)
    toy.pendown()
    toy.goto(100,200)
    toy.goto(100,-200)
    toy.goto(-100,-200)
    toy.goto(-100,200)
    toy.penup()


def toy_home():
    """
        function  resets and take toy to point(0,0)
    """
    toy.color("red")
    toy.home()
    toy.left(90)


def toy_turn_left():
    """
        make toy turn left
    """
    toy.left(90)


def toy_turn_right():
    """
        make toy turn right 
    """
    toy.right(90)


def draw_one_obstacle(x,y):
    """
        function draws one obstacle in toy mode
        parameter x is an obstacle in x position
        parameter y is an obstacle in y position
    """
    toy.begin_fill()
    toy.goto(x,y)
    toy.pendown()
    toy.goto(x+4,y)
    toy.goto(x+4,y+4)
    toy.goto(x,y+4)
    toy.goto(x,y)
    toy.end_fill()
    toy.penup()


def draw_obstacle(robot_name):
    """
        draws all obstacles one by one and resets toy
    """
    global obs

    values = sys.argv[len(sys.argv)-1].lower()
    if values == "toy":
        values = "obs"
    
    obs = import_helper.dynamic_import("maze."+values)
    print(''+robot_name+': Loaded '+values+'.')

    obstacles_list = obs.get_obstacles()
    for obstacle in obstacles_list:
        draw_one_obstacle(obstacle[0], obstacle[1])


def printing_obstacles(robot_name):
    """
        function prints a list of obstacles
    """
    pass
        
def show_position(robot_name,position_x,position_y):    
    """
        prints current postion of toy
    """
    toy.goto(position_x,position_y)
    
    
def is_position_allowed(new_x, new_y, position_x, position_y):
    """
        Checks if the new position will still fall within the max area limit
        :param new_x: the new/proposed x position
        :param new_y: the new/proposed y position
        :return: True if allowed, i.e. it falls in the allowed area, else False
    """
    min_y, max_y = -200, 200
    min_x, max_x = -100, 100
    
    return min_x <= new_x <= max_x and min_y <= new_y <= max_y,obs.is_path_blocked(position_x,position_y, new_x, new_y)


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


def setting_toy(robot_name):
    """
        initialize toy
    """
    toy.title(robot_name)
    toy.Screen().bgcolor("deep sky blue")
    toy.tracer(5,2)
    toy.penup()
    constraits_box()
    draw_obstacle(robot_name)
    toy_home()
    toy.penup()
    toy.tracer(1)
