def registrar_viagem(listaViagens):
    motorista=str(input("Nome do motorista: "))
    print("-------------------------------------------------")
    destino=str(input("Me diga seu destino: "))
    distancia=int(input("Distância percorrida(em km): "))
    print("-------------------------------------------------")
    valor=float(input("Valor gasto com combustível (em R$): "))
    consumo= (valor/distancia)

    viagem={
        "motorista":motorista,
        "destino":destino,
        "distancia":distancia,
        "valor":valor,
        






    }

    consumomax={
        "consumo":consumo
}
    
    listaViagens.append(viagem)
    listaViagens.append(consumomax)
    print("Viagem registrada")


def exibir_viagem(listaViagens):
    print("VIAGENS:")
    print("-------------------------------------------------")
    print(listaViagens)


def buscar_motorista(listaViagens):
    buscarmoto=str(input("Que motorista você quer buscar?: "))
    for viagem in listaViagens:
        if viagem["motorista"].lower()==buscarmoto.lower():
            print("Motorista encontrado, aqui está as viagens deste motosita:")
            print(viagem)
    if buscarmoto not in listaViagens:
            print("Motorista não encontrado")

def viagem_mais_cara(listaViagens):

    for viagem in listaViagens:
        consumomaximo=max(consumomax, key=consumomax.get)
        print(consumomax)

def media_consumo(listaViagens):
     for viagem in listaViagens:
        print("Aqui está o consumo de cada viagem:")
        print(viagem["consumo"])