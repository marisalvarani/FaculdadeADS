from conta import Conta

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
    assert ('saldo_inicial', 100) in extrato, (
        'Saque inicial não registrado no extrato')


def test_conta_extrato_2():
    c = Cliente('nome', 99999999, 'email@mail.com')
    cc = Conta([c], 1, 200)
    cc.sacar(150)
    cc.depositar(250)
    extrato = cc.tirar_extrato()
    assert len(extrato) == 3, (
        'O extrato deve conter duas entradas para esse teste')
    assert extrato[0] == ('saldo_inicial', 200), (
        'A primeira entrada está incorreta')
    assert extrato[1] == ('saque', 150), (
        'A segunda entrada está incorreta')
    assert extrato[2] == ('deposito', 250), (
        'A terceira entrada está incorreta')