import pygame as pg

pg.init()

pg.display.set_caption("TanksGame")
screen = pg.display.set_mode((1500, 975))

clock = pg.time.Clock()
FPS = 30

field = pg.image.load("C:\\Users\\arsen\\Desktop\\tanchikiGame\\assets\\tank_field.png").convert_alpha()
field = pg.transform.scale(field, (1500, 975))

blue_tank_original = pg.image.load('C:\\Users\\arsen\\Desktop\\tanchikiGame\\assets\\blue_tank.png').convert_alpha()
blue_tank_original = pg.transform.scale(blue_tank_original, (86, 110))
blue_tank = blue_tank_original  # Initialize the tank image
blue_tank_x = 100
blue_tank_y = 100
blue_bullets = []

red_tank_original = pg.image.load('C:\\Users\\arsen\\Desktop\\tanchikiGame\\assets\\red_tank.png').convert_alpha()
red_tank_original = pg.transform.scale(red_tank_original, (86, 110))
red_tank = red_tank_original
red_tank_x = 1300
red_tank_y = 800
red_bullets = []

bullet = pg.image.load("C:\\Users\\arsen\\Desktop\\tanchikiGame\\assets\\tank_bullet.png").convert_alpha()
bullet = pg.transform.scale(bullet, (16, 16))

block = pg.image.load("C:\\Users\\arsen\\Desktop\\tanchikiGame\\assets\\brick_block.png").convert_alpha()
block = pg.transform.scale(block, (192, 192))

# Flags to track movement
move_up_blue = False
move_down_blue = False
move_left_blue = False
move_right_blue = False

move_up_red = False
move_down_red = False
move_left_red = False
move_right_red = False

running = True
while running:
    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_w:
                move_up_blue = True
            elif event.key == pg.K_s:
                move_down_blue = True
            elif event.key == pg.K_d:
                move_right_blue = True
            elif event.key == pg.K_a:
                move_left_blue = True
            elif event.key == pg.K_UP:
                move_up_red = True
            elif event.key == pg.K_DOWN:
                move_down_red = True
            elif event.key == pg.K_RIGHT:
                move_right_red = True
            elif event.key == pg.K_LEFT:
                move_left_red = True
        elif event.type == pg.KEYUP:
            if event.key == pg.K_w:
                move_up_blue = False
            elif event.key == pg.K_s:
                move_down_blue = False
            elif event.key == pg.K_d:
                move_right_blue = False
            elif event.key == pg.K_a:
                move_left_blue = False
            elif event.key == pg.K_UP:
                move_up_red = False
            elif event.key == pg.K_DOWN:
                move_down_red = False
            elif event.key == pg.K_RIGHT:
                move_right_red = False
            elif event.key == pg.K_LEFT:
                move_left_red = False
        elif event.type == pg.K_e:


    # Move the blue tank based on the flags
    if move_up_blue and blue_tank_y>53:
        blue_tank_y -= 3
        blue_tank = pg.transform.rotate(blue_tank_original, 0)
    elif move_down_blue and blue_tank_y<815:
        blue_tank_y += 3
        blue_tank = pg.transform.rotate(blue_tank_original, 180)
    elif move_right_blue and blue_tank_x<1337:
        blue_tank_x += 3
        blue_tank = pg.transform.rotate(blue_tank_original, 270)
    elif move_left_blue and blue_tank_x>53:
        blue_tank_x -= 3
        blue_tank = pg.transform.rotate(blue_tank_original, 90)

    # Move the red tank based on the flags
    if move_up_red and red_tank_y>53:
        red_tank_y -= 3
        red_tank = pg.transform.rotate(red_tank_original, 0)
    elif move_down_red and red_tank_y<815:
        red_tank_y += 3
        red_tank = pg.transform.rotate(red_tank_original, 180)
    elif move_right_red and red_tank_x<1337:
        red_tank_x += 3
        red_tank = pg.transform.rotate(red_tank_original, 270)
    elif move_left_red and red_tank_x>53:
        red_tank_x -= 3
        red_tank = pg.transform.rotate(red_tank_original, 90)

    screen.blit(field, (0, 0))
    screen.blit(blue_tank, (blue_tank_x, blue_tank_y))
    screen.blit(red_tank, (red_tank_x, red_tank_y))

    pg.display.update()

pg.quit()
