from itertools import permutations
import time


def mensagem_sucesso(nome_wordlist):
    print("[+]Codigo Finalizado com Sucesso!")
    time.sleep(1)
    print(f"[+]Wordlist {nome_wordlist} Gerada!")


def main(nomes:list , datas:list,caracteres_especiais:list , nome_wordlist:str):
    with open(nome_wordlist , "w") as f:
        print("[+]Iniciando script!")
        for n in nomes:
            for d in datas:
                for c in caracteres_especiais:
                    possibilidades = (len(nomes)*len(datas)*len(caracteres_especiais)) * 18
                    try:

                        l = permutations([n,d,c])
                        l1 = permutations([n,d[4:],c])
                        l2 = permutations([n,d[:4],c])


                        for a in list(l):
                            f.write(f"{"".join(a[0:3])}\n")

                        for b in list(l1):
                            f.write(f"{"".join(b[0:3])}\n")

                        for c in list(l2):
                            f.write(f"{"".join(c[0:3])}\n")


                    except KeyboardInterrupt:
                        print("[+]Codigo encerrado!")
                    except Exception as erro:
                        print(f"[+]Algo deu errado ao rodar as permutacoes!\nErro:{erro}")


    mensagem_sucesso(nome_wordlist)



if __name__ == "__main__":
    print(r"""
____  __.                                  .__         
|    |/ _|____ _______  _____   ____ _______|__| ____   
|      < \__  \\_  __ \/     \_/ __ \\___   /  |/    \  
|    |  \ / __ \|  | \/  Y Y  \  ___/ /    /|  |   |  \ 
|____|__ (____  /__|  |__|_|  /\___  >_____ \__|___|  / 
        \/    \/            \/     \/      \/       \/  
""")
    

    nomes = input("Digite nomes separados:").split()
    datas = input("Digite datas (01012001):").split()
    caracteres_especiais = "! @ # $ % ^ & *".split()


    while True:
        try:
            nome_wordlist = input("Digite o nome ou local onde a wordlist sera salva:")
        except PermissionError:
            print("[+]Voce nao tem permissao para criar a wordlist nesse local!")
        else:
            break


    main(nomes , datas , caracteres_especiais , nome_wordlist)