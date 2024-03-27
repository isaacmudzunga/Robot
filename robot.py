import sys
import turtle
import maze_engine as mazern

#imoprt text or turtle world
toy_ = False
if "turtle" in sys.argv:
    from world.turtle.world import *
    toy_ = True
else:
    from world.text.world import *


# list of valid command names
valid_commands = ['off', 'help', 'forward', 'back', 'right', 'left', 'sprint',
                 'replay', 'silent', 'reversed', 'mazerun']

# variables tracking position and direction
global position_x, position_y, history_commands
history_commands = []

position_x = 0
position_y = 0
current_direction_index_ = 0


def get_robot_name():
    """
        function gets robot name
    """
    name = input("What do you want to name your robot? ")
    while len(name) == 0:
        name = input("What do you want to name your robot? ")
    return name


def get_command(robot_name):
    """
        Asks the user for a command, and validate it as well
        Only return a valid command
    """

    prompt = ''+robot_name+': What must I do next? '
    command = input(prompt)
    while len(command) == 0 or not valid_command(command):
        output(robot_name, "Sorry, I did not understand '"+command+"'.")
        command = input(prompt)
    return command.lower()

def do_help():
    """
        Provides help information to the user
        :return: (True, help text) to indicate robot can continue after this command was handled
    """
    return True, """I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD - move forward by specified number of steps, e.g. 'FORWARD 10'
BACK - move backward by specified number of steps, e.g. 'BACK 10'
RIGHT - turn right by 90 degrees
LEFT - turn left by 90 degrees
SPRINT - sprint forward according to a formula
REPLAY {n-m}- replay history commands n is start index_ m is end index_ 
SILENT - DOES COMMANDS SILENTLY
REVERSED - DOES COMMANDS IN REVERSE
"""


def split__input(command):
    """
        Splits the string at the first space character, to get the actual command, as well as the argument(s) for the command
        :return: (command, argument)
    """
    args = command.split(' ', 1)
    if len(args) > 1:
        return args[0], args[1]
    return args[0], ''


def is_int(value):
    """
        Tests if the string value is an int or not
        :param value: a string value to test
        :return: True if it is an int
    """
    try:
        int(value)
        return True
    except ValueError:
        return False


def check_range(command_):
    """
        function checks if the command range valid
        parameter command_ replay range as string
        return t_or_f boolean t_or_f true if range is valid
    """
    t_or_f = False
    if command_.find("-"):
        range_ = command_.split("-")
    if len(range_) == 2:
        if range_[0].isdigit() and range_[1].isdigit():
            t_or_f = True
    if command_.isdigit():
        t_or_f = True
    return t_or_f


def check_valid_command(value):
    """
        function check if movement command valid
    """
    if value in valid_commands:
        return value
    if check_range(value):
        return value
    return ""


def valid_command(command):
    """
        Returns a boolean indicating if the robot can understand the command or not
        Also checks if there is an argument to the command, and if it a valid int
    """
    check_command = command.lower().split(" ")

    maze_directions_commands = ["bottom", "top", "left", "right"]

    if check_command[0] == "mazerun" and len(check_command) <= 2:
        if len(check_command) == 2:
            return check_command[1] in maze_directions_commands
        return True

    if check_command[0] == "replay":
        my_valid_command = list(filter(lambda x: x != "", list(map(check_valid_command ,check_command))))
        if check_command == my_valid_command:
            return True

    (command_name, arg1) = split__input(command)

    return command_name.lower() in valid_commands and (len(arg1) == 0 or is_int(arg1))


def output(name, message):
    """
        function prints output message
    """
    print(''+name+": "+message)



def do_forward(robot_name, steps):
    """
        Moves the robot forward the number of steps
        :param robot_name:
        :param steps:
        :return: (True, forward output text)
    """
    global position_x, position_y, current_direction_index_

    area_t_or_f, obstacle_t_or_f, new_x, new_y = update_position(steps, position_x, position_y, current_direction_index_)
    if area_t_or_f and not obstacle_t_or_f:
        position_x = new_x
        position_y = new_y
        return True, ' > '+robot_name+' moved forward by '+str(steps)+' steps.'
    if obstacle_t_or_f:
        return True, ''+robot_name+': Sorry, there is an obstacleacle in the way.'
    if not area_t_or_f:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe area.'


def do_back(robot_name, steps):
    """
        Moves the robot forward the number of steps
        :param robot_name:
        :param steps:
        :return: (True, forward output text)
    """
    global position_x, position_y, current_direction_index_

    area_t_or_f, obstacle_t_or_f, new_x, new_y = update_position(-steps, position_x, position_y, current_direction_index_)
    if area_t_or_f and not obstacle_t_or_f:
        position_x = new_x
        position_y = new_y
        return True, ' > '+robot_name+' moved back by '+str(steps)+' steps.'
    if obstacle_t_or_f:
        return True, ''+robot_name+': Sorry, there is an obstacleacle in the way.'
    if not area_t_or_f:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe area.'


def do_right_turn(robot_name):
    """
        Do a 90 degree turn to the right
    """

    global current_direction_index_

    current_direction_index_ += 1
    if current_direction_index_ > 3:
        current_direction_index_ = 0

    if toy_:
        toy_turn_right()

    return True, ' > '+robot_name+' turned right.'


def do_left_turn(robot_name):
    """
        Do a 90 degree turn to the left
    """

    global current_direction_index_

    current_direction_index_ -= 1
    if current_direction_index_ < 0:
        current_direction_index_ = 3

    if toy_:
        toy_turn_left()

    return True, ' > '+robot_name+' turned left.'


def do_sprint(robot_name, steps):
    """
        Sprints the robot, i.e. let it go forward steps + (steps-1) + (steps-2) + .. + 1 number of steps, in iterations
        :param robot_name:
        :param steps:
        :return: (True, forward output)
    """

    if steps == 1:
        return do_forward(robot_name, 1)
    else:
        (do_next, command_output) = do_forward(robot_name, steps)
        print(command_output)
        return do_sprint(robot_name, steps - 1)


def reversed_replay(history_commands, reverse):
    """
        function that reverses history_commands if reverse is set to true
        :param history_commands: list of history commands
        :param reverse: boolean true/flase true if reverse needed
        :return history_commands: list of history commands
        :return reverse_: prefix to add to output command
    """
    reverse_ = ""
    if reverse:
        history_commands = list(filter(lambda x: x != "",history_commands[::-1]))
        reverse_ = " in reverse"
    else:
        history_commands = list(filter(lambda x: x != "",history_commands))
    return history_commands, reverse_


def replay_silent(silent):
    """
        functions that handels silent command
        parameter silent return boolean true if silent
        silent_ return prefix to add to output command
    """
    silent_ = ""
    if silent:
        silent_ = " silently"
    return silent_


def valid_replay_command(command):
    """
        checks input commands with listed commands and returns commands
    """
    movements = ['forward', 'back', 'right', 'left', 'sprint']
    for movement in movements:
        if movement in command:
            return command


def split__(movement):
    """
        splits replay range if "-" found
    """
    n = movement
    m = "0"
    if movement.find("-") > -1:
        slit_range = movement.split("-")
        n = slit_range[0]
        m = slit_range[1]
    return int(n), int(m)


def check_replay_range(command):
    """
        function check replay range
        parameter command store commands
        t_or_f  return boolean true if range valid
        return n, m int range
    """
    split_ = command.split(" ")
    n = 0
    m = 0
    t_or_f = False
    for movement in split_:
        if any(map(str.isdigit, movement)):
            t_or_f = True
            n, m = split__(movement)
    return t_or_f, n, m
    

def do_replay(robot_name, history_commands, command, reverse, silent):
    """
        replay command history.
        :param history_commands: history commands
        :param command: last inputed command
        :param reverse: boolean true if output must be in reverse
        :param silent: boolean true if output must be silent
    """
    replay_range, n, m = check_replay_range(command)

    movements = ['forward', 'back', 'right', 'left', 'sprint']
    history_commands = list(map(valid_replay_command, history_commands))
    history_commands =list(filter(lambda x: x != None, history_commands))

    history_commands, reverse_ = reversed_replay(history_commands, reverse)
    silent_ = replay_silent(silent)

    if replay_range:
        index_ = len(history_commands) - n
        history_commands = history_commands[index_:]

    x = 0
    for command in history_commands:
        handle_command(robot_name, command, history_commands, silent)
        if x == m and m > 0:
            break
        x += 1
    
    return True, " > {} replayed {} commands{}{}.".format(robot_name, len(history_commands) - m, reverse_, silent_), False

def add_history_commands(command, history_commands):
    """Function adds give command to the command history"""
    history_commands.append(command)
    return history_commands


def turn_robot(command):
    """
        Function turns the robot in the direction of the give command
        parameter command is the direction you wish the robot to face
    """
    global current_direction_index_, history_commands, robot_name

    directions_dict = {"U": 0, "R": 1, "D": 2, "L": 3}

    while current_direction_index_ != directions_dict[command]:
        handle_command(robot_name, "left", history_commands, False)


def maze_way(cord_list, direction):
    """
        function moves the maze to a given edge
        parameter cord_list the way past the obstacles
        parameter direction the heading the robot must go
    """
    global history_commands, robot_name, position_x, position_y

    for movement in cord_list:
        command, count = movement
        turn_robot(command)
        handle_command(robot_name, "forward "+str(count),history_commands, False)

    turn_robot(direction)
    handle_command(robot_name, "forward 10", history_commands, False)


def maze_solver(direction):
    """
        Function auto sloves a given maze with obstacleacle from point (0,0) to given direction
        parameter direction is a robot command, move robot to where user wants
    """
    global history_commands, robot_name, position_x, position_y

    obstacle_import = obs_import()

    end_x, end_y = mazern.edge_finder(direction, obstacle_import)
    solution = mazern.search_route(direction, position_x, position_y,end_x, end_y, obstacle_import)
    cord_list = mazern.back_path(solution, end_x, end_y, position_x, position_y)

    maze_way(cord_list, direction)

def handle_command(robot_name, command, history_commands, silent):
    """
        Handles a command by asking different functions to handle movement command.
        :param robot_name: the name given to robot
        :param command: the command entered by user
        :return: `True` if the robot must continue after the command, or else `False` if robot must shutdown
    """
    global position_x, position_y

    command_name = ""
    arg = ""

    direction = "top"
    directions_dict = {"top": "U", "bottom": "D", "left": "L", "right" : "R"}
    
    reverse = False

    if command.find("replay") != -1:
        if command.find("silent") != -1:
            silent = True
        if command.find("reversed") != -1:
            reverse = True
        (do_next, command_output, silent) = do_replay(robot_name, history_commands, command, reverse, silent)

    maze_way = False
    maze_directions_commands = ""
    if "mazerun" in command:
        maze_way = True
    else:
        (command_name, arg) = split__input(command)

    if command_name == 'off':
        return False
    elif command_name == 'help':
        (do_next, command_output) = do_help()
    elif command_name == 'forward':
        (do_next, command_output) = do_forward(robot_name, int(arg))
    elif command_name == 'back':
        (do_next, command_output) = do_back(robot_name, int(arg))
    elif command_name == 'right':
        (do_next, command_output) = do_right_turn(robot_name)
    elif command_name == 'left':
        (do_next, command_output) = do_left_turn(robot_name)
    elif command_name == 'sprint':
        (do_next, command_output) = do_sprint(robot_name, int(arg))
    elif maze_way:
        if " " in command:
            maze_directions_commands = command.split(" ")
            direction = maze_directions_commands[1]

        print("> {} starting maze run..".format(robot_name))
        maze_solver(directions_dict[direction])
        do_next = True
        command_output = "{}: I am at the {} edge.".format(robot_name, direction)
    
    if not silent:
        print(command_output)
        show_position(robot_name, position_x, position_y)

    return do_next

def robot_start():
    """
        This is the entry point for starting my robot
    """
    global position_x, position_y, current_direction_index_, robot_name, history_commands
    position_x = 0
    position_y = 0
    current_direction_index_ = 0

    robot_name = get_robot_name()
    output(robot_name, "Hello kiddo!")

    if toy_:
        setting_toy(robot_name)
    
    printing_obstacles(robot_name)

    history_commands = []
    command = get_command(robot_name)
    silent = False
    while handle_command(robot_name, command, history_commands, silent):
        history_commands = add_history_commands(command, history_commands)
        command = get_command(robot_name)

    output(robot_name, "Shutting down..")


if __name__ == "__main__":
    robot_start()