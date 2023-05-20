import numpy as np
from classes.Tranformations import *

def mapWindow(poli, window, viweport):

    lv= viweport.width
    av = viweport.height
    xi =window[0]
    yi = window[1]
    xf = window[2]
    yf= window[3]

    m= [[lv/(xf-xi), 0,1-xi*lv(xf-xi)],
        [0,av/(yf-yi),1-yi*av/(yf-yi)],
        [0,0,1]
    ]
    m = np.array(m)
    aplicaTransformacao(poli,m)

    

