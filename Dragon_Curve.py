import pygame as pg
import numpy as np
from pygame import freetype

# Variable Declaration:
screen_width = 800
screen_height = 800
run = True
pointlist = (int(screen_width * 0.5 + 200), int(screen_height * 0.5))
center_x = int(screen_width * 0.5 + 200)
center_y = int(screen_height * 0.5)
rotation = int(input('rotation? (Determines direction of rotation (0 = clockwise, 1 = anti-clockwise))'))    # Determines direction of rotation (0 = clockwise, 1 = anti-clockwise)
theta = int(input('theta? (Determines initial direction of extension of seedline in degrees(0 - 359)'))
radtheta = theta/180 * np.pi    # Determines initial direction of extension of seedline (0 = up, 1 = right, 2 = down, 3 = left)
size = int(input('size? (Determines line length)'))    # Determines line length
width = 1   # Determines line width

# Function Definitions:
def rotate(pts, rotdir = 0):
    center_x = pointlist[len(pointlist) - 2]
    center_y = pointlist[len(pointlist) - 1]
    if rotdir == 0:
        for i in range(len(pts) - 3, -1, -2):
            x = pts[i - 1]
            y = pts[i]
            res_x = center_x + center_y - y
            res_y = -center_x + center_y + x
            temp = list(pts)
            temp.append(res_x)
            temp.append(res_y)
            pts = tuple(temp)
    if rotdir == 1:
        for i in range(len(pts) - 3, -1, -2):
            x = pts[i - 1]
            y = pts[i]
            res_x = center_x - center_y + y
            res_y = center_x + center_y - x
            temp = list(pts)
            temp.append(res_x)
            temp.append(res_y)
            pts = tuple(temp)
    return pts

def draw(plot):
    for i in range(0, len(plot) - 2, 2):
        x1 = plot[i]
        y1 = plot[i + 1]
        x2 = plot[i + 2]
        y2 = plot[i + 3]
        pg.draw.line(win, (0, 0, 0), (x1, y1), (x2, y2), width)
        pg.display.update()

# Display Initialisation:
pg.display.init()
pg.freetype.init()
win = pg.display.set_mode((screen_width + 200, screen_height))
pg.display.set_caption("Dragon Curve")
win.fill((255, 255, 255))
pg.draw.line(win, (0, 0, 0), (199, 0), (199, screen_height), 1)
font = pg.freetype.SysFont('Consolas', 15)
font.render_to(win, (0, 5), "Heighway_Dragon_Fractal", (0, 0, 0))
font.render_to(win, (0, 60), "Iteration:", (0, 0, 0))
font.render_to(win, (0, 90), "Points:", (0, 0, 0))
font.render_to(win, (0, 120), "Size:", (0, 0, 0))
font.render_to(win, (0, 150), "Rotation:", (0, 0, 0))
font.render_to(win, (0, 180), "Initial Extension:", (0, 0, 0))
pg.display.update()

# Main:
# Seedline:
temp = list(pointlist)
temp.append(center_x + int(np.cos(radtheta) * size))
temp.append(center_y - int(np.sin(radtheta) * size))
pointlist = tuple(temp)
iter = 1
draw(pointlist)
pg.display.update()

# Subsequent iterations:
while run == True:
    ndata = int(len(pointlist)*0.5)
    key = pg.key.get_pressed()

    if key[pg.K_SPACE]:
        win.fill((255, 255, 255), (200, 0, screen_width, screen_height))
        pointlist = rotate(pointlist, 0)
        iter += 1
        win.fill((255, 255, 255), (0, 0, 198, screen_height))
        font.render_to(win, (0, 5), "Heighway_Dragon_Fractal", (0, 0, 0))
        font.render_to(win, (0, 60), "Iteration:" + str(iter), (0, 0, 0))
        font.render_to(win, (0, 90), "Points:" + str(ndata), (0, 0, 0))
        font.render_to(win, (0, 120), "Size:" + str(size), (0, 0, 0))
        font.render_to(win, (0, 150), "Rotation:" + str(rotation), (0, 0, 0))
        font.render_to(win, (0, 180), "Theta:" + str(theta), (0, 0, 0))
        draw(pointlist)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            run = False
            break
