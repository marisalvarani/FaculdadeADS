# Linguagem de Programação II
# AC03 ADS-EaD - Módulos e importação
# arquivo: banco.py

# A classe Banco ira precisar da classe Conta, que deve ser importada aqui:
# sigam o exemplo dado na live 03, anexei os arquivos na postagem do Classroom.
# import conta ou from conta import Conta

from conta import Conta

class Banco:
    """
    Classe que modela o banco

    possui os atributos públicos:
    + nome
    + contas

    possui o método público:
    + abre_conta()

    O nome deve ser recebido na inicialização do objeto e ser guardado em um
    atributo privado, acessível apenas para leitura através de uma property.

    Crie um atributo privado que irá armazenar as contas criadas no banco
    e utilze esse atributo para gerar automaticamente o número das novas
    contas do banco. A lista de contas deverá ser acessível apenas para leitura
    através de uma property `contas`.

    O método abre_conta deverá abrir uma nova conta, sendo responsável por
    atribuir o numero da conta em ordem crescente, a partir de 1 para a
    primeira conta aberta.

    ----------------------------------------------------------------------------
    Esta é a lista do que deve ser implementado nesta classe:
    o método __init__, 2 def's com property e 1 def normal

    Implemente os seguintes métodos, properties ou setters,
    de acordo com o que é pedido no enunciado.

    * Inicialização do objeto, com o método especial __init__
        deve receber na inicialização os atributos:
            nome
    * Property do nome do banco.
    * Property da lista de contas do banco.
    * Método abre_conta da classe Banco:
        recebe a lista de clientes e o saldo inicial da conta,
        caso o saldo inicial seja negativo levanta um ValueError (a conta não é aberta).
        DICA: O parâmetro clientes será uma lista com instâncias do tipo Cliente.
        DICA 2: sobre a lista de contas
        inicializar (no init) a lista de contas como uma lista vazia
        self.__contas = []

        no método abre_conta():
        - receber os parâmetros pedidos no enunciado
        - verificar se saldo inicial é negativo, ser for negativo dar um `raise ValueError`
        - calcular o número da conta com base na lista `self.__contas`
        - instanciar uma conta -> `c1 = Conta(clientes, numero, saldo)`
                            ou -> `c1 = conta.Conta(clientes, numero, saldo)`,
                            dependendo de como fizeram a importação da classe/módulo
        - adicionar na lista de contas -> `self.__contas.append(c1)`
    """
   

    def __init__(self, nome):
        self.__nome = nome
        self.__contas = []
                
        
    @property
    def nome(self):
        return self.__nome    

    @property
    def contas(self):
        return self.__contas

    def abre_conta(self, clientes, saldo):
        if saldo < 0:
            raise ValueError
        else:
            numero = len(self.__contas) + 1
            c1 = Conta(clientes, numero, saldo)
            self.__contas.append(c1)




