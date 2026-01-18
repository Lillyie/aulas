# isso é so um teste de projetinho que eu quero fazer para treinar condicionais

print("digite sua altura (Ex: 1.70):")
altura = float(input(""))
print("digite seu peso:")
peso = float(input(""))
imc = peso / (altura**2)
abaixo_peso = imc <= 18.9
peso_ideal = imc >= 19 and imc <= 24.9
sobrepeso = imc >= 25 and imc <= 29.9
obeso1 = imc >= 30 and imc <= 34.9
obeso2 = imc >= 35 and imc <= 39.9
obeso3 = imc >= 40

print(f'Seu IMC é de: {imc:.2f}')
print(10*"-")
if peso_ideal:
    print("Você está com um peso ideal!")
elif abaixo_peso:
    print("voce ta meio magro ein normie")
elif sobrepeso:
    print("você está sobrepeso! Mantenha uma alimentação saudável e faça exercicios regularmente!")
elif obeso1:
    print("você está com obesidade nivel 1! Sugiro que vá ao médico, mantenha uma boa alimentação e faça exercícios!")
elif obeso2:
    print("você está com obesidade nivel 2! Sua situação é alarmante, por favor procure um médico e cuide de sua saude!")
elif obeso3:
    print("Cuidado! Você está com obesidade morbida! Procure um médico imediatamente para reverter sua situação e garantir sua saude!")
print(10*"-")

#tuff, entretanto um jeito mais limpo seria assim:
'''
    altura = float(input("Digite sua altura (ex: 1.70): "))
    peso = float(input("Digite seu peso: "))

    imc = peso / altura**2

    print(f"\nSeu IMC é: {imc:.2f}")
    print("-" * 30)

    if 18.9 <= imc <= 24.9:
        print("Você está com peso ideal!")
    elif 25 <= imc <= 29.9:
        print("Você está com sobrepeso. Mantenha uma alimentação saudável e pratique exercícios!")
    elif 30 <= imc <= 34.9:
        print("Obesidade nível 1. É recomendado procurar um médico e cuidar da alimentação.")
    elif 35 <= imc <= 39.9:
        print("Obesidade nível 2. Situação alarmante, procure um médico.")
    else:
        print("Obesidade mórbida. Procure um médico imediatamente!")

    print("-" * 30)
'''