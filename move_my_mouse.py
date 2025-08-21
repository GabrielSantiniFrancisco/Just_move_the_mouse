# Author : Gabriel Francisco
# Email  : gabrielsantinifrancisco@outlook.com

# Description:
# This script automates mouse movement using the pyautogui library. It provides functions to:
# - Calculate the center of the main screen.
# - Move the mouse cursor to the center of the main screen.
# - Move the mouse cursor to random positions within a 250-pixel radius from the center of the main screen at regular intervals.
# When run directly, the script moves the mouse cursor to the center of the main screen,
# then starts random mouse movements within a 250-pixel radius from the center.
# Press Ctrl+C to terminate the script.

##########################
# INITIAL SETUP
##########################

import pyautogui
import time
import random
import math
from screeninfo import get_monitors

##########################
# FUNCTIONS
##########################

def get_main_screen_center() -> tuple[int, int]:
    """
    Calculates and returns the coordinates of the center point of the main screen.
    Returns:
        tuple[int, int]: A tuple containing the (x, y) coordinates of the center of the main screen.
    """
    monitors = get_monitors()
    if not monitors: return pyautogui.size()

    try: 
        main_screen = monitors[m_number]  
    except Exception:
        main_screen = monitors[m_number]

    center_x = main_screen.width // 2 + main_screen.x
    center_y = main_screen.height // 2 + main_screen.y

    return center_x, center_y

def move_to_center() -> None:
    """
    Moves the mouse cursor to the center of the main screen.

    Retrieves the center coordinates of the main screen using `get_main_screen_center()`,
    then moves the mouse cursor to that position over 0.5 seconds using `pyautogui.moveTo`.
    After moving, the function pauses execution for 20 seconds.
    
        Returns:
            None
    """
    center_x, center_y = get_main_screen_center()
    pyautogui.moveTo(center_x, center_y, duration=0.5)
    time.sleep(20)

def random_mouse_movement() -> None:
    """
    Moves the mouse cursor to random positions within a 250-pixel radius from the center of the main screen.

    The function continuously selects a random angle and radius, calculates a new position within the allowed radius,
    and moves the mouse cursor to that position over 0.5 seconds. If the calculated position exceeds the 250-pixel radius,
    the direction is reversed to keep the movement within bounds. The function pauses for 20 seconds after each move.

    Returns:
        None
    """
    screen_width, screen_height = pyautogui.size()
    initial_x, initial_y = get_main_screen_center()

    while True:
        angle = random.uniform(0, 2 * 3.14159)  
        radius = random.uniform(0, 250)  

        x_offset = int(radius * round(math.cos(angle)))
        y_offset = int(radius * round(math.sin(angle)))

        new_x = max(0, min(screen_width - 1, initial_x + x_offset))
        new_y = max(0, min(screen_height - 1, initial_y + y_offset)) 

        if math.sqrt((new_x - initial_x)**2 + (new_y - initial_y)**2) > 250:
            x_offset *= -1
            y_offset *= -1

            new_x = max(0, min(screen_width - 1, initial_x + x_offset))
            new_y = max(0, min(screen_height - 1, initial_y + y_offset))

        pyautogui.moveTo(new_x, new_y, duration=0.5)
        time.sleep(20)

##########################
# MAIN VARIABLES
##########################
m_number = 0

##########################
# DEFAULT EXECUTION
##########################

if __name__ == "__main__":
    """
    When run directly, the script moves the mouse cursor to the center of the main screen,
    then starts random mouse movements within a 250-pixel radius from the center.
    Press Ctrl+C to terminate the script.
    """
    try:
        move_to_center()
        random_mouse_movement()
    except KeyboardInterrupt:
        print("Script terminated.")
