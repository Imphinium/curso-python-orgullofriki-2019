import sys
import os
import pygame as pg
from pygame.locals import *

size = H, W = 680, 400
framerate = 10

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

def main():
	screen = pg.display.set_mode(size)
	clock = pg.time.Clock()

	background = pg.Surface(size)
	background = background.convert()
	background.fill((180, 30, 70))

	sprite, rect = load_png("python_30.png")
	sprite_xy = x, y = size[0] / 2 - rect.w / 2, size[1] / 2 - rect.h / 2
	rect.move_ip(sprite_xy)

	while True:
		clock.tick(framerate)
		# Escuchar eventos
		for event in pg.event.get():
			if event.type == QUIT:
				sys.exit(0)
			elif event.type == KEYDOWN:
				print(f"{event.key}")
				if event.key == 97:
					rect.move_ip((-1,0))
				elif event.key == 119:
					rect.move_ip((0,1))
				elif event.key == 100:
					rect.move_ip((1,0))
				elif event.key == 115:
					rect.move_ip((0,-1))
		# Actualizar estados de juego

		# Pintar
		screen.blit(background, (0,0))
		screen.blit(sprite, rect, rect)

		pg.display.flip()

if __name__ == "__main__":
	pg.init()
	main()