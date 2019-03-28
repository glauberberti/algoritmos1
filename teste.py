# #Faça um Programa que mostre a mensagem "Alô mundo!" na tela
# print ("alô mundo")
# # Faça um Programa que peça para o usuário digitar o nome dele e depois o sobrenome (um input para o nome e outro para o sobrenome). Apresente na tela uma mensagem de boas vindas com o nome e sobrenome do usuário.
#
# nome= input("digite seu nome ");sobrenome= input("digite seu sobrenome ")
# print("olá,",nome,sobrenome,",seja bem vindo")
# # Faça um Programa que peça um número para o usuário e então mostre a mensagem “O número informado foi X”, onde X é o número digitado.
#
# numero1= input ("digite um numero ")
# numero1= int(numero1)
# print("o numero digitado foi = ", numero1)
# # Faça um Programa que peça um número e apresente na tela o antecessor e o sucessor dele
# print("o numero antecessor é= ", numero1-1)
# print("o numero sucessor é= ",numero1+1)
# # Faça um Programa que peça dois números e imprima a soma deles.
# num2= input("Digite um numero= ")
# num2= int(num2)
# num3= input("Digite outro numero= ")
# num3= int(num3)
# print("a soma destes numeros é = ",num2+ num3)
# # Faça um Programa que peça três números e imprima o produto (multiplicação) deles.
# num4= input("digite um terceiro numero= ")
# num4= int(num4)
# print("a multiplicação destes 3 numeros é= ",num2*num3*num4)
# Faça um Programa que peça as 4 notas bimestrais e mostre a média aritmética.
# print("agora vamos calcular sua media bimestral anual, na materia de algoritimos")
# nota1= input("digite a nota do 1 bimestre=")
# nota2= input("digite a nota do 2 bimestre=")
# nota3= input("digite a nota do 3 bimestre=")
# nota4= input("digite a nota do 4 bimestre=")
# nota1= float(nota1)
# nota2= float(nota2)
# nota3= float(nota3)
# nota4= float(nota4)
# soma100= nota1+ nota2+ nota3+ nota4
# soma100= float(soma100)
# nota6= soma100/4
# nota6= float(nota6)
# print("o resultado, sendo a sua media bimestral: ",nota6)
# # Faça um Programa que converta metros para centímetros
# print("vamos converter metros para centímetros")
# medida1= input("selecione qual a metragem a ser conververtida, apenas numeros= ")
# medida1= int(medida1)
# print("o resultado é= ",medida1*100)
# # Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
# print("calcularemos neste exemplo o raio de um circulo")
# raio1= input("""digite quantos metros possuio raio,separe a matragem por ponto
# exemplo(0.00)= """)
# raio1= float(raio1)
# pi= 3.14
# print("o resultado do raio mencionado foi: ",3.14*(raio1* raio1))
# #Faça um Programa que peça a medida do lado de um quadrado, calcule e mostre sua área. Em seguida, mostre o dobro desta área para o usuário.
# alt= input("Digite a altura do quadrado em metros ")
# larg= input("Digite a largura do quadrado em metros ")
# alt= float(alt)
# larg= float(larg)
# print("a area do quadrado é= ",alt*larg, "m²")
# a=alt*larg
# a= float(a)
# print("o dobro desta area é= ",a*2,"m²")
# #(Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no dia.
# #Calcule e mostre quanto você ganhou no dia e o total do seu salário em um mês.)
# print("""vamos calcular seu salario diario e mensal""")
# ganhoHora=input("digite quanto você ganha por hora trabalhada= ")
# trabalhoHora= input("digite quantas horas por dia você trabalha= ")
# ganhoHora=float(ganhoHora)
# trabalhoHora=float(trabalhoHora)
# print("por dia você ganha=",ganhoHora*trabalhoHora, "reais.")
# ganhoDia= ganhoHora*trabalhoHora
# ganhoDia=float(ganhoDia)
# print("seu salario mensal é=",ganhoDia*30,"reais.")
# #Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.
# print("vamos tranformar graus Farenheit em graus Celsius")
# farenheit=input("digite graus Farenheit a serem transformados= ")
# farenheit=float(farenheit)
# vt=farenheit-32
# vt=float(vt)
# print("resultado ",vt*5/9,"graus C.")
#
# print("vamos tranformar graus Celsius em graus Farenheit")
# celsius=input("digite graus Celsius a serem transformados= ")
# celsius=float(celsius)
# vt2=celsius*9/5
# vt2=float(vt2)
# print("resultado ",vt2+32,"graus F.")
#
# #Tendo como dados de entrada a altura e peso de uma pessoa, construa um algoritmo que calcule seu IMC, usando a seguinte fórmula: imc = peso ÷ altura²
# print("vamos calcular imc(indice de massa corporal)")
# alt= input("mencione sua altura, ex(00.00)")
# peso= input("mecione seu peso, ex(00.00)")
# alt=float(alt)
# peso=float(peso)
# print("resultado do imc= ", peso/(alt*alt))
#
# #Dada a equação: ax2+bx+c=0peça para o usuário informar o valor de a, b e c e calcule
# # nao sei fazer##
#
# #Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em
# #metros quadrados da área a ser pintada. Considere que a cobertura da tinta é
# #de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de
# #18 litros, que custam R$ 80,00. O programa deve informar ao usuário a
# #quantidades de latas de tinta a serem compradas e o preço total.
# import math
# print(
# """vamos calcular quantos litros de tinta serão gastos para pintar uma area total""")
# m=input("quantos metros2 serao pintados= ")
# m=float(m)
# m2=m*m
# m2=float(m2)
# m2t=m2
# litros=m2t/3
# litros=int(litros)
# print("""o custo medio de 18l de tinta sao de 80.00 reais, no qual será usado
# como base neste exemplo:""")
# preco=80.0
# capacidade=18.0
# preco=float(preco)
# capacidade=float(capacidade)
# litros=math.ceil(litros)
# latas=litros/capacidade
# latas= math.ceil (latas)
# print("o total de latas que precisam ser compradas:",latas)
# total= latas*preco
# total=(total)
# print("o total em reais:",total)
#
# #Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo
# #que calcule seu peso ideal, utilizando as seguintes fórmulas:
# #Para homens: (72.7*h) - 58
# #Para mulheres: (62.1*h) - 44.7
# print("Calculando peso ideal.")
# sexo= input("informe seu sexo, sendo M (masculino) ou F (feminino)")
# masculino= m
# feminino= f
# if f: input("Digite sua altura ex:1.60")
# elif m:input("Digite sua altura ex:1.80")
#
# # Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
#
# n1 = int(input('insira um numero sendo positivo ou negativo: '))
#
# if (n1 < 0):
#     print ('O numero é negativo')
# else:
#     print ('O numero é positivo')
#
# # print ('_______________________________________________________________________')
# # Faça um Programa que peça dois números e imprima o maior deles.
# n1 = int(input("insira um numero: "))
# n2 = int(input("insira outro numero: "))
# if (n1>n2):
#     print ('este numero é maior',n1)
# else:
#     print ('este numero é menor',n2)
# # print ('_______________________________________________________________________')
# Faça um programa que peça um valor e informe na tela se o número é par ou ímpar.
# n1 = int(input("insira um numero: "))
#
# if (n1 %2):
#     print ('este numero é impar')
# else:
#     print ('este numero é par')
# # print ('_______________________________________________________________________')
#
# Faça um Programa que peça um número e informe se este número é múltiplo de 3
# teste
# n1= input("Insira um numero para multiplicarmos ele por (3): ")
# n1= int(n1)
# n2= n1**3
# print("resultado",n2)
# # print ('_______________________________________________________________________')
#
# numero =int(input('Digite um inteiro: '))
# if not (numero%3) :
#     print("É múltiplo de 3")
# else:
#     print("Não é múltiplo de 3")
#
# # print ('_______________________________________________________________________')
# #Faça um programa que peça dois números e informe se o primeiro é múltiplo do segundo.
# n1 = int(input("insira um numero: "))
# n2 = int(input("insira outro numero: "))
# if (n1>n2):
#     print ('o primeiro numero é multiplo',n2)
# else:
#     print ('o primeiro numero não é multiplo',n2)
# # print ('_______________________________________________________________________')
# # Faça um Programa que verifique o sexo de uma pessoa. O usuário deve informar ‘F’ ou ‘M’ e o programa deve escrever “Feminino” ou “Masculino”, conforme a letra digitada.
#
# sexo =(input('Insira f(feminino) ou m(masculino)'))
# sexo= sexo.upper()
# if (sexo == 'f' ):
#     print ('feminino')
# else:
#     print ('masculino')
# # print ('_______________________________________________________________________')
#
# Faça um algoritmo que leia os valores A, B, C e imprima na tela se a soma de A + B é maior que C.
#
# a= input("Dê um valor para a letra A: ")
# b= input("Dê um valor para a letra B: ")
# c= input("Dê um valor para a letra C: ")
# a= int(a)
# b=int(b)
# d= a+b
# c=int(c)
# d= int(d)
# print ("a soma de a+b é :",d)
# if (d>c):
#  print("a soma de a+b é maior que c")
# else:
#     print("a soma de a+b é menor que c")
# print ('_______________________________________________________________________')
# # Faça um algoritmo que peça um número e se ele for par some 5, se não, some 8.
# n1= int(input("digite um numero?"))
#
# if(n1 %2):
#         print("o numero informado é impar,",n1, "somando +8 o resultado é:",n1+8)
# else:
#         print("o numero informado é par",n1," somando +5 o resultado é: ",n1+5)
#
#
# #Crie um programa que peça uma nota de trabalho e uma de prova (as duas de 0 a 100).
# #Se a média aritmética das notas for maior ou igual a 60, escreva “Aprovado”, se não, “Reprovado”.
# trab=input("Digite a nota do seu trabalho(de 0 a 100): ")
# prova= input("Digite a nota da sua prova (de 0 a 100): ")
# trab= int(trab)
# prova= int(prova)
# ano= trab + prova
# ano= int(ano)
# res=ano/2
# print("média",res)
# res=int(res)
# if int(res >= 60):
#     print("aprovado")
# else:
#     print("reprovado")
# # print ('_______________________________________________________________________')
#
# # exemplo aprendendo utilisar elif ( ):
# id = input (" Digite sua idade: ")
# id = int(id)
# if(id<0):
#     print ("Idade Inválida!")
# elif (id<3):
#     print("Bebê!")
# elif(id <= 12):
#     print ("Criança!")
# elif(id < 18):
#     print ("Adolescente!")
# elif(id <60):
#     print ("Adulto!")
# else:
#     print ("Melhor idade!")
#
# # Exemplo condicao print
# print ("Cadastro de alunos: ")
# print("1 -Cadastrar")
# print("2 - Alterar")
# print("3 - Excluir")
# print("4 - Consultar")
# print("5 - Imprimir Relatório")
# n= input("digite o número da sua opção: ")
# n= int(n)
# if(n ==1 ):
#     print("Opção Cadastrar")
# if(n ==2 ):
#     print("Opção Alterar")
# if(n ==3 ):
#     print("Opção Excluir")
# if(n ==4 ):
#     print("Opção Consultar")
# if(n ==5 ):
#     print("Opção Imprimir Relatorio")
# else:
#     print("Comando Invalido")
#
# # Construa um programa que recebe três valores, A, B e C. Em seguida, apresente na tela somente o maior deles.
#
# a= input("Dê um valor para a letra A: ")
# b= input("Dê um valor para a letra B: ")
# c= input("Dê um valor para a letra C: ")
# a=int(a)
# b=int(b)
# c=int(c)
#
# if(a> b and a>c ):
#     print ("Valor A é o maior numero")
# elif (b> a and b>c):
#     print("Valor B é o maior numero")
# elif (c> a and c>b):
#     print ("Valor C é o maior numero")
#
# # Construa um programa que recebe três valores, A, B e C. Em seguida, apresente na tela os números em ordem crescente.
# a= input("Dê um valor para a letra A: ")
# b= input("Dê um valor para a letra B: ")
# c= input("Dê um valor para a letra C: ")
# a=int(a)
# b=int(b)
# c=int(c)
#
# if (a > b and a>c and b>c):
#     print('é o maior numero!!',a,b,c)
# elif (b> a and b>c and a>c):
#     print('é o maior numero!!',b,a,c)
# elif (c> b and c>a and b>a):
#     print('é o maior numero!!',c,b,a)
#
# elif (b>c and b>a and c>a ):
#     print('é o maior numero!!',b,c,a)
# elif(a>c and a>b and c>b):
#     print('é o maior numero!!',a,c,b)
# else:
#     print('é o maior numero!!',c,a,b)
#
#
# Em se tratando de linguagens de programação, o que é uma variável?
# R :Variavel é quando algum algoritmo informado pode sofrer alteraçao em um certo momento.

# Na linguagem Python, como é a declaração de uma variável?
# R: A declaracao de variavel  sao guardadas na memoria dos dispositivos, onde dentro da memoria possui varios locais para alocar dados/variaveis tendo que ser identificadas

# Na linguagem Python, quais são as regras para se nomear variáveis?
# R: o comando de atribuicao cria novas variaveis e da a elas valores, uma cria a string, outra da o valor inteir e a ultima um ponto flutuante( string, float, integer)

# As variáveis geralmente possuem um tipo de dado. O que é um tipo de dado? Na linguagem Python, quais são os tipos de dados mais comuns?
# R: os tipos de dados mais comuns sao caracteres e numericos que sao definidos para armazenar algum tipo de valor

# # Nas linguagens de programação, utilizamos um conjunto de operadores aritméticos. Utilizando a linguagem Python, quais são os principais operadores aritméticos?
# R: os principais operadores são a soma, subtração, divisao, multiplicaçao.
#
# # Em Python, caso tenhamos o código x = 4 ** 3, qual será o valor de x?
# R: x=64
#
# # Em Python, caso tenhamos o código x = 120 / 3, qual será o valor de x?
# R: x=40
# # Em Python, caso tenhamos o código x = 75 % 8, qual será o valor de x?
# R; 75/8 = 9(// resultado),… x=3(resto)
#
# 9 Em Python, a biblioteca math pode ser utilizada para efetuarmos cálculos matemáticos. Diversas funções matemáticas se tornam disponíveis para uso em seu programa. Com relação à biblioteca math:
#  Qual instrução deve ser utilizada no início do seu programa para que as funções da biblioteca math estejam disponíveis para uso em seu código?
#
# R:Import.match
#
#  Qual o código necessário para se apresentar na tela o resultado de raiz4?
# R: x=4**(1/2)
#
#  Qual o código necessário para, tendo-se x=14.8, atribuir à variável z o valor de x arredondado para baixo?
# R: math.floor
#  Qual o código necessário para, tendo-se x=14.8, atribuir à variável z o valor de x arredondado para cima?
# R: math.ceil
# #Qual o código necessário para, tendo-se x=14.8, atribuir à variável z o valor de x truncado (obter apenas a parte inteira de x)?
# R: math.trunc
#  Qual o código necessário para atribuir à variável x o valor 5³?
# R: math.5**3

# Implemente um programa que seja capaz de calcular e apresentar ao usuário a área de um círculo. Sabe-se que para calcular a área de um círculo utiliza-se
# a fórmula A=R2onde A é a área do círculo e R é o raio. Solicite ao usuário pelos dados necessários. Utilize a biblioteca matemática para se obter o valor exato de pi

# import math
# r=float(input("digite o raio:"))
# a=math.pi*(r*r)
# print("resultado",a)


# Nas linguagens de programação, utilizamos um conjunto de operadores relacionais. Utilizando a linguagem Python, quais são os principais operadores relacionais?
# Para que servem os operadores relacionais? Qual o resultado de uma expressão relacional?

# Descrição	Operador
# Maior que	>
# Menor que	<
# Igual a	==
# Maior ou igual a	>=
# Menor ou igual a	<=
 #  os ooperadores relacionais  são utilizados para comparar valores, o resultado de uma expressão e o resultado de uma expressao é um valor booleano(v ou f)


# Sabe-se que as variáveis x=10, y=20 e z=30. Desenvolva um algoritmo que, atribuindo-se os valores às variáveis, consiga realizar a troca dos valores, de forma que x receba o valor de
 # z, y receba o valor de x e z receba o valor de y. Apresente ao usuário os valores de x, y e z antes da troca e depois da troca.
# 
# print("")
# x=int(10)
# y=int(20)
# z=int(30)
# print("Apresentemos x=10, y=20, z=30")
#
# a=x
# b=y
# c=z
#
# x=b
# y=c
# z=a
# print("z",x)
# print("x",y)
# print("y",z)


# Implemente um programa que solicite ao usuário pelo dia, mês e ano no formato ddmmaa e apresente na tela o dia informado, o mês informado e o ano informado. Exemplo:
# data=100219. Dia: 10, Mês: 02 e Ano:19. Para o cálculo, utilize apenas os operadores / e %, convertendo os resultados sempre para inteiro).
