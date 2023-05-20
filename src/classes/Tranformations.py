import numpy as np

def criaTransformacao():
    matrix = [[1,0,0], [0,1,0], [0,0,1]]

    return np.array(matrix)

def compoeTranslacao(m, tx, ty):
    matrix = [[1,0,tx], [0,1,ty], [0,0,1]]
    matrix = np.array(matrix)

    return matrix.dot(m)

def compoeEscala(m, sx, sy):
    matrix = [[sx,0,0], [0,sy,0], [0,0,1]]
    matrix = np.array(matrix)

    return matrix.dot(m)

def compoeRotacao(m, ang):
    ang = ang*np.pi/180
   
    matrix = [[np.cos(ang),-np.sin(ang),0], [np.sin(ang),np.cos(ang),0], [0,0,1]]
    matrix = np.array(matrix)

    return matrix.dot(m)

def aplicaTransformacao(poligono, m):  
    for i in range(poligono.points.shape[0]):
        pt = poligono.points[i]
        pt = np.resize(pt, 3)
        pt[2] = 1
        
        pt = np.transpose(pt)
        
        pt = m.dot(pt)
        pt = np.transpose(pt)
     
        poligono.points[i] = pt[:2]

def translacao(pol, tx, ty):
    m = criaTransformacao()
    m = compoeTranslacao(m, tx, ty)
    aplicaTransformacao(pol, m)

def escala(pol, sx, sy):
    # Move o primeiro ponto do poligono para o ponto (0,0)
    dx = pol.points[0,0]
    dy = pol.points[0,1]
    translacao(pol, -dx, -dy)

    # Aplica escala
    m = criaTransformacao()
    m = compoeEscala(m, sx, sy)
    aplicaTransformacao(pol, m)

    # Retorna o primeiro ponto do poligono ao ponto original
    translacao(pol, dx, dy)

def rotacao(pol, ang, altura,largura):
    
    centro_x = int(largura/2)
    centro_y = int(altura/2)
    x_centro_poligono = int(np.mean(pol.points[:,0]))
    y_centro_poligono = int(np.mean(pol.points[:,1]))
    
    tx = centro_x - x_centro_poligono
    ty = centro_y - y_centro_poligono

    #Transladar o centro do poligono para o centro da janela
    translacao(pol, tx, ty)

    # Aplica  rotação
    m = criaTransformacao()
    m = compoeRotacao(m, ang)
    aplicaTransformacao(pol, m)

    # Translada o novo centro para o centro original
    x_centro_poligono2 = int(np.mean(pol.points[:,0]))
    y_centro_poligono2 = int(np.mean(pol.points[:,1]))
    delta_x = x_centro_poligono2 - x_centro_poligono
    delta_y = y_centro_poligono2 - y_centro_poligono
    translacao(pol, -delta_x, -delta_y)
