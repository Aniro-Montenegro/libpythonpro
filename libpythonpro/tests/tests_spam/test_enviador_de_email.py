import pytest as pytest

from libpythonpro.spam.test_enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'destinatario',
    ['capablanca1@bol.com.br', 'foo@bar.com.br']

)
def test_remetente(destinatario):
    enviador = Enviador()

    resultado = enviador.enviar(
        destinatario,
        'aniromontenegro79@gmail.com',
        'Cursos Python pro',
        'Primeira turma Guido Von Rossum aberta.'
    )
    assert destinatario in resultado


@pytest.mark.parametrize(
    'destinatario',
    ['', 'foo']

)
def test_remetente_invalido(destinatario):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            destinatario,
            'aniromontenegro79@gmail.com',
            'Cursos Python pro',
            'Primeira turma Guido Von Rossum aberta.'
        )
