from libpythonpro.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Aniro', email='capablanca1@bol.com.br')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(sessao):
    usuarios = [
                   Usuario(nome='Aniro', email='capablanca1@bol.com.br'),

                   Usuario(nome='Marisa', email='capablanca1@bol.com.br')
               ],
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
