import pygame as pg

pg.init()

pg.display.set_caption("TanksGame")
screen = pg.display.set_mode((1500, 975))

clock = pg.time.Clock()
FPS = 100

field = pg.image.load("C:\\Users\\arsen\\Desktop\\tanchikiGame\\assets\\tank_field.png").convert_alpha()
field = pg.transform.scale(field, (1500, 975))

blue_tank_original = pg.image.load('C:\\Users\\arsen\\Desktop\\tanchikiGame\\assets\\blue_tank.png').convert_alpha()
blue_tank_original = pg.transform.scale(blue_tank_original, (86, 110))
blue_tank = blue_tank_original
blue_tank_x = 100
blue_tank_y = 100
last_pressed_button_blue = "d_button"
blue_bullets = []

red_tank_original = pg.image.load('C:\\Users\\arsen\\Desktop\\tanchikiGame\\assets\\red_tank.png').convert_alpha()
red_tank_original = pg.transform.scale(red_tank_original, (86, 110))
red_tank = red_tank_original
red_tank_x = 1300
red_tank_y = 800
last_pressed_button_red = "left_arrow"
red_bullets = []

bullet_original = pg.image.load("C:\\Users\\arsen\\Desktop\\tanchikiGame\\assets\\tank_bullet.png").convert_alpha()
bullet_original = pg.transform.scale(bullet_original, (30, 18))
bullet_copy = bullet_original

block = pg.image.load("C:\\Users\\arsen\\Desktop\\tanchikiGame\\assets\\brick_block.png").convert_alpha()
block = pg.transform.scale(block, (96, 964))

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
                last_pressed_button_blue = 'w_button'
            elif event.key == pg.K_s:
                move_down_blue = True
                last_pressed_button_blue = 's_button'
            elif event.key == pg.K_d:
                move_right_blue = True
                last_pressed_button_blue = 'd_button'
            elif event.key == pg.K_a:
                move_left_blue = True
                last_pressed_button_blue = 'a_button'
            elif event.key == pg.K_UP:
                move_up_red = True
                last_pressed_button_red = 'up_arrow'
            elif event.key == pg.K_DOWN:
                move_down_red = True
                last_pressed_button_red = 'down_arrow'
            elif event.key == pg.K_RIGHT:
                move_right_red = True
                last_pressed_button_red = 'right_arrow'
            elif event.key == pg.K_LEFT:
                move_left_red = True
                last_pressed_button_red = 'left_arrow'
            elif event.key == pg.K_e:
                bullet_dict = {
                    "x": blue_tank_x + blue_tank.get_width() // 2,
                    "y": blue_tank_y + blue_tank.get_height() // 2,
                    "direction": last_pressed_button_blue
                }
                blue_bullets.append(bullet_dict)
            elif event.key == pg.K_SPACE:
                bullet_dict = {
                    "x": red_tank_x + red_tank.get_width() // 2,
                    "y": red_tank_y + red_tank.get_height() // 2,
                    "direction": last_pressed_button_red
                }
                red_bullets.append(bullet_dict)
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

    if move_up_blue and blue_tank_y > 53:
        blue_tank_y -= 1
        blue_tank = pg.transform.rotate(blue_tank_original, 0)
    elif move_down_blue and blue_tank_y < 815:
        blue_tank_y += 1
        blue_tank = pg.transform.rotate(blue_tank_original, 180)
    elif move_right_blue and blue_tank_x < 1337:
        blue_tank_x += 1
        blue_tank = pg.transform.rotate(blue_tank_original, 270)
    elif move_left_blue and blue_tank_x > 53:
        blue_tank_x -= 1
        blue_tank = pg.transform.rotate(blue_tank_original, 90)

    if move_up_red and red_tank_y > 53:
        red_tank_y -= 1
        red_tank = pg.transform.rotate(red_tank_original, 0)
    elif move_down_red and red_tank_y < 815:
        red_tank_y += 1
        red_tank = pg.transform.rotate(red_tank_original, 180)
    elif move_right_red and red_tank_x < 1337:
        red_tank_x += 1
        red_tank = pg.transform.rotate(red_tank_original, 270)
    elif move_left_red and red_tank_x > 53:
        red_tank_x -= 1
        red_tank = pg.transform.rotate(red_tank_original, 90)

    # Update blue bullets
    for blue_bullet in blue_bullets:
        direction = blue_bullet["direction"]
        if direction == 'w_button':
            blue_bullet["y"] -= 5
        elif direction == 's_button':
            blue_bullet["y"] += 5
        elif direction == 'a_button':
            blue_bullet["x"] -= 5
        elif direction == 'd_button':
            blue_bullet["x"] += 5

    # Update red bullets
    for red_bullet in red_bullets:
        direction = red_bullet["direction"]
        if direction == 'up_arrow':
            red_bullet["y"] -= 5
        elif direction == 'down_arrow':
            red_bullet["y"] += 5
        elif direction == 'left_arrow':
            red_bullet["x"] -= 5
        elif direction == 'right_arrow':
            red_bullet["x"] += 5

    # Remove off-screen bullets
    blue_bullets = [bullet for bullet in blue_bullets if 53 < bullet["x"] < 1420 and 53 < bullet["y"] < 905]
    red_bullets = [bullet for bullet in red_bullets if 53 < bullet["x"] < 1420 and 53 < bullet["y"] < 905]

    screen.blit(field, (0, 0))
    screen.blit(blue_tank, (blue_tank_x, blue_tank_y))
    screen.blit(red_tank, (red_tank_x, red_tank_y))

    for blue_bullet in blue_bullets:
        x_blue_bullet = blue_bullet["x"]
        y_blue_bullet = blue_bullet["y"]

        direction = blue_bullet["direction"]
        if direction == "w_button":
            bullet_copy = pg.transform.rotate(bullet_original, 90)
        elif direction == "s_button":
            bullet_copy = pg.transform.rotate(bullet_original, -90)
        elif direction == "a_button":
            bullet_copy = pg.transform.rotate(bullet_original, 180)
        elif direction == "d_button":
            bullet_copy = pg.transform.rotate(bullet_original, 0)

        screen.blit(bullet_copy, (x_blue_bullet, y_blue_bullet))

    for red_bullet in red_bullets:
        x_red_bullet = red_bullet["x"]
        y_red_bullet = red_bullet["y"]

        direction = red_bullet["direction"]
        if direction == 'up_arrow':
            bullet_copy = pg.transform.rotate(bullet_original, 90)
        elif direction == 'down_arrow':
            bullet_copy = pg.transform.rotate(bullet_original, -90)
        elif direction == 'left_arrow':
            bullet_copy = pg.transform.rotate(bullet_original, 180)
        elif direction == 'right_arrow':
            bullet_copy = pg.transform.rotate(bullet_original, 0)

        screen.blit(bullet_copy, (x_red_bullet, y_red_bullet))

    pg.display.update()

pg.quit()
