from collections import Counter


def veiculos_por_cliente(clientes, veiculos):
    """
    Retorna quantos veículos cada cliente já mandou transportar,
    ordenado do maior para o menor.
    """
    # Mapeia ID do cliente para o Nome do cliente
    mapa_clientes = {c["id"]: c["nome"] for c in clientes}
    
    # Conta a quantidade de veículos agrupados por cliente_id
    contagem = Counter(v["cliente_id"] for v in veiculos if "cliente_id" in v)
    
    resultado = []
    for cliente_id, quantidade in contagem.items():
        if cliente_id in mapa_clientes:
            resultado.append({
                "cliente": mapa_clientes[cliente_id],
                "quantidade": quantidade
            })
            
    # Ordena do maior para o menor pela quantidade de veículos
    resultado.sort(key=lambda x: x["quantidade"], reverse=True)
    return resultado


def clientes_sem_envio(clientes, veiculos):
    """
    Retorna a lista de nomes dos clientes cadastrados que nunca mandaram nenhum veículo.
    """
    # Conjunto com os IDs dos clientes que possuem pelo menos um veículo enviado
    clientes_com_envio = {v["cliente_id"] for v in veiculos if "cliente_id" in v}
    
    # Filtra os clientes cujo ID não está no conjunto acima
    sem_envio = [c["nome"] for c in clientes if c["id"] not in clientes_com_envio]
    return sem_envio


def destinos_por_cliente(clientes, veiculos, cliente_id):
    """
    Retorna para quais cidades um cliente específico já mandou veículos e a quantidade.
    """
    # Filtra apenas os veículos pertencentes ao cliente informado
    veiculos_do_cliente = [v for v in veiculos if v.get("cliente_id") == cliente_id]
    
    # Conta veículos por cidade de destino
    contagem = Counter(v["cidade_destino"] for v in veiculos_do_cliente if "cidade_destino" in v)
    
    resultado = [
        {"cidade": cidade, "quantidade": quantidade}
        for cidade, quantidade in contagem.items()
    ]
    
    # Ordena por quantidade decrescente
    resultado.sort(key=lambda x: x["quantidade"], reverse=True)
    return resultado


def clientes_por_eixo(clientes, veiculos, cidades):
    """
    Retorna quantos clientes DISTINTOS cada eixo atende.
    """
    if isinstance(cidades, list):
        mapa_cidade_eixo = {c["nome"]: c["eixo"] for c in cidades if "nome" in c and "eixo" in c}
    elif isinstance(cidades, dict):
        mapa_cidade_eixo = cidades
    else:
        mapa_cidade_eixo = {}

    # Dicionário onde a chave é o Eixo e o valor é um set() com IDs de clientes únicos
    eixo_clientes = {}

    for v in veiculos:
        cidade = v.get("cidade_destino")
        cliente_id = v.get("cliente_id")
        eixo = mapa_cidade_eixo.get(cidade)

        if eixo and cliente_id is not None:
            if eixo not in eixo_clientes:
                eixo_clientes[eixo] = set()  # Inicializa o conjunto para o eixo
            
            # O set() garante que o mesmo cliente só entra uma vez por eixo
            eixo_clientes[eixo].add(cliente_id)

    # Converte o conjunto para o número de clientes distintos
    resultado = [
        {"eixo": eixo, "clientes": len(conjunto_clientes)}
        for eixo, conjunto_clientes in eixo_clientes.items()
    ]

    # Ordena pelo eixo com maior número de clientes
    resultado.sort(key=lambda x: x["clientes"], reverse=True)
    return resultado