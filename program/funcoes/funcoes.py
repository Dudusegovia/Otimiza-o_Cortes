import matplotlib.pyplot as plt
import shutil
import random
from __init__ import *


# Matriz a ser plotada
def cria_imagem(matriz, string='test'):
    arquivo = open("nome_do_arquivo.txt", "w")
    arquivo.write(f'{matriz}')
    arquivo.close()
    # Cria o gráfico da matriz usando imshow
    plt.imshow(matriz, cmap='viridis', aspect='auto')
    plt.colorbar()  # Adiciona uma barra de cores para referência
    plt.title('Visualização da Matriz')
    plt.savefig(f'{string}.png')  # Salva a imagem como test.png
    plt.close()  # Fecha o plot para evitar conflito

# Caminho do arquivo de origem
    origem = f'{string}.png'

    # Caminho do diretório de destino
    destino = 'public/images'

    # Copiar o arquivo para o diretório de destino
    shutil.copy(origem, destino)

    return

def ordena_listas(lista_tesseras) -> Listas:
    listas=[]
    lista_rotacionda_tesseras=[]
    lista_ordenada=[]
    aux=Tessera([[]],0)
    for tesserad in lista_tesseras:
        tesserad.coloca_3_no_miolo_1()
        tesserad.calcula_area()    

    for i in range(len(lista_tesseras)):
        aux=Tessera([[]],0)
        for tesserad in lista_tesseras:
            if aux.area < tesserad.area:
                aux=tesserad
        lista_tesseras.remove(aux)
        lista_ordenada.append(aux)
        lista_rotacionda_tesseras.append(aux.cabeca_baixo_matriz())
    listas= [lista_ordenada, lista_rotacionda_tesseras]
    obj_listas = Listas(*listas)
    return obj_listas

def cria_global(connn,cursorr):
    global conn
    global cursor
    conn = connn
    cursor = cursorr
    
def adicionar_pro_df():

    cursor.execute('''CREATE TABLE IF NOT EXISTS dados (
                            sequencia TEXT,
                            num_2 INTEGER,
                            altura INTEGER,
                            zeros INTEGER)''')
    conn.commit()
    return conn, cursor

def adicionar_linha(sequencia=None, num_2=None, altura=None, zeros=None):
    # Verificar se a linha já existe
    cursor.execute("SELECT * FROM dados WHERE sequencia = ?", (sequencia,))
    linha_existente = cursor.fetchone()
    
    if linha_existente is None:
        # Se não existir, adiciona a linha
        cursor.execute("INSERT INTO dados (sequencia, num_2, altura, zeros) VALUES (?, ?, ?, ?)", (sequencia, num_2, altura, zeros))
        conn.commit()  # Confirma a transação
        return True
    else:
        return False


    
def faz_combinatoria(n: int, graus_liberdade: int) -> list:
    comb=[]
    list1 = [j for j in range(1,n+1)]
    list2 = [-k for k in range(1,n+1)]
    i=0
    while i < n:
        rand = random.randint(0, graus_liberdade-1)
        if rand == 0:
            comb.append(list1[i])
        else: 
            comb.append(list2[i])
        i+=1
    return comb

