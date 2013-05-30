from gasp import *

begin_graphics(800, 600, title="Snake")
set_speed(1)

snake_x = 300
snake_y = 300
snake = Box((snake_x, snake_y), 10, 10, filled=True)
dx = 10
dy = 10

update_when('key_pressed')
if key_pressed('w'):
    snake_y -= dy
if key_pressed('a'):
    snake_x -= dx
if key_pressed('d'):
    snake_x += dx
if key_pressed('s'):
    snake_y += dy
move_to(snake, (snake_x, snake_y))
    

end_graphics()




