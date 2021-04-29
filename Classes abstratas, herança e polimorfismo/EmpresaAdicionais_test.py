import pytest
from empresa import Empresa
from funcionarios import Estagiario, Programador, Vendedor


def test_listar_visitas_tipo():
    prog = Programador('Julia', 31, 'julia@empresa.com', 40)
    est = Estagiario('Pedro', 25, 'pedro@empresa.com', 20)
    vend1 = Vendedor('Mauro', 41, 'mauro@empresa.com', 35)
    vend2 = Vendedor('Carla', 36, 'carla@empresa.com', 45)
    vend3 = Vendedor('Gabriel Martins', 34, 'gabrielmartins@empresa.com', 22)
    emp = Empresa('ACME', 123456789, 'Tecnologia', [])
    emp.contrata(prog)
    emp.contrata(est)
    emp.contrata(vend1)
    emp.contrata(vend2)
    emp.contrata(vend3)
    vend1.realizar_visita(7)
    vend2.realizar_visita(10)
    vend3.realizar_visita(55)
    msg = 'O retorno da função não é o esperado.'
    assert emp.listar_visitas() == {'mauro@empresa.com': 7, 'carla@empresa.com': 10,
                                    'gabrielmartins@empresa.com': 55}, msg


def test_zerar_visitas_vendedores():
    prog = Programador('Julia', 31, 'julia@empresa.com', 40)
    est = Estagiario('Pedro', 25, 'pedro@empresa.com', 20)
    vend1 = Vendedor('Mauro', 41, 'mauro@empresa.com', 35)
    vend2 = Vendedor('Carla', 36, 'carla@empresa.com', 45)
    vend3 = Vendedor('Gabriel Martins', 34, 'gabrielmartins@empresa.com', 22)
    emp = Empresa('ACME', 123456789, 'Tecnologia', [])
    emp.contrata(prog)
    emp.contrata(est)
    emp.contrata(vend1)
    emp.contrata(vend2)
    emp.contrata(vend3)
    vend1.realizar_visita(7)
    vend2.realizar_visita(10)
    vend3.realizar_visita(55)
    msg = 'O retorno da função não é o esperado.'
    assert emp.listar_visitas() == {'mauro@empresa.com': 7, 'carla@empresa.com': 10,
                                    'gabrielmartins@empresa.com': 55}, msg
    emp.zerar_visitas_vendedores()
    msg = 'A função zerar_visitas_vendedores não zerou a visita de todos os vendedores'
    assert emp.listar_visitas() == {'mauro@empresa.com': 0, 'carla@empresa.com': 0,
                                    'gabrielmartins@empresa.com': 0}, msg

# ---------------------------------------------------------------
