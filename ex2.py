'''
Exercicio 2, Cálculo númerico - Bordoni
@objetivo: Comparação entre aproximação por diferença avançada, atrasada e centrada - Análise da propagação de erros
@entrada: 
	- uma função matemática x -> f(x) em um intervalo [a,b] e um ponto x0 pertencente a [a,b]
@saída: 
	- gráfico das três sequências
@autores: 
	- Giancarllo Rojas 
	- Victor Israel
'''
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt


exp_f = input('Digite a expressão da função: f(x) = ')
exp_df = input('Digite a expressão da derivada de f(x): f\'(x) = ')
val_a = int(input('Entre com o valor de a: a = '))
val_n = int(input('Entre com o valor de N: N = '))

def f(x):
    return eval(exp_f)
    
def Df(x):
    return eval(exp_df)

def h(k):
    return 2**(-k)

def Df_avancada(a, h):
    return (f(a + h) - f(a))/h;

def Df_centrada(a, h):
    return (f(a + h) - f(a - h))/(2*h);

def Df_atrasada(a, h):
    return (f(a) - f(a - h))/h;

ks = np.arange(0,val_n+1, 1)

val_correto = Df(val_a)

Df_av = []
Df_ce = []
Df_at = []
Err_av = []
Err_ce = []
Err_at = []

for k in range(0, val_n+1):
    Df_av.append(Df_avancada(val_a, h(k)))
    Df_ce.append(Df_centrada(val_a, h(k)))
    Df_at.append(Df_atrasada(val_a, h(k)))
    Err_av.append(Df_av[k] - Df(val_a))
    Err_ce.append(Df_ce[k] - Df(val_a))
    Err_at.append(Df_at[k] - Df(val_a))


print(Err_at)
#print(Df_av)
plt.figure(1);
plt.title('Aproximação por diferença avançada')
plt.plot(ks, Df_av, label='dif. avancaçada', linestyle='none', marker='.')
plt.plot(ks, Df_ce, label='dif. centrada', linestyle='none', marker='.')
plt.plot(ks, Df_at, label='dif. atrasada', linestyle='none', marker='.')
plt.xlabel('k')
plt.ylabel('D(' + str(val_a) + ')')
plt.grid(True)
plt.legend(loc='best')

plt.figure(2);
plt.title('Erro nas aproximações por DDPs')
plt.plot(ks, Err_av, label='dif. avancaçada', linestyle='none', marker='.')
plt.plot(ks, Err_ce, label='dif. centrada', linestyle='none', marker='.')
plt.plot(ks, Err_at, label='dif. atrasada', linestyle='none', marker='.')
plt.xlabel('k')
plt.ylabel('Erro')
plt.grid(True)
plt.legend(loc='best')
plt.yscale("log")
plt.show()