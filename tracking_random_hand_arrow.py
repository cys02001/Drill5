from pico2d import *
import random

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
arrow = load_image('hand_arrow.png')

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def draw_character(x, y):
    pass
def draw_arrow(x, y):
    arrow.draw(x, y)
def move_character(character_x, character_y, target_x, target_y, move_speed):
    pass


running = True
frame = 0
arrow_x = random.randint(0, TUK_WIDTH)
arrow_y = random.randint(0, TUK_HEIGHT)
character_x, character_y = TUK_WIDTH // 2, TUK_HEIGHT // 2
move_speed = 5

while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)

    draw_arrow(arrow_x, arrow_y)
    update_canvas()
    handle_events()
close_canvas()