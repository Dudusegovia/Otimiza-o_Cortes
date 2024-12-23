from classes.class_mosaico import *
from classes.class_tessera import *
from classes.class_listas import *
from funcoes.func_pestape import *
from funcoes.funcoes import *
from matriz_tesseras import *
import sqlite3
import time


global mosaicos_plotados
mosaicos_plotados = 0

global tesseras
tesseras = retorna_matrizes()

global tesseras_rotacionadas
tesseras_rotacionadas=retorna_rotacionada()

obj_lista = Listas(tesseras, tesseras_rotacionadas)

global graus_liberdade
graus_liberdade = obj_lista.conta_atributos()

global max_comb
max_comb = graus_liberdade**len(tesseras)
import os
# def funcao_sql_cria_conecta(nome:str='primeiro'):
#     global conn
#     global cursor
#     caminho = os.path.abspath(f'dados/dados_combinacoes_{nome}.db')
#     conn = sqlite3.connect(caminho)
#     cursor = conn.cursor()
#     cria_global(connn=conn, cursorr=cursor)
#     adicionar_pro_df()
    
import os
import sqlite3
def retorna_melhores_mosaicos(num_mosaic):
    lista_2=[]
    lista_altura=[]
    lista_zeros=[]
    list2=[]
    # Selecionar os maiores valores de uma coluna (exemplo: coluna "coluna1")
    cursor.execute("SELECT * FROM dados WHERE num_2 IS NOT NULL ORDER BY num_2 DESC LIMIT 1")
    maiores_valores = cursor.fetchall()
    print("Maiores valores de coluna1:")
    for row in maiores_valores:
        lista_2.append(json.loads(row[0]))
        list2.append([row[1],row[2], row[3]])
    # Selecionar os 10 menores valores de outra coluna (exemplo: coluna "coluna2")
    cursor.execute("SELECT * FROM dados WHERE altura IS NOT NULL ORDER BY altura ASC LIMIT 1")
    menores_valores = cursor.fetchall()
    print("\nMenores valores de coluna2:")
    for row in menores_valores:
        lista_altura.append(json.loads(row[0]))
        list2.append([row[1],row[2], row[3]])

    cursor.execute("SELECT * FROM dados where zeros IS NOT NULL ORDER BY zeros ASC LIMIT 1")
    menores_valores = cursor.fetchall()
    print("\nMenores valores de c3:")
    for row in menores_valores:
        lista_zeros.append(json.loads(row[0]))
        list2.append([row[1],row[2], row[3]])
        cursor.execute("SELECT * FROM dados where zeros IS NOT NULL ORDER BY zeros ASC LIMIT 1")
    menores_valores = cursor.fetchall()
    print("\nMenores valores de c3:")
    for row in menores_valores:
        lista_zeros.append(json.loads(row[0]))
        list2.append([row[1],row[2], row[3]])
    return [[lista_2, lista_altura, lista_zeros],list2]
        
def funcao_sql_cria_conecta(nome: str = 'primeiro'):
    global conn
    global cursor

    # Cria o diretório "dados" se não existir
    diretorio = 'dados'
    os.makedirs(diretorio, exist_ok=True)

    # Define o caminho absoluto para o banco de dados
    caminho = os.path.abspath(f'program/dados/dados_combinacoes_{nome}.db')

    # Conecta ao banco de dados SQLite
    try:
        conn = sqlite3.connect(caminho)
        cursor = conn.cursor()

        # Chama outras funções
        cria_global(connn=conn, cursorr=cursor)
        adicionar_pro_df()
        conn.commit()
        print(f"Banco de dados conectado em: {caminho}")
    except sqlite3.OperationalError as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")
def adiciona_comb_sql(num_comb=10):
    num_tesseras=len(tesseras)
    for i in range(num_comb):
        adicionar_linha(f"{(faz_combinatoria(n=num_tesseras, graus_liberdade=graus_liberdade))}")
import json

def tranforma_em_lista_tesseras(lista, tesseras, tesseras_rotacionadas):
    comb_tesser=[]
    for num in lista:
        if num < 0:
            comb_tesser.append(tesseras_rotacionadas[(num+1)*-1])
        elif num > 0:
            comb_tesser.append(tesseras[(num-1)])
    return comb_tesser

def cria_1_mosaico_e_aplica_no_banco(i):
    global mosaicos_plotados
    if mosaicos_plotados >= max_comb:
        print("acabou as combinatorias")
        return False
    cursor.execute("""SELECT * FROM dados;""")
    time.sleep(1)
    var1=cursor.fetchall()
    if var1[i][2] != None:
        print(var1[i][2])
        return False
    var = json.loads(var1[i][0])
    mosnovo=plota_todas(mosaico, tranforma_em_lista_tesseras(var, tesseras, tesseras_rotacionadas))
    mosnovo.conta_2_e_0()
    # mosnovo.conta_2_e_0()
    cursor.execute("""UPDATE dados SET num_2 = ?, altura = ?, zeros=? WHERE sequencia = ?""", (mosnovo.dois, mosnovo.altura, mosnovo.zeros, f'{var}'))

    conn.commit()
    if mosnovo == False:
        pass
    else:
        mosaicos_plotados+=1
    return mosnovo


while True:
    print("Bem vindo ao TESSELARIUS")
    x=1700
    y=30
    mosaico = Mosaico(x,y).coloca_borda()
    print("deseja criar um novo banco de dados? se sim, insira 's', se nao insira 'n'")
    resp = input()
    if resp == 'n' or resp == 'N':
        funcao_sql_cria_conecta(input("Digite o nome final do banco: "))
    else:
        funcao_sql_cria_conecta(input("digite um nome para o novo banco: "))
    cursor.execute("""SELECT COUNT(num_2)  FROM dados;""")

    var3=cursor.fetchall()
    mosaicos_plotados = int(var3[0][0])
    k=0
    decide=1
    quantos=int(input("Deseja plotar quantos mosaicos? "))
    while k < quantos:
        adiciona_comb_sql(decide)
        cria_1_mosaico_e_aplica_no_banco(mosaicos_plotados)
        k+=1
    while True:
        soun=input("deseja plotar mais mosaicos? s ou n")
        if  soun == 's' or soun == 'S':
            k=0
            quantos=int(input("Deseja plotar quantos mosaicos? "))
            while k < quantos:
                adiciona_comb_sql(decide)
                cria_1_mosaico_e_aplica_no_banco(mosaicos_plotados)
                k+=1
        else:
            break
    b=retorna_melhores_mosaicos(1)
    a=b[0]
    c=b[1]
    print(f"melhor sequencia para 2: {a[0][0]}: {c[0]}, melhor sequencia para altura: {a[1][0]}: {c[1]}, melhor sequencia para zeros: {a[2][0]}: {c[2]} \n")
    break
print("obrigado")

listaa = tranforma_em_lista_tesseras(a[1][0], tesseras, tesseras_rotacionadas)
lista2 = tranforma_em_lista_tesseras(a[0][0], tesseras, tesseras_rotacionadas)
lista3 = tranforma_em_lista_tesseras(a[2][0], tesseras, tesseras_rotacionadas)

kk = plota_todas(mosaico=mosaico, lista=listaa).mosaicum
cria_imagem(kk, "test")
print(np.array(kk))
cria_imagem(plota_todas(mosaico=mosaico, lista=lista2).mosaicum, "test2")
cria_imagem(plota_todas(mosaico=mosaico, lista=lista3).mosaicum, "test3")
import webbrowser

# Caminho corrigido
caminho_html = r'C:\Users\eduar\OneDrive\Área de Trabalho\Programação\Estudo_pessoal\modelos\tesselarius_roupas\public\index.html'

# Abrir no navegador padrão
webbrowser.open(caminho_html)
