# collisions

In Pygame, collisions are almost always handled using Rects. Because every Rect knows its own boundaries, Pygame can do the math for us to see if two rectangles are overlapping. Todo this, we use `colliderect`. It returns True if two Rects touch at any point, and False if they don't.  
