#создай игру "Лабиринт"!
from pygame import *
'''Необходимые классы'''


#класс-родитель для спрайтов
class GameSprite(sprite.Sprite):
   #конструктор класса
    def __init__(self, player_x, player_y, player_speed, width, height, player_image = None):
        super().__init__()
        # каждый спрайт должен хранить свойство image - изображение
        self.image = Surface((width, height))
        self.image.fill((0, 0, 0))
        if player_image:
            self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y


    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


#класс-наследник для спрайта-игрока (управляется стрелками)
class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed


player_l = Player(30, 200, 4, 50, 150)
player_r = Player(520,200, 4, 50, 150)
ball = GameSprite(200, 200, 4, 50, 50, 'ball.png')

#Игровая сцена:
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
window.fill((200, 255, 250))





game = True
finish = False
clock = time.Clock()
FPS = 60


font.init()
font = font.SysFont('Arial', 70)
lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0))

speed_x = 4
speed_y = 4

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if finish != True:
        window.fill((200, 255, 250))
        player_l.update_l()
        player_r.update_r()
        player_l.reset()
        player_r.reset()
        ball.reset()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
    if ball.rect.y < 0 or ball.rect.y > 450:
        speed_y *= -1
    if sprite.collide_rect(player_l, ball) or sprite.collide_rect(player_r, ball):
        speed_x *= -1
    if ball.rect.x < 0:
        finish = True
        window.blit(lose1, (200, 200)) 

    display.update()
    clock.tick(FPS)

