#API fake
def login(usuario,senha):
    if usuario == "admin" and senha == "1234":
        return 'Login realizado com sucesso!'
    else:
        return 'Usuário ou senha incorretos.'
    
def envia_email_log():
    return 'Email enviado com sucesso!'
