from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
       super().__init__()
       self.image = transform.scale(image.load(player_image), (size_x, size_y))
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if  keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if  keys[K_s] and self.rect.y <620:
            self.rect.y += self.speed

    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed


racket1 = Player('pencil.jpg', 30, 200, 4, 50, 150)
racket2 = Player('pencil.jpg', 520, 200, 4, 50, )
ball = GameSprite('ball.jpg', 200, 200, 4, 50, 50)

win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill((255, 0, 0))
game = True
finish = False
clock = time.Clock()

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.fill((255, 0, 0))
        racket1.update_l()
        racket2.update_r()
        racket1.reset()
        racket2.reset()
        ball.reset()

    display.update()
    clock.tick(60)
