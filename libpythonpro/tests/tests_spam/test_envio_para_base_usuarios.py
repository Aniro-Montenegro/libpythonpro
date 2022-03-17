from unittest.mock import Mock

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
        enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'capablanca1@bol.com.br',
        'Curso Python Pro',
        'Confira os módulos fantásticos'

    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Marisa', email='capablanca1@bol.com.br')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'marisa@bol.com.br',
        'Curso Python Pro',
        'Confira os módulos fantásticos'

    )
    enviador.enviar.assert_called_once_with == (
        'marisa@bol.com.br',
        'capablanca1@bol.com.br',
        'Curso Python Pro',
        'Confira os módulos fantásticos'

    )
