# fast_app: classe para criar o aplicativo
# serve: função para deixar o site online
# Titled: classe que facilita criação de títulos
from fasthtml.common import fast_app, serve, Titled
# importando funções do arquivo components.py como uma biblioteca
from components import gerar_titulo, gerar_formulario


# Criação do aplicativo
app, routes = fast_app()

# Will run on http://localhost:5001/
@routes("https://birthclock.onrender.com/")
def homepage():
    return gerar_titulo("Birthday Clock","Hello World")

@routes("https://birthclock.onrender.com/form")
def homepage():
    formulario = gerar_formulario()
    # terceiro parâmetro do formulario aceita estruturação do título (como concatenação de divs)
    return Titled("Formulário de teste",formulario)

#parei o tutorial aqui: https://youtu.be/-ff9RpzeHG4?t=1542

serve()