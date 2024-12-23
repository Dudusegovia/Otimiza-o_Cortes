from .class_tessera import Tessera
import numpy as np
        
class Mosaico(Tessera):
    def __init__(self, largura, altura=1):
        self.largura = largura
        self.altura=altura
        self.mosaicum = np.zeros((altura, largura), dtype=np.int8)
        self.tamanho_maximo = 100000
        self.zeros=0
        self.dois=0
        
    def coloca_borda(self):
        i=1
        while i < len(self.mosaicum):
            self.mosaicum[i][0] = 1
            self.mosaicum[i][-1] = 1
            i+=1
        j=0
        while j < len(self.mosaicum[0]):
            self.mosaicum[-1][j] = 1
            j+=1
        return self
    def conta_2_e_0(self):
        zeros=0
        dois=0
        for linha in self.mosaicum:
            for elemento in linha:
                if elemento == 0:
                    zeros+=1
                elif elemento == 2:
                    dois+=1
        self.zeros=zeros
        self.dois=dois