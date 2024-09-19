# Umpire DRS Kit

## Overview
The Umpire DRS Kit is a Python application designed to simulate the Decision Review System (DRS) used in cricket. It enables umpires to analyze video clips with controls for playback speed and decision-making.

## Features
- **Video Playback**: Play video forward or backward at adjustable speeds.
- **Decision Display**: Show "OUT" or "NOT OUT" decisions with graphics.
- **Sponsorship Display**: Display sponsor images during decision-making.
- **Threading Support**: Ensures smooth UI while processing decisions.

## Requirements
- Python 3.x
- Libraries:
  - `opencv-python`
  - `Pillow`
  - `imutils`
  - `tkinter` (included with Python)

## Installation
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <project_directory>
   ```

2. Install required packages:
   ```bash
   pip install opencv-python Pillow imutils
   ```

3. Ensure you have the following images in your project directory:
   - `welcome1.png`
   - `des.png`
   - `sponser.png`
   - `out.png`
   - `not_out.png`
   - `throw.ico`

## Usage
1. Run the application:
   ```bash
   python main.py
   ```

2. Control playback using the following buttons:
   - **Previous Slow**: Move back a few frames slowly.
   - **Previous Fast**: Move back quickly.
   - **Next Slow**: Move forward a few frames slowly.
   - **Next Fast**: Move forward quickly.
   - **OUT**: Declare "OUT".
   - **NOT OUT**: Declare "NOT OUT".

## Code Structure
- **Imports**: Necessary libraries for GUI, video processing, and threading.
- **Functions**:
  - `play(speed)`: Controls playback speed.
  - `pending(decision)`: Displays decision pending screen and final decision.
  - `out()` / `not_out()`: Handle decision threads.
- **Main Window**: Sets up the tkinter GUI and buttons.


## Contributing
Contributions are welcome! Feel free to submit issues or pull requests.

