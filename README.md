# AUT-MiniCAD
AUT-MiniCAD is a command based drawing tool made as an assignment for Automata. 


AUT-MiniCAD is written in python and uses pygame for all the rendering. Antlr4 is used to parse all user input.

# Drawing Commands

## Colors & Strokes

- `FILL_COLOR c`  
  Sets the fill color for shapes. Use hex codes (e.g. `#FF0000`).

- `BORDER_COLOR c`  
  Sets the border (stroke) color for shapes and lines.

- `STROKE_WIDTH px`  
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
  Loads a file using the specified filepath. File loading is seen as one action: calling undo will undo all actions executed by the file. Any changes made to the fill color, border color or stroke width will not persist (i.e. changing the fill color inside the file will not affect the RECT command outside the file).  


# Multiple commands, input files and strict whitepsace
AUT-MiniCAD can handle multiple commands at once, as long as they are separated by a semicolon: 

``CLEAR #000000;UNDO;``

> [!NOTE]
> Whitespace usage is strict. Command parameters have to be separated by exactly one space. Spaces in any other spot will result in a syntax error, even after a semicolon.

AUT-MiniCAD can also handle input from an input file. Simply write out all the commands and end them with a semicolon. You are not allowed to put space between commands, but you can put a newline.

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