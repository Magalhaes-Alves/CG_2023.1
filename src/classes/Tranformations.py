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
    