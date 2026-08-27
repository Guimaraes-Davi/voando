"""
Praca - Carregamento dos dados
==============================

Este arquivo le os tres arquivos JSON e devolve os dados prontos para uso
Serve apenas como importe das funcoes dele

ex:

    from dados import carregar_clientes, carregar_itens, carregar_pedidos

    clientes = carregar_clientes()
    itens = carregar_itens()
    pedidos = carregar_pedidos()

Os valores em dinheiro ja vem convertidos para Decimal
Não se usa float para dinheiro: 0.1 + 0.2 da 0.30000000000000004
"""

import json
from decimal import Decimal
from pathlib import Path

# Pasta onde estao os arquivos JSON, ao lado deste arquivo
PASTA = Path(__file__).parent / "arquivos"


def _ler(nome_arquivo):
    #Le um arquivo JSON e devolve o conteudo. Isso não é para importar, não precisa
    caminho = PASTA / nome_arquivo
    with open(caminho, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)



# ITENS

def carregar_itens():
    """
    Devolve um dicionario onde a chave e o id do item

    Exemplo do que sai:
        {
            1: {"id": 1, "nome": "Agua mineral 500ml",
                "valor": Decimal("3.00"), "alcoolico": False},
            ...
        }

    Assim vc pega um item direto pelo id:
        itens[7]["nome"]  ->  "Cerveja pilsen 350ml"
    """
    itens = {}

    for item in _ler("itens.json"):
        item["valor"] = Decimal(item["valor"])
        itens[item["id"]] = item

    return itens



# CLIENTES

def carregar_clientes():
    """
    Devolve a lista de clientes

    Campos de cada cliente:
        id             numero
        nome           texto
        documento      texto com 11 digitos (CPF) ou 14 (CNPJ)
        idade          numero, ou None quando e pessoa juridica
        bairro         bairro de Feira, ou nome da cidade se for de fora
        complemento    rua e numero, fica vazio quando e intermunicipal
        intermunicipal True ou False

    Foi adicionado um campo a mais para facilitar:
        tipo           "PF" ou "PJ", calculado pelo tamanho do documento
    """
    clientes = _ler("clientes.json")

    for cliente in clientes:
        if len(cliente["documento"]) == 11:
            cliente["tipo"] = "PF"
        else:
            cliente["tipo"] = "PJ"

    return clientes


def indexar_clientes(clientes):
    """
    Devolve um dicionario {id: cliente} a partir da lista

    Serve para achar um cliente rapido, sem varrer a lista toda vez:
        indice = indexar_clientes(clientes)
        indice[12]["bairro"]  ->  "Mangabeira"
    """
    indice = {}

    for cliente in clientes:
        indice[cliente["id"]] = cliente

    return indice



# PEDIDOS

def carregar_pedidos():
    """
    Devolve a lista de pedidos

    Campos de cada pedido:
        id            numero
        cliente_id    id do cliente que fez o pedido
        data          texto no formato "2026-03-10"
        entregue      True se a entrega deu certo
        motivo_falha  "CANCELADO", "ACIDENTE" ou "AUSENTE"
                      Fica None quando a entrega deu certo
        itens         lista das linhas do pedido

    Cada linha dentro de "itens" tem:
        item_id         id do produto
        quantidade      numero de unidades
        valor_unitario  Decimal, preco congelado no dia da venda

    Foram adicionados dois campos a mais para facilitar:
        valor_total   Decimal, soma de todas as linhas
        ano_mes       texto no formato "2026-03", para agrupar por mes
    """
    pedidos = _ler("pedidos.json")

    for pedido in pedidos:
        total = Decimal("0.00")

        for linha in pedido["itens"]:
            linha["valor_unitario"] = Decimal(linha["valor_unitario"])
            total += linha["valor_unitario"] * linha["quantidade"]

        pedido["valor_total"] = total
        pedido["ano_mes"] = pedido["data"][:7]

    return pedidos



# TESTE RAPIDO

if __name__ == "__main__":
    # Roda esse py dados.py para ver se da tudo certo. Lembra de la em cima colocar no caminho certo pros json
    itens = carregar_itens()
    clientes = carregar_clientes()
    pedidos = carregar_pedidos()

    print(f"Itens carregados:    {len(itens)}")
    print(f"Clientes carregados: {len(clientes)}")
    print(f"Pedidos carregados:  {len(pedidos)}")

    primeiro = pedidos[0]
    print()
    print("Primeiro pedido:")
    print(f"  id ............ {primeiro['id']}")
    print(f"  data .......... {primeiro['data']}")
    print(f"  valor total ... R$ {primeiro['valor_total']}")
    print(f"  entregue ...... {primeiro['entregue']}")
