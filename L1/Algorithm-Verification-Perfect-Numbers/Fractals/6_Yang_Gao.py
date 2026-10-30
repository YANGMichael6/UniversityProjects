#21/10/2025 Activité 6: Fractales

#1 Partie guidée: Courbes

Point = Tuple[float, float]
Courbe = List[Point]

O: Point = (0.0 , 0.0)
tri1: Courbe = [O, (0.0 ,0.3) , (0.4 ,0.0) , O]

#Q1)
import math

def longueur(c:Courbe) -> float:
    """Renvoie la longueur de la courbe"""
    res: float = 0
    x1: float
    y1: float
    x2: float
    y2: float
    i: int
    for i in range(len(c)-1):
        x1,y1 = c[i]
        x2,y2 = c[i+1]
        res = res + math.sqrt((x2-x1)**2+(y2-y1)**2)
    return res
        
assert abs((longueur(tri1) - 1.2)) < 10**-12

#Q2)

def segment(p1:Point, p2:Point) -> Image:
    """Renvoie l'image correspondant au segment reliant p1 et p2"""
    x1, y1 = p1 
    x2, y2 = p2
    return draw_line(x1, y1, x2, y2)

show_image(segment((0.1,0.0),(0.2,0.2)))

#Q3)

def image_courbe(c:Courbe) -> Image:
    """Renvoie l'image correspondant à la courbe c par des segments"""
    res: Image = draw_line(0,0,0,0)
    i: int
    for i in range(len(c)-1):
        res = overlay(res, segment(c[i],c[i+1]))
    return res

show_image(image_courbe(tri1))
    
#Q4

def deplace(p: Point, d: str, di: float) -> Point:
    """Précondition: d == "H" or d == "B" or d == "G" or d == "D"
    Renvoie le point obtenu en déplaçant p dans la direction d de la direction di"""
    x, y = p
    if d == "H":
        y = y + di
    if d == "B":
        y = y - di
    if d == "G":
        x = x - di
    if d == "D":
        x = x + di
    res: Point = (x,y)
    return res


assert deplace(O, "G", 1) == (-1.0, 0.0)
assert deplace(O, "H", 0.5) == (0.0 , 0.5)

#Q5)

def spirale(ori:Point, dec: float, n: int)->Courbe:
    """Précondition: n >= 0
        Renvoie une image de n spirales selon un point d'origine ori et un décalage dec"""
    res: List[Point] = []
    origine: Point = ori
    m: List[str] = ["D","H","G","B"]
    i: int
    j: str
    temp: int = 0
    for i in range(n):
        for j in m:
            res.append(deplace(origine, j, temp*dec))
            origine = deplace(origine, j, temp*dec)
            temp = temp + 1
    return res

show_image(image_courbe(spirale(O, 0.01, 400)))

#2 Suggestion: Flocon de Koch

def triangle_initial(p: Point, r: float) -> Courbe:
    """Retourne les coordonnées des points d'un triangle équilatéral pointant en haut, de "centre" p"""
    x, y = p
    return [(x, y+r), (x - r*math.sin(math.pi/3), y - r/2), (x + r*math.sin(math.pi/3), y - r/2), (x, y+r)]

def point_intermediaire(a: Point, b: Point, t: float) -> Point:
    """Retourne les coordonnées d'un point de longueur ab*t depuis a"""
    ax, ay = a
    bx, by = b
    return (ax + t*(bx - ax), ay + t*(by - ay))

assert point_intermediaire((0,0), (2,0), 0.5) == (1.0, 0.0)


def rotation(p: Point, centre: Point, angle: float) -> Point:
    """Tourne le point p autour du centre d’un angle en radians"""
    x, y = p
    cx, cy = centre
    distance_xc: float = x - cx
    distance_yc: float = y - cy
    x2: float = cx + distance_xc * math.cos(angle) + distance_yc * math.sin(angle)
    y2: float = cy - distance_xc * math.sin(angle) + distance_yc * math.cos(angle)
    return (x2, y2)

def koch_segment(a: Point, b: Point) -> Courbe:
    """Renvoie les coordonnées des 4 points après transformation du segment [ab] en 4 segments"""
    p1: Point = point_intermediaire(a, b, 1/3)
    p3: Point = point_intermediaire(a, b, 2/3)
    sommet: Point = rotation(p3, p1, math.pi/3)
    return [a, p1, sommet, p3, b]

def courbe_koch(a: Point, b: Point, n: int) -> Courbe:
    """Renvoie les coordonnées de chaque point après n transformations du segment [ab]"""
    pts: Courbe = koch_segment(a, b)
    courbe: Courbe = []
    sous_courbe: Courbe = []
    if n == 0:
        return [a, b]
    i: int
    for i in range(4):
        sous_courbe = courbe_koch(pts[i], pts[i+1], n-1)
        courbe = courbe + sous_courbe[:-1]
    courbe.append(b)
    return courbe

assert courbe_koch((0,0), (1,0), 0) == [(0,0), (1,0)]

def courbe_flocon(p: Point, r: float, n: int) -> Courbe:
    """Renvoie les coordonnées des points des 4 segments"""
    triangles: Courbe = triangle_initial(p, r)
    points: Courbe = []
    segments: Courbe = []
    i: int
    for i in range(3):
        segments = courbe_koch(triangles[i], triangles[i+1], n)
        points = points + segments[:-1]
    points.append(triangles[0])
    return points

def image_circuit(courbe: Courbe) -> Image:
    """Retourne l'image en superposant chaque segment au fur et à mesure"""
    x1, y1 = courbe[0]
    x2, y2 = courbe[1]
    res: Image = draw_line(x1, y1, x2, y2)
    i: int
    for i in range(1, len(courbe) - 1):
        X1, Y1 = courbe[i]
        X2, Y2 = courbe[i + 1]
        img_segment: Image = draw_line(X1, Y1, X2, Y2)
        res = overlay(res, img_segment)
    return res

show_image(image_circuit(courbe_flocon(O,0.8,6)))
