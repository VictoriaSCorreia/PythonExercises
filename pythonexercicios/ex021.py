# Tocando música

import pygame
pygame.init()
pygame.mixer.music.load('Grilo.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
