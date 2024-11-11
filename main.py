# FastHRML: classe para criar o aplicativo
# serve: função para deixar o site online
from fasthtml.common import FastHTML, serve

# Criação do aplicativo
app = FastHTML()

# Método para execução da home
@app.get("/")
def homepage():
    return "<h1>Hello</h1>"
    
serve()