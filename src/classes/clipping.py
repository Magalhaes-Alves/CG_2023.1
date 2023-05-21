INSIDE = 0  # Código para ponto dentro da janela
LEFT = 1    # Código para ponto à esquerda da janela
RIGHT = 2   # Código para ponto à direita da janela
BOTTOM = 4  # Código para ponto abaixo da janela
TOP = 8     # Código para ponto acima da janela

def compute_outcode(x, y, xmin, ymin, xmax, ymax):
    code = INSIDE
    if x < xmin:
        code |= LEFT
    elif x > xmax:
        code |= RIGHT
    if y < ymin:
        code |= BOTTOM
    elif y > ymax:
        code |= TOP
    return code

def cohen_sutherland(xmin, ymin, xmax, ymax, x1, y1, x2, y2):
    code1 = compute_outcode(x1, y1, xmin, ymin, xmax, ymax)
    code2 = compute_outcode(x2, y2, xmin, ymin, xmax, ymax)
    accept = False

    while True:
        if code1 == 0 and code2 == 0:
            accept = True
            break
        elif code1 & code2 != 0:
            break
        else:
            x = 0
            y = 0
            if code1 != 0:
                code_out = code1
            else:
                code_out = code2

            if code_out & TOP:
                x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1)
                y = ymax
            elif code_out & BOTTOM:
                x = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1)
                y = ymin
            elif code_out & RIGHT:
                y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1)
                x = xmax
            elif code_out & LEFT:
                y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)
                x = xmin

            if code_out == code1:
                x1 = x
                y1 = y
                code1 = compute_outcode(x1, y1, xmin, ymin, xmax, ymax)
            else:
                x2 = x
                y2 = y
                code2 = compute_outcode(x2, y2, xmin, ymin, xmax, ymax)

    if accept:
        print("Linha recortada de ({},{}) para ({},{})".format(x1, y1, x2, y2))
        return [(int(x1),int(y1)), (int(x2),int(y2))]
    else:
        print("Linha completamente fora da janela")
        return None
"""
Exemplo de uso

Definição da viewport
xmin = 100
ymin = 100
xmax = 400
ymax = 300

Pontos da linha
x1 = 50
y1 = 150
x2 = 450
y2 = 250

cohen_sutherland(xmin, ymin, xmax, ymax, x1, y1, x2, y2)"""

def is_inside(p1,p2,q):
    R = (p2[0] - p1[0]) * (q[1] - p1[1]) - (p2[1] - p1[1]) * (q[0] - p1[0])
    if R <= 0:
        return True
    else:
        return False

def compute_intersection(p1,p2,p3,p4):
    
    """
    given points p1 and p2 on line L1, compute the equation of L1 in the
    format of y = m1 * x + b1. Also, given points p3 and p4 on line L2,
    compute the equation of L2 in the format of y = m2 * x + b2.
    
    To compute the point of intersection of the two lines, equate
    the two line equations together
    
    m1 * x + b1 = m2 * x + b2
    
    and solve for x. Once x is obtained, substitute it into one of the
    equations to obtain the value of y.
    
    if one of the lines is vertical, then the x-coordinate of the point of
    intersection will be the x-coordinate of the vertical line. Note that
    there is no need to check if both lines are vertical (parallel), since
    this function is only called if we know that the lines intersect.
    """
    
    # if first line is vertical
    if p2[0] - p1[0] == 0:
        x = p1[0]
        
        # slope and intercept of second line
        m2 = (p4[1] - p3[1]) / (p4[0] - p3[0])
        b2 = p3[1] - m2 * p3[0]
        
        # y-coordinate of intersection
        y = m2 * x + b2
    
    # if second line is vertical
    elif p4[0] - p3[0] == 0:
        x = p3[0]
        
        # slope and intercept of first line
        m1 = (p2[1] - p1[1]) / (p2[0] - p1[0])
        b1 = p1[1] - m1 * p1[0]
        
        # y-coordinate of intersection
        y = m1 * x + b1
    
    # if neither line is vertical
    else:
        m1 = (p2[1] - p1[1]) / (p2[0] - p1[0])
        b1 = p1[1] - m1 * p1[0]
        
        # slope and intercept of second line
        m2 = (p4[1] - p3[1]) / (p4[0] - p3[0])
        b2 = p3[1] - m2 * p3[0]
    
        # x-coordinate of intersection
        x = (b2 - b1) / (m1 - m2)
    
        # y-coordinate of intersection
        y = m1 * x + b1
    
    intersection = (x,y)
    
    return intersection

def clip(subject_polygon,clipping_polygon):
    
    final_polygon = subject_polygon.copy()
    clipping_polygon = clipping_polygon[::-1]
    for i in range(len(clipping_polygon)):
        
        # stores the vertices of the next iteration of the clipping procedure
        next_polygon = final_polygon.copy()
        
        # stores the vertices of the final clipped polygon
        final_polygon = []
        
        # these two vertices define a line segment (edge) in the clipping
        # polygon. It is assumed that indices wrap around, such that if
        # i = 1, then i - 1 = K.
        c_edge_start = clipping_polygon[i - 1]
        c_edge_end = clipping_polygon[i]
        
        for j in range(len(next_polygon)):
            
            # these two vertices define a line segment (edge) in the subject
            # polygon
            s_edge_start = next_polygon[j - 1]
            s_edge_end = next_polygon[j]
            
            if is_inside(c_edge_start,c_edge_end,s_edge_end):
                if not is_inside(c_edge_start,c_edge_end,s_edge_start):
                    intersection = compute_intersection(s_edge_start,s_edge_end,c_edge_start,c_edge_end)
                    final_polygon.append(intersection)
                final_polygon.append(tuple(s_edge_end))
            elif is_inside(c_edge_start,c_edge_end,s_edge_start):
                intersection = compute_intersection(s_edge_start,s_edge_end,c_edge_start,c_edge_end)
                final_polygon.append(intersection)
    
    return (final_polygon)

"""Exemplo de uso
subject_polygon = [(100, 100), (200, 100), (200, 200), (100, 200)]  # Polígono a ser recortado
clip_polygon = [(150, 150), (250, 150), (250, 250), (150, 250)]  # Polígono de recorte

result_polygon = sutherland_hodgman(subject_polygon, clip_polygon)
print("Polígono recortado:", result_polygon)"""
