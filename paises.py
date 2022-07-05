import json

import requests

URL = "https://restcountries.com/v3.1/all"
URL_NAME = "https://restcountries.com/v3.1/name/"


def requisicao(url):
    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            return resposta.text
    except:
        print("Erro ao fazer a requisição em {}".format(url))


def parsing(resposta_texto):
    try:
        return json.loads(resposta_texto)
    except:
        print("Erro ao fazer o Parsing do texto")


def mostrar_paises(lista_paises):
    for pais in lista_paises:
        print(pais['name']['common'])


def numero_paises(lista_paises):
    print(len(lista_paises))


def mostrar_populacao(nome_pais):
    texto_resposta = requisicao("{}{}".format(URL_NAME, nome_pais))
    if texto_resposta:
        lista_de_paises = parsing(texto_resposta)
        for pais in lista_de_paises:
            print("{}: {}".format(pais['name']['common'], pais['population']))
    else:
        print("Pais não encontrado")


def mostrar_moeda(nome_pais):
    texto_resposta = requisicao("{}{}".format(URL_NAME, nome_pais))
    if texto_resposta:
        lista_de_paises = parsing(texto_resposta)
        if lista_de_paises:
            for pais in lista_de_paises:
                print("\nMoedas do", pais['name']['common'])
                moedas = pais['currencies']
                for moeda in moedas:
                    print(moeda)
    else:
        print("Pais não encontrado")


if __name__ == "__main__":
    texto_da_resposta = requisicao(URL)
    if texto_da_resposta:
        lista_paises = parsing(texto_da_resposta)
        if lista_paises:
            numero_paises(lista_paises)
            mostrar_moeda(input("Digite o nome do pais: "))




