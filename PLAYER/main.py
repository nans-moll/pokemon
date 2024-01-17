import pygame
pygame.init()

#generer la fenetre de notre jeu
pygame.display.set_caption("pokemon")
pygame.display.set_mode((800, 600))

running =True

# boucle tant que cett condition est vrai
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()


