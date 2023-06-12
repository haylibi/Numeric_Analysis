#Trabalho 3
#def coef(ab,od):
#    k=od
#    for j in range(1,len(ab)):
#        for i in range(len(ab)-1,j-1,-1):
#            k[i] = (float(k[i])-float(k[i-1]))/(float(ab[i])-float(ab[i-j]))
#    return k
#x = symbols('x')
#def poli1(ab,od):
#    l=coef(ab,od)
#    p=0
#    for i in range(len(ab)):
#        adic = 1
#        for j in range(i):
#            adic *= (x-ab[j])
#        p += (l[i]*adic)
#    return horner(p)

#def difdiv(XL,YL):
#    if len(XL) == 2:
#        return (YL[1]-YL[0])/(XL[1]-XL[0])
#    else:
#        return (difdiv(XL[1:],YL[1:])-difdiv(XL[:-1],YL[:-1]))/(XL[-1]-XL[0])


#def poli(XL,YL):
#    K = ''
#    if len(XL) == 2:
#        return (''.join([str(YL[0]),'+(x-',str(XL[0]),')*',str(difdiv(XL,YL))]))
#    else:
#        for i in range(len(XL)):
#            K+= '(x-'+str(XL[i])+')*'
#        K = K[:-1]
#        return (''.join([str(poli(XL[:-1],YL[:-1])),'+',K,'*',str(difdiv(XL,YL))]))
    
#def poli(XL,YL,x):
#    K = 1
#    if len(XL) == 2:
#        return YL[0]+(x-XL[0])*difdiv(XL,YL)
#    else:
#        for i in range(len(XL)):
#            K*= x-XL[i]
#        return (poli(XL[:-1],YL[:-1],x)+ K*difdiv(XL,YL))


#METODO LAGRANGE
import numpy as np
import sympy as sp
import math

x = sp.symbols('x')

def lagrange(X,Y):
    L=[]
    pol = []
    for i in range(len(X)):
        p = ''
        d = ''
        for j in range(len(X)):
            if i != j:
                p += '(x-'+str(X[j])+')*'
                d += '('+str(X[i])+'-'+str(X[j])+')*'
        p = p[:-1]
        d = d[:-1]
        L.append(p+'/('+d+')')
    for i in range(len(L)):
        pol += L[i]+'*'+str(Y[i])+'+'
    return ''.join(pol[:-1])
            
#def lagrange(X,Y):
#    x = sp.symbols('x')
#    L=0
#    for i in range(len(X)):
#        p = 1
#        d = 1
#        for j in range(len(X)):
#            if i != j:
#                p*= x-X[j]
#                d *=X[i]-X[j]
#        L+=Y[i]*p/d
#    return L                            #Explicar que ha erros no polinomio devido as divisoes que o computador faz


def h(L,i):
    return L[i]-L[i-1]

#def spline(XL,YL):
#    x = sp.symbols('x')
#    S = []
#    M = {0:sp.symbols(chr(0)),len(XL)-1:sp.symbols(chr(len(XL)))}
#    hi = h(XL,1)
#    for i in range(1,len(XL)-1):
#        hi1 = h(XL,i+1)
#        M[i] = hi/6*sp.symbols(chr(i-1)) + sp.symbols(chr(i))*(hi+hi1)/3+sp.symbols(chr(i+1))*hi1/6-(YL[i+1]-YL[i])/hi1+(YL[i]-YL[i-1])/hi
#        hi = hi1
#    Lista = []
#    for i in range(len(M)):
#        Lista.append(M[i])
#    print(M)
#    print(sp.solve(Lista,[sp.symbols(chr(i)) for i in range(len(XL))]))

def spline(XL,YL):
    x = sp.symbols('x')
    MM = [[1]+(len(XL)-1)*[0]]
    Lista = [0]
    hi = h(XL,1)
    for i in range(1,len(XL)-1):
        MM.append([])
        Lista.append([])
        hi1 = h(XL,i+1)
        MM[-1] = ((i-1)*[0] + [hi/6,(hi+hi1)/3,hi1/6] + (len(XL)-i-2)*[0])
        Lista[-1] = ((YL[i+1]-YL[i])/hi1)-((YL[i]-YL[i-1])/hi)
        hi = hi1
    MM.append([])
    MM[-1] = (len(XL)-1)*[0]+[1]
    Lista += [0]
    M1 = np.matrix(MM)
    M2 = np.matrix(Lista)
    M = (np.linalg.solve(M1,np.transpose(M2)))
    S = []
    for i in range(1,len(XL)):
        hi = XL[i]-XL[i-1]
        c = YL[i-1]-(M[i-1]*(hi**2))/6
        d = YL[i]-(M[i]*(hi**2)/6)
        S.append([])
        S[-1] = (M[i-1]*(XL[i]-x)**3)/(6*hi) + (M[i]*(x-XL[i-1])**3)/(6*hi) + c*(XL[i]-x)/hi + (d*(x-XL[i-1]))/hi
    #for i in range(len(S)):
    #    print('S%d =' % (i+1),sp.horner(S[i]))
    return S
    
    
def S(K,LX,LY):
    SL = spline(LX,LY)
    for i in range(len(XL)-1):
        if LX[i]<=K<=LX[i+1]:
            return SL[i].subs(x,K)
#Exercicio 2)b)
def f(x):
    return 4*x**2+math.sin(9*x)

lista = [-1,-0.75,-0.5,-0.25,0,0.25,0.5,0.75,1]
for i in lista:
    print(i,f(i))
    
XL = [0,1,2,2.5,3,4]
YL = [1.4,0.6,1.0,0.6,0.6,1.0]
