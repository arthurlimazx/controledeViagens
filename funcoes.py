from tabulate import tabulate


def registrar_viagem(listaViagens):


    motorista=str(input("Nome do motorista: "))
    print("-------------------------------------------------")
    destino=str(input("Me diga seu destino: "))
    distancia=float(input("Distância percorrida(em km): "))
    print("-------------------------------------------------")
    combustivel=float(input("Valor gasto com combustível (em R$): "))
    consumo= (combustivel/distancia)

    viagem={
        "motorista":motorista,
        "destino":destino,
        "distancia":distancia,
        "valor":combustivel,
        "consumo":consumo






    }


        

    
    listaViagens.append(viagem)
    print("Viagem registrada")
    print("-------------------------------------------------")
    
    return


def exibir_viagem(listaViagens):
    for viagem in listaViagens:
        print("VIAGENS:")
        print("-------------------------------------------------")
        print(tabulate(listaViagens, headers="keys"))
        return


def buscar_motorista(listaViagens):
    buscarmoto=str(input("Que motorista você quer buscar?: "))
    
    encontrou= [m for m in listaViagens if m["motorista"].lower()==buscarmoto.lower()]
    
    if encontrou:
        print("Motorista encontrado, aqui está as viagens deste motosita:")
        print(tabulate(encontrou, headers="keys"))
        print("-------------------------------------------------")

    else:
        print("Nenhum motorista com esse nome fi")
        print("-------------------------------------------------")

        return

def viagem_mais_cara(listaViagens):
    maiorgasto=listaViagens[0]["valor"]
    for c in listaViagens:
        if c["valor"]>maiorgasto:
           maiorgasto=c["valor"]
        maiscaro={
        
        "viagem":c["destino"],
        "valor":maiorgasto 
        }

    
        
    print(tabulate([maiscaro], headers="keys"))
        
   

def media_consumo(listaViagens):
     print("Aqui está o consumo de cada viagem:")
     for m in listaViagens:
        
        print(m["destino"])
        print(m["consumo"])
        print("-------------------------------------------------")


        