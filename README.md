# CPSC-6160
This repository holds the project source code for the two-dimensional game I created the first semester of my senior year in my CPSC 6160 2D Game Engine class.

Nia Dicks - Milestone 3 - README.txt

The game I am currently making is an escape-type room that utilizes items within the rooms
to escape out of the doorway. Within a single room, clues hint at how to
leave the room. The character is a detective who was kidnapped by a killer and must escape
before the killer returns.

** There is input printing to the command terminal that will be printed on the game screen
in the final game **

The following parts of this README will explain the contents of the zip file uploaded
to Canvas - depicting what I have developed in this game thus far.

**  To run these file run GameManager.py  **

GameManager.py
	This is the overall game controller and manages the other components. It will host
	the creation, drawing, and movement of players, items, inventory, etc. Runs the game.

Room.py
	This room class allows items to be added, selected, and drawn to a room.
	Right now, there is one set room with a set background; as I advance, this file will
	import other background images for different rooms. The room class
	creates a list of items within it.

Player.py
	This player class sets the frames of the player's sprite sheet, gives
	the player a surrounding light glow, handles its movements, and creates the inventory.
	The player class creates a detective who can patrol around the room (using AD keys
	to find items)

Inventory.py
	This is the inventory class that creates the inventory and shows the current inventory
	the player has. Right now, the inventory is a list of the items selected.

Item.py
	This is the item class that draws an item, allows it to be selected, and shows it
 	is selected items. The version of that item will be zoomed in for the player once 
	it has been selected.

Popup.py
	This handles the pop up image/interaction when an item is found in the room. Once
	an item is foudn it will be added to the inventory list. Most pop up are images of
	found items but some are interactive as well. (Not all pop ups in the game are showing)

Timer.py
	This handles the timer in the game. Right now it is set to 10 minutes this may
	change depending on how many final puzzles there are.

Button.py
	This class handles the buttons on the main menu page. The three buttons I have in this game
	are the play button, quit button, and menu button.

sprites (folder)
	This folder holds the sprite sheet of the player in the game - detective.png

image (folder)
	This hosts the photos of the items within the room - all are free to use

background_imgs (folder)
	This hosts the images of the background (just one for now) - all are free to use

music (folder)
	This host the music used in the background of the game - all are free to use



** The following below are the item required for the last submission**

YourLifeOrMineThumbnail.png
	This is the thumbnail image for the game

Final Project Poster - Nia Dicks.pdf
	This is the final project poster

Milestone 1 - Nia Dicks.pdf
	This is the milestone 1 presentation

Final Project Vido - Nia Dicks.mp4
	This is the gameplay video of my video game.

This README depicts the progress I have made in my game and my code along with all the materials required
for this submission. All mentioned here is in the zip file submitted.
