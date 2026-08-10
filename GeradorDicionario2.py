from itertools import permutations
from datetime import datetime
from time import sleep
import subprocess
import platform
import os


def receber_dados():
    nomes = input("Digite nomes espacados com virgula (nome nome1):").split()


    while True:
        datas = input("Digite datas (01012001):").split()
        datas_validas = []
        erro = False
        for data in datas:
            try:
                d = datetime.strptime(data, "%d%m%Y")

            except ValueError:
                print(f"[-]Data:{data} removida da lista!")
                opcao = input("Deseja reescrever a data?[y/n]:")
                if opcao.lower() == "y" or opcao == '':
                    erro = True
                else:
                    erro = False

            else:
                datas_validas.append(data)
            
        if erro:
            continue
        else:
            break
        


    while True:
        nome_wordlist = input("Digite o nome do local onde a wordlist ira ser salva (/home/user/wordlist):")
        if os.access(nome_wordlist, os.W_OK) == False:
            print("[-]Voce nao tem permissao para escrever nesse diretorio!")
        else:
            break


    return nomes, datas_validas, nome_wordlist


def gerar_wordlist(*data):
    with open(data[2] , "w") as dicionario:
        CARACTERES_ESPECIAIS = "! @ # $ % ^ & *".split()
        print("[+]Gerando wordlist!")
        for n in data[0]:
            for d in data[1]:
                for c in CARACTERES_ESPECIAIS:

                    permutacoes_padrao = permutations([n,d,c])
        
                    permutacoes_dia = permutations([n,d[:4],c])
        
                    permutacoes_ano = permutations([n,d[4:],c])
        
        
                    for permutacao_padrao in permutacoes_padrao:
                        dicionario.write(f'{"".join(permutacao_padrao)}\n')

                    for permutacao_dia in permutacoes_dia:
                        dicionario.write(f'{"".join(permutacao_dia)}\n')

                    for permutacao_ano in permutacoes_ano:
                        dicionario.write(f'{"".join(permutacao_ano)}\n')


    print("[+]Wordlist gerada com sucesso!")


def main():
    sistema = platform.system()
    if sistema == "Windows":
        subprocess.run("cls", shell=True)
    elif sistema == "Linux":
        subprocess.run("clear")
    
    print(r"""
    ____  __.                                  .__         
    |    |/ _|____ _______  _____   ____ _______|__| ____   
    |      < \__  \\_  __ \/     \_/ __ \\___   /  |/    \  
    |    |  \ / __ \|  | \/  Y Y  \  ___/ /    /|  |   |  \ 
    |____|__ (____  /__|  |__|_|  /\___  >_____ \__|___|  / 
            \/    \/            \/     \/      \/       \/  
    """)


    gerar_wordlist(*receber_dados())


if __name__ == "__main__":
    main()