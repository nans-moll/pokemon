import pygame
import sys
import os

# Initialisation de Pygame
pygame.init()

# Définition des couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Configuration de l'écran
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pokemon Game Menu")


# Chargement de l'image du logo Pokemon
logo_img = pygame.image.load(os.path.join("pokemon-logo.png"))
logo_img = pygame.transform.scale(logo_img, (300, 150))  # Redimensionner l'image


"""
# Chargement de la musique du menu
pygame.mixer.music.load("menu_music.mp3")
pygame.mixer.music.play(-1)  # -1 signifie de jouer en boucle
"""

# Définition de la police
font = pygame.font.SysFont(None, 60)

# Définition des fonctions pour afficher le texte centré
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)

# Fonction principale pour afficher le menu
def main_menu():
    while True:
        screen.fill(WHITE)
        # Afficher l'image du logo Pokemon
        screen.blit(logo_img, (WIDTH // 2 - 200, HEIGHT // 4))
        
        mouse_x, mouse_y = pygame.mouse.get_pos()
        
        # Dessiner les boutons
        start_btn = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 50, 200, 50)
        load_btn = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 20, 200, 50)
        quit_btn = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 90, 200, 50)
        
        pygame.draw.rect(screen, GREEN, start_btn)
        pygame.draw.rect(screen, GREEN, load_btn)
        pygame.draw.rect(screen, GREEN, quit_btn)
        
        draw_text("Start Game", font, BLACK, screen, WIDTH // 2, HEIGHT // 2)
        draw_text("Load Game", font, BLACK, screen, WIDTH // 2, HEIGHT // 2 + 70)
        draw_text("Quit", font, BLACK, screen, WIDTH // 2, HEIGHT // 2 + 140)
        
        # Gestion des événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_btn.collidepoint(mouse_x, mouse_y):
                    # Arrêter la musique et commencer le jeu
                    pygame.mixer.music.stop()
                    print("Starting Game...")
                if load_btn.collidepoint(mouse_x, mouse_y):
                    # Arrêter la musique et charger la partie
                    pygame.mixer.music.stop()
                    print("Loading Game...")
                if quit_btn.collidepoint(mouse_x, mouse_y):
                    pygame.quit()
                    sys.exit()
                    
        pygame.display.update()

# Lancement du menu
if __name__ == "__main__":
    main_menu()

