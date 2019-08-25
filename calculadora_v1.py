# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

print("\n******************* Python Calculator *******************")

print("\nSelecione o número da opção desejada: ")

print("\n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão")

#Solicita os números que serão calculados
opcao = int(input("\nDigite sua opção (1, 2, 3, 4):"))
n1=float(input("\nInforme o primeiro número: "))
n2=float(input("\nInforme o segundo número:"))

if (opcao==1):
    soma = n1 + n2
    print("{} + {} ={}".format(n1,n2,soma))
Elif (opcao==2):
    subtracao = n1 - n2
    print("{} - {} ={}".format(n1,n2,subtracao))
Elif (opcao==3):
    multiplicacao = n1 * n2
    print("{} X {} ={}".format(n1,n2,multiplicacao))
Elif (opcao==4):
    divisao = n1 / n2
    print("{} / {} ={}".format(n1,n2,divisao))
Else:
    print("Você digitou a opção incorreta")