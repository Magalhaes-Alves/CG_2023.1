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
    else:
        print("Linha completamente fora da janela")

# Definição da viewport
xmin = 100
ymin = 100
xmax = 400
ymax = 300

#Pontos da linha
x1 = 50
y1 = 150
x2 = 450
y2 = 250

cohen_sutherland(xmin, ymin, xmax, ymax, x1, y1, x2, y2)