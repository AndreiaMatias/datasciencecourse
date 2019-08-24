
# coding: utf-8

# # <font color='blue'>Data Science Academy - Python Fundamentos - Capítulo 3</font>
# 
# ## Download: http://github.com/dsacademybr

# ## Exercícios - Loops e Condiconais

# In[2]:


# Exercício 1 - Crie uma estrutura que pergunte ao usuário qual o dia da semana. Se o dia for igual a Domingo ou 
# igual a sábado, imprima na tela "Hoje é dia de descanso", caso contrário imprima na tela "Você precisa trabalhar!"
Dia_semana = input("Qual o dia da semana?")
if (Dia_semana == "Domingo") or (Dia_semana =="sábado"):
    print("Dia de descanso")
else:
    print("Você precisa trabalhar")


# In[6]:


# Exercício 2 - Crie uma lista de 5 frutas e verifique se a fruta 'Morango' faz parte da lista
morango="não"
frutas=["banana", "morango", "maçã", "pera", "uva"]
for fruta in frutas:
    if fruta=="morango":
        morango="sim"
if morango =="sim":
    print("Morango está na lista")
else:
    print("Morango não está na lista")
        


# In[7]:


# Exercício 3 - Crie uma tupla de 4 elementos, multiplique cada elemento da tupla por 2 e guarde os resultados em uma 
# lista
lista=[]
num = (1,2,3,4)
for numero in num:
    lista.append(numero*2)
print(lista)


# In[8]:


# Exercício 4 - Crie uma sequência de números pares entre 100 e 150 e imprima na tela

for i in range(100,150,2):
    print(i)


# In[9]:


# Exercício 5 - Crie uma variável chamada temperatura e atribua o valor 40. Enquanto temperatura for maior que 35, 
# imprima as temperaturas na tela
temperatura = 40
while (temperatura >35):
    print(temperatura)
    temperatura -=1


# In[11]:


# Exercício 6 - Crie uma variável chamada contador = 0. Enquanto counter for menor que 100, imprima os valores na tela,
# mas quando for encontrado o valor 23, interrompa a execução do programa
contador = 0

while contador<100:
    print(contador)
    contador +=1
    if (contador==23):
        break


# In[24]:


# Exercício 7 - Crie uma lista vazia e uma variável com valor 4. Enquanto o valor da variável for menor ou igual a 20, 
# adicione à lista, apenas os valores pares e imprima a lista
lista=[]
num=4
while (num<=20):
    if(num%2==0):
        lista.append(num)
    num +=1
print(lista)


# In[26]:


# Exercício 8 - Transforme o resultado desta função range em uma lista: range(5, 45, 2)
lista=[]
nums = range(5, 45, 2)
for i in nums:
    lista.append(i)
    
print(lista)


# In[28]:


# Exercício 9 - Faça a correção dos erros no código abaixo e execute o programa. Dica: são 3 erros.
temperatura = float(input('Qual a temperatura? '))
if temperatura > 30:
    print('Vista roupas leves.')
else:
    print('Busque seus casacos.')


# In[31]:


# Exercício 10 - Faça um programa que conte quantas vezes a letra "r" aparece na frase abaixo. Use um placeholder na 
# sua instrução de impressão

# “É melhor, muito melhor, contentar-se com a realidade; se ela não é tão brilhante como os sonhos, tem pelo menos a 
# vantagem de existir.” (Machado de Assis)

frase = "É melhor, muito melhor, contentar-se com a realidade; se ela não é tão brilhante como os sonhos, tem pelo menos a vantagem de existir." 
contador = 0
for caracter in frase:
    if caracter =='r':
        contador +=1
print("A letra 'r' aparecer {} vezes".format(contador))
        


# # Fim

# ### Obrigado - Data Science Academy - <a href="http://facebook.com/dsacademybr">facebook.com/dsacademybr</a>
