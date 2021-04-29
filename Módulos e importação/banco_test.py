from cliente import Cliente
from conta import Conta
from banco import Banco


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


# ---------------------------- #
# -- Testes da classe Banco -- #
# ---------------------------- #
def test_cria_banco():
    try:
        b = Banco('nome')
    except Exception:
        assert False, 'Erro ao criar o Banco'
    else:
        assert hasattr(b, 'nome'), 'Não criou o atributo público nome'


def test_banco_nome():
    b = Banco('nome')
    assert b.nome == 'nome', 'Atributo nome com valor incorreto'


def test_banco_contas_vazias():
    b = Banco('nome')
    assert b.contas == [], (
        'O banco deve começar sem nenhuma conta (lista vazia)')


def test_banco_contas_existentes():
    b = Banco('nome')
    c = Cliente('nome', 99999999, 'email@mail.com')
    b.abre_conta([c], 200)
    b.abre_conta([c], 300)
    assert len(b.contas) == 2, 'O banco deveria ter 2 contas'
    for cc in b.contas:
        assert isinstance(cc, Conta), ('Os elementos da lista de contas '
                                       'devem ser instâncias da classe Conta')


def test_banco_numero_conta():
    b = Banco('nome')
    c = Cliente('nome', 99999999, 'email@mail.com')
    for _ in range(5):
        b.abre_conta([c], 100)
    ccs = b.contas
    assert len(ccs) == 5, 'O banco deveria ter 5 contas'
    assert all([isinstance(cc, Conta) for cc in ccs]), (
        'Os elementos da lista de contas '
        'devem ser instâncias da classe Conta'
    )
    ordinais = ['primeira', 'segunda', 'terceira', 'quarta', 'quinta']
    msg = 'A {} conta deve ter o numero {}'
    for i, texto in enumerate(ordinais):
        assert ccs[i].numero == i+1, msg.format(texto, i+1)


def test_banco_abre_conta_erro():
    b = Banco('nome')
    c = Cliente('nome', 99999999, 'email@mail.com')
    try:
        b.abre_conta([c], -100)
    except ValueError:
        pass
    except Exception:
        assert False, (
            'Erro diferente de ValueError para saldo inicial negativo')
    assert len(b.contas) == 0, 'Abriu uma conta com saldo inicial negativo'


# ---------------------------- #
# -- Testes da classe Conta -- #
# ---------------------------- #
def test_cria_conta():
    try:
        c = Cliente('nome', 99999999, 'email@mail.com')
        cc = Conta([c], 1, 0)
    except Exception:
        assert False, 'Erro ao criar conta'
    else:
        assert hasattr(cc, 'clientes'), 'Não criou o atributo público clientes'
        assert hasattr(cc, 'numero'), 'Não criou o atributo público numero'
        assert hasattr(cc, 'saldo'), 'Não criou o atributo público saldo'


def test_conta_clientes():
    c = Cliente('nome', 99999999, 'email@mail.com')
    cc = Conta([c], 1, 0)
    clientes = cc.clientes
    assert len(clientes) == 1, 'Esta conta deveria ter apenas 1 cliente'
    assert clientes[0].nome == 'nome', 'Nome do cliente incorreto'
    assert clientes[0].email == 'email@mail.com', 'Email do cliente incorreto'
    assert clientes[0].telefone == 99999999, 'Telefone do cliente incorreto'


def test_conta_numero():
    c = Cliente('nome', 99999999, 'email@mail.com')
    cc = Conta([c], 1, 0)
    assert cc.numero == 1, 'Número da conta incorreto'


def test_conta_saldo():
    c = Cliente('nome', 99999999, 'email@mail.com')
    cc = Conta([c], 1, 100)
    assert cc.saldo == 100, 'Saldo da conta incorreto'


def test_conta_deposito():
    c = Cliente('nome', 99999999, 'email@mail.com')
    cc = Conta([c], 1, 100)
    cc.depositar(200)
    assert cc.saldo == 300, 'Saldo da conta incorreto'
    assert ('deposito', 200) in cc.tirar_extrato(), (
        'Depósito não registrado no extrato')


def test_conta_saque():
    c = Cliente('nome', 99999999, 'email@mail.com')
    cc = Conta([c], 1, 100)
    cc.sacar(50)
    assert cc.saldo == 50, 'Saldo da conta incorreto'
    assert ('saque', 50) in cc.tirar_extrato(), (
        'Saque não registrado no extrato')


def test_conta_saque_erro():
    c = Cliente('nome', 99999999, 'email@mail.com')
    cc = Conta([c], 1, 100)
    try:
        cc.sacar(150)
    except ValueError:
        assert cc.saldo == 100, (
            'O saldo não deve ser alterado quando o saque for inválido')
        assert ('saque', 150) not in cc.tirar_extrato(), (
            'Um saque inválido não deve ser registrado no extrato')
    except Exception:
        assert False, 'Erro diferente de ValueError para saque inválido'
    else:
        assert False, 'Permitiu a realização de um saque inválido'


def test_conta_extrato():
    c = Cliente('nome', 99999999, 'email@mail.com')
    cc = Conta([c], 1, 100)
    extrato = cc.tirar_extrato()
    assert type(extrato) == list, 'O extrato deve ser uma lista'
    assert len(extrato) == 1, (
        'O extrato deve conter apenas uma entrada para esse teste')
    assert ('saldo inicial', 100) in extrato, (
        'Saque inicial não registrado no extrato')


def test_conta_extrato_2():
    c = Cliente('nome', 99999999, 'email@mail.com')
    cc = Conta([c], 1, 200)
    cc.sacar(150)
    cc.depositar(250)
    extrato = cc.tirar_extrato()
    assert len(extrato) == 3, (
        'O extrato deve conter duas entradas para esse teste')
    assert extrato[0] == ('saldo inicial', 200), (
        'A primeira entrada está incorreta')
    assert extrato[1] == ('saque', 150), (
        'A segunda entrada está incorreta')
    assert extrato[2] == ('deposito', 250), (
        'A terceira entrada está incorreta')