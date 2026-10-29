import math

#Activité 2: approximation de pi

#1)Partie guidée

#question 1
def terme_leibniz(n: int) -> float:
    """précondition: n >= 0
        renvoie un le n-ième terme de la somme"""
    return (-1)**n/(2*n+1)

assert terme_leibniz(0) == 1
assert terme_leibniz(1) == -1/3
assert terme_leibniz(10) == 1/21

#question 2
def somme_leibniz(n: int) -> float:
    """précondition: n >= 0
        renvoie la somme des n premiers termes"""
    i: int = 0
    s: float = 0
    while i <= n:
        s = s + terme_leibniz(i)
        i = i + 1
    return s

assert somme_leibniz(0) == 1
assert somme_leibniz(1) == 1 - 1 / 3
assert somme_leibniz(4) == 1 - 1 / 3 + 1 / 5 - 1 / 7 + 1 / 9

#question 3
def approx_leibniz(n: int) -> float:
    """précondition: n >= 0
        renvoie une approximation de pi à partir de la somme des n premiers termes multipliés par 4"""
    return somme_leibniz(n) * 4


#question 4
assert abs(approx_leibniz(100) - math.pi) < (10**-2)
assert abs(approx_leibniz(1000) - math.pi) < (10**-3)
assert abs(approx_leibniz(10000) - math.pi) < (10**-4)

#SUGGESTION 2: Formule des frères Chudovsky
def factorielle(n: int) -> int:
    """précondition: n >= 0
        renvoie la factorielle de n"""
    i: int = 0
    res: int = 1
    while i < n:
        i = i + 1
        res = res * i
    return res

assert factorielle(0) == 1
assert factorielle(3) == 6

def M(q: int) -> float:
    """précondition: q >= 0
        renvoie le q-ieme terme de la suite M"""
    return factorielle(6 * q)/(factorielle(3*q)*factorielle(q)**3)

assert M(0) == 1
assert M(1) == 120

def L(q: int) -> float:
    """précondition: q >= 0
        renvoie le q-ieme terme de la suite L"""
    return q*545140134+13591409

assert L(0) == 13591409

def X(q:int)->float:
    """précondition: q >= 0
        renvoie le q-ieme terme de la suite X"""
    return (-262537412640768000)**q

assert X(1) == -262537412640768000

def approx_chudnovsky(n: int) -> float:
    """précondition: n >= 0
        renvoie une approximation de pi"""
    i: int = 0
    s: float = 0
    C: float = 426880*math.sqrt(10005)
    while i <= n:
        s = s + (M(i) * L(i))/X(i)
        i = i + 1
    return C * s**-1

assert abs(approx_chudnovsky(10) - math.pi) < (10**-1)


#SUGGESTION 3:
def approx_chudnovsky_optim(n: int) -> float:
    """précondition: n >= 1
        renvoie une approximation de pi en stockant le (n-1)-ième terme"""
    C: float = 426880 * math.sqrt(10005)
    s: float = 0
    M: float = 1
    L: int = 13591409
    X: int = 1
    i: int = 0
    while i <= n:
        if i > 0:
            M = M * ((6*i) * (6*i-1) * (6*i-3) * (6*i-4)*(6*i-5))/((3*i) * (3*i-1) * (3*i-2) * (i**3))
        #il s'agit de la formule de Mq = Mq-1 * "Mq/Mq-1" (avec leur expression factorielle simplifiée)
            L = L + 545140134
            X = X * -262537412640768000
        s = s + (M*L/X)
        i = i + 1
    return C * s**-1

assert abs(approx_chudnovsky_optim(15) - math.pi) < (10**-2)







    
