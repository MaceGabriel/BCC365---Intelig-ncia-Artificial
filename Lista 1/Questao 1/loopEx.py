def ex1():
    x = 0
    for i in range(3,334,3):
        x+=i
    print("Valor total da soma",x)

ex1()

# def ex2(notas):
#     #nota = 0
#     soma = 0
#     for i in range(notas):
#         soma += float(input("Nota " + str(i+1)+ " :"))

#     print("Media das notas",soma/notas)

# ex2(10)

def ex3():

    numero = -1
    while numero>10 or numero<1:
        numero = int(input("Digite um numero de 1 a 10: "))
    
    for i in range(1,11,1):
        print("%2d x %2d = %3d" %(i,numero,i*numero))
    

ex3()