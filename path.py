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
if __name__ == "__main__":
    serve()