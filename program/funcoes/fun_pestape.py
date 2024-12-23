import copy
from __init__ import *
from classes.class_mosaico import Mosaico
from classes.class_tessera import Tessera

def pestapar(mosaicu: Mosaico, tesseraa: Tessera, x=0, y=0):
    mosaico = mosaicu.mosaicum
    tesser = tesseraa.matriz1
    colunas_tesser=len(tesser[0])
    linhas_tesser=len(tesser)
    i=-1
    im=-1-x

    if y + colunas_tesser > len(mosaico[0]):
        return "y + tamanho tessera ultrapassou"
    elif x + linhas_tesser > len(mosaico):
        return "x + altura tessera ultrapassou"
    
    while i > -linhas_tesser-1:
        j=0
        jm=0+y
        while j < colunas_tesser:
            mosaico[im][jm] += tesser[i][j]
            if mosaico[im][jm] > 3:
                return "sobreposicao"
            j+=1
            jm+=1
        i-=1
        im-=1
    mosaicu.mosaicum = mosaico
    return mosaicu

def translada_pestape(mosaicu: Mosaico, tesseraa: Tessera):
    linhas_tessera=len(tesseraa.matriz1)
    colunas_mosaico=len(mosaicu.mosaicum[0])
    x=0
    y=0
    aumentou=0
    while x + linhas_tessera  < mosaicu.tamanho_maximo:
        result = pestapar(mosaicu=copy.deepcopy(mosaicu), tesseraa=tesseraa, x=x, y=y)
        if result == "sobreposicao" and aumentou > 2*linhas_tessera:
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
            for i in range(linhas_tessera):
                mosaicu.mosaicum.insert(0, [0 for _ in range(colunas_mosaico)])
            mosaicu.altura+=linhas_tessera
        else:
            return result
        
def plota_todas(mosaico: Mosaico, lista:list[Tessera]):
    novo_mosaico = copy.deepcopy(mosaico)
    for tesse in lista:
        novo_mosaico=translada_pestape(novo_mosaico, tesse)
    return novo_mosaico