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
  Draws an ellipse inside the bounding box starting at `(x, y)` with width `w` and height `h`.

>- `POLYGON x0 y0 x1 y1 ... xn yn`  sq
  Draws a closed polygon connecting all the given points in order.

## History

>- `UNDO`  
  Reverts the last drawing action.

>- `REDO`  
  Reapplies the last undone action.
