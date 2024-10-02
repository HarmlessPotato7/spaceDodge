import pygame

class Star:
    def __init__(self, w,h, x, y):
        pygame.init()

        self.w = w
        self.h = h
        self.x = x
        self.y = y

        self.friction = 0.8
        self.speed = 2
        self.vel = 0

        self.hb = pygame.Rect(self.x,self.y,self.w,self.h)

    def update(self,dt):
        self.vel += self.speed*dt
        self.vel *= self.friction
        self.y += self.vel
        self.hb.y=self.y
        return self.y < 750

    def draw(self,surf):
        pygame.draw.rect(surf,(255,255,255),self.hb)