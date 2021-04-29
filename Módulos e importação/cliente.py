# Linguagem de Programação II
# AC03 ADS-EaD - Módulos e importação
# arquivo: cliente.py



class Cliente:
    """
    Classe que modela os clientes do banco.

    possui os atributos públicos:
    + nome
    + telefone
    + email

    e não possui nenhum método (público ou privado).

    O nome deve ser recebido na inicialização do objeto e ser guardado em
    um atributo privado, não podendo ser alterado posteriormente, após o cliente
    ter sido criado. O valor do atributo deve ser acessado pelo identificador
    público `nome` (use uma @property para isso).

    Tanto o email quando o telefone também precisam ser obrgatoriamente
    recebidos na inicialização e guardados em atributos privados.
    O acesso externo deve ser feito pelos atributos públicos
    `telefone` e `email`, usando a property e o setter.

    Considerações ao atribuir o valor do telefone e do email, válidas
    tanto para a incialização do objeto quanto para uma eventual
    alteração posterior feita através do atributo público:
    * caso o email não seja uma string, levanta um TypeError;
    * caso o email não seja válido (verificar se contém o @) levanta um ValueError;
    * caso o telefone não seja um número inteiro levanta um TypeError.

    ------------------------------------------------------------------------
    Esta é a lista do que deve ser implementado nesta classe:
    o método __init__, 3 def's com property e 2 def's com setter

    Implemente os seguintes métodos, properties ou setters,
    de acordo com o que é pedido no enunciado.

    * Inicialização do objeto, como método especial __init__
        deve receber na inicialização os atributos:
            nome,
            telefone,
            email
    * Property do nome
    * Property do telefone
    * Setter do telefone
    * Property do email
    * Setter do email
    """

    def __init__(self, nome, telefone, email):
        self.__nome = nome
        self.telefone = telefone
        self.email = email
        

    @property
    def nome(self):
        """Property do nome do cliente"""
        return self.__nome
        

    @property
    def telefone(self):
        """Property do telefone do cliente"""
        return self.__telefone
        

    @telefone.setter
    def telefone(self, novo_telefone):
        """
        Setter do telefone do cliente, caso não receba um número,
        levanta um TypeError
        """
        if type(novo_telefone) == int:
            self.__telefone = novo_telefone
        else:
            raise TypeError
       

    @property
    def email(self):
        """Property do email do cliente"""
        return self.__email

    @email.setter
    def email(self, novo_email):
        """
        Setter do email do cliente, lançamento de exceções:
        levanta um TypeError caso não receba uma string; e
        levanta um ValueError caso não receba um email válido (contendo o @)
        """
        s = 0
        if type(novo_email) != str:
            raise TypeError
        else:
            for x in novo_email:
                if x == "@":
                    s = s+1
            if s==1:
                self.__email = novo_email
            else:
                raise ValueError



        