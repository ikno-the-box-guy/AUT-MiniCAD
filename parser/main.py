import os

import pygame as pg
import tkinter as tk
import tkinter.filedialog
from src.DrawState import DrawState
from src.processing.Interpreter import interpret_file, interpret_text

_white = pg.Color('white')


def main():
    screen = pg.display.set_mode((1280, 720))
    clock = pg.time.Clock()

    root = tk.Tk()
    root.withdraw()

    input_box = pg.Rect(30, 30, 200, 32)
    caret = pg.Rect(input_box.x + 5, input_box.y + 5, 2, input_box.h - 10)
    output_box = pg.Rect(30, 92, 432, 597)
    import_box = pg.Rect(430, 30, 32, 32)
    divider = pg.Rect(492, 0, 1, 720)

    input_font = pg.font.Font(os.path.join("fonts", 'JetBrainsMono-Regular.ttf'), 20)
    output_font = pg.font.Font(os.path.join("fonts", 'JetBrainsMono-Regular.ttf'), 20)

    commands = []
    text = ''
    output = []
    done = False

    while not done:
        draw_surface = pg.Surface((787, 720))
        draw_state = DrawState(draw_surface)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.MOUSEBUTTONDOWN:
                if import_box.collidepoint(event.pos):
                    # Open file dialog to select a file
                    file_path = tk.filedialog.askopenfilename(
                        title="Select a file",
                        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
                    )
                    if file_path:
                        commands = interpret_file(file_path)
                        output.append(f"Loaded commands from file")
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    if text.strip():
                        output.append(text)
                        new_commands = interpret_text(text)

                        for command in new_commands:
                            if command.name == 'UNDO':
                                if commands:
                                    commands.pop()
                            else:
                                commands.append(command)

                        text = ''
                elif event.key == pg.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode

        # Clear screen
        screen.fill((30, 30, 30))

        # Render import box
        pg.draw.rect(screen, _white, import_box, 2)
        import_text = input_font.render("F", True, _white)
        screen.blit(import_text, (import_box.x + 10, import_box.y + 2))

        # Render text
        txt_surface = input_font.render(text[-30:], True, _white)

        # Resize box if text too long
        input_box.w = min(370, max(200, txt_surface.get_width()+10))

        # Render text
        screen.blit(txt_surface, (input_box.x+5, input_box.y + 2))
        # Render input_box
        pg.draw.rect(screen, _white, input_box, 2)
        # Render caret
        caret.x = input_box.x + 5 + txt_surface.get_width()
        pg.draw.rect(screen, _white, caret)

        # Render console output
        for i, line in enumerate(reversed(output)):
            if i >= output_box.h // 28:  # Clipping
                break

            txt_surface = output_font.render(line, True, _white)
            screen.blit(txt_surface, (output_box.x+5, output_box.y + output_box.h - (i + 1) * 28 - 1))

        # Render output box
        pg.draw.rect(screen, _white, output_box, 2)

        # Render divider
        pg.draw.rect(screen, _white, divider)

        # Execute commands
        for command in commands:
            command.exec(draw_state)

        # Render draw surface
        screen.blit(draw_surface, (493, 0))

        # Display everything
        pg.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()
