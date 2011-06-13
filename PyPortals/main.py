__author__ = 'Nuts)'
import pygame
from platforms import Platform
from player import Player
from pygame.locals import *
from vector2 import Vector2
#from math import *
#from parser import Parser
map1 =\
"""
1..........................................................................1
1..........................................................................1
1..........................................................................1
1..........................................................................1
1..............1111111111..................................................1
1..........................................................................1
1..........................................................................1
1..........................................................................1
1..........................................................................1
1................1111......................................................1
1..........................................................................1
1..........................................................................1
1..........................................................................1
1..........................................................................1
1..........................................................................1
1..........................................................................1
1............1111..........................................................1
1..........................................................................1
1..........................................................................1
1..........................................................................1
11.........................................................................1
1..........................................................................1
1..........................................................................1
1111111111111111111111111111111111111111111111111111111111111111111111111111
"""
clock = pygame.time.Clock()
def parse_level():
    #Parse the level
    x, y = 0, 0
    for row in map1.split("\n"):
        for char in row:

            #Spawn a platform if the character is a 1
            if char == "1":
                Platform([x*16, y*16])

        #Update the read position.
            x += 1
        x = 0
        y += 1
def main():
    pygame.init()
    pygame.display.set_caption("PyPortals v0.4b") # title name
    logo = pygame.image.load("data/logo.png") # path to title-logo
    portalgun = pygame.image.load("data/portalgun2.png") # portal gun image
    pygame.display.set_icon(logo)#set up title logo
    screen = pygame.display.set_mode((1220, 400),0,32)#set screen resolution
    #Create some groups.
    sprites = pygame.sprite.Group()
    platforms = pygame.sprite.Group()
    #Set the sprites' groups
    Player.groups = sprites
    Platform.groups = sprites, platforms

    sprite_speed = 300.
    sprite_rotation = 0.
    sprite_rotation_speed = 360. # Degrees per second
    #background = pygame.image.load(background_image_filename).convert()

    #The player will loop through all the sprites contained in this
    #group, and then collide with them.
    Player.collision_sprites = platforms
    #Create some starting objects
    player = Player()
    parse_level()
    #Main loop
    while True:
        pygame.mouse.set_visible(False)
        pygame.event.set_grab(True)
        #Update
        clock.tick(35)
        sprites.update()
        #Get input
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                return
            if e.type == KEYDOWN:
                if e.key == K_ESCAPE:
                    pygame.quit()
                    return
                if e.key == K_w:
                    if not player.jumping:
                        player.jump_speed = -5.5
                        player.jumping = True
                if e.key == K_1:#main charecter change model
                   # player.image = pygame.image.load("data/portalgun.png") #MAIN CHARECTER CHANGE PART
                    pass
        key = pygame.key.get_pressed()#slow motion part
        if key[pygame.K_m]:#---||---
            clock.tick(10)#---||---
        sprite = portalgun
        sprite_pos = Vector2(player.rect.x+10,player.rect.y+10)
        pygame.display.flip()
        movement_direction = 0.
        rotation_direction = pygame.mouse.get_rel()[0]/10.0
        #screen.blit(background, (0,0))
        pressed_keys = pygame.key.get_pressed()
        pressed_mouse = pygame.mouse.get_pressed()

        if pressed_keys[K_LEFT]:
             rotation_direction = +1.
        if pressed_keys[K_RIGHT]:
             rotation_direction = -1.

        pygame.display.flip()
        rotated_sprite = pygame.transform.rotate(sprite, sprite_rotation)
        w, h = rotated_sprite.get_size()
        sprite_draw_pos = Vector2(sprite_pos.x-w/2, sprite_pos.y-h/2)


        time_passed = clock.tick()
        time_passed_seconds = time_passed / 1000.0

        sprite_rotation += rotation_direction * sprite_rotation_speed * time_passed_seconds
        pygame.display.flip()
        

        #print(player.rect.x)
        #Draw the scene
        screen.blit(screen, (0,0))
        screen.fill((0, 0, 0))
        screen.blit(rotated_sprite, sprite_draw_pos)
        sprites.draw(screen)
        pygame.display.flip()
if __name__ == "__main__":
    main()
