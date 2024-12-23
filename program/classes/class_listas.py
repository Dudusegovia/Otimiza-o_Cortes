class Listas:
    def __init__(self, *args):
        for i , valor in enumerate(args):
            setattr(self, f"lista_{i}", valor) # cria atributos dinamicamente, com o nome lista_1, lista_2 ... e atribui o valor provindo dos argumentos passados

    def retorna_atributos(self) -> list:
        # Exibe os atributos criados dinamicamente
        atributos=[]
        for nome, valor in self.__dict__.items():
            atributos.append(valor)
        return atributos
        
    def conta_atributos(self):
        aux=0
        for nome in self.__dict__.items():
            aux+=1
        return aux

