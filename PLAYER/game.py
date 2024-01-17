import pygame
import pyscroll

pygame.init()

# Générer la fenêtre de notre jeu
pygame.display.set_caption("pokemon")
pygame.display.set_mode((500, 300))

running = True

# Générer un joueur sur un fichier game
player_position = tmx_data.get_objet_by_name("hero_01_white_f_run.png")
self.player = Player(player_position.x, player_position.y)

# Définir une liste qui va stocker les rectangles de collision
self.walls = []

for obj in tmx_data.objects:
    if obj.type == "collision":
        self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

# Dessiner le groupe de calque
self.group = pyscroll.pyscrollGroup(map_layeur=map_layeur, default_layer=3)
self.groupe.add(self.player)

def handle_input(self):
    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_UP]:
        self.player.move_up()
        self.player.change_animation('up')
    elif pressed[pygame.K_DOWN]:
        self.player.move_down()
        self.player.change_animation('down')
    elif pressed[pygame.K_LEFT]:
        self.player.move_left()
        self.player.change_animation('left')
    elif pressed[pygame.K_RIGHT]:
        self.player.move_right()
        self.player.change_animation('right')

def update(self):
    self.group.update()

    # Vérification collision
    for sprite in self.group.sprites():
        if sprite.feet.collidelist(self.walls) > -1:
            sprite.move_back()

def run(self):
    clock = pygame.time.Clock()

    # Boucle du jeu
    running = True

    while running:
        self.player.save_location()
        self.handle_input()
        self.update()
        self.group.center(self.player.rect.center)
        self.group.draw(self.screen)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        clock.tick(60)

pygame.quit()
