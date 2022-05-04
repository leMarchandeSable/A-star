import pygame
import numpy as np
import time
import os


class Spot:
    def __init__(self, i, j):
        # i et j sont les indices dans grid : i l'indice des lignes j l'indice des colonnes
        self.i = i
        self.j = j

        # f g et h sont propre a chaque node / spot
        self.f = 0
        self.g = np.inf
        self.h = 0

        # list avec les voisins de self
        self.neighbors = []

        # on garde en mémoire le précédent spot
        self.previous = None

        # on créer des obstacles
        self.wall = False
        if np.random.rand() < wall_rate / 100:
            self.wall = True

    def show(self, color):
        # on convertie les indices en postion sur le canvas
        x = int(self.i * rez)
        y = int(self.j * rez)
        rec = pygame.Rect(x, y, rez, rez)

        # on trace les carrées et les contours
        pygame.draw.rect(surface, color, rec)
        # pygame.draw.rect(surface, noir, rec, 1)

        # on trace les murs
        if self.wall:
            pygame.draw.rect(surface, noir, rec)

        # on affiche la valeur de f, g et h sur la grille
        """
        text_surface_f = police.render(str(self.f), True, noir)
        text_surface_g = police.render(str(self.g), True, noir)
        text_surface_h = police.render(str(self.h), True, noir)

        text_rect_f = text_surface_f.get_rect()
        text_rect_g = text_surface_g.get_rect()
        text_rect_h = text_surface_h.get_rect()

        text_rect_f.center = (x + rez // 2, y + rez // 2)
        text_rect_g.center = (x + rez // 5, y + rez // 5)
        text_rect_h.center = (x + 4 * rez // 5, y + rez // 5)

        surface.blit(text_surface_f, text_rect_f)
        surface.blit(text_surface_g, text_rect_g)
        surface.blit(text_surface_h, text_rect_h)
        """

    def add_neighbors(self):
        # on ajoute les 4 voisins direct de self quand ils existent
        if self.i > 0:
            self.neighbors.append(grid[self.i - 1, self.j])
        if self.i < H // rez - 1:
            self.neighbors.append(grid[self.i + 1, self.j])
        if self.j > 0:
            self.neighbors.append(grid[self.i, self.j - 1])
        if self.j < L // rez - 1:
            self.neighbors.append(grid[self.i, self.j + 1])

        # on ajoute les 4 voisins en diagonale de self quand ils existent
        if self.i < 0 and self.j < 0:
            self.neighbors.append(grid[self.i - 1, self.j - 1])
        if self.i < H // rez - 1 and self.j > 0:
            self.neighbors.append(grid[self.i + 1, self.j - 1])
        if self.i > 0 and self.j < L // rez - 1:
            self.neighbors.append(grid[self.i - 1, self.j + 1])
        if self.i < H // rez - 1 and self.j < L // rez - 1:
            self.neighbors.append(grid[self.i + 1, self.j + 1])


def heuristique(a, b):
    # heuristique est la distance potentiel entre les spot a et b

    d = np.sqrt((a.i - b.i)**2 + (a.j - b.j)**2)     # euclidienne
    # d = abs(a.i - b.i) + abs(a.j - b.j)              # manathan

    return d


def draw():

    for i in range(H // rez):
        for j in range(L // rez):
            grid[i, j].show(blanc)

    for cell in close_set:
        cell.show(rouge)

    for cell in open_set:
        cell.show(vert)

    for cell in path:
        cell.show(bleu)

    start.show(gris)
    end.show(gris)


def save(surface, doc_name):

    path = 'C:/Users/simon/Documents/IPSA/A2/python/Pygame/'

    # creer le dossier parent uniquement s'il n'existe pas
    if doc_name not in os.listdir(path):
        os.chdir(path)
        os.mkdir(doc_name)

    # on enregiste les images
    os.chdir(path + doc_name)
    pygame.image.save(surface, str(round(time.time(), 1)) + ".jpg")


def maze_generation():
    launched = 1
    while launched:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                launched = 0

        surface.fill(blanc)

        if sum(pygame.mouse.get_pressed()) > 0:
            x, y = pygame.mouse.get_pos()
            i = x//rez
            j = y//rez

            grid[i, j].wall = True

        draw()
        pygame.display.flip()


# ----------------------------------------------------------------------------------------------------------------------
# initialisation constante
H = 800
L = 600
rez = 20
wall_rate = 0              # en pourcentage


blanc = (255, 255, 255)
gris = (150, 150, 150)
noir = (0, 0, 0)
rouge = (255, 0, 0)
bleu = (0, 0, 255)
vert = (0, 255, 0)

# initialisation environnement
grid = np.array([np.array([Spot(i, j) for j in range(L // rez)]) for i in range(H // rez)])         # on créer la grille
[[grid[i, j].add_neighbors() for i in range(H // rez)] for j in range(L // rez)]                    # on défini tout les voisins

start = grid[0, 0]
end = grid[H // rez - 1, L // rez - 1]
start.wall = False
end.wall = False
start.g = 0
start.f = heuristique(start, end)

open_set = [start]
close_set = []
path = []
finish = False

# initialisation fenetre
pygame.init()
pygame.display.set_caption("A*")
surface = pygame.display.set_mode((H, L))

# initialisation text
police = pygame.font.Font('freesansbold.ttf', 10)

# initialisation labyrinthe
maze_generation()

# ----------------------------------------------------------------------------------------------------------------------
# boucle infinie
launched = 1
while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = 0

    surface.fill(blanc)

    # ------------------------------------------------------------------------------------------------------------------
    # algorithme A*
    # on test si l'algorithme n'est pas fini
    if len(open_set) > 0 and not finish:
        
        # on cherche le spot avec le f min
        current = min(open_set, key=lambda spot: spot.f)

        # fin du code le chemin est trouvé
        if current == end:
            finish = True

        # on stoque le meilleur chemin
        path = []
        temp = current
        path.append(temp)
        while temp.previous is not None:
            path.append(temp.previous)
            temp = temp.previous

        # la meilleur option (current) est retiré de l'open_set, on sait que c'est le meilleur
        open_set.remove(current)
        close_set.append(current)

        # on cherche un meilleur chemin parmis les voisins de current
        for neighbor in current.neighbors:
            # on calcul un neighbor.g potentiel : g_temp
            g_temp = current.g + heuristique(current, neighbor)

            # on cherche si g_temp est meilleur que l'ancien chemin
            if g_temp < neighbor.g and not neighbor.wall:
                neighbor.g = g_temp
                neighbor.h = heuristique(neighbor, end)
                neighbor.f = neighbor.g + neighbor.h
                # on fixe sont antécedant
                neighbor.previous = current

                if neighbor not in open_set:
                    # on dit que ce voisins est intéressant
                    open_set.append(neighbor)
    # ------------------------------------------------------------------------------------------------------------------
    draw()

    pygame.display.flip()
