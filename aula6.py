# qual letra apareceu mais vezes
frase = input("digite uma frase: ").strip()

i = 0
ltr_mv = '' #letra que mais apareceu
qtd_mv = 0 #quantidade de quantas vezes apareceu a letra que mais apareceu

while i < len(frase):
    ltr_atual = frase[i] #aponta qual letra aparece de acordo com o indice(i)
                             #ltr_atual é a letra que vai ser analisada no momento
    
    if ltr_atual == ' ': #caso ltr_atual seja um espaço, pule
        i+=1               #em frases longas, obviamente o espaço vai aparecer +vezes
        continue

    qtd_atual = frase.count(ltr_atual) #quantas vezes a letra atual aparece

    """SE a letra atual apareceu mais vezes que a 
        ULTIMA letra que apareceu mais vezes, a quantidade
        de vezes que a letra atual apareceu vai ser a nova
        qtd_mv, e tbm vai ser a nova letra que mais apareceu (ltr_mv)
        até aparecer outra letra que apareceu mais vezes"""
    if qtd_mv < qtd_atual:
        qtd_mv = qtd_atual
        ltr_mv = ltr_atual
   
    i+=1

printpreguiça = f' A letra que apareceu mais vezes foi "{ltr_mv}", \naparecendo um total de {qtd_mv}!'
print(printpreguiça) #printar qual foi a letra que mais apareceu e quantas vezes ela apareceu