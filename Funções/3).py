def Credito(Valor):
    Valor = Valor*2
    return Valor

def Debito(Valor):
    Valor = Valor/10
    return Valor    

ValorFinanceiro = 10
print(Credito(ValorFinanceiro))
print(Debito(ValorFinanceiro))