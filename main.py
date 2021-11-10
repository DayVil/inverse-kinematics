import sys

import pygame as pg

from scripts.segment import SegmentBuilder


def main():
    # Settings
    name = "Inverse Kinematics"
    framerate = 60
    width = 600
    height = 400
    center = [width / 2, height / 2]
    window_size = (width, height)

    # Inits
    pg.init()
    pg.display.set_caption(name)
    clock = pg.time.Clock()

    # Screen
    screen = pg.display.set_mode(window_size)

    # Segment
    segments = SegmentBuilder(10, 50, center)

    while True:
        screen.fill((0, 0, 0))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

        mouse_pos = pg.mouse.get_pos()
        segments.draw_segments(screen, mouse_pos)

        pg.display.update()
        clock.tick(framerate)


if __name__ == '__main__':
    main()
