from cliente import Cliente



# ------------------------------ #
# -- Testes da classe Cliente -- #
# ------------------------------ #
def test_cria_cliente():
    try:
        c = Cliente('nome', 99999999, 'email@mail.com')
    except Exception:
        assert False, 'Erro ao criar o cliente'
    else:
        assert hasattr(c, 'nome'), 'não criou o atributo público nome'
        assert hasattr(c, 'telefone'), 'não criou o atributo público telefone'
        assert hasattr(c, 'email'), 'não criou o atributo público email'


def test_cria_cliente_telefone_invalido():
    try:
        Cliente('nome', 'não é número', 'email@mail.com')
    except TypeError:
        pass
    except Exception:
        assert False, 'Erro diferente de TypeError para telefone inválido'
    else:
        assert False, 'Criou cliente com telefone inválido'


def test_cria_cliente_email_invalido():
    try:
        Cliente('nome', 99999999, 'não é email')
    except ValueError:
        pass
    except Exception:
        assert False, 'Erro diferente de ValueError para email inválido'
    else:
        assert False, 'Criou cliente com email inválido'


def test_cliente_nome():
    c = Cliente('nome', 99999999, 'email@mail.com')
    assert c.nome == 'nome', 'Atributo nome com valor incorreto'
    try:
        c.nome == 'novo_nome'
    except AttributeError:
        pass
    except Exception:
        assert c.nome == 'nome', 'O atributo nome não pode ser alterado'
    assert c.nome == 'nome', 'O atributo nome não pode ser alterado'


def test_cliente_telefone():
    c = Cliente('nome', 99999999, 'email@mail.com')
    assert c.telefone == 99999999, 'Atributo telefone com valor incorreto'
    c.telefone = 88888888
    assert c.telefone == 88888888, 'Não atualizou o valor de telefone'


def test_cliente_telefone_erro():
    c = Cliente('nome', 99999999, 'email@mail.com')
    try:
        c.telefone = 'não é telefone'
    except TypeError:
        pass
    except Exception:
        assert False, 'Erro diferente de TypeError para telefone inválido'
    assert c.telefone == 99999999, 'telefone não poderia ser alterado aqui'


def test_cliente_email():
    c = Cliente('nome', 99999999, 'email@mail.com')
    assert c.email == 'email@mail.com', 'Atributo email com valor incorreto'
    c.email = 'outro@mail.com'
    assert c.email == 'outro@mail.com', 'Não atualizou o valor de email'


def test_cliente_email_erro():
    c = Cliente('nome', 99999999, 'email@mail.com')
    try:
        c.email = 'não é email'
    except ValueError:
        pass
    except Exception:
        assert False, 'Erro diferente de ValueError para email inválido'
    assert c.email == 'email@mail.com', 'email não poderia ser alterado aqui'