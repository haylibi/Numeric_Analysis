#Trabalho 4
from math import *
import time

def I_r(eps):
    start = time.time()
    a = float(input('Extremo esquerdo (a): '))
    b = float(input('Extremo direito (b): '))
    maxi = float(input('Maximo da derivada em [a,b]: '))
    n = int(((b-a)**2)/(2*eps)*maxi)+1
    soma = 0
    print('n =',n)
    for i in range(n):
        soma += (f(a+i*abs((a-b))/n)*(abs(a-b)/n))
    print('Integral =',soma,'Tempo de execucao:',time.time()-start)
    
def f(x):
    return cos(x)**30/(sin(x)**30+cos(x)**30)


def I_s(a,b):           #Justificar que o calculo do integral na regra de simpson para n, calcula para 2n pontos.
    par = 0
    impar = 0
    for k in range(20):
        I = 0
        par += impar
        impar = 0
        n = 2**k
        h = abs(b-a)/(2*n)
        for j in range(n):
            impar += f((a+h)+2*h*j)
        I += f(a)+ f(b) + 4*impar + 2*par
        print('k =', k, 'Integral =', h*I/3, '|I-In| =', abs(Valor_Integral-h*I/3))

Valor_Integral = 0.785398138155361


def I(a,b):
    for k in range(20):
        I = 0
        par = 0
        impar = 0
        n = 2**k
        h = abs(b-a)/(2*n)
        for i in range(1,2*n):
            if i%2 == 1:
                impar+=f(a+i*h)
            else:
                par += f(a+i*h)
        I = f(a) + f(b) + 4*impar+2*par
        print('k =', k, 'Integral =', h*I/3, '|I-In| =', abs(Valor_Integral-h*I/3))
        
        
