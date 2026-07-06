class Celular:
    marca = 'Samsung'
    modelo = 'Galaxy S21'
    cor = 'Preto'
    tem_capa = True
    bateria = '6000 mAh'

    def fazer_ligacao(self, numero):
        print(f'Ligando para {numero}...')
    
    def enviar_mensagem(self, numero, mensagem):
        print(f'Enviando mensagem para {numero}: {mensagem}')
    
    def tirar_foto(self):
        print('Foto tirada com sucesso!')
    
    def calcular(self, num1, num2):
        print(num1 + num2)
    
celular1 = Celular()

celular1.fazer_ligacao(51954545654)

celular1.calcular(10, 20)
