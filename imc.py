#calculadora de IMC

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

print("Calculadora de IMC")
peso = float(input("insira seu peso: "))
altura = float(input("Insira sua altura em METROS (ex: 1.75): "))
imc = calcular_imc(peso, altura)

print('Seu IMC é: {:.2f}'.format(imc))