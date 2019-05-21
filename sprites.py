import sys
import os
import random
import pygame as pg
from pygame.locals import *

_G = 0.5
_J = 10
_V = 1
_F = 0.1

def load_png(name):
    """ Load image and return image object"""
    fullname = os.path.join('game_assets', name)
    try:
        image = pg.image.load(fullname)
        if image.get_alpha is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except pg.error:
        print(f"Cannot load image: {fullname}")
        raise SystemExit
    return image, image.get_rect()

class Player(pg.sprite.Sprite):
    def __init__(self, screen, ground, *args, **kwargs):
        pg.sprite.Sprite.__init__(self)
        self.image, self.rect = load_png("player.png")
        self.screen = screen
        self.ground = ground
        self.was_flying = True
        self.facing_right = True
        self.was_facing_rigth = True

        self.x = self.screen.get_size()[0] / 100 * 20
        self.y = self.screen.get_size()[1] / 100 * 10
        self.rect.move_ip((self.x, self.y))

        self.a = (0,0)
        self.v = (0,0)
    def update(self):
        if not self.touching_ground():
            self.a = (self.a[0], _G)
            self.was_flying = True
        else:
            self.a = (self.a[0], 0)
            if self.was_flying:
                self.v = (self.v[0], 0)
                self.was_flying = False

        if self.x < 0:
            self.x = 0
            self.v = (0, self.v[1])

        if self.x > self.screen.get_size()[0] - 32:
            self.x = self.screen.get_size()[0] - 32
            self.v = (0, self.v[1])

        if self.y > self.screen.get_size()[1]:
            self.y = self.screen.get_size()[1] / 100 * 10

        self.a = (self.a[0]*_F, self.a[1])

        self.v = (self.v[0] + self.a[0],
                  self.v[1] + self.a[1])

        self.x += self.v[0]
        self.y += self.v[1]
        self.move_abs((self.x, self.y))

    def move_ip(self, coords):
        self.rect.move_ip(coords)

    def move_abs(self, coords):
        self.rect.left = coords[0]
        self.rect.top = coords[1]

    def touching_ground(self):
        return pg.sprite.spritecollideany(self, self.ground, False)

    def jump(self):
        if self.touching_ground():
            self.v = (self.v[0], -_J)

    def move_right(self):
        if self.facing_right == False:
            self.horizontal_flip()
        self.a = (self.a[0]+_V, self.a[1])
        self.facing_right = True

    def move_left(self):
        if self.facing_right == True:
            self.horizontal_flip()
        self.a = (self.a[0]-_V, self.a[1])
        self.facing_right = False

    def horizontal_flip(self):
        self.image = pg.transform.flip(self.image, True, False)


class Ground(pg.sprite.Sprite):
    def __init__(self, coords, texture, *args, **kwargs):
        pg.sprite.Sprite.__init__(self)
        self.image, self.rect = load_png(texture)

        sprite_xy = coords[0], coords[1]
        self.rect.move_ip(sprite_xy)

    def update(self):
        pass

    def move_ip(self, coords):
        self.rect.move_ip(coords)

    def move_abs(self, coords):
        self.rect.left = coords[0]
        self.rect.top = coords[1]

class Sword(pg.sprite.Sprite):
    def __init__(self, player, *args, **kwargs):
        pg.sprite.Sprite.__init__(self)
        self.image, self.rect = load_png("sword.png")
        self.player = player
        self.facing_right = True
        self.drawn = True
        self.frames_delta = 0

        self.x = self.player.x + 20
        self.y = self.player.y
        self.rect.move_ip((self.x, self.y))

    def update(self, frames):
        if self.player.facing_right:
            self.x = self.player.x + 20
            if not self.facing_right:
                self.horizontal_flip()
            self.facing_right = True
        else:
            self.x = self.player.x - 20
            if self.facing_right:
                self.horizontal_flip()
            self.facing_right = False

        self.y = self.player.y
        self.move_abs((self.x, self.y))

        if self.drawn and self.frames_delta + 15 == frames:
            self.drawn = False


    def move_ip(self, coords):
        self.rect.move_ip(coords)

    def move_abs(self, coords):
        self.rect.left = coords[0]
        self.rect.top = coords[1]

    def horizontal_flip(self):
        self.image = pg.transform.flip(self.image, True, False)

    def toDraw(self, frames):
        if not self.drawn:
            self.drawn = True
            self.frames_delta = frames



class Enemy(pg.sprite.Sprite):
    def __init__(self, player, *args, **kwargs):
        pg.sprite.Sprite.__init__(self)
        self.image, self.rect = load_png("enemy.png")
        self.player = player

        self.x = random.choice([-40, player.screen.get_size()[0]+40])
        self.y = 230
        self.move_abs((self.x, self.y))

    def update(self):
        if self.x > self.player.x:
            self.x -= 1
        else:
            self.x += 1
        self.move_abs((self.x, self.y))

    def move_ip(self, coords):
        self.rect.move_ip(coords)

    def move_abs(self, coords):
        self.rect.left = coords[0]
        self.rect.top = coords[1]