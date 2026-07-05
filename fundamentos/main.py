import api
import os 

ambiente = os.environ.get('AMBIENTE')
usuario = os.environ.get('USUARIO_API')
senha = os.environ.get('SENHA_API')

login = api.login(usuario, senha)
print(login)

if ambiente == 'dev':
    email = api.envia_email_log()
    print(email)