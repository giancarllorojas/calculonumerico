'''
Exercicio 1, Cálculo númerico - Bordoni
@objetivo: Aproximação por diferenças divididas finitas
@entrada: 
	- uma função matemática x -> f(x) em um intervalo [a,b]
@saída: 
	- 3 gráficos com as aproximações
@autores: 
	- Giancarllo Rojas 
	- Victor Israel
'''
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

expre = input('Digite a função: f(x) = ')
a = int(input('Entre com o "a" do intervalo [a,b]: '))
b = int(input('Entre com o "b" do intervalo [a,b]: '))

def f(x):
    return eval(expre)
    
def Df(x, h):
    return (f(x + h) - f(x))/h;

def reta_sec(x, a, inclinacao):
    return inclinacao*(x-a) + f(a)
    
x = np.linspace(a, b, 100);
y = f(x)

ponto_medio = (a+b)/2
hs = (0.5, 0.2, 0.05) #valores de h apra se desenhar os plots

cont = 1;
for h in hs:
    plt.figure(cont)
    cont += 1
    plt.title('Aproximação por diferença avançada')
    plt.plot(x,y, label='F(x)')
    plt.plot(x, reta_sec(x, ponto_medio, Df(ponto_medio, h)), label='reta sec. h: ' + str(h))
    plt.plot([[ponto_medio],[ponto_medio+h]], [f(ponto_medio), f(ponto_medio+h)], 'bo')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axhline(y=0, c='k')
    plt.axvline(x=0, c='k')
    plt.legend()

plt.show();