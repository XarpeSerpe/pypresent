#Escenas de la presentacion
import pygame


#Constantes

WIDTH = 800
HEIGHT = 480

#Funciones

def load_image(filename, transparent = False): #Aun no redimensiona
	try: image = pygame.image.load(filename)
	except pygame.error, message:
		raise SystemExit, message
	image = image.convert()
	if transparent:
		color = image.get_at((0,0))# toma el color de la esquina superior izquierda
	images.set_colorkey(color,RLEACCEL) # el color tomado se asigna a transparente
	#Escalado para llenar pantalla sin deformar
	image_width = image.get_width()
	image_height = image.get_height()
	if image_height <= image_width:
		escala = WIDTH/image_width
		image = pygame.transform.scale(image, (WIDTH,escala*image_height))
	else:
		escala = HEIGHT/image_height
		image = pygame.transform.scale(image, (escala*image_width,HEIGHT))
	return image


def carga_escena(scene):
	if scene == 0:
		imagen = load_image('./img/presentacion.png')
	elif scene == 1:
		imagen = load_image('./img/geocentrico.jpg')
	elif scene == 2:
		imagen = load_image('./img/copernico.jpg')
	elif scene == 3:
		imagen = load_image('./img/retrogrado.jpg')
	elif scene == 4:
		imagen = load_image('./img/kepler.jpg')
	
	return imagen
