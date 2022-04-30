#https://docs.python.org/pt-br/3/library/csv.html
import pymongo
import pandas as pd

myclint = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclint['Projeto']
mycol = mydb['proj']

#criar um for com as sequintes informarções
#O usuario devera inserir as informações ou já gerar as informações manualmente
#Criar um objeto com a função de fazer a leitura de um arquivo csv
#Criar um objeto que ira ler as funções do banco de dados (mongodb) e ira transformalas em txt
#sair do programa

print("Opção 1: Inserir manualmente as informações")
print("Opção 2: Faz a leitura de um arquivo CSV")
print("Opção 3: Ira ler um banco de dados e ira gerar um arquivo .txt")
print("Opção 4: Sair do programa")

opcao = int(input("Digite uma opção: "))

if opcao == 1:
    print("\n------ Insira os dados ------\n")
#Talvez retirar essas entradas de dados, porém verificar o erro
    nome = str(input("Digite o um nome: \n"))
    idade = int(input("Digite sua idade: \n"))
    civil = str(input("Digite seu estado civil: \n"))
    filhos = int(input("Digite a sua quantidade de filhos: \n"))
    endereco = str(input("Digite seu endereço: \n"))
    numero = int(input("Digite o numero da sua residencia: \n"))

    mydb.proj.insert_one({
        "Nome": nome,
        "Idade": idade,
        "Estado Civil": civil,
        "Filhos": filhos,
        "Endereço": endereco,
        "Numero da residencia": numero
        })
#mydb.proj.insert_one({
#       "id": 1,
#        "Nome": "João Antonio",
#        "Idade": 40,
#        "Estado Civil": "Casado",
#        "Filhos": 2,
#        "Endereço": "Rua das Palmeiras",
#        "Numero da residencia": 552
#        })
#

#usar o metodo insert
#inserir as informações acima para esse banco de dados
if opcao == 2:
    mydoc = mycol.find().sort("place",1)
    #csv = pd.read_csv('C:\\Users\\gusta\\OneDrive\\Área de Trabalho\\Projeto-Andre\\AcervoEnap_Koha12032021.csv','r')
    f = open("C:\\Users\\gusta\\OneDrive\\Área de Trabalho\\Projeto-Andre\\AcervoEnap_Koha12032021.csv", encoding='UTF-8')
    csv = f.readlines()
    for x in csv:
        item = x.split(";")
        mydb.proj.insert_one({
            "Nome": item[0],
            "Idade": item[1],
            "Estado Civil": item[2],
            "Filhos": item[3],
            "Endereço": item[4],
            "Numero da residencia": item[5]
        })

#Ler o arquivo acervo enap koha e transformaldo em txt
if opcao == 3:
    mydoc = mycol.find().sort("place",1)
    #csv = pd.read_csv('C:/Users/gusta/OneDrive/Área de Trabalho/Projeto-Andre/AcervoEnap_Koha12032021.csv','r')
    fw = open("C:\\Users\\gusta\\OneDrive\\Área de Trabalho\\Projeto-Andre\\Saida.txt", 'w')
    dadosout = []
    for dout in mydoc:
        dadosout.append(str(dout))

    fw.writelines(dadosout)
    fw.close()

#transformalo em txt

if opcao == 4:
    print("Programa encerrado")