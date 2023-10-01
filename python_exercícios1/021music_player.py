import pygame
# Precisamos iciciar o pygame.
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
# Precisamos esperar o evento terminar para poder finalizar o programa.
pygame.event.wait()
