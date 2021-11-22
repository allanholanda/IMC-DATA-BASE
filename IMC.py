import pyodbc
import pandas as pd
import os
import time

#Função para se conectar ao banco de dados:
def retornar_conexao_sql():
    server = "DESKTOP-8TL04IN\SQLEXPRESS"
    database = "Base_IMC"
    string_conexao = 'Driver={SQL Server Native Client 11.0};Server='+server+';Database='+database+';Trusted_Connection=yes;'
    conexao = pyodbc.connect(string_conexao)
    return conexao.cursor()

#Definindo a variável cursor:
cursor = retornar_conexao_sql()

#Criar a tabela:
table = """CREATE TABLE Dados_Corporais (
	Nome varchar(50) not null,
	Idade int not null,
	Peso float not null,
	Altura float not null,
	Imc float not null,
)"""
cursor.execute(table)

#Função para realizar uma conexão e exibir a tabela:
def select_table():
    dados_conexao = ("Driver={SQL Server Native Client 11.0};"
                     "Server=DESKTOP-8TL04IN\SQLEXPRESS;"
                     "Database=Base_IMC;"
                     "Trusted_Connection=yes;")
    return dados_conexao

#Função estética
def lin():
    print(60 * '-')

#Função anônima pra limpeza das telas
clear = lambda: os.system('cls')

#Listas para receber dados exclusivamente:
lst_nome = []
lst_imc = []

#Entrada de dados
z = 1
while z == 1:
    nome = str(input("Digite um nome: "))
    idade = int(input("Digite uma idade: "))
    peso = float(input("Digite um peso em quilogramas: "))
    altura = float(input("Digite uma altura em metros: "))

    #Calculando o IMC
    imc = peso / (altura * altura)

    #Inserindo os dados nas listas:
    lst_nome.append(nome)
    lst_imc.append(imc)

    #Criando o comando para inserir inserir os dados na tabela
    insert = """insert into Dados_Corporais (Nome,Idade,Peso,Altura,Imc) values ('{}', {}, {}, {}, {:.2f})""" .format(nome,idade,peso,altura,imc)
    cursor.execute(insert)
    cursor.commit()

    if z == 2:
        break
    z = int(input('\nDigite 1 para inserir mais dados, ou 2 para finalizar:  '))

#Comando para limpar a primeira tela:
clear()

#Exibindo a tabela:
conexao = pyodbc.connect(select_table())
cursor = conexao.cursor()
tabela = pd.read_sql('select * from Dados_Corporais', conexao)
lin()
print(tabela)
lin()

#Exibindo o maior e o menor imc:
maior_imc = max(lst_imc)
menor_imc = min(lst_imc)
iM = lst_imc.index(maior_imc)
im = lst_imc.index(menor_imc)
nome_maior = lst_nome[iM]
nome_menor = lst_nome[im]
print('MAIOR IMC: {} - {:.2f}Kg/m²'.format(nome_maior, maior_imc))
print('MENOR IMC: {} - {:.2f}Kg/m²'.format(nome_menor, menor_imc))

#Deletar dados da tabela:
delete = """drop table Dados_Corporais"""

#Finalizando o programa:
lin()
sair = int(input('Digite 3 para excluir os dados armazenados e sair do programa: '))
lin()
if sair == 3:
    cursor.execute(delete)
    cursor.commit()
    time.sleep(1.0)
    exit()