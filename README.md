# Just Move The Mouse

## Overview
This script, inspired by the advanced automation capabilities of Skynet, is designed to simulate alien-like mouse movements on your computer screen. It leverages the `pyautogui` library to automate mouse movements, providing functionality to:

- Calculate the center of the main screen.
- Move the mouse cursor to the center of the main screen.
- Perform random mouse movements within a 250-pixel radius from the center of the main screen at regular intervals.

## Features
- **Main Screen Centering**: Automatically calculates and moves the mouse to the center of the main screen.
- **Randomized Movements**: Simulates random mouse movements within a defined radius, mimicking alien-like behavior.
- **Customizable Intervals**: Pauses for 20 seconds between movements, ensuring a natural flow.

## Requirements
- Python 3.6+
- Libraries:
  - `pyautogui`
  - `screeninfo`

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/GabrielSantiniFrancisco/Just_move_the_mouse.git
   ```
2. Navigate to the project directory:
   ```bash
   cd <project-directory>
   ```
3. Install the required dependencies:
   ```bash
   pip install pyautogui screeninfo
   ```

## Usage
1. Run the script:
   ```bash
   python <script-name>.py
   ```
2. The script will:
   - Move the mouse to the center of the main screen.
   - Start random mouse movements within a 250-pixel radius from the center.

3. To terminate the script, press `Ctrl+C`.

## Code Structure
- **`get_main_screen_center()`**: Calculates the center of the main screen.
- **`move_to_center()`**: Moves the mouse to the center of the main screen.
- **`random_mouse_movement()`**: Simulates random mouse movements within a 250-pixel radius.

## Notes
- Ensure that the required libraries are installed before running the script.
- The script is designed for educational and entertainment purposes. Use responsibly.

## Disclaimer
This script is a fun automation tool and is not intended for malicious purposes. Always ensure compliance with local laws and regulations when using automation tools.
