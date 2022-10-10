def ex1():
    Dx={"Salgado":4.5,"Lanche":6.50,"Suco":3.00,"Refrigerante":3.50,"Doce":1.00}
    print(Dx)

ex1()

def ex2():
    Dx={"João":4.5,"Carlos":6.50,"Matheus":7.00,"Roberta":10.00,"Gabriel":3.40}
    notas = sum(Dx.values())
    numeroAlunos = float(len(Dx.keys()))
    print(notas/numeroAlunos)

ex2()