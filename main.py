import pygame
from constants import *
from apple import Apple
from strawberry import Strawberry
from bomb import Bomb
from player import Player
from cloud import Cloud

# initalize pygame
pygame.init()

# configues the screen
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# sprite group
all_sprites = pygame.sprite.Group()

# cloud group
cloud_sprites = pygame.sprite.Group()

# fruits Group
fruit_sprites = pygame.sprite.Group()

# instance of fruit
apple = Apple()
strawberry = Strawberry()
fruit_sprites.add(apple)
fruit_sprites.add(strawberry)

# instance of Player
player = Player()

# instance of Cloud
cloud1 = Cloud()
cloud2 = Cloud()
cloud3 = Cloud()
all_sprites.add(cloud1, cloud2, cloud3)

# make bomb
bomb = Bomb()

# adding sprites to group
all_sprites.add(player)
all_sprites.add(apple)
all_sprites.add(strawberry)
all_sprites.add(bomb)

# getting the clock
clock = pygame.time.Clock()

background_color = (150, 180, 200)

# game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_LEFT:
                player.left()
            elif event.key == pygame.K_RIGHT:
                player.right()
            elif event.key == pygame.K_UP:
                player.up()
            elif event.key == pygame.K_DOWN:
                player.down()

    # clear screen
    screen.fill(background_color)
    # move and render Sprites
    for entity in all_sprites:
        entity.move()
        entity.render(screen)
    # check Colisions
    fruit = pygame.sprite.spritecollideany(player, fruit_sprites)
    if fruit:
        fruit.reset()
    # check collision player and bomb
    if pygame.sprite.collide_rect(player, bomb):
        running = False
    # update the window
    pygame.display.flip()
    # update the window
    clock.tick(60)
