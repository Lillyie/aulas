# exercício 1: checar se um numero é impar ou par
'''
    num = input('digite um número inteiro: ').strip()

    if num.isdigit():
        while num == float:
            print("por favor digite um número inteiro")
        print(f'{num} é par!' if (int(num) % 2 == 0) else f'{num} é impar!')
    else:
        print("por favor digite um número inteiro")
'''
# 3 erros no total


# exercício 2: saudação correta para cada parte do dia
'''
    hora = input("que horas são? ").strip()

    if not hora.isdigit():
        print("por favor digite um horário válido")
    else:
        ihora = int(hora)

        if ihora > 24 or ihora < 0:
            print("por favor digite um horário valido")
        elif ihora < 12:
            print("bom dia!")
        elif ihora < 17:
            print("boa tarde!")
        else:
            print("boa noite!")
'''
#varios erros mds do ceu


# exercício 3: contando letras de um nome
'''
    nome = input("digite seu nome: ").strip()

    letras = len(nome)

    if letras > 6:
        print("seu nome é muito grande!")
    elif letras == 5 or letras == 6:
        print("seu nome é de tamanho médio!")
    elif letras <= 4:
        print("seu nome é curto!")
'''
# ESSE FOI DE PRIMEIRA