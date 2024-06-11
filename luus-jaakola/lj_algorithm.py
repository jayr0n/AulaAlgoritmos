import numpy as np
import sys
sys.path.append('../')
from values.funcoes_objetivo import FuncoesObjetivo
from values.valores_funcao import ValoresFuncaoObjetivo
from values.grafico_3d import solution_plot_2d 

def lj_algorithm(funcao_objetivo, limites, epsilon=0.01, nout=200, nint=200):
    solucoes = []
    l_inferior, l_superior = np.asarray(limites).T # no caso o meu limite inferior e superior está vindo do array
    solucao = np.random.uniform(l_inferior, l_superior, 2) # Na solução inicial eu to passando o X1 e X2
    melhor_fobjetivo = funcao_objetivo(solucao) # Recebendo o melhor valor da função objetivo
    r = l_superior - l_inferior # Definindo a amplitude do intervalo de busca

    for _ in range(nout):

        for i in range(nint):

            R = np.random.uniform(-0.5, 0.5, 2) # Gerando um matriz de números aleatórios entre -0.5 e 0.5
            nova_solucao = solucao + (R * r) # Gerando aleatoriamente uma solução inicial (adicionando um ruído a solução inicial)

            if funcao_objetivo(nova_solucao) < melhor_fobjetivo: # Verificando se a nova solução é que melhor
                melhor_fobjetivo = funcao_objetivo(nova_solucao) # A melhor função objetivo passa a ser a nova função objetivo
                solucao = nova_solucao # A solução passa a ser a nova solução
                solucoes.append(solucao)
        r = r * (1 - epsilon) # contraindo o r, ou seja, os limites da amplitude de intervalo em %
    return solucao, melhor_fobjetivo, solucoes

# nout = 75  # Número máximo de iterações Nout
# nint = 75  # Número máximo de iterações Nint
# epsilon = 0.5 # Definindo minha contração
limites = ValoresFuncaoObjetivo.valor_f_obj4() # Definindo meu os limites pro meu X1 e X2
funcao_objetivo = FuncoesObjetivo.f_obj4

melhor_solucao, melhor_valor, solucoes = lj_algorithm(funcao_objetivo, limites)

# print("Melhor solução:", melhor_solucao)
# print("Melhor valor:", melhor_valor)
solution_plot_2d(funcao_objetivo, limites, melhor_solucao, solucoes, '4')
