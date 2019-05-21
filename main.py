import sys
import pygame as pg
from pygame.locals import *

size = H, W = 680, 400
framerate = 60

def main():
	screen = pg.display.set_mode(size)
	clock = pg.time.Clock()

	background = pg.Surface(size)
	background = background.convert()
	background.fill((180, 30, 70))

	test = pg.Surface((200, 200))
	test = test.convert()
	test.fill((30, 70, 180))
	i=0

	while True:
		clock.tick(framerate)
		# Escuchar eventos
		for event in pg.event.get():
			if event.type == QUIT:
				sys.exit(0)
		# Actulizar estados de juego

		# Pintar
		screen.blit(background, (0,0))
		screen.blit(test, (i, 200))
		i+=1
		pg.display.flip()

if __name__ == "__main__":
	pg.init()
	main()