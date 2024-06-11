import sys
sys.path.append('../')
import numpy as np
from numpy.random import *
import matplotlib.pyplot as plt
from values.funcoes_objetivo import FuncoesObjetivo 
from values.valores_funcao import ValoresFuncaoObjetivo
from values.grafico_3d import solution_plot_2d 

#  in our simulations, we can use the following values of parameters α = 0.2, γ = 1,
#  and β0 = 1. As an example, we now use the FA to find the global maxima of the following function

# caso a função seja a 2, os parametros deverão ser n_vagalumes=20, n_iteracoes=100, alpha=0.55, beta_0=1, gamma=1
# para qualquer outra função os valores de parametro podem ser n_vagalumes=20, n_iteracoes=100, alpha=0.05, beta_0=1, gamma=1
import numpy as np
from numpy.random import rand

def firefly_algorithm(f_objetivo, limites, n=40, max_iter=300, alpha=0.05, beta_min=0.55, gamma=1.0):
    # Initialization of parameters and population
    dimensoes = len(limites)
    populacao = np.random.rand(n, dimensoes)
    for i in range(n):
        for j in range(dimensoes):
            populacao[i][j] = limites[j][0] + populacao[i][j] * (limites[j][1] - limites[j][0])
    
    # Main loop of the Firefly Algorithm
    for t in range(max_iter):
        for i in range(n):
            for j in range(n):
                if f_objetivo(populacao[j]) < f_objetivo(populacao[i]):
                    r = np.linalg.norm(populacao[i] - populacao[j])
                    attractiveness = beta_min * np.exp(-gamma * r**2)
                    beta = 1.0  # Ensure beta is defined, adjust as needed
                    populacao[i] += alpha * attractiveness * (populacao[j] - populacao[i]) + beta * (np.random.rand(dimensoes) - 0.5)
                    # Ensure the new position is within bounds
                    for k in range(dimensoes):
                        populacao[i][k] = np.clip(populacao[i][k], limites[k][0], limites[k][1])
    
    # Find the best solution
    best_index = np.argmin([f_objetivo(ind) for ind in populacao])
    melhor_solucao = populacao[best_index]
    melhor_fobjetivo = f_objetivo(melhor_solucao)
    
    return melhor_solucao, melhor_fobjetivo, populacao

funcao_objetivo = FuncoesObjetivo.f_obj4
limites = ValoresFuncaoObjetivo.valor_f_obj4()

melhor_solucao, melhor_valor_funcao_objetivo, solucoes = firefly_algorithm(funcao_objetivo, limites)
solution_plot_2d(funcao_objetivo, limites, melhor_solucao, solucoes, '4')