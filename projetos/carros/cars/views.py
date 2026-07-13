from django.shortcuts import render
from django.http import HttpResponse

def cars_view(request):
    html = '''
    <html>
        <head>
            <title>Meus carros</title>
        </head>
        <body>
            <H1>Carros PyCode</H1>
            <p>Só carro top</p>
        </body>
    </html>
    '''
    return HttpResponse(html)

