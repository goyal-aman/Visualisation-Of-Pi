import pygame
from collisions import *
pygame.init()


s1, s2 = 100, 50
x1,y1 = 1000, 250
x2, y2 = 500, y1+s1-s2


power = int(input('enter: '))
step = 10*(power)
v1 =  (-5/step)

m1, m2 = 100**(power-1), 1
v2 = 0


# temp_x1 = 0
red = (255, 0, 0)
blue = (0, 0, 255)


def message_to_print(msg, color):
    font = pygame.font.SysFont(None, 40)
    text = font.render(msg, True, color)
    win.blit(text, [10,10])





win = pygame.display.set_mode((1200, 500))
win.fill((255, 255, 255))
pygame.display.set_caption('simulation')

Collisions = 0
run = True
while run:
    click_sound = pygame.mixer.Sound("rss/click.wav")
    pygame.time.delay(10)
    sound_collide, sound_reverse = True, True
    for i in range(step):

        message_to_print('collision ' + str(Collisions), (0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


        # biger block
        x1 += v1
        if x1>s2+2:
            t=x1

        if not x2 + s2 < x1 or x1 + s1 < x2:
            v2_temp = exchange_vel(v2, m2, v1, m1)
            v1_temp = exchange_vel(v1, m1, v2, m2)
            if sound_collide:
                click_sound.play()
                sound = False

            v2, v1 = v2_temp, v1_temp
            Collisions += 1


        # smaller Block
        x2 += v2
        if x2 <= 0:
            v2 = reverse_vel(v2)
            if sound_reverse:
                click_sound.play()
                sound_reverse = False
            Collisions += 1
        pygame.draw.rect(win, blue, (x2, y2, s2, s2))
        pygame.draw.rect(win, red, (t, y1, s1, s1))

        pygame.display.update()
        win.fill((255, 255, 255))

pygame.quit()
