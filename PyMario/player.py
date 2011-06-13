__author__ = 'Nuts)'
import pygame
from pygame.locals import *
class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.image.load("data/mario1.png")

        self.rect = self.image.get_rect(topleft=[0, 0])
        self.jump_speed = 0
        self.jumping = False

        left_walking_frames = [pygame.image.load("data/mario"+str(x)+"-l.png") for x in range(1,4)]
        right_walking_frames = [pygame.image.load("data/mario"+str(x)+".png") for x in range(1,4)]
    def update(self):

        #Get the current key state.
        key = pygame.key.get_pressed()

        #Move left/right
        dir = 0
        if key[K_a]:
            dir = -1
        if key[K_d]:
            dir = 1

        #Increase the jump speed so you fall
        if self.jump_speed < 5:
            self.jump_speed += 0.3

        #We fell off a platform!
        if self.jump_speed > 2:
            self.jumping = True
        #print (self.jump_speed)
        self.move(2 * dir, self.jump_speed)
    def __move(self, dx, dy):

        #Create a temporary new rect that has been moved to dx and dy
        new_rect = Rect(self.rect)
        new_rect.x += dx
        new_rect.y += dy
        #print (new_rect.x)
        #loop through all the sprites we're supposed to collide with
        #(collision_sprites is defined in the main() function below)
        for sprite in self.collision_sprites:

            #If there's a collision between the new rect (the one that's

            #been moved) and the sprite's rect then we check
            #for what direction the sprite is moving, and then we
            #clamp the "real" rect to that side
            if new_rect.colliderect(sprite.rect):

                #Check the X axis
                if dx > 0: #moving right
                    self.rect.right = sprite.rect.left
                elif dx < 0: #moving left
                    self.rect.left = sprite.rect.right

                #Check the Y axis
                if dy > 0: #moving down
                    self.rect.bottom = sprite.rect.top

                    #Landed!
                    self.jump_speed = 0
                    self.jumping = False
                elif dy < 0: #moving up
                    self.rect.top = sprite.rect.bottom
                    self.jump_speed = 0 #oww, we hit our head

                #Break the function so we'll skip the line below
                return

        #If there's no collision, move the rect!
        self.rect = Rect(new_rect)

    #Calls __move for the X and Y axises
    def move(self, dx, dy):
        if dx:
            self.__move(dx, 0)
        if dy:
            self.__move(0, dy)
        #print(dx)
  