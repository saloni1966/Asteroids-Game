'''
To-do list breakdown:

Setup and Initialization:

Import necessary modules: pygame, math, and random.
Initialize pygame.
Load Game Resources:

Load images for background, player ship, asteroids, stars, and alien ship.
Load sound effects for shooting and collisions.
Initialize Game Window:

Set window dimensions.
Set window title.
Create the game window surface.
Define Game Variables:

Initialize variables such as gameover state, player lives, score, rapid fire mode, etc.
Define Player Class:

Implement methods for initializing player attributes, drawing player, turning left/right, moving forward, and updating player location.
Define Bullet Class:

Implement methods for initializing bullet attributes, moving bullet, drawing bullet, and checking if bullet is off-screen.
Define Asteroid Class:

Implement methods for initializing asteroid attributes and drawing asteroid.
Define Star Class:

Implement methods for initializing star attributes and drawing star.
Define Alien Class:

Implement methods for initializing alien attributes and drawing alien.
Define AlienBullet Class:

Implement methods for initializing alien bullet attributes and drawing alien bullet.
Define Function to Redraw Game Window:
Implement function to update game screen with current game state, including player, bullets, asteroids, stars, aliens, and relevant texts.
Instantiate Player and Game Objects:
Create an instance of the player.
Initialize lists for player bullets, asteroids, stars, aliens, and alien bullets.
Main Game Loop:
Implement the main loop to handle game logic and events.
Game Logic:
Check for player input and update player actions accordingly.
Update positions and states of game objects (asteroids, stars, aliens, etc.).
Handle collisions between game objects.
Update game state variables such as score, lives, and rapid fire mode.
Handle game over condition.
Event Handling:
Check for pygame events such as quitting the game, key presses for shooting, toggling sound, and restarting the game.
Update Display:
Redraw the game window with the updated game state.
Quit Pygame:
Quit pygame when the game loop exits.

'''


'''
explaination -
This code is a simple game built using the Pygame library in Python. Let's break down the main components and their functionality:

Imports:

pygame: The main library for building games in Python.
math: Used for mathematical operations.
random: Utilized for generating random numbers.
Initialization:

pygame.init(): Initializes all imported Pygame modules.
Defines window dimensions (sw and sh), loads images and sounds, sets up the window, clock, and initializes various game variables.
Classes:

Player: Represents the player's spaceship. It handles the player's movement, rotation, and drawing on the screen.
Bullet: Represents bullets fired by the player's spaceship. It handles movement, drawing, and checking if it goes off-screen.
Asteroid, Star, Alien, AlienBullet: Represent various entities in the game, such as asteroids, stars, aliens, and bullets fired by aliens. Each class handles its movement, drawing, and initialization.
Redrawing the Game Window:

redrawGameWindow(): Function responsible for updating and redrawing the game window. It blits the background, player, asteroids, bullets, stars, aliens, and alien bullets onto the screen. It also displays text for lives, score, high score, and a "Play Again" prompt when the game is over.
Game Loop:

The while run: loop represents the main game loop. Within this loop:
The clock is ticked.
Various game events are handled, including player input, collisions between entities, and game state changes.
Entities are updated and moved according to their respective logic.
The game window is redrawn in each iteration of the loop.
Event Handling:

Pygame events are processed within the main loop, including quitting the game, handling key presses for player movement and actions, toggling sound, and restarting the game when the "Tab" key is pressed after a game over.
Game Over Handling:

If the player's lives reach zero (lives <= 0), the gameover flag is set to True, triggering the display of the "Play Again" prompt.
Exiting the Game:

When the game window is closed (pygame.QUIT event), the game loop exits, and Pygame is quit (pygame.quit()).


'''