from funcoes import *


ListaViagens=[]
while True:



    print("BEM VINDO AO CONTROLE DE VIAGENS")
    print("-------------------------------------------------")

    print("1 - Registrar nova viagem")
    print("2 - Exibir todas as viagens") 
    print("3 - Buscar viagens por motorista") 
    print("4 - Exibir viagem mais cara") 
    print("5 - Mostrar média geral de consumo") 
    print("0 - Sair")
    print("-------------------------------------------------")


    escolha=int(input("Digite o numero da sua escolha: "))
    if escolha==1:
        print(registrar_viagem(ListaViagens))
    elif escolha==2:
        print(exibir_viagem(ListaViagens))
        
       
    elif escolha==3:
        print(buscar_motorista(ListaViagens))
    elif escolha==4:
        print(viagem_mais_cara(ListaViagens))
    elif escolha==5:
        print(media_consumo(ListaViagens))
