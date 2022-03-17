import pytest as pytest

from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario
from libpythonpro.spam.test_enviador_de_email import Enviador


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Aniro', email='capablanca1@bol.com.br'),

            Usuario(nome='Marisa', email='capablanca1@bol.com.br')
        ],
        [
            Usuario(nome='Marisa', email='capablanca1@bol.com.br')
        ]
    ]

)
def test_qtd_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
        enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'capablanca1@bol.com.br',
        'Curso Python Pro',
        'Confira os módulos fantásticos'

    )
    assert len(usuarios) == enviador.qtd_email_enviados


class EnviadorMock(Enviador):
    def __init__(self):
        super().__init__()
        self.qtd_email_enviados = 0
        self.parametros_de_envio = None

    def enviar(self, remetente, destinatario, assunto, corpo):
        self.parametros_de_envio = (remetente, destinatario, assunto, corpo)
        self.qtd_email_enviados += 1


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Marisa', email='capablanca1@bol.com.br')
    sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'marisa@bol.com.br',
        'Curso Python Pro',
        'Confira os módulos fantásticos'

    )
    assert enviador.parametros_de_envio == (
        'marisa@bol.com.br',
        'capablanca1@bol.com.br',
        'Curso Python Pro',
        'Confira os módulos fantásticos'

    )
