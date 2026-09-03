from dados import indexar_cidades

def documento_valido(documento):
    documento = documento.replace(".","").replace("-","").replace("/","")
    if(not documento.isdigit()):
        return False
    if(not (len(documento)==11 or len(documento) == 14)):
        return False
    return True

def placa_valida(placa):
    if (not len(placa) == 7):
        return False

    cont_letras = 0
    for i in range(3):
        if placa[i].isalpha():
            cont_letras += 1

    cont_numbers = 0
    for i in range(3,7):
        if placa[i].isdigit():
            cont_numbers += 1

    if(cont_letras == 3):
        if(cont_numbers==4):
            return True
        elif(cont_numbers==3):
            if(placa[3].isdigit() and placa[4].isalpha()):
                return True

    return False

def porte_valido(porte):
    if (porte == "BAIXO" or porte == "ALTO"):
        return True
    return False

def destino_valido(cidade_destino, cidades):
    indice_cidades = indexar_cidades(cidades)
    return cidade_destino in indice_cidades

def validar_veiculo(veiculo, cidades):
    erros = []

    if not placa_valida(veiculo.get("placa", "")):
        erros.append("Placa inválida")

    if not porte_valido(veiculo.get("porte", "")):
        erros.append("Porte inválido")

    if not destino_valido(veiculo.get("cidade_destino", ""), cidades):
        erros.append("Destino inválido")

    return erros