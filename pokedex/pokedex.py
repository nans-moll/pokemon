import pygame
import json

class Pokedex:
    def __init__(self, data_file):
        self.data_file = data_file

    def charger_donnees_pokemon(self):
        with open(self.data_file, 'r', encoding='utf-8') as f:
            donnees = json.load(f)
        return donnees

    def obtenir_donnees_pokemon(self, identifiant):
        donnees = self.charger_donnees_pokemon()
        for pokemon in donnees:
            if str(pokemon['id']) == str(identifiant) or pokemon['name']['nom'].lower() == identifiant.lower():
                return pokemon
        return None

    def obtenir_image_pokemon(self, image_path):
        return pygame.image.load(image_path).convert_alpha()

    def afficher_pokemon(self, identifiant):
        pokemon_data = self.obtenir_donnees_pokemon(identifiant)
        if pokemon_data:
            nom = pokemon_data['name']['nom'].capitalize()
            type_pokemon = pokemon_data['type'][0].capitalize()
            hp = pokemon_data['base']['HP']
            poids = pokemon_data['profile']['poids']
            taille = pokemon_data['profile']['hauteur']
            description = pokemon_data['description']

            LARGEUR = 800
            HAUTEUR = 600
            BLANC = (255, 255, 255)
            NOIR = (0, 0, 0)
            POLICE = pygame.font.SysFont(None, 24)  # Création de la police après l'initialisation de pygame

            ecran = pygame.display.set_mode((LARGEUR, HAUTEUR))
            pygame.display.set_caption("Pokédex")

            image_path = "003sb.png"  # Définir le chemin vers l'image par défaut
            image = self.obtenir_image_pokemon(image_path)

            if image:
                image = pygame.transform.scale(image, (200, 200))
            else:
                print("Impossible de charger l'image du Pokémon.")

            running = True
            while running:
                ecran.fill(BLANC)

                ecran.blit(image, (400, 50))
                texte_nom = POLICE.render(nom, True, NOIR)
                ecran.blit(texte_nom, (400 + (200 - texte_nom.get_width()) // 2, 10))
                texte_type = POLICE.render("Type: " + type_pokemon, True, NOIR)
                ecran.blit(texte_type, (10, 250))
                texte_hp = POLICE.render("HP: " + str(hp), True, NOIR)
                ecran.blit(texte_hp, (10, 280))
                texte_poids = POLICE.render("Poids: " + str(poids), True, NOIR)
                ecran.blit(texte_poids, (10, 310))
                texte_taille = POLICE.render("Taille: " + str(taille), True, NOIR)
                ecran.blit(texte_taille, (10, 340))
                texte_description = POLICE.render("Description: " + description, True, NOIR)
                ecran.blit(texte_description, (10, 370))

                pygame.display.flip()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False

            pygame.quit()
        else:
            print("Le Pokémon demandé n'existe pas.")

    def recherche_par_nom_ou_id(self, identifiant):
        pygame.init()
        recherche = ""
        POLICE = pygame.font.SysFont(None, 24)  # Création de la police après l'initialisation de pygame
        LARGEUR = 800
        HAUTEUR = 600
        BLANC = (255, 255, 255)
        NOIR = (0, 0, 0)
        ecran = pygame.display.set_mode((LARGEUR, HAUTEUR))
        pygame.display.set_caption("Recherche Pokémon")

        bouton_retour = pygame.Rect(20, 20, 100, 50)
        POLICE_BOUTON = pygame.font.SysFont(None, 20)
        texte_retour = POLICE_BOUTON.render("Retour", True, NOIR)

        running = True
        while running:
            ecran.fill(BLANC)

            pygame.draw.rect(ecran, NOIR, (250, 250, 300, 30), 2)  # Dessine une bordure pour la zone de texte
            texte_entree = POLICE.render(recherche, True, NOIR)
            ecran.blit(texte_entree, (255, 255))

            ecran.blit(texte_retour, bouton_retour)

            texte_label = POLICE.render("Entrez le nom ou l'ID du Pokémon:", True, NOIR)
            ecran.blit(texte_label, (250, 220))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if bouton_retour.collidepoint(event.pos):
                        running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.afficher_pokemon(recherche)
                    elif event.key == pygame.K_BACKSPACE:
                        recherche = recherche[:-1]
                    else:
                        recherche += event.unicode

        pygame.quit()

# Exemple d'utilisation
if __name__ == "__main__":
    pokedex = Pokedex('pokedata.json')
    pokedex.recherche_par_nom_ou_id("")
