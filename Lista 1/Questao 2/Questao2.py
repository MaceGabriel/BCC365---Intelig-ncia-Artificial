import numpy as np
import math

nums = [i for i in range(1,1001)]
sentence = "Practice Problems to Drill List Comprehension in Your Head."

# def a():
#     div8 = [numero for numero in nums if numero%8 == 0]

#     print("Questao 2.a: ",div8)
#     print(" ")
# a()

# def b():
#     num6 = [numero for numero in nums if numero%8 == 0]

#     print("Questao 2.b: ", num6)
#     print(" ")
# b()

def c():   
    espacBranco = [1 for espaco in sentence if espaco == ' ']

    print("Questao 2.c: ", len(espacBranco))
    print(" ")
c()

def d():
   
    semVogais = [(palavras) for palavras in sentence if palavras != 'a' if palavras != 'e' if palavras != 'i' if palavras != 'o' if palavras!= 'u']

    print("Questao 2.d: ", semVogais)
    print(" ")
d()