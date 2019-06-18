from typing import Tuple
import colorsys

import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

n_rects_to_compare = 20


def generate_recursive_hue(hue_size: int):
    current_divisor = 2
    n_prev_colors_current_divisor = 0
    while True:
        current_step_size = (hue_size / current_divisor)
        new_hue = n_prev_colors_current_divisor * current_step_size + (current_step_size / 2)
        n_prev_colors_current_divisor += 1

        yield new_hue

        if n_prev_colors_current_divisor >= current_divisor:
            current_divisor *= 2
            n_prev_colors_current_divisor = 0


def draw_rect(color: Tuple[int, int, int], pos: Tuple[int, int], size: Tuple[int, int]):
    rect = (pos[0], pos[1], pos[0] + size[0], pos[1] + size[1])

    pygame.draw.rect(screen, color, rect)


def main():
    global screen
    pygame.init()
    screen_size = (600, 400)
    screen = pygame.display.set_mode(screen_size)
    screen.fill(WHITE)
    size = screen_size[0] / n_rects_to_compare, screen_size[1]
    hue_iterator = generate_recursive_hue(360)
    for i in range(n_rects_to_compare):
        hue = next(hue_iterator)
        print(f"{hue}, ", end="")
        rgb_color = colorsys.hsv_to_rgb(hue / 360, 50 / 100, 50 / 100)
        adj_rgb = ([elem * 2 for elem in rgb_color])

        pos = (i * size[0], 0)

        draw_rect(adj_rgb, pos, size)
    pygame.display.flip()
    while True:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                return  # Flag that we are done so we exit this loop
    # end forcefully


if __name__ == '__main__':
    main()
