# Importing necessary html elements
from fasthtml.common import Div, H1, P, Form,Input,Button

def gerar_titulo(titulo,subtitulo):
    return Div(
        H1(titulo),
        P(subtitulo),
        P("Esse componente foi gerado com FastHRML")
    )

def gerar_formulario():
    formulario = Form(
        Input(type="text", name="tarefa",placeholder="input the text here"),
        Button("Enviar"),
        method="post",
        action="/adicionar_tarefa"
    )
    return formulario

