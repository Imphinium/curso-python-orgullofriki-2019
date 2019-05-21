import sys
import os
import pygame as pg
from pygame.locals import *

size = H, W = 680, 400
framerate = 60

def load_png(name):
    """ Load image and return image object"""
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
        if image.get_alpha is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except pygame.error:
        print(f"Cannot load image: {fullname}")
        raise SystemExit
    return image, image.get_rect()

def main():
	screen = pg.display.set_mode(size)
	clock = pg.time.Clock()

	background = pg.Surface(size)
	background = background.convert()
	background.fill((180, 30, 70))

	while True:
		clock.tick(framerate)
		# Escuchar eventos
		for event in pg.event.get():
			if event.type == QUIT:
				sys.exit(0)
		# Actulizar estados de juego

		# Pintar
		screen.blit(background, (0,0))
		pg.display.flip()

if __name__ == "__main__":
	pg.init()
	main()