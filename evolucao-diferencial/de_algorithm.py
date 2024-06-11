# Tamanho da População
# Taxa de Cruzamento
# Taxa de Mutação
# Cálculo da Aptidão (Fitness)
# Tamanho do Cromossomo
# Número Máximo de Gerações
# In addition, the canonical DE requires very few control parameters (3 to be precise: the scale factor, the crossover rate and the population size) — 
# a feature that makes it easy to use for the practitioners.
# NP tamanho da populacao
# F ∈ [0, 2] fator de mutação
# CR crossover rate CR ∈ [0, 1]
import sys
sys.path.append('../')
import numpy as np
from numpy.random import *
import matplotlib.pyplot as plt
from values.funcoes_objetivo import FuncoesObjetivo 
from values.valores_funcao import ValoresFuncaoObjetivo
from values.grafico_3d import solution_plot_2d 
# função 4 NumGeracoes = 1000, NP = 90, f = 0.55, CR = 0.032
# f = 0.2, CR = 0.5
#C𝑅 = 0,8 e 𝐹 = 0,2

def evolucao_diferencial(fobjetivo, limites, NumGeracoes = 200, NP = 20, f = 0.7, CR = 0.9):
    dimensoes = len(limites) # Estabelecendo as dimensoes
    l_inferior, l_superior = np.asarray(limites).T # Definindo os limites inferior e superior
    trial = np.zeros(dimensoes)
   
    populacao_inicial = l_inferior + (rand(NP, dimensoes) * (l_superior - l_inferior)) # Gerando a populacao inicial
    f_objetivo_incial = np.asarray([fobjetivo(ind) for ind in populacao_inicial]) # rodando o melhor resultado para populacao inicial
    melhor_valor_funcao_objetivo = np.argmin(f_objetivo_incial) # melhor valor funcao objetivo
    melhor_solucao = populacao_inicial[melhor_valor_funcao_objetivo] # melhor solucao
    #apenas para salvar as soluções para plotagem
    solucoes = []
    for k in range(NumGeracoes):
        for i in range(NP):
            a, b, c = populacao_inicial[choice(NP, 3, replace=False)] # selecionando 3 candidatos diferentes entre si
            rnbr = randint(1, dimensoes) # selecionando o R para crossover
            for j in range(dimensoes):
                if (rand(1) < CR) or (j == rnbr): # fazendo o trial, caso o rand(1) seja menor que o cross over ou o j seja igual o R
                    trial[j] = np.clip(a[j] + f * (b[j] - c[j]), l_inferior[j], l_superior[j]) # fazendo o vetor tentativa(trial)
                else:
                    trial[j] = populacao_inicial[i, j] # fazendo o vetor tentativa(trial), caso o valor não seja atendido

            # Fazendo a seleção, operação responsável por escolher os cromossomos mais aptos, que serão utilizados na próxima geração
            valor_f_objetivo_trial = fobjetivo(trial) 
            if valor_f_objetivo_trial <= fobjetivo(populacao_inicial[i]): # Se função objetivo do meu trial(cruzamento) é menor que a funcao objetivo populacao
                populacao_inicial[i] = trial.copy() # caso seja positivo, a minha populacao incial recebe os valores de trial(Crossover)
                if valor_f_objetivo_trial < melhor_valor_funcao_objetivo: # verificar a minha população modificada
                    melhor_solucao = trial.copy() # então trocamos os valores da melhor solucao com a populacao cruzada
                    melhor_valor_funcao_objetivo = valor_f_objetivo_trial # o melhor valor da funcao objetivo passa a ser o valor da funcao da populacao cruzada
            solucoes.append(melhor_solucao)
    return melhor_solucao, melhor_valor_funcao_objetivo, solucoes

funcao_objetivo = FuncoesObjetivo.f_obj3
limites = ValoresFuncaoObjetivo.valor_f_obj3()

melhor_solucao, melhor_valor_funcao_objetivo, solucoes = evolucao_diferencial(funcao_objetivo, limites)
solution_plot_2d(funcao_objetivo, limites, melhor_solucao, solucoes, '3')

