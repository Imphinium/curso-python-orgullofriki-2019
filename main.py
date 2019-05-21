import sys
import os
import random
import pygame as pg
from pygame.locals import *

size = H, W = 680, 400
framerate = 1

def load_png(name):
    """ Load image and return image object"""
    fullname = os.path.join('assets', name)
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

class Apple(pg.sprite.Sprite):
	def __init__(self, *args, **kwargs):
		pg.sprite.Sprite.__init__(self)
		self.image, self.rect = load_png("python_30.png")

		sprite_xy = x, y = size[0] / 2 - self.rect.w / 2, size[1] / 2 - self.rect.h / 2
		self.rect.move_ip(sprite_xy)

	def update(self):
		_pos = (random.randint(0, size[0]-self.rect.width),
			random.randint(0, size[1]-self.rect.height))
		self.move_abs(_pos)

	def move_ip(self, coords):
		self.rect.move_ip(coords)

	def move_abs(self, coords):
		self.rect.left = coords[0]
		self.rect.top = coords[1]

def main():
	screen = pg.display.set_mode(size)
	clock = pg.time.Clock()

	background = pg.Surface(size)
	background = background.convert()
	background.fill((180, 30, 70))

	screen.blit(background, (0,0))

	apple_sprite = Apple()
	apple_group = pg.sprite.Group(apple_sprite)



	while True:
		clock.tick(framerate)
		# Escuchar eventos
		for event in pg.event.get():
			if event.type == QUIT:
				sys.exit(0)
			elif event.type == KEYDOWN:
				print(f"{event.key}")
				if event.key == 97:
					apple_sprite.move_ip((-1,0))
				elif event.key == 119:
					apple_sprite.move_ip((0,1))
				elif event.key == 100:
					apple_sprite.move_ip((1,0))
				elif event.key == 115:
					apple_sprite.move_ip((0,-1))
		# Actualizar estados de juego
		

		# Pintar
		screen.blit(background, apple_sprite.rect, apple_sprite.rect)
		apple_group.update()
		apple_group.draw(screen)

		pg.display.flip()

if __name__ == "__main__":
	pg.init()
	main()