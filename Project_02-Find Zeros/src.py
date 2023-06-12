from math import *
#Exercicio 1
def F(x):
    '''funcao dada'''
    return sin(10*x)-x-0.1
def dfdx(x):
    '''Derivada da funcao dada'''
    return 10*cos(10*x)-1
def suc1(n,x0):
    '''n-esimo termo da sucessao que obtemos executando o metodo de newton comecando com o valor "x0"'''
    x = x0
    for i in range(n):
        x = -F(x)/dfdx(x)+x
    return x

def Ex1():
    x0 = float(input('Por favor indique qual o valor inicial de x para aplicar o processo de newton: '))
    epsilon = input('Indique o erro que pretende estimar a sua solucao: ').split('*')
    if epsilon[0]=='10':
        epsilon = float(int(epsilon[0])**int(epsilon[2]))
    else:
        epsilon = float(int(epsilon[0])*10**int((epsilon[3])))
    count = 0
    erro = abs(x0-(-F(x0)/dfdx(x0)+x0))
    while erro>epsilon:
        x0 = suc1(1,x0)
        erro = abs(x0-(-F(x0)/dfdx(x0)+x0))
        count+=1
    print('Foram precisas %d iteracoes e o valor obtido foi'% (count),x0, "erro absoluto estimado: ",erro)

#Exercicio 2

def f(x):
    return sin(10*x)-0.1
def Ex2():
    x0 = float(input('Por favor indique o valor inicial de x0 para aplicar o metodo iterativo simples de aproximacao: '))
    epsilon = input('Indique o erro que pretende estimar a sua solucao: ')
    epsilon = epsilon.split('*')
    if epsilon[0]=='10':
        epsilon = float(int(epsilon[0])**int(epsilon[2]))
    else:
        epsilon = float(int(epsilon[0])*10**int((epsilon[3])))
    n = 0
    x1 = f(x0)
    erro = abs(x1-x0)
    while erro > epsilon and n<=500000:
        x0 = x1
        x1 = f(x0)
        erro = abs(x1-x0)
        n+=1
    if n >= 500000:
        print("Iteracoes: %d\nErro: %f\nXn =" % (n,erro),x1)
        return('Numero de iteracoes excedido')
    print('Foram precisas %d iteracoes e o valor obtido foi' %(n),x0,"erro absoluto:",erro)
