from fasthtml.common import *
from components import gerar_titulo, clockdown_timer # Importando funções do arquivo components.py como uma biblioteca
from card3d import card_3d
from datetime import datetime # Importando biblioteca para coleta de horário atual

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

    url_gift = "https://github.com/patriani/BirthClock/blob/main/images/gift_with_bg.png?raw=true"
    return Div(
        Div(card_3d('', url_gift, 1.5, left_align=True, hx_get='/click'))
    )


@rt("/click")
#Modificar para evento de confetes
#def get(): return P('Clicked!')
def contagem_regressiva():
    # Definir o horário de destino: meia-noite de 13/12/2024
    data_destino = datetime(2024, 12, 13, 0, 0, 0)

    while True:
        # Hora atual
        agora = datetime.now()

        # Calcular o tempo restante
        tempo_restante = data_destino - agora

        # Se o tempo restante for menor ou igual a zero, encerrar a contagem
        if tempo_restante.total_seconds() <= 0:
            print("Chegamos a meia-noite de 13/12/2024!")
            break

        # Extrair dias, horas, minutos e segundos restantes
        dias = tempo_restante.days
        horas, resto = divmod(tempo_restante.seconds, 3600)
        minutos, segundos = divmod(resto, 60)

        # Exibir o tempo restante
        clock_down=f"Tempo restante: {dias}d {horas:02}h {minutos:02}m {segundos:02}s"
        
        # Confdição para confete e código
        # Condição para return apenas do clockdown
        
        return P(clock_down)

        # Aguardar 1 segundo antes de atualizar
        

serve()