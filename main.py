import pygame, time, random, sys
from player import Player
from star import Star
from pygame.locals import *

class Game:
    def __init__(self):
        pygame.init()

        self.screen_size = pygame.Vector2(600,750)
        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption("ooh smooth")

        self.bg_img = pygame.image.load("bg.jpg").convert()
        self.font_48 = pygame.font.Font("Metrofutura.ttf", 48)
        self.font_32 = pygame.font.Font("Metrofutura.ttf", 32)
        self.lose_txt = self.font_48.render("GAME OVER", 1, (255,0,0))
        self.i_txt = self.font_32.render("PRESS SPACE TO CONTINUE", 1, (255,255,255))
        self.time_txt = self.font_48.render("Time:", 1, (255,255,255))

        self.player = Player(self.screen_size)

        self.star_w = 10
        self.star_h = 20
        self.star_time = time.time()
        self.star_increment = 1.5
        self.stars = []

        self.survival_time = time.time()
        self.fps_time = time.time()

    def run(self):
        last_time = time.time()
        clock = pygame.time.Clock()
        fps = 60
        fps_txt = self.font_48.render(f"FPS: {fps}", 1, (255,255,255))
        while True:
            now = time.time()
            dt = now - last_time
            dt *= 60
            last_time = now

            time_txt = self.font_48.render(f"Time: {now - self.survival_time:.0f}s", 1, (255,255,255))

            for event in pygame.event.get():
                if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            self.player.update(dt)
            self.spawn_stars()
            for star in self.stars:
                star.update(dt)
                if star.y >= self.screen_size.y:
                    self.stars.remove(star)
                elif star.hb.colliderect(self.player.hb):
                    self.reset()

            if now - self.fps_time >= 1:
                fps = int(clock.get_fps())
                fps_txt = self.font_48.render(f"FPS: {fps}", 1, (255,255,255))
                self.fps_time = now
            

            self.screen.blit(self.bg_img, (0,0))
            for star in self.stars:
                star.draw(self.screen)
            self.player.draw(self.screen)
            self.screen.blit(time_txt, (self.screen_size.x-150,10))
            self.screen.blit(fps_txt,(10,10))
            pygame.display.flip()

            clock.tick(60)

    def reset(self):
        self.screen.blit(self.lose_txt, (self.screen_size.x // 2 - self.lose_txt.get_width() // 2, self.screen_size.y // 2 - self.lose_txt.get_height() // 2))
        self.screen.blit(self.i_txt, (self.screen_size.x//2 - self.i_txt.get_width()//2,self.screen_size.y//2+self.lose_txt.get_height()//2+10))
        pygame.display.update()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN and event.key == K_SPACE:
                    waiting = False

        self.player.vel = 0
        self.player.x, self.player.y = self.screen_size.x // 2 - self.player.w // 2, self.screen_size.y - self.player.h

        self.stars.clear()
        self.star_increment = 1.5
        self.star_time = time.time()
        self.survival_time = time.time()

    def spawn_stars(self):
        now = time.time()
        if now - self.star_time >= self.star_increment:
            for _ in range(3):
                star_x = random.randint(0, int(self.screen_size.x-self.star_w))
                star = Star(self.star_w, self.star_h, star_x, -self.star_h)
                self.stars.append(star)
            self.star_time = now
            self.star_increment = max(0.2, self.star_increment - 0.05)

if __name__ == '__main__':
    game = Game()
    game.run()