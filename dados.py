"""
Voando - Carregamento dos dados
===============================

Le os cinco arquivos JSON e devolve os dados prontos para uso
n altere este arquivo. Apenas importe as funcoes dele

Como usar:

    from dados import carregar_veiculos, carregar_cidades

    veiculos = carregar_veiculos()
    cidades = carregar_cidades()

A sua funcao deve receber os dados por parametro
Nao chame carregar_* dentro dela. Certo assim:

    def contar_por_situacao(veiculos):
        ...

    if __name__ == "__main__":
        contar_por_situacao(carregar_veiculos())
"""

import json
from pathlib import Path

PASTA = Path(__file__).parent / "arquivos"


def _ler(nome_arquivo):
    # Le um arquivo JSON e devolve o conteudo. Uso interno
    with open(PASTA / nome_arquivo, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


# ---------------------------------------------------------------
# CIDADES
# ---------------------------------------------------------------

def carregar_cidades():
    """
    Lista das 13 cidades atendidas

    Campos:
        nome           texto
        distancia_km   numero, distancia a partir de Feira de Santana
        eixo           "SALVADOR", "LITORAL_NORTE" ou "SERTAO"

    A distancia define a ordem das paradas de uma viagem
    """
    return _ler("cidades.json")


def indexar_cidades(cidades):
    """
    Devolve {nome: cidade} para achar uma cidade sem varrer a lista

        indice = indexar_cidades(cidades)
        indice["Salvador"]["eixo"]  ->  "SALVADOR"
    """
    indice = {}
    for cidade in cidades:
        indice[cidade["nome"]] = cidade
    return indice


# ---------------------------------------------------------------
# CEGONHAS
# ---------------------------------------------------------------

def carregar_cegonhas():
    """
    Lista das 3 cegonhas da frota

    Campos:
        id                    numero
        placa                 texto
        capacidade_superior   5 veiculos
        capacidade_inferior   4 veiculos

    Veiculo de porte ALTO so cabe na rampa inferior
    """
    return _ler("cegonhas.json")


# ---------------------------------------------------------------
# CLIENTES
# ---------------------------------------------------------------

def carregar_clientes():
    """
    Lista dos clientes que contratam o transporte

    Campos:
        id          numero
        nome        texto
        documento   texto, 11 digitos (CPF) ou 14 (CNPJ)
        telefone    texto
    """
    return _ler("clientes.json")
 

def indexar_clientes(clientes):
    # Devolve {id: cliente}
    indice = {}
    for cliente in clientes:
        indice[cliente["id"]] = cliente
    return indice


# ---------------------------------------------------------------
# VEICULOS
# ---------------------------------------------------------------

def carregar_veiculos():
    """
    Lista dos veiculos transportados

    Campos:
        id                 numero
        modelo             texto
        placa              texto, 7 caracteres
        porte              "BAIXO" ou "ALTO"
        cliente_id         id do cliente dono
        cidade_destino     nome da cidade de entrega
        data_contratacao   texto "2026-08-14", define a ordem na fila
        situacao           "AGUARDANDO", "EM_TRANSPORTE" ou "ENTREGUE"
    """
    return _ler("veiculos.json")


def indexar_veiculos(veiculos):
    # Devolve {id: veiculo}
    indice = {}
    for veiculo in veiculos:
        indice[veiculo["id"]] = veiculo
    return indice


# ---------------------------------------------------------------
# VIAGENS
# ---------------------------------------------------------------

def carregar_viagens():
    """
    Lista das viagens realizadas e em curso

    Campos:
        id               numero
        cegonha_id       id da cegonha usada
        data             texto "2026-07-05"
        eixo             corredor rodoviario da viagem
        paradas          lista de cidades, na ordem de entrega
        veiculos         lista de ids dos veiculos embarcados
        rampa_superior   lista de ids, do fundo para a boca da rampa
        rampa_inferior   lista de ids, do fundo para a boca da rampa
        situacao         "EM_CURSO" ou "CONCLUIDA"
        total_manobras   numero de movimentos extras no descarregamento

    Nas rampas, o ultimo id da lista e o que esta na boca, ou seja,
    o primeiro a descer
    """
    return _ler("viagens.json")


# ---------------------------------------------------------------
# TESTE RAPIDO
# ---------------------------------------------------------------

if __name__ == "__main__":
    # Rode "python dados.py" para conferir se esta tudo certo
    cidades = carregar_cidades()
    cegonhas = carregar_cegonhas()
    clientes = carregar_clientes()
    veiculos = carregar_veiculos()
    viagens = carregar_viagens()

    print(f"cidades .... {len(cidades)}")
    print(f"cegonhas ... {len(cegonhas)}")
    print(f"clientes ... {len(clientes)}")
    print(f"veiculos ... {len(veiculos)}")
    print(f"viagens .... {len(viagens)}")

    aguardando = 0
    for veiculo in veiculos:
        if veiculo["situacao"] == "AGUARDANDO":
            aguardando += 1
    print()
    print(f"na fila de embarque: {aguardando}")
