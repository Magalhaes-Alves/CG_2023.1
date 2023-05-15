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
    print(np.cos(ang))
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

def translacao(poligono, tx, ty):
    m = criaTransformacao()

    m = compoeTranslacao(m, tx, ty)
    aplicaTransformacao(poligono, m)

def escala(poligono, sx, sy):
    m = criaTransformacao()
    # Precisa fazer a translacao antes em relação ao ponto mais proximo da origem(0,0)
    tx = poligono.points[0][0]
    ty = poligono.points[0][0]
    translacao(poligono, -tx, -ty)
    m = compoeEscala(m, sx, sy)
    aplicaTransformacao(poligono, m)
    # Aplica a translação novamente 
    translacao(poligono, tx, ty)

def rotacao(poligono, ang):
    m = criaTransformacao()
    # É necessário transladar o poligono
    m = compoeRotacao(m, ang)
    aplicaTransformacao(poligono, m)
    