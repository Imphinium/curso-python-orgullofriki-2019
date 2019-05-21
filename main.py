import sys
import pygame as pg
from pygame.locals import *

size = H, W = 680, 400

def main():
	screen = pg.display.set_mode(size)

	while True:
		for event in pg.event.get():
			if event.type == QUIT:
				sys.exit()
		pg.display.flip()
		pass

if __name__ == "__main__":
	pg.init()
	main()