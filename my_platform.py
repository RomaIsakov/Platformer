import play
import pygame
from random import randint
platforms = []
coin_sound = pygame.mixer.Sound('coin.wav')
sea_sound = pygame.mixer.Sound('sea.ogg')
play.set_backdrop('gray')
pygame.display.set_caption("совершенная форма платформера")
personaj = play.new_circle(color = 'purple', x = -300, y = 0, radius = 25, border_color = 'black', border_width = 15) 
platforma = play.new_box(color = (248, 192, 77), x = -350, y = -30, width = 150, height = 10)


#счетчик монет
score_txt = play.new_text(words='Монеты:', x=play.screen.right-100, y=play.screen.top-30, size=70)
score = play.new_text(words='0', x=play.screen.right-30, y=play.screen.top-30, size=70)

#подсказки
text = play.new_text(words='Жми SPACE чтобы прыгнуть, a/d чтоюы двигаться', x=0, y=play.screen.bottom+60, size=70)

sea = play.new_box(
        color='blue', width=play.screen.width, height=50, x=0, y=play.screen.bottom+20
    )

def create_platforms():
    platforma1 = play.new_box(color = (248, 192, 77), x = 350, y = 0, width = 150, height = 10)
    platforma1.start_physics(can_move = True, mass = 100, obeys_gravity = False)
    platforms.append(platforma1)
    

def draw_coins():
    #добавь сюда монетки, которык будет собирать персонаж
    pass

@play.when_program_starts
def start():
    platforma.start_physics(can_move = False, mass = 9999)
    personaj.start_physics(can_move = True, mass = 1)
    #подключи фоновую музыку

 
    create_platforms()
    draw_coins()

@play.repeat_forever
async def game():
    if play.key_is_pressed('d'):
        personaj.physics.x_speed = 20
    elif play.key_is_pressed('a'):
        personaj.physics.x_speed = -20
    elif play.key_is_pressed('space'):
        personaj.physics.y_speed = 50
        await play.timer(1)
        personaj.physics.y_speed = 0
    else:
        personaj.physics.x_speed = 0
    #тут опиши процесс игры
    for platform in platforms:
        platform.physics.x_speed = -26.7
    await play.timer(seconds=1/48)

play.start_program()