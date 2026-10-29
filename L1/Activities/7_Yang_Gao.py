#Activité 7 INFO 04/11/2025

#1 Partie guidée

Coord = Tuple[int, int]
Dir = str
# un élément de Dir est soit "N", soit "S", soit "E", soit "O"

#Q1

def deplace(c: Coord, d: Dir) -> Coord:
    """Renvoie les coordonnées du point c après déplacement d."""
    (x, y) = c
    if d == "N":
        y = y + 1
    if d == "E":
        x = x + 1
    if d == "S":
        y = y - 1
    if d == "O":
        x = x - 1
    return (x,y)

ori : Coord = (0, 0)
p1 : Coord = (3, 3)
p2 : Coord = (0, 2)
assert deplace(ori , "N") == (0, 1)
assert deplace(p1 , "E") == (4, 3)
assert deplace(deplace(p2 , "N"), "S") == p2

#Q2)

def deplace_chemin(c: Coord, ch: List[Dir]) -> Coord:
    """Renvoie les coordonnées de c après déplacement du chemin ch."""
    if ch == []:
        return c
    else:
        return deplace_chemin(deplace(c, ch[0]), ch[1:])
    

assert deplace_chemin(ori, ["N", "N"]) == p2
assert deplace_chemin(ori, ["N", "E", "S", "O"]) == ori
assert deplace_chemin(ori, []) == ori

#Q3

Case = Tuple[bool, bool, bool, bool, str]
Laby = List[List[Case]]

laby1 : Laby = [[( True , True , False , False , ""),
(False , False , True , False , "ENTREE")],
[( True , False , False , True , ""),
(False , False , True , False , "SORTIE")]]

laby2 : Laby = [
[( True , False , False , False , ""),
(False , True , True , False , ""),
(True , True , False , False , ""),
(False , False , True , False , "ENTREE")],
[( False , False , False , False , ""),
(True , True , False , True , ""),
(True , False , True , True , ""),
(False , True , True , False , "")],
[( True , False , False , False , ""),
(False , False , True , True , ""),
(True , True , False , False , ""),
(False , False , True , True , "")],
[( True , False , False , False , "SORTIE"),
(True , False , True , False , ""),
(True , False , True , True , ""),
(False , False , True , False , "")]
]

laby3 : Laby = [[(True, True, False, False, ''), (False, False, True, False, ''), (False, True, False, False, ''), (True, False, False, False, ''), (True, True, True, False, ''), (True, False, True, False, ''), (True, True, True, False, ''), (True, False, True, False, ''), (True, False, True, False, ''), (True, False, True, False, ''), (False, False, True, False, ''), (True, True, False, False, ''), (True, False, True, False, ''), (False, True, True, False, ''), (False, True, False, False, ''), (True, False, False, False, ''), (False, True, True, False, ''), (False, True, False, False, ''), (False, True, False, False, ''), (False, True, False, False, 'ENTREE')], [(True, False, False, True, ''), (False, True, True, False, ''), (True, True, False, True, ''), (True, False, True, False, ''), (True, False, True, True, ''), (False, False, True, False, ''), (False, False, False, True, ''), (True, False, False, False, ''), (True, True, True, False, ''), (True, True, True, False, ''), (True, False, True, False, ''), (True, True, True, True, ''), (False, False, True, False, ''), (False, True, False, True, ''), (False, True, False, True, ''), (True, False, False, False, ''), (True, False, True, True, ''), (False, True, True, True, ''), (False, True, False, True, ''), (False, True, False, True, '')], [(True, True, False, False, ''), (True, True, True, True, ''), (True, False, True, True, ''), (True, True, True, False, ''), (True, False, True, False, ''), (False, True, True, False, ''), (True, False, False, False, ''), (False, True, True, False, ''), (False, False, False, True, ''), (False, True, False, True, ''), (True, False, False, False, ''), (True, True, True, True, ''), (False, False, True, False, ''), (True, False, False, True, ''), (False, True, True, True, ''), (True, False, False, False, ''), (False, True, True, False, ''), (True, False, False, True, ''), (False, True, True, True, ''), (False, True, False, True, '')], [(False, True, False, True, ''), (True, False, False, True, ''), (False, False, True, False, ''), (True, False, False, True, ''), (False, True, True, False, ''), (False, False, False, True, ''), (False, True, False, False, ''), (True, True, False, True, ''), (False, False, True, False, ''), (True, True, False, True, ''), (False, True, True, False, ''), (False, True, False, True, ''), (False, True, False, False, ''), (True, False, False, False, ''), (False, True, True, True, ''), (True, True, False, False, ''), (True, True, True, True, ''), (True, False, True, False, ''), (False, True, True, True, ''), (False, True, False, True, '')], [(True, False, False, True, ''), (True, True, True, False, ''), (False, False, True, False, ''), (True, False, False, False, ''), (False, True, True, True, ''), (True, True, False, False, ''), (True, False, True, True, ''), (False, True, True, True, ''), (True, False, False, False, ''), (False, False, True, True, ''), (False, False, False, True, ''), (True, True, False, True, ''), (True, False, True, True, ''), (False, True, True, False, ''), (True, True, False, True, ''), (False, False, True, True, ''), (False, True, False, True, ''), (False, True, False, False, ''), (False, False, False, True, ''), (False, True, False, True, '')], [(True, False, False, False, ''), (True, True, True, True, ''), (False, False, True, False, ''), (True, False, False, False, ''), (True, False, True, True, ''), (True, True, True, True, ''), (False, True, True, False, ''), (False, False, False, True, ''), (True, True, False, False, ''), (False, False, True, False, ''), (False, True, False, False, ''), (False, False, False, True, ''), (True, False, False, False, ''), (False, False, True, True, ''), (False, True, False, True, ''), (False, True, False, False, ''), (True, False, False, True, ''), (True, True, True, True, ''), (False, False, True, False, ''), (False, True, False, True, '')], [(True, False, False, False, ''), (True, True, True, True, ''), (True, False, True, False, ''), (False, False, True, False, ''), (True, False, False, False, ''), (False, True, True, True, ''), (False, False, False, True, ''), (False, True, False, False, ''), (False, True, False, True, ''), (True, False, False, False, ''), (False, True, True, True, ''), (False, True, False, False, ''), (True, True, False, False, ''), (False, False, True, False, ''), (False, False, False, True, ''), (True, True, False, True, ''), (False, False, True, False, ''), (False, True, False, True, ''), (True, True, False, False, ''), (False, True, True, True, '')], [(True, True, False, False, ''), (True, False, True, True, ''), (False, False, True, False, ''), (True, True, False, False, ''), (True, False, True, False, ''), (False, True, True, True, ''), (False, True, False, False, ''), (False, True, False, True, ''), (False, True, False, True, ''), (True, True, False, False, ''), (True, False, True, True, ''), (False, False, True, True, ''), (False, True, False, True, ''), (True, False, False, False, ''), (False, True, True, False, ''), (True, False, False, True, ''), (True, True, True, False, ''), (True, False, True, True, ''), (False, True, True, True, ''), (False, False, False, True, '')], [(False, False, False, True, ''), (True, True, False, False, ''), (False, True, True, False, ''), (False, False, False, True, ''), (True, False, False, False, ''), (True, False, True, True, ''), (False, True, True, True, ''), (False, True, False, True, ''), (False, True, False, True, ''), (False, True, False, True, ''), (True, False, False, False, ''), (False, True, True, False, ''), (False, True, False, True, ''), (False, True, False, False, ''), (True, True, False, True, ''), (False, False, True, False, ''), (True, False, False, True, ''), (False, True, True, False, ''), (True, False, False, True, ''), (False, True, True, False, '')], [(False, True, False, False, ''), (False, True, False, True, ''), (True, False, False, True, ''), (False, True, True, False, ''), (True, False, False, False, ''), (True, True, True, False, ''), (True, False, True, True, ''), (True, False, True, True, ''), (True, False, True, True, ''), (False, False, True, True, ''), (True, False, False, False, ''), (True, False, True, True, ''), (False, True, True, True, ''), (True, False, False, True, ''), (False, True, True, True, ''), (False, True, False, False, ''), (True, False, False, False, ''), (False, True, True, True, ''), (True, True, False, False, ''), (False, False, True, True, '')], [(True, False, False, True, ''), (False, True, True, True, ''), (True, False, False, False, ''), (True, True, True, True, ''), (True, False, True, False, ''), (True, True, True, True, ''), (True, False, True, False, ''), (False, True, True, False, ''), (False, True, False, False, ''), (False, True, False, False, ''), (True, False, False, False, ''), (False, True, True, False, ''), (True, False, False, True, ''), (True, False, True, False, ''), (True, False, True, True, ''), (False, True, True, True, ''), (True, True, False, False, ''), (False, False, True, True, ''), (True, False, False, True, ''), (False, True, True, False, '')], [(True, False, False, False, ''), (True, False, True, True, ''), (False, False, True, False, ''), (True, False, False, True, ''), (False, True, True, False, ''), (False, True, False, True, ''), (True, False, False, False, ''), (True, False, True, True, ''), (True, False, True, True, ''), (True, False, True, True, ''), (True, False, True, False, ''), (False, False, True, True, ''), (True, True, False, False, ''), (False, True, True, False, ''), (True, True, False, False, ''), (True, True, True, True, ''), (False, True, True, True, ''), (True, False, False, False, ''), (False, True, True, False, ''), (False, False, False, True, '')], [(False, True, False, False, ''), (True, False, False, False, ''), (True, True, True, False, ''), (False, True, True, False, ''), (False, True, False, True, ''), (True, False, False, True, ''), (True, False, True, False, ''), (True, False, True, False, ''), (True, False, True, False, ''), (True, True, True, False, ''), (True, True, True, False, ''), (False, False, True, False, ''), (False, False, False, True, ''), (True, True, False, True, ''), (False, False, True, True, ''), (False, True, False, True, ''), (True, False, False, True, ''), (False, True, True, False, ''), (True, False, False, True, ''), (False, True, True, False, '')], [(False, True, False, True, ''), (True, False, False, False, ''), (False, False, True, True, ''), (False, True, False, True, ''), (True, False, False, True, ''), (True, True, True, False, ''), (False, True, True, False, ''), (True, True, False, False, ''), (True, True, True, False, ''), (False, True, True, True, ''), (True, False, False, True, ''), (False, True, True, False, ''), (True, False, False, False, ''), (True, True, True, True, ''), (False, True, True, False, ''), (True, False, False, True, ''), (False, False, True, False, ''), (True, False, False, True, ''), (False, False, True, False, ''), (False, True, False, True, '')], [(True, False, False, True, ''), (True, False, True, False, ''), (True, True, True, False, ''), (False, True, True, True, ''), (False, True, False, False, ''), (False, False, False, True, ''), (False, True, False, True, ''), (False, False, False, True, ''), (False, False, False, True, ''), (False, True, False, True, ''), (False, True, False, False, ''), (False, True, False, True, ''), (True, False, False, False, ''), (False, False, True, True, ''), (True, False, False, True, ''), (True, False, True, False, ''), (True, True, True, False, ''), (False, False, True, False, ''), (True, True, False, False, ''), (False, False, True, True, '')], [(True, True, False, False, ''), (True, False, True, False, ''), (False, False, True, True, ''), (False, False, False, True, ''), (False, True, False, True, ''), (True, False, False, False, ''), (True, True, True, True, ''), (False, False, True, False, ''), (False, True, False, False, ''), (False, False, False, True, ''), (True, False, False, True, ''), (True, True, True, True, ''), (True, False, True, False, ''), (True, True, True, False, ''), (False, False, True, False, ''), (False, True, False, False, ''), (True, True, False, True, ''), (False, True, True, False, ''), (False, True, False, True, ''), (False, True, False, False, '')], [(True, False, False, True, ''), (True, True, True, False, ''), (False, False, True, False, ''), (False, True, False, False, ''), (True, True, False, True, ''), (False, False, True, False, ''), (True, False, False, True, ''), (True, True, True, False, ''), (False, False, True, True, ''), (True, True, False, False, ''), (False, False, True, False, ''), (True, False, False, True, ''), (False, True, True, False, ''), (True, True, False, True, ''), (False, True, True, False, ''), (True, True, False, True, ''), (False, True, True, True, ''), (True, False, False, True, ''), (False, False, True, True, ''), (False, True, False, True, '')], [(False, True, False, False, ''), (True, False, False, True, ''), (True, True, True, False, ''), (False, False, True, True, ''), (False, True, False, True, ''), (True, True, False, False, ''), (True, True, True, False, ''), (True, True, True, True, ''), (True, False, True, False, ''), (False, False, True, True, ''), (False, True, False, False, ''), (False, True, False, False, ''), (False, False, False, True, ''), (False, False, False, True, ''), (True, True, False, True, ''), (False, True, True, True, ''), (True, False, False, True, ''), (True, True, True, False, ''), (True, True, True, False, ''), (False, False, True, True, '')], [(True, False, False, True, ''), (False, True, True, False, ''), (True, False, False, True, ''), (True, True, True, False, ''), (False, False, True, True, ''), (False, False, False, True, ''), (False, False, False, True, ''), (True, True, False, True, ''), (True, False, True, False, ''), (False, False, True, False, ''), (True, False, False, True, ''), (True, False, True, True, ''), (True, True, True, False, ''), (True, True, True, False, ''), (False, False, True, True, ''), (False, False, False, True, ''), (True, False, False, False, ''), (False, False, True, True, ''), (False, True, False, True, ''), (False, True, False, False, '')], [(True, False, False, False, 'SORTIE'), (True, False, True, True, ''), (True, False, True, False, ''), (True, False, True, True, ''), (True, False, True, False, ''), (True, False, True, False, ''), (True, False, True, False, ''), (True, False, True, True, ''), (True, False, True, False, ''), (True, False, True, False, ''), (False, False, True, False, ''), (True, False, False, False, ''), (False, False, True, True, ''), (True, False, False, True, ''), (False, False, True, False, ''), (True, False, False, False, ''), (True, False, True, False, ''), (True, False, True, False, ''), (True, False, True, True, ''), (False, False, True, True, '')]]


def deplace_possible(la: Laby, c: Coord, d: Dir) -> bool:
    """Précondition: c est une coordonnée possible dans la      Décide si la direction d est possible depuis les coordonnées c dans le labyrinthe la."""
    long: int = len(la)
    larg: int = len(la[0])
    x, y = c
    if not (0 <= x < long and 0 <= y < larg):
        return False
    n,e,s,o,_ = la[x][y]
    if d == "N" and n == True:
        return True
    if d == "E" and e == True:
        return True
    if d == "S" and s == True:
        return True
    if d == "O" and o == True:
        return True
    else:
        return False

assert deplace_possible(laby1, (0, 1), "S") == True
assert not deplace_possible(laby1, (0, 1), "N") == True
assert not deplace_possible(laby1, (0, 1), "E") == True

#Q4)

def chemin_possible(la: Laby, c: Coord, ch: List[Dir]) -> bool:
    """Décide si les déplacements sont possibles à partir de c dans la"""
    if ch == []:
        return True
    else:
        return deplace_possible(la, c, ch[0]) and chemin_possible(la, deplace(c,ch[0]), ch[1:])

assert chemin_possible(laby1, (0, 1), ["S", "E", "N"]) == True
assert chemin_possible(laby1, (0, 1), ["S", "N", "S", "E", "N"]) == True
assert not chemin_possible(laby1, (0, 1), ["S", "O"]) == True
assert not chemin_possible(laby1, (0, 1), ["S", "E", "N", "O"]) == True


#Q5)

def est_solution(la: Laby, c: Coord, ch: List[Dir]) -> bool:
    """Décide si le couple (c, ch) est solution du labyrinthe la."""
    x,y = c
    n,e,s,o,d = la[x][y]
    X,Y = deplace_chemin(c, ch)
    _,_,_,_,f = la[X][Y]
    return f == "SORTIE" and chemin_possible(la,c,ch) and d == "ENTREE"

assert est_solution(laby1, (0, 1), ["S", "E", "N"]) == True
assert est_solution(laby1, (0, 1), ["S", "E", "O", "E", "N"]) == True
assert not est_solution(laby1, (0, 0), ["E", "N"]) == True
assert not est_solution(laby1, (0, 1), ["S", "E"]) == True
assert not est_solution(laby1, (0, 1), ["E"]) == True

#2 SUGGESTION: Marche aléatoire

import random

def de() -> int:
    """Renvoie un chiffre aléatoire entre 1 et 4 inclus"""
    return int(random.random()*4)+1

def decide_dir(n:int) -> str:
    """Précondition: 0 <= n <= 4
    Choisis la direction selon n"""
    if n == 1:
        return 'N'
    if n == 2:
        return 'E'
    if n == 3:
        return 'S'
    if n == 4:
        return 'O'

def marche_aleatoire(la: Laby, debut: Coord, limite: int) -> List[Dir]:
    """Précondition: 0 <= limite <= 900
    Trouve une solution aléatoire pour sortir du labyrinthe la."""
    chemin: List[Dir] = []
    position: Coord = debut
    x,y = position
    (_,_,_,_,f) = la[x][y]
    if limite <= 0 or f == 'SORTIE':
        return chemin
    lance: int = de()
    direction: str = decide_dir(lance)
    if deplace_possible(la, position, direction) and f != 'SORTIE':
        position = deplace(position, direction)
        suite: List[Dir] = marche_aleatoire(la, position, limite - 1)
        chemin.append(direction)
        X,Y = position
        (_,_,_,_,F) = la[X][Y]
        f = F
        return chemin + suite
    else:
        return marche_aleatoire(la, debut, limite - 1)


assert est_solution(laby1, (0,1), marche_aleatoire(laby1, (0,1), 900)) == True
assert est_solution(laby2, (0,3), marche_aleatoire(laby2, (0,3), 900)) == True
assert est_solution(laby3, (0,19), marche_aleatoire(laby3, (0,19), 900)) == False #Cette assertion se base sur le fait que l'on ne peut pas trouver le chemin en 900 déplacements ou moins. Si cela était possible, alors il faudrait beaucoup de chance pour que l'assertion soit vraie.

#SUGGESTION 3: Main droite

def droite(direc: Dir) -> Dir:
    """Renvoie la direction direc vers la droite"""
    if direc == "N":
        return "E"
    if direc == "E":
        return "S"
    if direc == "S":
        return "O"
    if direc == "O":
        return "N"

def gauche(direc: Dir) -> Dir:
    """Renvoie la direction direc vers la gauche"""
    if direc == "N":
        return "O"
    if direc == "O":
        return "S"
    if direc == "S":
        return "E"
    if direc == "E":
        return "N"

def demi_tour(direc: Dir) -> Dir:
    """Renvoie le déplacement inverse de direc"""
    if direc == "N":
        return "S"
    if direc == "S":
        return "N"
    if direc == "E":
        return "O"
    if direc == "O":
        return "E"

def ordre_main_droite(direc: Dir) -> List[Dir]:
    """Renvoie la direction droite selon l'orientation"""
    return [droite(direc), direc, gauche(direc), demi_tour(direc)]

def main_droite(la: Laby, position: Coord, direc: Dir, limite: int = 900) -> List[Dir]:
    """Précondition: 0 <= limite <= 900
    Trouve la solution pour sortir du labyrinthe la avec la méthode de la main droite."""    
    if limite <= 0:
        return []
    orientation: Dir = direc
    x, y = position
    (_,_,_,_,f) = la[x][y]
    if f == 'SORTIE':
        return []
    d: str
    for d in ordre_main_droite(orientation):
        if deplace_possible(la, position, d):
            prochain: Coord = deplace(position, d)
            suite: List[Dir] = main_droite(la, prochain, d, limite - 1)
            return [d] + suite
    return []

assert est_solution(laby1, (0,1), main_droite(laby1, (0,1), 'N', 900)) == True
assert est_solution(laby2, (0,3), main_droite(laby2, (0,3), 'N', 900)) == True
assert est_solution(laby3, (0,19), main_droite(laby3, (0,19), 'N', 900)) == True
