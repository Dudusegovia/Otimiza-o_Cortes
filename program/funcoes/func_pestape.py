import copy
from __init__ import *
from classes.class_mosaico import Mosaico
from classes.class_tessera import Tessera
import numpy as np
def pestapar(mosaicoo: np.array, tesseraa: Tessera, x=0, y=0):
    mosaicooo = (mosaicoo)
    tesser = tesseraa.matriz1
    colunas_tesser=len(tesser[0])
    linhas_tesser=len(tesser)
    i=-1
    im=-1-x

    if y + colunas_tesser > len(mosaicooo[0]):
        return "y + tamanho tessera ultrapassou"
    elif x + linhas_tesser > len(mosaicooo):
        return "x + altura tessera ultrapassou"
    
    while i > -linhas_tesser-1:
        j=0
        jm=0+y
        while j < colunas_tesser:
            mosaicooo[im][jm] += tesser[i][j]
            if mosaicooo[im][jm] > 3:
                return "sobreposicao"
            j+=1
            jm+=1
        i-=1
        im-=1
    
    return mosaicooo

def translada_pestape(tesseraa: Tessera, novo_mosaico):
    linhas_tessera=len(tesseraa.matriz1)
    colunas_mosaico=len(novo_mosaico.mosaicum[0])
    x=0
    y=0
    matriz = copy.deepcopy(novo_mosaico.mosaicum)
    aumentou=0
    while x + linhas_tessera  < novo_mosaico.tamanho_maximo:
        result = pestapar(mosaicoo=copy.deepcopy(matriz), tesseraa=tesseraa, x=x, y=y)
        if isinstance(result, np.ndarray):
            return result
        elif result == "sobreposicao" and aumentou > 2*linhas_tessera:
            raise ValueError("Erro no valor da tessera ou mosaico")
        elif len(tesseraa.matriz1[0]) > colunas_mosaico:
            raise ValueError("largura da tessera maior que a do mosaico")
        elif result == "sobreposicao":
            y+=1
        elif result == "y + tamanho tessera ultrapassou":
            x+=1
            y=0
        elif result == "x + altura tessera ultrapassou":
            aumentou+=1
            for i in range(1):
                matriz =  np.insert(matriz, 0, np.zeros(colunas_mosaico, dtype=np.int8), axis=0)
            novo_mosaico.altura+=1
        else:
            print("a\naa\naaa\naaaa\naaaa\naaaa")
        
def plota_todas(mosaico: Mosaico, lista:list[Tessera]):
    novo_mosaico = copy.deepcopy(mosaico)
    for tesse in lista:
        novo_mosaico.mosaicum=translada_pestape(tesse, novo_mosaico)
    return novo_mosaico