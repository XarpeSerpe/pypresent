#!/usr/bin/python
# -*- coding: utf-8 -*-

#Modulos

import sys, pygame, math, time, scenes # anhado un fichero con todas las escenas en orden
from pygame.locals import *

#Constantes

WIDTH = 800
HEIGHT = 480

#Clases

#Funciones

def main():
	screen = pygame.display.set_mode((WIDTH, HEIGHT), FULLSCREEN)
	pygame.display.set_caption("Big Bang")
	background_image = scenes.load_image('./img/fondo.jpg')
	scene = 0
	while True:
		keys = pygame.key.get_pressed() 
		for eventos in pygame.event.get():
			if eventos.type == QUIT:
				sys.exit(0)
		if keys[K_RIGHT]:
			scene = scene + 1
		if keys[K_LEFT]:
			scene = scene - 1
		if keys[K_ESCAPE]:
			sys.exit(0)
		if scene <= -1:
			scene = 0
		background_image = scenes.carga_escena(scene)
		screen.blit(background_image, (0,0))
		pygame.display.flip()
		
		
	return 0

if __name__ == '__main__':
	pygame.init()
	main()
