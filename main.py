import sys
import pygame as pg
from pygame.locals import *

size = H, W = 680, 400

def main():
	screen = pg.display.set_mode(size)

	background = pg.Surface(size)
	background = background.convert()
	background.fill((180, 30, 70))

	screen.blit(background, (0,0))

	while True:
		for event in pg.event.get():
			if event.type == QUIT:
				sys.exit(0)
		pg.display.flip()
		pass

if __name__ == "__main__":
	pg.init()
	main()