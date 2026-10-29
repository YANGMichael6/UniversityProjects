#Activité 3

#Partie Guidée: Simulation

#Q1)
def divise(k: int, n: int) -> bool:
    """ Pre : k > 0 and n >= 0
    Decide si k divise n """
    return n % k == 0

def est_parfait(n: int) -> bool:
    """ Pre : n >= 1
    Decide si n est un nombre parfait."""
    s : int = 0
    i : int = 1
    while i != n :
        if divise(i, n):
            s = s + i
        i = i + 1
    return n == s

assert divise(10, 100) == True
assert divise(10, 36) == False

assert est_parfait(6) == True
assert est_parfait(42) == False

#Q2)

def est_parfait_simulee(n:int) -> bool:
    """Précondition: n >= 1
        Decide si un n est un nombre parfait et affiche les valeurs de i et s en entrée et à chaque sortie de boucle"""
    s : int = 0
    i : int = 1
    print("debut de boucle, s = ", s)
    print("debut de boucle, i = ", i)
    print("="*19)
    while i != n :
        if divise(i, n):
            s = s + i
        i = i + 1
        print("fin du tour ", i-1, " s = ", s)
        print("fin du tour ", i-1, " i = ", i)
        print("="*19)
    print("sortie de boucle, s =", s, " et n =", n)
    return n == s
    
#Suggestion 2: Test

#Q1)

def test_parfait(n: int) -> bool:
    """Précondition: 1 <= n <= 137438691328
    Regarde si la fest cohérent avec la liste des 7 premiers nombres parfaits"""
    error: bool = False #le test est faux au départ
    i: int
    for i in range(1, n+1):
        if (i == 6 or i == 28 or i == 496 or i == 8128 or i == 33550336 or i == 8589869056 or i == 137438691328):
            error = error or not est_parfait(i) #si est_parfait(i) est vrai, on donne True à la valeur de error, sinon False
        else:
            error = error or est_parfait(i) #si est_parfait(i) est False, alors on donne False à error ou "error d'avant" qui a soit False, soit True en valeur
    return not error

assert test_parfait(1000) == True
assert test_parfait(6) == True   #notre fonction est_parfait marche donc bel et bien

#Suggestion 3

#Q1)

#Correction: la fonction est_parfait doit renvoyer soit True quand la somme des diviseurs propres de n est égale à n, soit False dans le cas contraire (inférieure ou supérieure à n.) D'après l'invariant, la somme s doit être inférieure ou égale à i - 1, ce qui assure que la boucle while s'arrêtera lorsque i == n, c'est-à-dire lorsque s > n-1. Donc l'invariant prouve donc la correction de ce programme.

#Q2)

def invariant(i: int, n: int, s: int) -> bool:
    """Précondition: s = "(la somme des diviseurs de n) <= i-1" and 1 <= i <= n and n >= 1
    Decide si l'invariant est vrai"""
    somme : int = 0
    l:int
    for l in range(1, i):
        if divise(l, n):
            somme = somme + l
    return somme == s

def est_parfait_invariant(n: int) -> bool:
    """Précondition: n >= 1
        decide si n est parfait et renvoie si l'invariant est toujours vrai ou non"""
    s: int = 0
    i: int = 1
    if invariant(i, n, s):
        print("Invariant vrai")
    else:
        print(False)
    while i != n:
        if divise(i, n):
            s = s + i
        i = i + 1
        if invariant(i, n, s):
            print("Invariant vrai")
        else:
            print("Invariant faux")
    return s == n

#Q4)

#invariant: "s est égal à la somme de tous les diviseurs de n inférieurs ou égaux à i−1"

#Initialisation: En entrée de boucle, on a i == 1 et s == 0. La somme des diviseurs de n (soit s) doivent être inférieurs ou égale à i-1. L'invariant est donc vrai en début de boucle, car: i-1 = 1-1 <= 0 = s (puisque les diviseurs de 0 inférieure à i-1 n'existe pas pour i = 1).

#Hérédité: On suppose que l'invariant est vrai au début. On aurait donc qu'à chaque boucle que la somme des diviseurs propres soient <= i.
#Lorsque i != n, si i divise n, alors s = s + i (un divisuer de n), puis i = i+1. Donc au final s reste la somme de diviseurs de n, et respecte la condition suivante: s <= i (tel que i == (i+1) - 1).
#Si i ne divise pas n, alors s conserve sa valeur (s == somme de diviseurs de n, toujours <= i-1), puis i = i+1, et donc l'invariant reste toujours vrai.

#Terminaison: Quand i == n, on sort de la boucle, et le programme renvoie False si s > n ou s < n, sinon True si et seulement s == n. En effet, l'invariant ici "est" s <= n-1, ce qui correspond à savoir si s==n ou non, donc implique forcément la sortie d'un booléen lors du return. Donc en sortie de boucle, l'invariant est toujours vrai même en sortie de boucle.
