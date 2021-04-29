import pytest

from empresa import Empresa
from funcionarios import Estagiario, Programador, Vendedor


# ---------------------------------------------------------- #
# ---------------------- Programador ----------------------- #
# ---------------------------------------------------------- #
def test_programador_carga_horaria():
    prog = Programador('Fulano', 25, 'fulano@empresa.com', 40)
    msg = ('a property carga_horaria não retornou o valor da '
           'carga horaria semanal')
    assert prog.carga_horaria == 40, msg


@pytest.mark.parametrize('carga_horaria', [-5, 19, 42])
def test_programador_carga_horaria_invalida(carga_horaria):
    try:
        Programador('Fulano', 25, 'fulano@empresa.com', carga_horaria)
    except Exception as erro:
        class_name = erro.__class__.__name__
        msg = f'Erro encontrado ({class_name}) diferente de ValueError'
        assert isinstance(erro, ValueError), msg
    else:
        raise AssertionError('Programador criado com carga horária inválida')


def test_programador_altera_carga_horaria():
    prog = Programador('Fulano', 25, 'fulano@empresa.com', 40)
    prog.carga_horaria = 36
    msg = 'A carga horária não foi alterada para o novo valor'
    assert prog.carga_horaria == 36, msg


def test_programador_altera_carga_horaria_invalida():
    prog = Programador('Fulano', 25, 'fulano@empresa.com', 40)
    try:
        prog.carga_horaria = 16
    except ValueError:
        msg = 'A carga horaria foi alterada antes de levantar o ValueError'
        assert prog.carga_horaria == 40, msg
    except Exception as erro:
        class_name = erro.__class__.__name__
        msg = f'Erro encontrado ({class_name}) diferente de ValueError'
        raise AssertionError(msg)
    else:
        raise AssertionError('Não levantou ValueError para carga inválida')


def test_programador_calcula_salario():
    prog = Programador('Fulano', 25, 'fulano@empresa.com', 40)
    msg = 'Salário do programador calculado incorretamente'
    assert prog.calcula_salario() == 6300, msg


def test_programador_recebe_aumento():
    prog = Programador('Fulano', 25, 'fulano@empresa.com', 40)
    prog.aumenta_salario()
    msg = 'Aumento do salário de programador calculado incorretamente'
    assert prog.calcula_salario() == 6615, msg


# ---------------------------------------------------------- #
# ----------------------- Estagiário ----------------------- #
# ---------------------------------------------------------- #
def test_estagiario_carga_horaria():
    est = Estagiario('Fulano', 25, 'fulano@empresa.com', 20)
    msg = ('a property carga_horaria não retornou o valor da '
           'carga horaria semanal')
    assert est.carga_horaria == 20, msg


@pytest.mark.parametrize('carga_horaria', [-5, 10, 35])
def test_estagiario_carga_horaria_invalida(carga_horaria):
    try:
        Estagiario('Fulano', 25, 'fulano@empresa.com', carga_horaria)
    except Exception as erro:
        class_name = erro.__class__.__name__
        msg = f'Erro encontrado ({class_name}) diferente de ValueError'
        assert isinstance(erro, ValueError), msg
    else:
        raise AssertionError('Estagiário criado com carga horária inválida')


def test_estagiario_altera_carga_horaria():
    est = Estagiario('Fulano', 25, 'fulano@empresa.com', 20)
    est.carga_horaria = 30
    msg = 'A carga horária não foi alterada para o novo valor'
    assert est.carga_horaria == 30, msg


def test_estagiario_altera_carga_horaria_invalida():
    est = Estagiario('Fulano', 25, 'fulano@empresa.com', 20)
    try:
        est.carga_horaria = 36
    except ValueError:
        msg = 'A carga horaria foi alterada antes de levantar o ValueError'
        assert est.carga_horaria == 20, msg
    except Exception as erro:
        class_name = erro.__class__.__name__
        msg = f'Erro encontrado ({class_name}) diferente de ValueError'
        raise AssertionError(msg)
    else:
        raise AssertionError('Não levantou ValueError para carga inválida')


def test_estagiario_calcula_salario():
    est = Estagiario('Fulano', 25, 'fulano@empresa.com', 20)
    msg = 'Salário do estagiário calculado incorretamente'
    assert est.calcula_salario() == 1645, msg


def test_estagiario_recebe_aumento():
    est = Estagiario('Fulano', 25, 'fulano@empresa.com', 20)
    est.aumenta_salario()
    msg = 'Aumento do salário do estagiário calculado incorretamente'
    assert abs(est.calcula_salario() - 1714.75) < 0.01, msg


# ---------------------------------------------------------- #
# ------------------------ Vendedor ------------------------ #
# ---------------------------------------------------------- #
def test_vendedor_carga_horaria():
    vend = Vendedor('Fulano', 25, 'fulano@empresa.com', 20)
    msg = ('a property carga_horaria não retornou o valor da '
           'carga horaria semanal')
    assert vend.carga_horaria == 20, msg


@pytest.mark.parametrize('carga_horaria', [-5, 10, 50])
def test_vendedor_carga_horaria_invalida(carga_horaria):
    try:
        Vendedor('Fulano', 20, 'fulano@empresa.com', carga_horaria)
    except Exception as erro:
        class_name = erro.__class__.__name__
        msg = f'Erro encontrado ({class_name}) diferente de ValueError'
        assert isinstance(erro, ValueError), msg
    else:
        raise AssertionError('Vendedor criado com carga horária inválida')


def test_vendedor_altera_carga_horaria():
    vend = Vendedor('Fulano', 25, 'fulano@empresa.com', 20)
    vend.carga_horaria = 45
    msg = 'A carga horária não foi alterada para o novo valor'
    assert vend.carga_horaria == 45, msg


def test_vendedor_altera_carga_horaria_invalida():
    vend = Vendedor('Fulano', 25, 'fulano@empresa.com', 20)
    try:
        vend.carga_horaria = 46
    except ValueError:
        msg = 'A carga horaria foi alterada antes de levantar o ValueError'
        assert vend.carga_horaria == 20, msg
    except Exception as erro:
        class_name = erro.__class__.__name__
        msg = f'Erro encontrado ({class_name}) diferente de ValueError'
        raise AssertionError(msg)
    else:
        raise AssertionError('Não levantou ValueError para carga inválida')


def test_vendedor_visitas():
    vend = Vendedor('Fulano', 25, 'fulano@empresa.com', 20)
    msg = 'O número de visitas deve ser iniciado em zero'
    assert vend.visitas == 0, msg


def test_vendedor_realizar_visitas():
    vend = Vendedor('Fulano', 25, 'fulano@empresa.com', 20)
    msg = 'Não atualizou o número de visitas do vendedor corretamente'
    vend.realizar_visita(3)
    assert vend.visitas == 3, msg
    vend.realizar_visita(6)
    assert vend.visitas == 9, msg


@pytest.mark.parametrize('n_visitas', ['5', 'abc', 5.2, -3, 0, [], {}])
def test_vendedor_realizar_visitas_erro(n_visitas):
    vend = Vendedor('Fulano', 25, 'fulano@empresa.com', 20)
    try:
        vend.realizar_visita(n_visitas)
    except TypeError:
        msg = 'Levantou TypeError para entrada do tipo int'
        assert not isinstance(n_visitas, int), msg
    except ValueError:
        msg = 'Não levantou TypeError para entrada de tipo diferente de int'
        assert isinstance(n_visitas, int), msg
        assert n_visitas <= 0, 'Levantou ValueError para entrada válida'
    except Exception as erro:
        class_name = erro.__class__.__name__
        msg = f'Erro encontrado ({class_name}) diferente do tipo pedido'
        raise AssertionError(msg)
    else:
        raise AssertionError('Não levantou erro para entrada inválida')


def test_vendedor_zerar_visitas():
    vend = Vendedor('Fulano', 25, 'fulano@empresa.com', 20)
    vend.realizar_visita(5)
    vend.zerar_visitas()
    msg = 'O número de visitas não foi zerado corretamente'
    assert vend.visitas == 0, msg


def test_vendedor_calcula_salario01():
    vend = Vendedor('Fulano', 25, 'fulano@empresa.com', 20)
    msg = 'Salário do vendedor calculado incorretamente'
    assert vend.calcula_salario() == 3050.0, msg


def test_vendedor_calcula_salario02():
    vend = Vendedor('Fulano', 25, 'fulano@empresa.com', 20)
    vend.realizar_visita(23)
    msg = 'Salário do vendedor calculado incorretamente'
    assert vend.calcula_salario() == 3740.0, msg


def test_vendedor_recebe_aumento():
    vend = Vendedor('Fulano', 25, 'fulano@empresa.com', 20)
    vend.aumenta_salario()
    msg = 'Aumento do salário do vendedor calculado incorretamente'
    assert abs(vend.calcula_salario() - 3185.0) < 0.01, msg


# ---------------------------------------------------------- #
# ------------------------ Empresa ------------------------- #
# ---------------------------------------------------------- #
def test_empresa_equipe_vazia():
    emp = Empresa('ACME', 123456789, 'Tecnologia', [])
    msg = 'A lista de funcionários deve começar com o valor passado'
    assert emp.equipe == [], msg


def test_empresa_equipe_inicial():
    est = Estagiario('Pedro', 25, 'pedro@empresa.com', 20)
    emp = Empresa('ACME', 123456789, 'Tecnologia', [est])
    msg = 'A lista de funcionários dever começar com o valor passado'
    assert len(emp.equipe) == 1, msg
    msg = 'O objeto de funcionário recebido em `equipe` não deve ser alterado'
    assert emp.equipe[0] is est, msg


def test_empresa_contrata():
    est = Estagiario('Maria', 25, 'maria@empresa.com', 20)
    prog = Programador('Ana', 31, 'ana@empresa.com', 40)
    vend = Vendedor('Marcos', 28, 'marcos@empresa.com', 35)
    emp = Empresa('ACME', 123456789, 'Tecnologia', [])
    emp.contrata(est)
    emp.contrata(prog)
    emp.contrata(vend)
    msg = 'A equipe não contém o número correto de funcionários contratados'
    assert len(emp.equipe) == 3, msg
    msg = 'O {0} item da equipe não é o {0} funcionário contratado'
    assert emp.equipe[0] is est, msg.format('primeiro')
    assert emp.equipe[1] is prog, msg.format('segundo')
    assert emp.equipe[2] is vend, msg.format('terceiro')


def test_empresa_folha_pagamento_1():
    prog = Programador('Julia', 31, 'julia@empresa.com', 40)
    est = Estagiario('Pedro', 25, 'pedro@empresa.com', 20)
    vend1 = Vendedor('Mauro', 41, 'mauro@empresa.com', 35)
    vend2 = Vendedor('Carla', 36, 'carla@empresa.com', 45)
    emp = Empresa('ACME', 123456789, 'Tecnologia', [])
    emp.contrata(prog)
    emp.contrata(est)
    emp.contrata(vend1)
    emp.contrata(vend2)
    vend1.realizar_visita(7)
    vend2.realizar_visita(10)
    assert emp.folha_pagamento() == 19955.0, 'Folha de pagamento calculada errada'


def test_empresa_folha_pagamento_2():
    prog = Programador('Julia', 31, 'julia@empresa.com', 40)
    est = Estagiario('Pedro', 25, 'pedro@empresa.com', 20)
    vend1 = Vendedor('Mauro', 41, 'mauro@empresa.com', 35)
    vend2 = Vendedor('Carla', 36, 'carla@empresa.com', 45)
    emp = Empresa('ACME', 123456789, 'Tecnologia', [])
    emp.contrata(prog)
    emp.contrata(est)
    emp.contrata(vend1)
    emp.contrata(vend2)
    vend1.realizar_visita(3)
    vend2.realizar_visita(5)
    msg = 'Folha de pagamento calculada errada'
    assert emp.folha_pagamento() == 19685.0, msg
    emp.dissidio_anual()
    msg = 'Folha de pagamento calculada errada após o dissidio'
    assert abs(emp.folha_pagamento() - 20609.75) < 0.01, msg
# ---------------------------------------------------------------