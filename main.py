from fasthtml.common import *
from components import gerar_titulo, clockdown_timer # Importando funções do arquivo components.py como uma biblioteca
from card3d import card_3d
from datetime import datetime # Importando biblioteca para coleta de horário atual
import random # to select a random "keep calm" frase

hdrs = [Style('''* { box-sizing: border-box; }
    html, body { width: 100%; height: 100%; display: flex; justify-content: center; align-items: center;}
    body { 
        font-family: 'Arial Black', 'Arial Bold', Gadget, sans-serif;
        perspective: 1500px; background-color:black;;
    }''')]

#background: linear-gradient(#666, #222)

app = FastHTML(hdrs=hdrs)
rt = app.route

@rt('/')
def homepage():

    url_gift = "https://github.com/patriani/BirthClock/blob/main/images/gift_with_bg.png?raw=true"
    return Div(
        Div(card_3d('', url_gift, 1.5, left_align=True, hx_get='/click'))
    )


@rt("/click")
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
        clock_down=f" {dias}d {horas:02}h {minutos:02}m {segundos:02}s"
        
        # Confdição para confete e código
        # Condição para return apenas do clockdown
 
        seed = random.randint(0, 36)

        frases_vector = [ "Segura firme, ainda faltam ",    "Só mais um pouco! Restam apenas ",    "Calma, estamos quase lá! Só mais ",    "A paciência é uma virtude. Espere por ",    "Está pertinho! Só faltam ",    "Respire fundo e espere mais ",    "Você está indo muito bem! Só mais ",    "Continue forte, faltam só ",    "Logo logo chega! Espere só mais ",    "Não desista! Faltam só mais ",    "Tudo está no tempo certo. Só faltam ",    "Segure a emoção! Faltam apenas ",    "Está quase! Espere só mais ",    "O melhor está por vir! Restam só ",    "Quase lá! Só mais ",    "Acalme o coração, ainda faltam ",    "Confie! Só mais ",    "Você está tão perto! Só faltam ",    "Mais um pouquinho! Restam apenas ",    "Continue acreditando! Só mais ",    "Logo chega! Espere mais ",    "Sorria! Falta bem pouco: ",    "Fique firme! Restam só ",    "Estamos quase no fim! Mais ",    "O que é bom sempre vale a pena esperar! Só faltam ",    "Persistência é tudo! Só mais ",    "Tão perto agora! Faltam ",    "Que expectativa boa! Ainda restam ",    "Não apresse o tempo, faltam apenas ",    "A jornada é tão bonita quanto o destino. Só mais ",    "O melhor está chegando. Faltam só ",    "Continue positiva! Só mais ",    "Aguente firme! Restam apenas ",    "Está bem próximo agora! Só mais ",    "Cada segundo vale a pena! Restam ",    "Está chegando a hora! Só faltam ",    "Está quase no fim! Aguarde só mais "]        

        sty= StyleX('keepcalm.css')
        return Div(P(frases_vector[seed],clock_down,sty))

        

serve()