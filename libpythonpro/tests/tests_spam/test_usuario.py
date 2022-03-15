from libpythonpro.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Aniro')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(sessao):
    usuarios = [Usuario(nome='Aniro'), Usuario(nome='Marisa')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
