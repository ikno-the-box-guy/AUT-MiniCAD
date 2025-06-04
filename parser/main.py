import pygame as pg


_white = pg.Color('white')


def main():
    screen = pg.display.set_mode((1280, 720))
    clock = pg.time.Clock()

    input_box = pg.Rect(30, 30, 200, 32)
    caret = pg.Rect(input_box.x + 5, input_box.y + 5, 2, input_box.h - 10)
    output_box = pg.Rect(30, 92, 432, 597)
    divider = pg.Rect(492, 0, 1, 720)

    text = ''
    output = []
    done = False

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    if text.strip():
                        output.append(text)
                        text = ''
                elif event.key == pg.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode

        # Clear screen
        screen.fill((30, 30, 30))

        # Render text
        font = pg.font.Font(None, 32)
        txt_surface = font.render(text, True, _white)

        # Resize box if text too long
        # TODO: Add a maximum width for the input box
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width

        # Render text
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Render input_box
        pg.draw.rect(screen, _white, input_box, 2)
        # Render caret
        caret.x = input_box.x + 5 + txt_surface.get_width()
        pg.draw.rect(screen, _white, caret)

        # Render console output
        font = pg.font.Font(None, 28)
        for i, line in enumerate(reversed(output)):
            if i >= output_box.h // 28: # Clipping
                break

            txt_surface = font.render(line, True, _white)
            screen.blit(txt_surface, (output_box.x+5, output_box.y + output_box.h - (i + 1) * 28))

        # Render output box
        pg.draw.rect(screen, _white, output_box, 2)

        # Render divider
        pg.draw.rect(screen, _white, divider)

        pg.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()
