def ex1():
    L = [5,7,2,9,4,1,3]
    print("Tamanho da lista: " + str(len(L)))  
    print("Maior valor da lista: " + str(max(L)))
    print("Menor valor da lista: " + str(min(L)))
    print("Soma dos elementos da lista: " + str(sum(L)))
    L.sort()   
    print("Lista em ordem crescente: " + str(L))
    L.reverse()
    print("Lista em ordem decrescente: " + str(L))

ex1()
    
def ex2():
    L = list(range(3,50,3))
    print(L)

ex2()