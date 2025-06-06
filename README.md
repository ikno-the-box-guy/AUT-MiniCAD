# AUT-MiniCAD
AUT-MiniCAD is a command based drawing tool made as an assignment for Automata. 


AUT-MiniCAD is written in Python and uses **Pygame** for rendering. **ANTLR4** is used to parse all user input.

# Dependencies
This project was made using **Python 3.12**. The required pip dependencies are listed in ``requirements.txt``. This project also relies on [tkinter](https://docs.python.org/3/library/tkinter.html), which usually comes bundled with Python, but may need to be installed separately in some cases. 

# Drawing Commands
Note that all commands are case sensitive.

## Colors & Strokes

- `FILL c`  
  Sets the fill color for shapes. Use hex codes (e.g. `#FF0000`).

- `BORDER c`  
  Sets the border (stroke) color for shapes and lines.

- `WIDTH px`  
  Sets the thickness of strokes and borders in pixels.

- `CLEAR c`  
  Clears the entire canvas and fills it with the specified color.


## Shape Drawing

- `LINE x0 y0 x1 y1`  
  Draws a straight line from point `(x0, y0)` to `(x1, y1)` using the current stroke width and border color.

- `RECT x y w h`  
  Draws a rectangle with the top-left corner at `(x, y)`, width `w`, and height `h`. Uses current fill, border color, and stroke width.

- `ELLIPSE x y w h`  
  Draws an ellipse inside the bounding box starting at `(x, y)` with width `w` and height `h`. Uses current fill, border color, and stroke width.

- `POLY x0 y0 x1 y1 ... xn yn`
  Draws a closed polygon connecting all the given points in order. Uses current fill, border color, and stroke width.

## Misc

- `UNDO`  
  Reverts the last drawing action.

- `LOAD "fp"`
  Loads a file using the specified filepath. File loading is seen as one action: calling ``UNDO`` will undo all actions executed by the file. \
  Any changes made to the fill color, border color or stroke width within the file will not persist outside the file (i.e. changing the fill color inside the file will not affect the ``RECT`` command outside the file).  


# Multiple commands, input files and strict whitepsace
AUT-MiniCAD can handle multiple commands at once, as long as they are separated by a semicolon: 

``CLEAR #000000;UNDO;``

> [!NOTE]
> Whitespace usage is strict. Command parameters have to be separated by exactly one space. Spaces in any other spot will result in a syntax error, even after a semicolon.

You can also load commands from an input file. Simply list all the commands, each ending with a semicolon.
You are **not** allowed to put spaces between commands, but you may use newlines.

``LOAD "input.txt"``

- **input.txt:**
```C#
FILL #FF0000;
BORDER #00FF00;
WIDTH 5;
RECT 100 100 200 200;
LINE 103 103 297 297;
LINE 297 103 103 297;
UNDO;
```