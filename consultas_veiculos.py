def buscar_por_placa(veiculos, placa):
    placa_buscada = placa.upper()
    for veiculo in veiculos:
        if veiculo.get("placa", "").upper() == placa_buscada:
            return veiculo
    return None

def filtrar_por_situacao(veiculos, situacao):
    situacao_buscada = situacao.upper()
    veiculos_filtrados = []
    for veiculo in veiculos:
        if veiculo.get("situacao", "").upper() == situacao_buscada:
            veiculos_filtrados.append(veiculo)
    return veiculos_filtrados

def filtrar_por_cidade(veiculos, cidade):
    cidade = cidade.lower()
    veiculos_filtrados = []
    for veiculo in veiculos:
       if veiculo.get("cidade_destino", "").lower() == cidade:
            veiculos_filtrados.append(veiculo)
    return veiculos_filtrados

def contar_por_eixo(veiculos, cidades):
    dicionario_cidades = {}
    for cidade in cidades:
        nome = cidade.get("nome")
        eixo = cidade.get("eixo")
        dicionario_cidades[nome] = eixo
    contagem_eixo = {}
    
    for veiculo in veiculos:
        if veiculo.get("situacao") == "AGUARDANDO": 
            cidade_destino = veiculo.get("cidade_destino")
            eixo = dicionario_cidades.get(cidade_destino) 
            if eixo:
                if eixo in contagem_eixo:
                    contagem_eixo[eixo] += 1
                else:
                    contagem_eixo[eixo] = 1
    
    resultado = []
    for eixo, quantidade in contagem_eixo.items():
        resultado.append({"eixo": eixo, "quantidade": quantidade})
    return resultado

def veiculos_do_cliente(veiculos, cliente_id):
    veiculos_cliente = []
    for veiculo in veiculos:
        if veiculo.get("cliente_id") == cliente_id:
            veiculos_cliente.append(veiculo)
    return veiculos_cliente