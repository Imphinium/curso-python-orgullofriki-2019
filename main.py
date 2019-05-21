import sys
import pygame as pg
from pygame.locals import *

size = H, W = 680, 400
framerate = 1

def main():
	screen = pg.display.set_mode(size)
	clock = pg.time.Clock()

	background = pg.Surface(size)
	background = background.convert()
	background.fill((180, 30, 70))

	while True:
		clock.tick()
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