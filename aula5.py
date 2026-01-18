#exercicio de while
import time

nome = input("digite um nome: ").strip()

ind = 0
novo_nome = ""

while ind < len(nome):
    letra = nome[ind]
    novo_nome += letra
    ind +=1
    time.sleep(0.2)
    print(novo_nome)

ind = 0

'''while ind < len(nome):
    letra = nome[ind]
    time.sleep(0.2)
    print(letra)

    ind+=1'''