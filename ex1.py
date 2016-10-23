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
from pylab import *

expre = input('Digite a função: f(x) = ')
a = int(input('Entre com o "a" do intervalo [a,b]: '))
b = int(input('Entre com o "b" do intervalo [a,b]: '))

def f(x):
    return eval(expre)
    
def Df(x, h):
    return (f(x + h) - f(x))/h;

def reta_sec(x, a, inclinacao):
    return inclinacao*(x-a) + f(a)
    
x = np.linspace(a, b, 10000);
y = f(x)

ponto_medio = a+ (b-a)/2
print(ponto_medio)

figure(1)
title('Aproximação por diferença avançada')
plot(x,y, label='F(x)')
plot(x, reta_sec(x, ponto_medio, Df(ponto_medio, 0.5)), label='reta sec. h: 0.5')
plot([[ponto_medio],[ponto_medio+0.5]], [f(ponto_medio), f(ponto_medio+0.5)], 'bo')
xlabel('x')
ylabel('y')
legend()

figure(2)
title('Aproximação por diferença avançada')
plot(x,y, label='F(x)')
plot(x, reta_sec(x, ponto_medio, Df(ponto_medio, 0.2)), label='reta sec. h: 0.2')
plot([[ponto_medio],[ponto_medio+0.2]], [f(ponto_medio), f(ponto_medio+0.2)], 'bo')
xlabel('x')
ylabel('y')
legend()

figure(3)
title('Aproximação por diferença avançada')
plot(x,y, label='F(x)')
plot(x, reta_sec(x, ponto_medio, Df(ponto_medio, 0.05)), label='reta sec. h: 0.2')
plot([[ponto_medio],[ponto_medio+ 0.05]], [f(ponto_medio), f(ponto_medio+ 0.05)], 'bo')
xlabel('x')
ylabel('y')
legend()

show();