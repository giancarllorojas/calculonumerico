'''
Exercicio 3, Cálculo númerico - Bordoni
@objetivo: Resolução de equação do calor pelo método de Crank Nicholson
@objetivo:
    	- equação definida por: dT(x,t)/dt = pd²T(x,t)/dx² + qdT(x,t)/dx + rT
    	- condições de contorno:
         - alfa*T(0,t) + rô*dT(0,t)/dx = h(t) em 0 < t < tau
         -	beta*T(L,t) + a*dT(0, t)/dx = g(t) em 0 < t < tau
@entrada: 	
	- Valores númericos de L, p, q, a, beta, rô, alfa, e tau
	- Função da distribuição inicial de temperatura x->f(x) em [0,L]
	- t->h(t) e t->g(t) em [0,t] que definem condições de contorno

@saída: 
	- Resolução do problema de valor inicial e de contorno
	- Demonstração grafica da solução
@teoria:
     - implementação baseada no seguinte paper:
     - http://www.sfu.ca/~rjones/bus864/notes/notes2.pdf
@autores: 
	- Giancarllo Rojas
	- Victor Israel
'''

import numpy as np
import matplotlib.pyplot as plt


print("###########################################################")
print("Resolução númerica da equação diferencial:\n")
print("dT(x,t)/dt = p*dT²(x,t)/dx + q*dT(x,t)/dx + r*T(x,t)\n")
print("com T(x,0) = f(x), x em [0,L] e condições de contorno:")
print("a*T(0,t) + c*(dT(0,t)/dx) = h(t) 0 < t < τ")
print("b*T(0,t) + d*(dT(0,t)/dx) = g(t) 0 < t < τ")
print("###########################################################")
print("\n\nentre com:")

exp_f = input("f(x) = ")
exp_h = input("h(t) = ")
exp_g = input("g(t) = ")

L = int(input("L = "))
tau = int(input("τ = "))

p = float(input("p = "))
q = float(input("q = "))
r = float(input("r = "))

a = float(input("a = "))
c = float(input("c = "))

b = float(input("b = "))
d = float(input("d = "))

def f(x):
    return eval(exp_f)
    
def h(t):
    return eval(exp_h)
    
def g(t):
    return eval(exp_g)



N_x = 10                  
N_t = 100
dx = float(L)/float(N_x)
dt = float(tau)/float(N_t)

valores_iniciais = np.array([k*dx for k in range(N_x)])

#preenche a malha com a condição inicial
for k in range(N_x):
    valores_iniciais[k] = f(k*dx)
    
# ------------------------------------------------------
# Função que acha a soluções de T(x,t+1) para 0 <= x <= L
# @entrada: int t
#           array vals_t
#           float dx, dt
#           float a,b,c,d 
# @saida: array T com os valores de T(x, t+1)
def resolve_t_mais_1(t, vals_t, dx, dt, p, q, r, a, b, c, d):
    #calculando os valores de contorno, dado as equações de contorno entradas
    contorno_0 = (dx*h(t) - c*vals_t[1])/(dx*a - c)
    contorno_L = (dx*g(t) - d*vals_t[1])/(dx*b - d)

    #montando o vetor de resultados F, para a equação matricial: A*T(i+1) = F(i)
    F = [contorno_0]
    #coeficientes para Di da formula (16) do paper citado
    coef_a = (2.*dt*p) + (dt*dx*q) 
    coef_b = (4.*dx*dx) - (4.*dt*p) + (2.*dx*dx*dt*r)
    coef_c = (2.*dt*p) - (dt*dx*q)
    for i in range(1, N_x-1):
        #d = (2.*dt + dt*dx*q)*vals_t[i+1] + ((4.*dx*dx) - (4.*dt*p) + (2.*dx*dx*dt*r))*vals_t[i] + ((2.*dt*p) - (dt*dx*q))*vals_t[i-1]
        f_i = coef_a*vals_t[i+1] + coef_b*vals_t[i] + coef_c*vals_t[i-1]
        #print(vals_t[i+1])
        F.append(f_i)
    F.append(contorno_L)
    F = np.array(F)

    #calculando os parametros para montar a matriz A
    Ai = -(2.*dt*p + dt*dx*q)
    Bi = 4.*dx*dx + 4.*dt*p - 2.*dx*dx*dt*r
    Ci = -(2.*dt*p - dt*dx*q)

    #montando a matriz tridiagonal A
    m_A = np.diagflat([Ai for i in range(N_x-1)], -1) +\
             np.diagflat([Bi for i in range(N_x)]) +\
             np.diagflat([Ci for i in range(N_x-1)], 1)

    #resolvendo: A*T = F
    T = np.linalg.solve(m_A, F)
    return T

solucoes = []
valores_t = valores_iniciais
#interativamente chama a função resolve_t_mais_1 para t de 0 até N_t(tamanho da discretização temporal)
for t in range(0, N_t):
    solucao_t1 = resolve_t_mais_1(t, valores_t, dx, dt, p, q, r, a, b, c, d)
    solucoes.append(solucao_t1)
    valores_t = solucao_t1

#plotando o mapa de calor
solucoes = np.matrix(solucoes)

malha_x = np.array([k*dx for k in range(N_x)])
malha_t = np.array([i*dx for i in range(N_t)])

fig, ax = plt.subplots()
plt.xlabel('x')
plt.ylabel('t')
#print(solucoes)
heatmap = ax.pcolor(malha_x, malha_t, np.array(solucoes))
colorbar = plt.colorbar(heatmap)
#plt.show()