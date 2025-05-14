import pygame
pygame.init() #iniciar a biblioteca do pygame
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()