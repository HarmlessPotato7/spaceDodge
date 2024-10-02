import pygame
from pygame.locals import *

class Player:
    def __init__(self,screen_size):
        pygame.init()
        self.screen_size = screen_size

        self.w = 40
        self.h = 60
        self.x = self.screen_size.x//2 - self.w//2
        self.y = self.screen_size.y - self.h

        self.vel = 0
        self.speed = 2
        self.friction = 0.8

        self.hb = pygame.Rect(self.x,self.y,self.w,self.h)

    def update(self,dt):
        keys = pygame.key.get_pressed()
        if keys[K_LEFT] or keys[K_a]:
            self.vel -= self.speed*dt
        elif keys[K_RIGHT] or keys[K_d]:
            self.vel += self.speed*dt
        
        self.vel *= self.friction
        self.x += self.vel

        self.x = pygame.math.clamp(self.x, 0, self.screen_size.x-self.w)
        self.hb.x=self.x

    def draw(self,surf):
        pygame.draw.rect(surf, (255,0,0), self.hb)