# Events

Pygame records everything: a key press or clicking the "X" on the window. These are stored in a Queue (a list of things that happened). You're probably asking yourself, "How do we contact this queue?" We use `pygame.event.get()` to empty that list and react to them. If you don't do this, your program won't do anything.

**There are two ways to handle keyboard input in Pygame**:
* Event Handling (`pygame.KEYDOWN`): Best for single actions (like jumping or firing a gun).
* Key logging (`pygame.key.get_pressed()`): Best for continuous motion (like walking).
