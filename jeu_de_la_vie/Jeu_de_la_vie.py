import random
import copy


class jeu_de_la_vie:
    def __init__(self,nombre_de_colonne , nombre_de_ligne, nombres_de_cellules):
        print("initialisation")
        self.nombres_de_cellules = nombres_de_cellules
        self.nombre_de_ligne = nombre_de_ligne
        self.nombre_de_colonne = nombre_de_colonne
        self.board = {}
        for col in range (nombre_de_colonne):
            for lin in range (nombre_de_ligne):
                self.board [(col,lin)] = False
        self.initialisation ()

    def initialisation (self):
        for nombres_de_boucles in range (self.nombres_de_cellules):
            row = random.randint(0, self.nombre_de_ligne - 1)
            col = random.randint(0, self.nombre_de_colonne - 1)
            self.board [(col,row)] = True

    def compute_next_step(self, coordinates, alive, copy_board):
        col = coordinates[0]
        line = coordinates[1]
        nombres_de_voisins_vivants = 0
        if line > 0 :
            if self.board [col,line-1] == True :
                nombres_de_voisins_vivants = nombres_de_voisins_vivants + 1
            if col > 0 and self.board [col-1,line-1] == True:
                nombres_de_voisins_vivants = nombres_de_voisins_vivants + 1
            if col < self.nombre_de_colonne-1 and self.board [col+1,line-1] == True:
                nombres_de_voisins_vivants = nombres_de_voisins_vivants + 1
        if line < self.nombre_de_ligne-1 :
            if self.board[col, line +1] == True:
                nombres_de_voisins_vivants = nombres_de_voisins_vivants + 1
            if col > 0 and self.board[col - 1, line + 1] == True:
                nombres_de_voisins_vivants = nombres_de_voisins_vivants + 1
            if col < self.nombre_de_colonne-1 and self.board[col + 1, line + 1] == True:
                nombres_de_voisins_vivants = nombres_de_voisins_vivants + 1
        if col > 0 and self.board[col - 1, line] :
            nombres_de_voisins_vivants = nombres_de_voisins_vivants + 1
        if col < self.nombre_de_colonne-1 and self.board[col + 1, line] :
            nombres_de_voisins_vivants = nombres_de_voisins_vivants + 1

        if alive :
            if not(nombres_de_voisins_vivants == 2 or nombres_de_voisins_vivants == 3):
                copy_board [coordinates]=False
        if not alive:
            if nombres_de_voisins_vivants == 3:
                copy_board [coordinates]= True




    def nouveau_tour (self):
        copy_board = copy.deepcopy(self.board)
        for coordinates, is_alive in self.board.items():
            self.compute_next_step(coordinates, is_alive, copy_board)
        self.board = copy_board

