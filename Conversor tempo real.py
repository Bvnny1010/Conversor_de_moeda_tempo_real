import json, requests

moedas_disponiveis = ["USD", "EUR", "BRL", "JPY"]

for moeda in moedas_disponiveis:
    print(f"- {moeda}")

valor_inicial = input("INSIRA O VALOR DESEJADO PARA CAMBIAR: ")
origem = input("MOEDA DE ORIGEM: ")
dest = input("MOEDA DE DESTINO: ")

if origem in moedas_disponiveis and dest in moedas_disponiveis:
    requisicao = requests.get(f"https://economia.awesomeapi.com.br/{origem}-{dest}")
    cotacao = requisicao.json()
    valor_inicial_float = float(valor_inicial)
    cotacao_bid_float = float(cotacao[0]['bid'])
    resultado = valor_inicial_float * cotacao_bid_float


    print(f"{valor_inicial} {origem} equivale a {resultado:.2f} {dest}")

else:
    print("Modas Inválidas")


