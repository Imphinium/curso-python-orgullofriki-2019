import sys
import os
import random
import sprites
import pygame as pg
from pygame.locals import *

screen_size = H, W = 680, 400
framerate = 60

def createGround(texture):
	ground_group = pg.sprite.Group()
	for i in range(10):
		for j in range(43*2):
			ground_tile = sprites.Ground((j*16 - 43*16, screen_size[1]-i*16), texture)
			ground_group.add(ground_tile)
	return ground_group

def generate_gradient(from_color, to_color, height, width):
    channels = []
    for channel in range(3):
        from_value, to_value = from_color[channel], to_color[channel]
        channels.append(
            numpy.tile(
                numpy.linspace(from_value, to_value, width), [height, 1],
            ),
        )
    return numpy.dstack(channels)

def scene_start(screen, clock):
	framerate = 20
	done = False

	font = pg.font.SysFont("comicsansms", 46)
	text1 = font.render("gêm fwriadol ddrwg", True, (255, 255, 255))
	font = pg.font.SysFont("comicsansms", 24)
	text2 = font.render("WASD para moverte", True, (255, 255, 255))
	text3 = font.render("Estacio para atacar", True, (255, 255, 255))
	font = pg.font.SysFont("comicsansms", 32)
	text4 = font.render("Pulsa cualquier tecla para empezar", True, (255, 255, 255))

	bg = pg.Surface(screen_size)
	bg = bg.convert()
	bg.fill((115, 3, 192))

	screen.blit(bg, (0,0))
	
	screen.blit(text1, (120, 10))
	screen.blit(text2, (220, 90))
	screen.blit(text3, (230, 140))
	screen.blit(text4, (80, 300))

	pg.display.flip()
	pg.time.delay(500)
	pg.event.clear()

	while not done:
		for event in pg.event.get():
			if event.type == QUIT:
				sys.exit(0)
			elif event.type == KEYDOWN:
				done = True	
		clock.tick(framerate)

		pg.display.flip()

def scene_end(screen, clock, points):
	framerate = 20
	done = False

	font = pg.font.SysFont("comicsansms", 46)
	text1 = font.render("TE LA RE MAMASTE", True, (0, 0, 0))
	font = pg.font.SysFont("comicsansms", 32)
	text4 = font.render(f"Has perdido con {points} puntos", True, (0, 0, 0))
	font = pg.font.SysFont("comicsansms", 24)
	text2 = font.render("ESC para salir", True, (0, 0, 0))
	text3 = font.render("Otra tecla para volver a empezar", True, (0, 0, 0))

	bg = pg.Surface(screen_size)
	bg = bg.convert()
	bg.fill((140, 252, 63))

	screen.blit(bg, (0,0))
	
	screen.blit(text1, (105, 10))
	screen.blit(text2, (240, 90))
	screen.blit(text3, (155, 140))
	screen.blit(text4, (130, 300))

	pg.display.flip()
	pg.time.delay(500)
	pg.event.clear()

	while not done:
		for event in pg.event.get():
			if event.type == QUIT:
				sys.exit(0)
			elif event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					sys.exit(0)
				else:
					main()
		clock.tick(framerate)

		pg.display.flip()


def main():
	screen = pg.display.set_mode(screen_size)
	clock = pg.time.Clock()
	font = pg.font.SysFont("comicsansms", 32)
	frames = 0
	points = 0

	text = font.render(f"Enemigos asesinados: {points}", True, (0, 0, 0))

	sky = pg.Surface(screen_size)
	sky = sky.convert()
	sky.fill((80, 140, 210))

	screen.blit(sky, (0,0))

	ground_group = createGround("ice.png")

	player = sprites.Player(screen, ground_group)
	player_group = pg.sprite.Group(player)

	sword = sprites.Sword(player)
	sword_group = pg.sprite.Group(sword)

	enemies_group = pg.sprite.Group()

	scene_start(screen, clock)

	while True:
		clock.tick(framerate)
		frames += 1
		# Escuchar eventos
		for event in pg.event.get():
			if event.type == QUIT:
				sys.exit(0)
			elif event.type == KEYDOWN:
				if event.key == K_w:
					player.jump()
				if event.key == K_SPACE:
					sword.toDraw(frames)

		keys = pg.key.get_pressed()
		if keys[pg.K_d]:
			player.move_right()
		if keys[pg.K_a]:
			player.move_left()

		# Actualizar estados de juego
		player_group.update()
		sword_group.update(frames)
		enemies_group.update()

		if sword.drawn:
			if pg.sprite.spritecollide(sword, enemies_group, True):
				points += 1
				text = font.render(f"Enemigos asesinados: {points}", True, (0, 0, 0))
		if pg.sprite.groupcollide(enemies_group, player_group, False, False):
			scene_end(screen, clock, points)

		if frames % 60 == 0:
			enemies_group.add(sprites.Enemy(player))

		# Pintar
		screen.blit(sky, (0,0))
		ground_group.draw(screen)
		player_group.draw(screen)
		if sword.drawn:
			sword_group.draw(screen)
		enemies_group.draw(screen)

		screen.blit(text, (10, 10))

		pg.display.flip()

if __name__ == "__main__":
	pg.init()
	main()