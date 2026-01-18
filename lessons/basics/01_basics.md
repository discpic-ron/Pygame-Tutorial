# Basics

**Key Concepts in this Lesson**
* Initialization: pygame.init() wakes up the Pygame modules (sound, display, etc.).
* The Surface: The window (or `screen`) is a grid of pixels where `(0, 0)` is the top-left corner.
* The Event Loop: Pygame captures everything the user does (mouse clicks, key presses) and puts them in a "queue." If you don't empty this queue, the window will freeze.
* The Clock: Without `clock.tick(60)`, the game will run as fast as your CPU allows, which makes the game inconsistent on different computers.
