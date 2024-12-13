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

# Global click counter
click_count = 0

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
    
    # Variável global para acumular clicks: opção de easter egg
    global click_count
    click_count += 1
    
    frases_vector = [ "Segura firme, ainda faltam ",    "Só mais um pouco! Restam apenas ",    "Calma, estamos quase lá! Só mais ",    "A paciência é uma virtude. Espere por ",
    "Está pertinho! Só faltam ",    "Respire fundo e espere mais ",    "Você está indo muito bem! Só mais ",    "Continue forte, faltam só ",    "Logo logo chega! Espere só mais ",
    "Não desista! Faltam só mais ",    "Tudo está no tempo certo. Só faltam ",    "Segure a emoção! Faltam apenas ",    "Está quase! Espere só mais ",    "O melhor está por vir! Restam só ",
    "Quase lá! Só mais ",    "Acalme o coração, ainda faltam ",    "Confie! Só mais ",    "Você está tão perto! Só faltam ",    "Mais um pouquinho! Restam apenas ",    "Continue acreditando! Só mais ",
    "Logo chega! Espere mais ",    "Sorria! Falta bem pouco: ",    "Fique firme! Restam só ",    "Estamos quase no fim! Mais ",    "O que é bom sempre vale a pena esperar! Só faltam ",
    "Persistência é tudo! Só mais ",    "Tão perto agora! Faltam ",    "Que expectativa boa! Ainda restam ",    "Não apresse o tempo, faltam apenas ",    "A jornada é tão bonita quanto o destino. Só mais ",
    "O melhor está chegando. Faltam só ",    "Continue positiva! Só mais ",    "Aguente firme! Restam apenas ",    "Está bem próximo agora! Só mais ",    "Cada segundo vale a pena! Restam ",
    "Está chegando a hora! Só faltam ",    "Está quase no fim! Aguarde só mais "]        

    images_v=['https://github.com/patriani/BirthClock/blob/main/images/barto.jpeg?raw=true','https://github.com/patriani/BirthClock/blob/main/images/curi_jardim.jpeg?raw=true',
    'https://github.com/patriani/BirthClock/blob/main/images/curi_quarto.jpeg?raw=true','https://github.com/patriani/BirthClock/blob/main/images/porao.jpeg?raw=true',
    'https://github.com/patriani/BirthClock/blob/main/images/vinhedo_bar.jpeg?raw=true','https://github.com/patriani/BirthClock/blob/main/images/acai.jpeg?raw=true',
    'https://github.com/patriani/BirthClock/blob/main/images/beijo.jpeg?raw=true','https://github.com/patriani/BirthClock/blob/main/images/carro.jpeg?raw=true',
    'https://github.com/patriani/BirthClock/blob/main/images/coracao.jpeg?raw=true','https://github.com/patriani/BirthClock/blob/main/images/dormindo.jpeg?raw=true',
    'https://github.com/patriani/BirthClock/blob/main/images/macaquinho.jpeg?raw=true','https://github.com/patriani/BirthClock/blob/main/images/peixinho.jpeg?raw=true',
    'https://github.com/patriani/BirthClock/blob/main/images/social.jpeg?raw=true']
    
    # Folha de estilos
    sty = StyleX('keepcalm.css')
    sty_2 = StyleX('Dday.css')
    
    # Definir o horário de destino: meia-noite de 13/12/2024
    data_destino = datetime(2024, 12, 13, 00, 00, 00)

    while True:

        # Hora atual
        agora = datetime.now()

        # Calcular o tempo restante
        tempo_restante = data_destino - agora

        # Extrair dias, horas, minutos e segundos restantes
        dias = tempo_restante.days
        horas, resto = divmod(tempo_restante.seconds, 3600)
        minutos, segundos = divmod(resto, 60)

        # Exibir o tempo restante
        clock_down=f" {dias}d {horas:02}h {minutos:02}m {segundos:02}s"
         
        seed = random.randint(0, 36)

        # Se o tempo restante for menor ou igual a zero, encerrar a contagem
        if (tempo_restante.total_seconds() <= 0):
            return Div(Div(P("Parabéns AMOOOOR!🎉 Desejo muito mais novidades empolgantes, tranquilidade, muuuuuuuita saúde, a companhia de bons amigos e MUITO EU na sua vida. Fico feliz demais por podermos comemorar juntos mais um aniversário seu. Quero que cada ano seja mais e mais especial. Você vem fazendo isso por mim em várias datas festivas e eu também vou sempre tentar trazer uma pitada de mágica pros seus aniversários, Natais, Páscoas e em todas as outras datas que você valoriza. Continua sendo minha cúmplice, meu amor e minha maior amiga? Me dá um abração e um beijo se sim.",sty_2)))

        if(click_count==15):
            return (Div(P("Cupom de uso único: TRENTO_ORIGINAL_NAMORADO10",style="margin: 0; font-size: 16px; color: #333;"),style="background-color: white; padding: 20px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); border-radius: 8px; text-align: center;"))

        if(click_count==30):
            return (Div(P("Cupom de uso único: TRENTO_DARK_NAMORADO10",style="margin: 0; font-size: 16px; color: #333;"),style="background-color: white; padding: 20px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); border-radius: 8px; text-align: center;"))

        if (click_count%6==0):
            seed_images = random.randint(0, (len(images_v)-1))
            print(images_v[seed_images])
            return Div(
            Div(card_3d('', images_v[seed_images], 1.5, left_align=True, hx_get='/click'))
            )

        return (Div(P(frases_vector[seed],clock_down,sty)),Div(f"Você já clicou {click_count} vezes !!",style="color:white; bottom: 0; "),Div(" Birthday Clockdown V1.2.1",style="font-size:x-small ;margin-top:14px; color:white; bottom: 0; "))

        


serve()

