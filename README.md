# Rock Paper Scissors

This is a simple Python script that lets you play Rock Paper Scissors against the computer.

## Features
- Play interactively in the terminal
- Random computer choices
- Keeps score of wins, losses, and ties

## Requirements
- Python 3.x

## Usage
1. Open a terminal and navigate to the project directory.
2. Run the script:
	```powershell
	python rps.py
	```
3. Follow the on-screen prompts to play.


## How it works
You will be prompted to enter your choice (rock, paper, or scissors). The computer will randomly select its choice, and the winner will be displayed. The game can be played repeatedly until you choose to exit.

## Persistent Score Tracking
Global wins, losses, and ties are tracked across sessions using a `scores.json` file in the same folder as the script. This file is automatically created and updated as you play.

**Tip:** For best results, run the script in a dedicated folder to keep your score file organized and avoid conflicts with other projects.
