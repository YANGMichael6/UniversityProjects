#Activité 10: Jeux de Platezau

#Partie Guidée: Le Tic-Tac-Toe

CaseT = str
# les elements de CaseT sont soit " " soit "O" soit "X"
PlateauT = List[List[CaseT]]
# les elements de PlateauT sont des matrices 3x3

#Q1)

def plateaut_vide() -> PlateauT:
    """Renvoie un plateau de tic-tac-toe de jeu vide."""
    return [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

assert plateaut_vide() == [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
pla1 : PlateauT = plateaut_vide()
assert pla1[1][1] == " "
assert pla1[0][2] == " "

#Q2)

def videt(pla: PlateauT, i: int, j: int) -> bool:
    """Précondition: 2 >= i >= 0 and 2 >= j >= 0
        Décide si la case (i, j) est vide ou non."""
    return pla[i][j] == " "

assert videt(pla1, 1, 1) == True
assert videt(pla1, 0, 2) == True

#Q3)

def jouex(pla: PlateauT, i: int, j: int) -> None:
    """ *** procédure ***
    Précondition: 2 >= i >= 0 and 2 >= j >= 0
    Dessine 'X' dans la case (i,j) de pla."""
    pla[i][j] = "X"

def joueo(pla: PlateauT, i: int, j: int) -> None:
    """ *** procédure *** 
    Précondition: 2 >= i >= 0 and 2 >= j >= 0
    Dessine '0' dans la case (i,j) de pla."""
    pla[i][j] = "O"

assert videt(pla1 , 0, 2) == True
assert jouex(pla1 , 1, 1) == None
assert joueo(pla1 , 0, 2) == None
assert videt(pla1 , 0, 2) == False

#Q4)

def dessine_plateaut(pla: PlateauT) -> str:
    """Renvoie une chaine de caractère correspondant à un affichage du plateau: la case (0,0) étant en bas à gauche."""
    res: str = ''
    l: int
    c: int
    for l in range(len(pla)-1, -1, -1):
        for c in range(len(pla[0])):
            res = res + pla[c][l]
        res = res + "\n"
    return res

assert dessine_plateaut(pla1) == 'O  \n X \n   \n'
print(dessine_plateaut(pla1))

def dessine_plateaut_bord(pla: PlateauT) -> str:
    """Renvoie une chaine de caractère correspondant à un affichage du plateau: la case (0,0) étant en bas à gauche."""
    res: str = "/---\ \n"
    l: int
    c: int
    for l in range(len(pla)-1, -1, -1):
        res = res + "|"
        for c in range(len(pla[0])):
            res = res + pla[c][l]
        res = res + "|" + "\n"
    res = res + "\---/"
    return res

assert dessine_plateaut_bord(pla1) == '/---\\ \n|O  |\n| X |\n|   |\n\\---/'
print(dessine_plateaut_bord(pla1))

#Q5)

def gagnet(pla: PlateauT, s: CaseT) -> bool:
    """Précondition: s == 'X' or s == 'O'
    Décide si le plateau pla est gagnant pour s."""
    j: int
    ligne: List[str]
    if (pla[0][0] == s and pla[1][1] == s and pla[2][2] == s) or (pla[2][0] == s and pla[1][1] == s and pla[0][2] == s):
        return True #vérifie les diagonales
    for ligne in pla:
        if ligne == [s,s,s]:
            return True #vérifie les lignes
    for j in range(len(pla[0])):
        if pla[0][j] == s and pla[1][j] == s and pla[2][j] == s:
            return True #vérifie les colonnes
    return False

assert gagnet([["O", " ", "X"], ["O", "X", " "], ["X", " ", " "]], "X") == True
assert gagnet([["O", " ", "X"], ["O", "X", " "], ["X", " ", " "]], "O") == False
assert gagnet([["X", " ", "O"], ["X", "O", " "], ["X", " ", " "]], "X") == True
assert gagnet([["X", " ", "O"], ["O", "X", " "], ["X", " ", " "]], "X") == False
assert gagnet([["O", "O", "O"], ["O", "O", "O"], ["O", "O", "O"]], "O") == True

#Q6)

def pleint(pla: PlateauT) -> bool:
    """Décide si le plateau pla est plein."""
    i: int
    j: int
    for j in range(len(pla)-1,-1,-1):
        for i in range(len(pla[0])):
            vide: bool = videt(pla, j, i)
            if vide:
                return False
    return True

assert pleint([["X", " ", "O"], ["O", "X", " "], ["X", " ", " "]]) == False
assert pleint([["O", "X", "O"], ["X", "O", "X"], ["O", "X", "O"]]) == True

#Q7)

import random

def case_aleatoire() -> int:
    """Renvoie un chiffre entre 0 et 2 inclu"""
    return int(random.random()*3)

def tourt(pla: PlateauT, i: int, j: int) -> None:
    """ *** procédure *** """
    if videt(pla, i, j):
        jouex(pla,i,j)
    else:
        print("***Cette case est prise***")
        return None
    if not gagnet(pla,'X') and not pleint(pla):
        I: int = case_aleatoire()
        J: int = case_aleatoire()
        while not videt(pla, I, J):
            I = case_aleatoire()
            J = case_aleatoire()
        joueo(pla, I, J)
        print(dessine_plateaut_bord(pla) + '\n' + "L'ordinateur joue en ( ", I, " , ", J, " )")
    if gagnet(pla, 'O'):
        print(dessine_plateaut_bord(pla) + '\n' + " *** PERDU *** ")
    elif gagnet(pla, 'X'):
        print(dessine_plateaut_bord(pla) + '\n' + " *** GAGNE ***")
    elif pleint(pla):
        print(dessine_plateaut_bord(pla) + '\n' + " ***EGALITE ***")
            
        
plat_essai: PlateauT = plateaut_vide()
assert not pleint(plat_essai) == True
assert tourt(plat_essai, 0, 0) == None



#Q9) SUGGESTION

def centre_case(i: int, j: int) -> Tuple[float, float, float]:
    """Renvoie la position du centre d’une case du plateau où le centre du plateau est en (0,0), avec le pas (l'écart entre les cases)."""
    pas: float = 0.6
    x: float = (j - 1) * pas
    y: float = (i - 1) * pas
    return x, y, pas

def grille() -> Image:
    """Dessine la grille du Tic-Tac-Toe."""
    long: float = 0.90
    pas: float = 0.6
    res: Image = overlay(draw_line(-long, -long, long, -long), draw_line(-long, long, long, long), draw_line(-long, -long, -long, long), draw_line(long, -long, long, long))
    k: int
    v: int
    for k in range(1,3):
        x: float = -long + k * pas
        res = overlay(res, draw_line(x, -long, x, long))
    for v in range(1,3):
        y: float = -long + v * pas
        res = overlay(res, draw_line(-long, y, long, y))
    return res

def dessine_x(i: int, j: int) -> Image:
    """Dessine le symbole 'X' dans une case recentré de (i,j)."""
    x, y, pas = centre_case(i, j)
    proportion: float = 0.35 * pas
    return overlay(draw_line(x - proportion, y - proportion, x + proportion, y + proportion), draw_line(x - proportion, y + proportion, x + proportion, y - proportion))

def dessine_o(i: int, j: int) -> Image:
    """Dessine le symbole 'O' dans une case recentré de (i,j)."""
    x, y, pas = centre_case(i, j)
    prop: float = 0.35 * pas
    x1: float = x - prop
    y1: float = y + prop
    x2: float = x + prop 
    y2: float = y - prop
    return draw_ellipse(x1, y1, x2, y2)

def draw_symbol(i: int, j: int, s: str) -> Image:
    """Dessine le symbole s aux coordonnées (i,j)."""
    if s == "X":
        return dessine_x(i, j)
    elif s == "O":
        return dessine_o(i, j)

def dessine_plateau_graphique(pla: PlateauT) -> Image:
    """Dessine le plateau Tic-Tac-Toe en graphe."""
    res: Image = grille()
    i: int
    j: int
    for i in range(len(pla)):
        for j in range(len(pla)-1, -1, -1):
            s: str = pla[j][i]
            if s == "O" or s == "X":
                res = overlay(res, draw_symbol(i, j, s))
    return res

show_image(dessine_plateau_graphique(pla1))

#SUGGESTION: Jeu de dames

CaseD = str
PlateauD = List[List[CaseD]]

def plateaud_debut() -> PlateauD:
    """Renvoie un plateau du jeu de dame qui débute."""
    case: CaseD = ' '
    Noir: str = 'N'
    Blanc: str = 'B'
    prec: str
    ligne: List[CaseD] = []
    res: PlateauD = []
    for _ in range(3):
        for _ in range(4):
            ligne.append(Blanc)
            ligne.append(case)
        res.append(ligne)
        ligne = []
        prec = Blanc
        Blanc = case
        case = prec
    for _ in range(2):
        res.append([' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])
    ligne = []
    case = ' '
    for _ in range(3):        
        for _ in range(4):
            ligne.append(case)
            ligne.append(Noir)
        res.append(ligne)
        ligne = []
        prec = case
        case = Noir
        Noir = prec
    return res

def vided(pla: PlateauD, i: int, j: int) -> bool:
    """Précondition: 7 >= i >= 0 and 7 >= j >= 0
        Décide si la case (i, j) est vide ou non."""
    return pla[i][j] == " "

assert plateaud_debut() == [['B', ' ', 'B', ' ', 'B', ' ', 'B', ' '], [' ', 'B', ' ', 'B', ' ', 'B', ' ', 'B'], ['B', ' ', 'B', ' ', 'B', ' ', 'B', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', 'N', ' ', 'N', ' ', 'N', ' ', 'N'], ['N', ' ', 'N', ' ', 'N', ' ', 'N', ' '], [' ', 'N', ' ', 'N', ' ', 'N', ' ', 'N']]

plad1 : PlateauD = plateaud_debut()
assert plad1[1][1] == "B"
assert plad1[1][6] == " "

def joueB(pla: PlateauD, pi: int, pj: int, i: int, j: int) -> None:
    """ *** procédure ***
    Précondition: 7 >= i >= 0 and 7 >= j >= 0 and 7 >= pi >= 0 and 7 >= pj >= 0
    Dessine 'B' dans la case (i,j) de pla."""
    pla[i][j] = "B"
    pla[pi][pj] = " "

def joueN(pla: PlateauD ,pi: int, pj: int, i: int, j: int) -> None:
    """ *** procédure *** 
    Précondition: 7 >= i >= 0 and 7 >= j >= 0 and 7 >= pi >= 0 and 7 >= pj >= 0
    Dessine 'N' dans la case (i,j) de pla."""
    pla[i][j] = "N"
    pla[pi][pj] = " "

assert vided(plad1, 3, 1) == True
assert joueB(plad1, 2, 0, 3,1) == None
assert joueN(plad1, 5, 1, 4,0) == None
assert vided(plad1, 4, 0) == False

def dessine_plateaud(pla: PlateauD) -> str:
    """Renvoie une chaine de caractère correspondant à un affichage du plateau: la case (0,0) étant en bas à gauche."""
    res: str = ''
    l: int
    c: int
    for l in range(len(pla)-1, -1, -1):
        for c in range(len(pla[0])):
            res = res + pla[l][c]
        res = res + "\n"
    return res

assert dessine_plateaud(plad1) == ' N N N N\nN N N N \n   N N N\nN       \n B      \n  B B B \n B B B B\nB B B B \n'
print(dessine_plateaud(plad1))

def dessine_plateaud_bord(pla: PlateauD) -> str:
    """Renvoie une chaine de caractère correspondant à un affichage du plateau pla: la case (0,0) étant en bas à gauche."""
    res: str = "/--------\ \n"
    l: int
    c: int
    for l in range(len(pla)-1, -1, -1):
        res = res + "|"
        for c in range(len(pla[0])):
            res = res + pla[l][c]
        res = res + "|" + "\n"
    res = res + "\--------/"
    return res

assert dessine_plateaud_bord(plad1) == '/--------\\ \n| N N N N|\n|N N N N |\n|   N N N|\n|N       |\n| B      |\n|  B B B |\n| B B B B|\n|B B B B |\n\\--------/'

print(dessine_plateaud_bord(plad1))

def gagned(pla: PlateauT, s: CaseT) -> bool:
    """Précondition: s == 'N' or s == 'B'
    Décide si le plateau pla est gagnant pour s."""
    i: str
    j: int
    perd:str
    if s == 'N':
        perd = 'B'
    else:
        perd = 'N'
    for j in range(8):
        for i in pla[j]:
            if i == perd:
                return False                        
    return True
