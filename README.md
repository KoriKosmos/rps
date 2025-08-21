# Rock Paper Scissors

This is a simple Python script that lets you play Rock Paper Scissors against the computer.

## Features
- Play interactively in the terminal
- Random computer choices
- Keeps score of wins, losses, and ties

## Requirements
- Python 3.x


## Usage
### Terminal Version
1. Open a terminal and navigate to the project directory.
2. Run the script:
	```powershell
	python rps.py
	```
3. Follow the on-screen prompts to play.

### GUI Version
1. Open a terminal and navigate to the project directory.
2. Run the GUI script:
	```powershell
	python rps_gui.py
	```
3. A window will open where you can play using buttons and see your score.

### Packaging as an Executable
You can package either version as a standalone executable using PyInstaller and UV:
```powershell
uv add pyinstaller
uv run pyinstaller --onefile rps.py      # For terminal version
uv run pyinstaller --onefile rps_gui.py  # For GUI version
```
The executable will be created in the `dist` folder.

#### Pre-built Executables
You can also download ready-to-run executables from the [Releases](https://github.com/KoriKosmos/rps/releases) section of this repository.


## How it works
You will be prompted to enter your choice (rock, paper, or scissors). The computer will randomly select its choice, and the winner will be displayed. The game can be played repeatedly until you choose to exit.

## Persistent Score Tracking
Global wins, losses, and ties are tracked across sessions using a `scores.json` file in the same folder as the script. This file is automatically created and updated as you play.

**Tip:** For best results, run the script in a dedicated folder to keep your score file organized and avoid conflicts with other projects.
