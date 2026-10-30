import math

def rotation(dx: float, dy: float, theta: float) -> Tuple[float, float]:
    xr: float = dx * math.cos(theta) - dy * math.sin(theta)
    yr: float = dx * math.sin(theta) + dy * math.cos(theta)
    return (xr, yr)

def courbe_koch(x1: float, y1: float, x2: float, y2: float, n: int) -> Image:
    if n == 0:
        return draw_line(x1, y1, x2, y2)
    dx: float = x2 - x1
    dy: float = y2 - y1
    v1x: float = dx/3
    v1y: float = dy/3
    v4x: float = dx/3
    v4y: float = dy/3
    rdx, rdy = rotation(dx/3, dy/3, math.pi/3)   
    rdx2, rdy2 = rotation(dx/3, dy/3, -math.pi/3)
    bx: float = x1 + v1x
    by: float = y1 + v1y
    cx: float = bx + rdx
    cy: float = by + rdy
    dx: float = cx + rdx2
    dy: float = cy + rdy2
    img1: Image = courbe_koch(x1, y1, bx, by, n - 1)
    img2: Image = courbe_koch(bx, by, cx, cy, n - 1)
    img3: Image = courbe_koch(cx, cy, dx, dy, n - 1)
    img4: Image = courbe_koch(dx, dy, x2, y2, n - 1)
    return overlay(img1, img2, img3, img4)

show_image(courbe_koch(-1.0, 0.0, 1.0, 0.0, 3))
