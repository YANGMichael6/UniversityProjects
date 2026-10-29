import random

def sujet(i: int) -> str:
    """précondition: 1 <= i <= 6
        renvoie une chaîne"""
    if i == 1:
        return "Rayan"
    if i == 2:
        return "Chabib"
    if i == 3:
        return "Michael"
    if i == 4:
        return "Axel"
    if i == 5:
        return "Dagobert"
    else:
        return "Toto"

assert sujet(3) == "Michael"
assert sujet(5) == "Dagobert"

def verbe (v: int) -> str:
    """précondition: 1<= v <=6
        renvoie une chaine """
    if v== 1:
        return "mange"
    if v==2:
        return "détruit"
    if v==3:
        return "casse"
    if v==4:
        return "frappe"
    if v==5:
        return "regarde"
    else:
        return "observe"

def cod(m: int) -> str:
    """précondition: 1 <= m <= 6
        renvoie une chaîne"""
    if m == 1:
        return "du chocolat"
    if m == 2:
        return "des escargots"
    if m == 3:
        return "du dentifrice"
    if m == 4:
        return "de l'herbe"
    if m == 5:
        return "du riz"
    else:
        return "du taboulet"

def lieu(o: int) -> str:
    """précondition: 1 <= o <= 6
        renvoie une chaîne"""
    if o == 1:
        return "dans la fôret"
    if o == 2:
        return "dans la maison"
    if o == 3:
        return "à Paris"
    if o == 4:
        return "à Marseille"
    if o == 5:
        return "à Jussieu"
    else:
        return "dans la rue"

assert verbe(1) == "mange"
assert verbe(5) == "regarde"
assert cod(1) == "du chocolat"
assert cod(4) == "de l'herbe"
assert lieu(2) == "dans la maison"
assert lieu(6) == "dans la rue" 

def phrase(i: int, v: int, m: int, o: int) -> str:
    """précondtion: 1 <= i <= 6, 1 <= v <= 6, 1 <= m <= 6, 1 <= o <= 6
        renvoie une chaîne"""
    return sujet(i) + " " + verbe(v) + " " + cod(m) + " " + lieu(o) + "."

assert phrase(3, 1, 1, 2) == "Michael mange du chocolat dans la maison."

def de6() -> int:
    """renvoie un entier aléatoire compris entre 1 et 6"""
    return int(random.random()*6) + 1

def phrase_aleatoire() -> str:
    """ renvoie une phrase aléatoire"""
    i: int = de6()
    v: int = de6()
    m: int = de6()
    o: int = de6()
    return sujet(i) + " " + verbe(v) + " " + cod(m) + " " + lieu(o) + "."

#SUGGESTION 2

def cct(t:int) -> str:
    """précondition: 1 <=t <=8
        renvoie une chaine"""
    
    if t == 1:
        return "ce soir"
    if t == 2:
        return "demain"
    if t == 3:
        return "ce matin"
    if t == 4:
        return "cet après-midi"
    if t == 5:
        return "après avoir mangé"
    if t == 6:
        return "dans une heure"
    if t == 7:
        return "avant de manger"
    else:
        return "pendant une heure"

assert cct(3) == "ce matin"
assert cct(8) == "pendant une heure"

def adjectif(a:int) -> str:
    """precondition: 1 <= a <= 8
        renvoie une chaine"""
    if a == 1:
        return "Le plus beau"
    if a == 2:
        return "Le grand"
    if a == 3:
        return "Le mauvais"
    if a == 4:
        return "L'horrible"
    if a == 5:
        return "L'immonde"
    if a == 6:
        return "L'atroce"
    if a == 7:
        return "Le majestueux"
    else:
        return "L'incroyable"
assert adjectif(1)== "Le plus beau"
assert adjectif(3) == "Le mauvais"

def de8() -> int:
    """renvoie un entier aléatoire compris entre 1 et 8"""
    return int(random.random()*8) + 1


def phrase_aleatoire2() -> str:
    """ renvoie une phrase aléatoire"""
    i: int = de6()
    v: int = de6()
    m: int = de6()
    o: int = de6()
    a: int = de8()
    t: int = de8()
    return adjectif(t)+ " " + sujet(i) + " " + verbe(v) + " " + cod(m) + " " + lieu(o) + " " + cct(t)+ "."

#SUGGESTION 3

def verbe2(v2: int) -> str:
    """précondition: 1<= v2 <=8
        renvoie une chaine"""
    if v2 == 1:
        return "mange"
    if v2 == 2:
        return "detruit"
    if v2 == 3:
        return "casse"
    if v2 == 4:
        return "frappe"
    if v2 == 5:
        return "regarde"
    if v2 == 6:
        return "observe"
    #fin des verbes transitifs
    if v2 == 7:
        return "dort"
    else:
        return "court"
    #fin des verbes intransitifs
    
assert verbe2(1)== "mange"
assert verbe2(8)== "court"

def phrase_aleatoire3() -> str:
    """ renvoie une phrase aléatoire"""
    i: int = de6()
    v2: int = de8()
    m: int = de6()
    o: int = de6()
    a: int = de8()
    t: int = de8()
    if v2 <= 6:
        return adjectif(t)+ " " + sujet(i) + " " + verbe2(v2) + " " + cod(m) + " " + lieu(o) + " " + cct(t)+ "."
    else:
        return adjectif(t)+ " " + sujet(i) + " " + verbe2(v2) +" "+ lieu(o) + " " + cct(t)+ "."

#SUGGESTION 4

def nom_du_joueur(n: int) -> str:
    """précondition: 1 <= n <= 6
        renvoie une chaîne"""
    if n == 1:
        return "héros"
    if n == 2:
        return "justicier"
    if n == 3:
        return "voyageur"
    if n == 4:
        return "jeune homme"
    if n == 5:
        return "humain"
    else:
        return "aventurier"

assert nom_du_joueur(2) == "justicier"
assert nom_du_joueur(3) == "voyageur"

def de2() -> int:
    """renvoie un entier aléatoire entre 1 et 2"""
    return int(random.random()*2) + 1

def chemin_sinueux_aleatoire(r: int) -> str:
    "précondition: r = 1 ou r = 2"
    if r == 1:
        return "Vous parvenez avec effort à trouver le repère ennemi, et vous réussissez à le vaincre. Félicitation ! FIN DE L'HISTOIRE."
    if r == 2:
        return "Le chemin était si éprouvant que vous décidez finalement d'abandonner votre périple. Dommage... FIN DE L'HISTOIRE."

assert chemin_sinueux_aleatoire(1) == "Vous parvenez avec effort à trouver le repère ennemi, et vous réussissez à le vaincre. Félicitation ! FIN DE L'HISTOIRE."
assert chemin_sinueux_aleatoire(2) == "Le chemin était si éprouvant que vous décidez finalement d'abandonner votre périple. Dommage... FIN DE L'HISTOIRE."

def chemin_facile_aleatoire(d: int) -> str:
    "précondition: d = 1 ou d = 2"
    if d == 1:
        return "Vous trouver facilement le repère ennemi et réussissez difficilemet à vaincre l'ennemi. Félicitation ! FIN DE L'HISTOIRE."
    if d == 2:
        return "Vous trouver facilement le repère ennemi, mais vous ne parvenez pas à le vaincre par manque d'expérience. Dommage... FIN DE L'HISTOIRE. "

assert chemin_facile_aleatoire(1) == "Vous trouver facilement le repère ennemi et réussissez difficilemet à vaincre l'ennemi. Félicitation ! FIN DE L'HISTOIRE."
assert chemin_facile_aleatoire(2) == "Vous trouver facilement le repère ennemi, mais vous ne parvenez pas à le vaincre par manque d'expérience. Dommage... FIN DE L'HISTOIRE. "


def ldvelh(c: int) -> str:
    """précondition: 1 <= c <= 3
        renvoie un récit aléatoire"""
    if c == 1:
        return "Evènement 1. BIENVENUE " + nom_du_joueur(de6()) + ", vous avez été choisi pour combattre le roi maléfique de ce monde. Choisissez maintenant quel chemin prendre pour abattre l'ennemi: allez en 2 pour le chemin sinueux, allez en 3 pour le chemin facile."
    if c == 2:
        return "Evènement 2. " + chemin_sinueux_aleatoire(de2())
    if c == 3:
        return "Evènement 3. " + chemin_facile_aleatoire(de2())
    

