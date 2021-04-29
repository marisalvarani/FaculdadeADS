# Linguagem de Programação II
# Atividade Contínua 04 - Classes abstratas, herança e polimorfismo
# Arquivo: funcionarios.py



class Pessoa:
    '''
    Classe Abstrata Pessoa - não deve ser alterada
    '''
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade


class Funcionario(Pessoa):
    '''
    Classe Abstrata funcionário.
    Métodos (ou properties) que tenham exatamente a mesma implementação
    em todas as classes filhas podem ser editados nesta classe,
    enquanto métodos (ou properties) que tenham uma implementação
    específica devem ser editados nas classes filhas.

    Exemplos: 
    * aumenta_salario terá a mesma implementação em todas as subclasses,
      pois o dissídio é de 5% sobre o valor da hora para todos os funcionários.
    * calcula_salario terá uma implementação específica para cada tipo,
      pois dependendo da classe de funcionário, o cálculo segue regras diferentes.

    Em relação a property e o setter de carga_horaria, eles podem ser implemetados
    em cada subclasse, pois o setter deve seguir regras diferentes para cada tipo
    de funcionário, ou ambos podem ser implementados apenas nesta classe, e a
    verificação da validade da carga horária ser feita em função de atributos
    (limites de carga horária mínima e máxima) que serão definidos no inicializador
    das subclasses. Isso funciona pois o self é uma referência pro objeto e
    a classe Funcionario é abstrata, ou seja, não será instanciada diretamente.
    '''
    def __init__(self, nome, idade, email, carga_horaria):
        '''
        Construtor da classe Funcionário - lembre-se de usar o super para acessar o construtor
        da classe mãe e criar atributos que já estão definidos lá.
        '''
        super().__init__(nome, idade)
        self.__email = email
        self.carga_horaria = carga_horaria

    @property
    def email(self):
        return self.__email
        
    def calcula_salario(self):
        '''
        Calcula e retorna o salário do mês para o funcionário
        '''
        raise NotImplementedError
    
    
    @property
    def carga_horaria(self):
        '''
        Retorna a carga horária de trabalho do funcionário
        '''
        raise NotImplementedError

    @carga_horaria.setter
    def carga_horaria(self, nova_carga_horaria):
        '''
        altera a carga horária do funcionário, respeitando o limite de horas por categoria.
        Caso o numero informado seja inválido, de acordo com o cargo, levanta um ValueError
        - Este método não possui retorno;
        '''
        raise NotImplementedError

    def aumenta_salario(self):
        '''
        Aplica um aumento de 5% no valor da hora trabalhada para o funcionário
        - Este método não possui retorno;
        '''
        raise NotImplementedError


'''
DICAS:

Se uma classe não possui um método definido, mas este método é definido em
alguma classe mãe acima, a classe irá herdar e usar tal método exatamente como
ele está definido na classe acima.

Isto também se aplica ao construtor, se Programador não define um __init__, então
esta classe está automaticamente usando o __init__ da classe Funcionário (se
funcionário tampouco definisse um __init__, então seria usado o de Pessoa, e se
pessoa tampouco o fizesse, seria usado o de `object`, que é a classe base do Python
usada automaticamente para todos as classes que criamos).

Caso você queira ou precise adicionar atributos extras na classe Programador
(ou qualquer outra classe filha de Funcionário), defina o método construtor,
faça a utilização do super e adicione os atributos extra que serão específicos
daquela classe, sejam eles recebidos por parâmetros ou não.

Lembrando sempre que o enunciado define quais são os parâmetros obrigatórios
de uma classe, então se forem criados parâmetros obrigatórios extras, isso
irá gerar erros nos testes de correção.
'''


class Programador(Funcionario):
    '''
    Funcionário do tipo Programador:
    - salario base por hora 35.00;
    - regime de trabalho entre 20h e 40h semanais, caso contrário levanta um ValueError;
    - cálculo do sálario mensal: calcule o pagamento semanal através do número de horas
      trabalhadas na semana e o sálario base (por hora) e considere que o mês
      possui sempre 4.5 semanas.
    '''
    
    def __init__(self, nome, idade, email, carga_horaria):
        super().__init__(nome, idade, email, carga_horaria)
        self.__salario_hora = 35.00
        self.__semanas_mes = 4.5
        self.__salario = 0

    def calcula_salario(self):
        self.__salario = self.__carga_horaria*self.__salario_hora*self.__semanas_mes
        return self.__salario
 
    @property
    def carga_horaria(self):
        return self.__carga_horaria

    @carga_horaria.setter
    def carga_horaria(self, nova_carga_horaria):
        if nova_carga_horaria >= 20 and nova_carga_horaria <= 40:
          self.__carga_horaria = nova_carga_horaria
        else:
          raise ValueError

    def aumenta_salario(self):
        novo_salario_hora = self.__salario_hora + (self.__salario_hora*0.05)
        self.__salario_hora = novo_salario_hora




class Estagiario(Funcionario):
    '''
    Funcionário do tipo Estagiario:
    - salario base por hora 15.50;
    - auxilio alimentação fixo de 250 reais por mês;
    - regime de trabalho deve estar entre 16h e 30h semanais, caso contrário levanta um ValueError;
    - cálculo do sálario mensal: calcule o pagamento semanal através do número de horas
      trabalhadas na semana e o sálario base (por hora) e considere que o mês
      possui sempre 4.5 semanas, e por fim calcule e adicione os auxílios.
    '''
    def __init__(self, nome, idade, email, carga_horaria):
      super().__init__(nome, idade, email, carga_horaria)
      self.__salario_hora = 15.50
      self.__auxilio_alimentacao = 250.00
      self.__semanas_mes = 4.5
      self.__salario = 0

    @property
    def carga_horaria(self):
      return self.__carga_horaria
    
    def calcula_salario(self):
      self.__salario = (self.__carga_horaria*self.__salario_hora*self.__semanas_mes) + self.__auxilio_alimentacao
      return self.__salario 
    
    @carga_horaria.setter
    def carga_horaria(self, nova_carga_horaria):
      if nova_carga_horaria >= 16 and nova_carga_horaria <= 30:
        self.__carga_horaria = nova_carga_horaria
      else:
        raise ValueError

    def aumenta_salario(self):
      novo_salario_hora = self.__salario_hora + (self.__salario_hora*0.05)
      self.__salario_hora = novo_salario_hora

  


class Vendedor(Funcionario):
    '''
    Funcionário do tipo Vendedor:
    - salario base por hora 30.00;
    - auxilio alimentação fixo de 350 reais por mês;
    - auxilio transporte de 30 reais por visita realizada ao cliente;
    - regime de trabalho deve estar entre 15h e 45h semanais, caso contrário
      levanta um ValueError;
    - possui um atributo privado que guarda o número de visitas realizadas no mês,
      começando sempre em zero;
    - cálculo do sálario mensal: calcule o pagamento semanal através do número de horas
      trabalhadas na semana e o sálario base (por hora) e considere que o mês
      possui sempre 4.5 semanas, e por fim calcule e adicione os auxílios;
    - além dos métodos de Funcionário, deve implementar os métodos:
      * realizar_visita; e
      * zerar_visitas.
    '''
    def __init__(self, nome, idade, email, carga_horaria):
         super().__init__(nome, idade, email, carga_horaria)
         self.__salario_hora = 30.00
         self.__auxilio_alimentacao = 350.00
         self.__auxilio_transporte = 30.00
         self.__n_visitas = 0
         self.__semanas_mes = 4.5
         self.__salario = 0

    @property
    def carga_horaria(self):
      return self.__carga_horaria

    @carga_horaria.setter
    def carga_horaria(self, nova_carga_horaria):
      if nova_carga_horaria >= 15 and nova_carga_horaria <= 45:
        self.__carga_horaria = nova_carga_horaria
      else:
        raise ValueError

    
    @property
    def visitas(self):
        """
        Retorna o número de visitas realizadas pelo vendedor até o momento
        """
        return self.__n_visitas
        

    def realizar_visita(self, n_visitas):
        '''
        Recebe um número inteiro e incrementa o número de visitas realizadas no mês
        com o valor recebido. Antes de fazer a alteração, verifique:
        * se n_visitas é um número inteiro e levante um TypeError caso contrário;
        * se n_visitas é positivo e maior que zero, levantando um ValueError caso contrário.

        - Este método não possui retorno;
        '''
        if type(n_visitas) != int:
            raise TypeError
        elif n_visitas <= 0:
            raise ValueError
        else:
            self.__n_visitas = self.__n_visitas + n_visitas

    def calcula_salario(self):
      self.__salario = (self.__carga_horaria*self.__salario_hora*self.__semanas_mes) + self.__auxilio_alimentacao + (self.__auxilio_transporte*self.__n_visitas)
      return self.__salario
 

    def zerar_visitas(self):
        '''
        Quando chamado deve redefinir o número de visitas realizadas pelo vendedor para zero,
        de modo a começar a contagem para o mês seguinte.
        - Este método não possui retorno;
        '''
        self.__n_visitas = 0

    def aumenta_salario(self):
      novo_salario_hora = self.__salario_hora + (self.__salario_hora*0.05)
      self.__salario_hora = novo_salario_hora

     