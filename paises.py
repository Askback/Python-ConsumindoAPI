import json
import sys

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


def mostrar_paises():
    texto_resposta = requisicao(URL)
    if texto_resposta:
        lista_de_paises = parsing(texto_resposta)
        if lista_de_paises:
            for pais in lista_de_paises:
                print(pais['name']['common'])


def numero_paises():
    texto_resposta = requisicao(URL)
    if texto_resposta:
        lista_de_paises = parsing(texto_resposta)
        if lista_de_paises:
            return len(lista_de_paises)


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


def ler_nome_pais():
    try:
        nome_do_pais = sys.argv[2]
        return nome_do_pais
    except:
        print("\n é preciso digitar o nome do pais")


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("### Bem vindo ao sistema de paises via CLI ###")
        print("\nPara utiliza é muito simples, basta digitar:")
        print("\npython paises.py <argumento> <pais>")
        print("\n---Argumentos disponiveis: paises, numero, moeda, populacao ---")
    else:
        argumento1 = sys.argv[1]

        if argumento1 == "numero":
            quantidade_de_paises = numero_paises()
            print("\nExistem no mundo {} países".format(quantidade_de_paises))
        elif argumento1 == "paises":
            mostrar_paises()
        elif argumento1 == "moeda":
            pais = ler_nome_pais()
            if pais:
                mostrar_moeda(pais)
        elif argumento1 == "populacao":
            pais = ler_nome_pais()
            if pais:
                mostrar_populacao(pais)
        else:
            print("\nArgumento inválido")





