import copy
import numpy as np
class Tessera:
    def __init__(self, matriz1:np.array, area=0):
        self.matriz1=matriz1
        self.area=area
        
    def cabeca_baixo_matriz(self):
        
        matriz1=self.matriz1
        
        matriz2 = np.flip(matriz1, axis=(0,1))
        
        tessera_nova = Tessera(matriz2, area=self.area)
        
        return copy.deepcopy(tessera_nova)
    
    def coloca_3_no_miolo_1(self):
        matriz1=self.matriz1
        linhas = len(matriz1) - 1
        colunas = len(matriz1[0]) - 1
        matriz2= copy.deepcopy(matriz1)
        i=1
        while i < linhas:
            if i == linhas:
                break
            j=1
            while j < colunas:
                if  np.count_nonzero(matriz1[i] == 1) > 2:
                    if j == colunas:
                        pass
                    else: 
                        if (matriz1[i][j-1] == 1) and (matriz1[i][j] == 1) and (matriz1[i][j+1] == 1) and (matriz1[i-1][j] == 1) and (matriz1[i+1][j] == 1):
                            matriz2[i][j] = 3
                j+=1
            i+=1
            self.matriz1 = matriz2
        return self

    def calcula_area(self) -> None:
        areaa=0
        for lista in self.matriz1:
            for num in lista:
                if num == 3:
                    areaa+=1
        self.area = areaa
        return