# fast_app: classe para criar o aplicativo
# serve: função para deixar o site online
# Titled: classe que facilita criação de títulos
from fasthtml.common import *
# importando funções do arquivo components.py como uma biblioteca
from components import gerar_titulo
from card3d import card_3d

hdrs = [Style('''* { box-sizing: border-box; }
    html, body { width: 100%; height: 100%; display: flex; justify-content: center; align-items: center; }
    body { 
        font-family: 'Arial Black', 'Arial Bold', Gadget, sans-serif;
        perspective: 1500px; background: linear-gradient(#666, #222);
    }''')]

app = FastHTML(hdrs=hdrs)
rt = app.route

@rt('/')
def homepage():
    ##.Outra forma de chamar classes:
    #return gerar_titulo("Birthday Clock","Hello World")
    
    url_gift = "https://github.com/patriani/BirthClock/blob/main/images/A_vibrant_gift_box.png?raw=true"
    return Div(
        Div(card_3d('Components!', url_gift, 1.5, left_align=True, hx_get='/click')),
    )

@rt("/click")
#Modificar para evento de confetes
def get(): return P('Clicked!')

serve()