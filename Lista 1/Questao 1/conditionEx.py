n1 = float(input("Nota 1 do aluno: "))
n2 = float(input("Nota 2 do aluno: "))

media = (n1+n2)/2

# if media >= 6:
#     print("Aprovado")

# else:
#     print("Reprovado")

if media > 6:
    print("Aprovado")

elif media >= 4:
    print("Exame")

else:
    print("Reprovado")  

