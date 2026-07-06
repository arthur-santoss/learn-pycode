class Carro:
    numero_rodas = 4
    quantidade_passageiros = 5

    def acelerar(self,modelo):
        print(f'Acelerando o {modelo}...')

    def frear(self):
        print('Freando o carro...')

    def buzinar(self):
        print('Buzinando o carro...')


class Uno(Carro):
    modelo = 'Uno'
    marca = 'Fiat'
    ano = 1992

class Celta(Carro):
    modelo = 'Celta'
    marca = 'Chevrolet'
    ano = 2009
    km_rodados = 121000

uno = Uno()
uno.acelerar(uno.modelo)

celta = Celta()
celta.acelerar(celta.modelo)