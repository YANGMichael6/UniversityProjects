#Activité 5
# 1
#q1
Polyn = List[int]
ex1: Polyn = [3, 0, 2]
ex2: Polyn = [1, -1, 1, -1, 0]
ex3: Polyn = [27]
ex4: Polyn = []

def degré(p:Polyn) -> int:
    """Renvoie le degré du polynôme p"""
    i: int
    for i in range(len(p)-1,-1,-1):
        if p[i]!=0:
            return i
    return 0

#Correction:
def degre(p:Polyn)->int:
    """Renvoie le degré du polynôme p"""
    i: int
    for i in range(len(p)):
        if p[-i-1]!=0:
            return len(p) - i - 1
    return 0

assert degré(ex1) == 2
assert degré(ex2) == 3
assert degré(ex3) == 0
assert degre(ex1) == 2
assert degre(ex2) == 3
assert degre(ex3) == 0

#Q2

def somme(p1: Polyn, p2:Polyn) -> Polyn:
    """Renvoie la somme de 2 polynômes p1 et p2"""
    s_p: Polyn = []
    p_degre_grand: Polyn
    p_degre_petit: Polyn
    if len(p1) >= len(p2):
        p_degre_grand = p1
        p_degre_petit = p2
    else:
        p_degre_grand = p2
        p_degre_petit = p1
    difference: int = len(p_degre_grand) - len(p_degre_petit)
    i:int
    for i in range(difference):
        p_degre_petit.append(0)
    k:int
    for k in range(len(p_degre_grand)):
        s_p.append(p_degre_grand[k] + p_degre_petit[k])
    return s_p

#Correction

def somme2(p1:Polyn, p2:Polyn)->Polyn:
    """Renvoie la somme de 2 polynôme p1 et p2"""
    res:Polyn = []
    i:int
    for i in range(max(len(p1),len(p2))):
        r:int = 0
        if i<len(p1):
            r = r + p1[i]
        if i<len(p2):
            r = r + p2[i]
        res.append(r)
    return res

            
assert somme(ex1, ex1) == [6, 0, 4]
assert somme(ex1, ex4) == ex1
assert somme(ex1, ex2) == [4, -1, 3, -1, 0]
assert somme2(ex1, ex1) == [6, 0, 4, 0, 0]
assert somme2(ex1, ex4) == ex1
assert somme2(ex1, ex2) == [4, -1, 3, -1, 0]

#Q3)
#Correction

def normalise(p:Polyn) -> Polyn:
    """Renvoie un polynôme normalisé"""
    i:int
    res:Polyn = []
    if p == []:
        return[]
    for i in range(degre(p)+1):
        res.append(p[i])
    if res == [0]:
        return []
    return res


assert normalise(ex1) == [3,0,2]
assert normalise(ex2) == [1, -1, 1, -1]
assert normalise([0 ,0 ,0 ,0 ,0]) == []
assert normalise([]) == []


#Q4)

def produit(p1:Polyn,p2:Polyn)->Polyn:
    """Renvoie le produit de deux polynômes"""
    res:Polyn = []
    i: int
    if (normalise(p1) == []) or (normalise(p2) == []):
        return []
    for i in range(degre(p1) + degre(p2) + 1):
        temp:int = 0
        j: int
        for j in range(max(0,i-degre(p2)), min(i,degre(p1)) + 1):
            temp = temp + p1[j] * p2[i-j]
        res.append(temp)
    return res

assert normalise(produit(ex1, ex4)) == []
assert normalise(produit(ex1, ex1)) == [9, 0, 12, 0, 4]
assert normalise(produit(ex1, ex2)) == [3, -3, 5, -5, 2, -2]
assert normalise(produit(ex1, ex3)) == [81,0,54] #erreur dans l'assert du sujet ?
assert normalise(produit([1, 1], [1, 0, 1])) == [1, 1, 1, 1]

#2 SUGGESTION: Autre opérations

#Multiplication par un entier

def multiplication_p(p:Polyn, n:int) -> Polyn:
    """Renvoie un polynôme multiplié par n"""
    res:Polyn = []
    i:int
    for i in range(0,len(p)-1):
        res.append(p[i]*n)
    return normalise(res)

assert multiplication_p(ex1,10) == [30,0,20]
assert multiplication_p(ex1,0) == []

def puissance_p(p:Polyn, n:int) -> Polyn:
    """Renvoie un polynôme mis à la puissance n"""
    res: Polyn = p
    i:int
    if n == 0:
        return [1]
    for i in range(n-1):
        res = produit(res, p)
    return normalise(res)

assert puissance_p(ex1,2) == [9, 0, 12, 0, 4]
assert puissance_p(ex1,0) == [1]

def derivee(p:Polyn)->Polyn:
    """Renvoie la dérivée du polynôme p"""
    res: Polyn = []
    p1:Polyn = normalise(p)
    i: int
    for i in range(degre(p1)):
        res.append((i+1)*p1[i+1])
    return normalise(res)

assert normalise(derivee([1,2,3,5])) == [2,6,15]
assert normalise(derivee(ex1)) == [0, 4]
assert normalise(derivee(ex4))== []

#3 SUGGESTION: Fonction associée

def valeur(p: Polyn, x: float) -> float:
    """Renvoie la valeur de la fonction associée au polynôme pcalculée en x"""
    p1: Polyn = normalise(p)
    res: float = 0
    i: int
    for i in range(len(p1)):
        res = res + p1[i]*x**i
    return res

assert valeur(normalise(ex1), 0) == 3
assert valeur(normalise(ex1), 1) == 5
assert valeur(ex4, 2.5) == 0

def courbe_poly(p:Polyn, nx: int, ny: int)-> Image:
    """Précondtion: nx >= 0 and ny>=0
        Renvoie le graphe fonctionnel approximé par des droites de la fonction associée au polynôme p"""
    courbe: Image = draw_line(0,0,0,0)
    i:int
    for i in range(-nx, nx+1):
        courbe = overlay(courbe, draw_line(i*10**-1, valeur(p, i*10**-1), (i+1)*10**-1, valeur(p, (i+1)*10**-1))) #On trace des lignes pour représenter la courbe (ici, on réduit la valeur de i pour pouvoir afficher sur la fenêtre
    return courbe
    

show_image(courbe_poly([1,-1,1,-1],10,100))


#4 SUGGESTION: Présentation

def cdp(p: Polyn) -> str:
    """Renvoie la forme avec les 'X' du polynôme p, avec '.' entre coef et X"""
    p1: Polyn = normalise(p)
    if p1 == []:
        return "0"  
    res: str = ""
    coef_str: str
    terme: str
    premier: bool = True
    for i in range(len(p1) - 1, -1, -1):
        coef: int = p1[i]
        if coef != 0:
            if coef == 1 and i != 0:
                coef_str = ""
            elif coef == -1 and i != 0:
                coef_str = "-"
            else:
                coef_str = str(coef)
            if i == 0:
                terme = coef_str
            elif i == 1:
                if coef_str == "" or coef_str == "-":
                    terme = coef_str + "X"
                else:
                    terme = coef_str + ".X"
            else:
                if coef_str == "-" or coef_str == "":
                    terme = coef_str + "X^" + str(i)
                else:
                    terme = coef_str + ".X^" + str(i)
            if premier:
                res = res + terme
                premier = False
            else:
                if coef > 0:
                    res = res + " + " + terme
                else:
                    if terme[0] == "-":
                        res = res + " - " + terme[1:]
                    else:
                        res = res + " - " + terme
    return res

assert cdp(ex1) == "2.X^2 + 3"
assert cdp(ex4) == "0"
assert cdp(ex2) == "-X^3 + X^2 - X + 1"
assert cdp(ex3) == "27"
assert cdp(produit(ex1, ex2)) == "-2.X^5 + 2.X^4 - 5.X^3 + 5.X^2 - 3.X + 3"


