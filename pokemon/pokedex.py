import pygame
import json

pygame.init()

# Charger les données du fichier JSON
with open('pokedex.json', 'r') as file:
    pokedex_data = json.load(file)

# Initialiser Pygame
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Pokédex')

font = pygame.font.Font(None, 36)

def display_pokemon(pokemon):
    screen.fill((255, 255, 255))
    
    # Afficher les informations du Pokémon
    text = font.render(f"ID: {pokemon['id']}", True, (0, 0, 0))
    screen.blit(text, (20, 20))

    text = font.render(f"Name: {pokemon['name']}", True, (0, 0, 0))
    screen.blit(text, (20, 60))

    text = font.render(f"Type: {pokemon['type']}", True, (0, 0, 0))
    screen.blit(text, (20, 100))

    # Charger et afficher l'image du Pokémon
    image = pygame.image.load(pokemon['image'])
    screen.blit(image, (400, 50))

    pygame.display.flip()

# Boucle principale
running = True
current_pokemon_index = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                current_pokemon_index = (current_pokemon_index + 1) % len(pokedex_data)
            elif event.key == pygame.K_LEFT:
                current_pokemon_index = (current_pokemon_index - 1) % len(pokedex_data)

    display_pokemon(pokedex_data[current_pokemon_index])

pygame.quit()
