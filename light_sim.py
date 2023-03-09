import pygame
import sys
import math
import numpy as np
import numba
pygame.init()
white = (255, 255, 255)
red = (90, 100, 120)
clock = pygame.time.Clock()
s_w = 1000
s_h = 700
b_size = 25
n = 130
length = 370
angle = math.pi/n
bl = tuple()
blocks_set = tuple()
koef = int(length / 50)
kk = (255 / (length / koef * 2))
sc = pygame.display.set_mode((s_w, s_h))


# @numba.njit(fastmath=True)
def r_cast():
    mouse_pos = pygame.mouse.get_pos()
    m_x = mouse_pos[0]
    m_y = mouse_pos[1]
    for i in np.array(range(1, n * 2 + 1)):
        an = i * angle
        cos = math.cos(an)
        sin = math.sin(an)
        for len in range(0, length + 1, koef):
            l_x = m_x + len * cos
            l_y = m_y + len * sin
            c = int(255 - (len / koef * 2) * kk)
            if -30.0 < l_x < s_w + 30.0 and -30.0 < l_y < s_h + 30.0:
                l_x_1 = m_x + (len - koef) * cos
                l_y_1 = m_y + (len - koef) * sin
                pygame.draw.line(sc, (c, c, c), (l_x_1, l_y_1), (l_x, l_y), n // 12)
                l_x_st = l_x // b_size * b_size
                l_y_st = l_y // b_size * b_size
                if (l_x_st, l_y_st) in bl:
                    break
            else:
                break


def draw():
    global bl, blocks_set
    click = pygame.mouse.get_pressed()
    mouse_pos = pygame.mouse.get_pos()
    m_x = mouse_pos[0]
    m_y = mouse_pos[1]
    bl = set(bl)
    blocks_set = set(blocks_set)
    if click[0] == 1:
        b_x = m_x // b_size * b_size
        b_y = m_y // b_size * b_size
        blocks_set.add((b_x, b_y, b_size, b_size))
        bb_size = int(b_size / 4)
        for i in range(0, bb_size + 1):
            bl.add((b_x + i, b_y))
            bl.add((b_x, b_y + i))
        for i in range(0, bb_size + 1):
            bl.add((b_x + i, b_y + bb_size))
            bl.add((b_x + bb_size, b_y + i))

    for i in tuple(blocks_set):
        pygame.draw.rect(sc, red, i)

def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def main():
    while True:
        events()
        sc.fill((0, 0, 0))
        r_cast()
        draw()
        clock.tick()
        pygame.display.set_caption(f'fps: {int(clock.get_fps())}')
        pygame.display.flip()


if __name__ == '__main__':
    main()