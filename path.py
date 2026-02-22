from fasthtml.common import *

app, rt = fast_app()

@rt("/")
def home():
    return Html(
        Head(Title("Ternos do Interclasses")),
        Body(
            H1("Escolha sua Camisa"),
            Div("Suas opções aqui...")
        )
    )

# Roda em: https://seu-site.render.com
