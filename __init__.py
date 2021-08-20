from lona import html
from lona.html import Div, H1, HTML, Table
from lona.html.nodes import Button
from lona.view import LonaView
from lona import LonaApp

app = LonaApp(__file__)

@app.route('/')
class ClockView(LonaView):
    def handle_request(self, request):
        div_titulo = Div(H1('Titulo Luna'))
        div_titulo.style['text-align'] = 'center'

        botao_alert = Button('Clique em mim!')
        div_botao_alert = Div(botao_alert)
        div_botao_alert.style['text-align'] = 'center'

        div_mensagem = Div()
        div_mensagem.style['text-align'] = 'center'

        html = HTML(
            div_titulo,
            div_botao_alert, 
            div_mensagem, )

        self.show(html)

        input_event = self.await_click(botao_alert)
        if input_event.node == botao_alert:
            div_mensagem.set_text('aaa')

        return html

app.run(port=8080)