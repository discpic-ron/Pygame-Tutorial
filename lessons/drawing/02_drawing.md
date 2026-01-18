# Drawing

Before we use images (Sprites), we need to know how to draw basic geometry. This is useful for health bars, hitboxes, or simple prototyping.

**What you need to know**

Pygame provides a library of functions to draw directly onto a surface. The common syntax is: `pygame.draw.shape(surface, color, coordinates, thickness)`
* Shape: Before the parathensis, we add a shape to draw
* Surface: Where to draw (usually our `screen`).
* Color: An (R, G, B) tuple or a string name like `"red"`.
* Coordinates: Where it goes.
* Width: (Optional) If you leave this out, the shape is filled. If you put a number, it becomes an outline.

You can also use `pygame.Shape()`. 
