
# Labyrinth Game Python

## Purpose

This is a labyrinth Game done while following the software engineering course at 
Novosibirsk state university.

The goal is to create a simple game with as much good practices and features that fits
a production environment as possible.

The lecturer of this Course is Graninas : https://github.com/graninas

## Specification

Created using vanilla `python3`

## Build a distribution
install pyinstaller using pip:

`pip install pyinstaller`

create you own distribution. It will be located in dist/main.

`pyinstaller main.py`
 
## Start the Game
to start the game you can execute the latest distribution (available for linux environment)
 
 `./dist/main/main`
 
 If you have python installed on your machine, you can execute the main.py file
 
 `python3 main.py`

## Game Description

This is Command Line Interfaced version of the labyrinth Game:

[Labyrinth (Wiki)](https://en.wikipedia.org/wiki/Labyrinth_%28paper-and-pencil_game%29)

"Labyrinth" is a one-player turn-by-turn game which should be implemented as a console application.

The Game consists of labyrinth, labyrinth objects, user inventory, CLI interface.

The Computer is the master of game.

Game is controlled by text commands.

Initially, the player can't see the labyrinth. The player should explore the labyrinth on its own.

The Goal is to find the treasure and to exit the labyrinth. There will be some special cells
like 'wormholes' (teleporters) ...etc.

## Game Commands
`quit` : exit the game

`show` : shows the labyrinth (it's cheating :D)

`save [filename]` : Saves the game in a file

`load [filename]` : Loads the saved game 

`go-up` or `z`: Makes a move upward

`go-down` or `s`: Makes a move downward

`go-left` or `q`: Makes a move on the left

`go-right` or `d`: Makes a move on the left

`skip` : Skips your turn (and execute the cell action on which you are)
