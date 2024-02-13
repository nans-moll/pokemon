import pygame
import json

class Pokedex:
    def __init__(self, data_file):
        self.data_file = data_file
        pygame.init()
        self.ecran = pygame.display.set_mode((1067, 600))
        pygame.display.set_caption("Pokédex")
        self.BLANC = (255, 255, 255)
        self.NOIR = (0, 0, 0)
        self.POLICE = pygame.font.SysFont(None, 20)

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

            face_image_path = pokemon_data['face']
            image = self.obtenir_image_pokemon(face_image_path)

            if image:
                image = pygame.transform.scale(image, (200, 200))
            else:
                print("Impossible de charger l'image du Pokémon.")

            # Charger l'image du bouton de retour
            bouton_retour_image = pygame.image.load("unnamed.png").convert_alpha()
            bouton_retour_image = pygame.transform.scale(bouton_retour_image, (50, 50))
            x_retour, y_retour = 10, 10

            running = True
            while running:
                self.ecran.fill(self.BLANC)

                # Afficher l'image de fond
                self.afficher_image_fond()

                self.ecran.blit(image, (300, 200))
                texte_nom = self.POLICE.render(nom, True, self.NOIR)
                self.ecran.blit(texte_nom, (370, 190))
                texte_type = self.POLICE.render("Type: " + type_pokemon, True, self.NOIR)
                self.ecran.blit(texte_type, (600, 250))
                texte_hp = self.POLICE.render("HP: " + str(hp), True, self.NOIR)
                self.ecran.blit(texte_hp, (600, 280))
                texte_poids = self.POLICE.render("Poids: " + str(poids), True, self.NOIR)
                self.ecran.blit(texte_poids, (600, 310))
                texte_taille = self.POLICE.render("Taille: " + str(taille), True, self.NOIR)
                self.ecran.blit(texte_taille, (600, 340))

                # Afficher la description du Pokémon
                self.afficher_description(description)

                # Afficher l'image du bouton de retour
                self.ecran.blit(bouton_retour_image, (x_retour, y_retour))

                pygame.display.flip()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if x_retour < event.pos[0] < x_retour + 100 and y_retour < event.pos[1] < y_retour + 50:
                            running = False
                            return  # Retourner à la recherche

            pygame.quit()
        else:
            print("Le Pokémon demandé n'existe pas.")

    def afficher_description(self, description):
        # Séparer la description en lignes pour s'assurer qu'elle ne dépasse pas la largeur de la fenêtre
        lignes = []
        ligne_actuelle = ''
        mots = description.split()
        for mot in mots:
            texte = self.POLICE.render(mot, True, self.NOIR)
            largeur, _ = texte.get_size()
            if largeur + self.POLICE.size(" ")[0] > 380:  # Si le mot dépasse la largeur maximale
                if ligne_actuelle:  # S'il y a déjà du texte sur la ligne actuelle
                    lignes.append(ligne_actuelle)
                ligne_actuelle = mot + ' '  # Commencer une nouvelle ligne avec ce mot
            else:
                ligne_actuelle += mot + ' '

        if ligne_actuelle:  # Ajouter la dernière ligne
            lignes.append(ligne_actuelle)

        # Afficher les lignes de la description
        y = 400
        for ligne in lignes:
            texte_description = self.POLICE.render(ligne, True, self.NOIR)
            self.ecran.blit(texte_description, (10, y))
            y += self.POLICE.size(" ")[1]  # Augmenter la position en y pour afficher la prochaine ligne

    def recherche_par_nom_ou_id(self, identifiant):
        recherche = ""
        running = True
        while running:
            self.ecran.fill(self.BLANC)

            pygame.draw.rect(self.ecran, self.NOIR, (100, 250, 200, 30), 2)
            texte_entree = self.POLICE.render(recherche, True, self.NOIR)
            self.ecran.blit(texte_entree, (105, 255))

            texte_label = self.POLICE.render("Entrez le nom ou l'ID du Pokémon:", True, self.NOIR)
            self.ecran.blit(texte_label, (10, 220))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.afficher_pokemon(recherche)
                    elif event.key == pygame.K_BACKSPACE:
                        recherche = recherche[:-1]
                    else:
                        recherche += event.unicode

        pygame.quit()

    def afficher_image_fond(self):
        image_fond = pygame.image.load("fond2.png").convert()
        image_fond = pygame.transform.scale(image_fond, (1067, 600))
        self.ecran.blit(image_fond, (0, 0))

# Exemple d'utilisation
if __name__ == "__main__":
    pokedex = Pokedex('pokedata.json')
    pokedex.recherche_par_nom_ou_id("")