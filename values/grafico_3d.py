import matplotlib.pyplot as plt
import numpy as np

def solution_plot_2d(f_objetivo, limites_funcao, melhor_solucao, solucoes_intermediarias, funcaoObjetivo):
    # Definindo os limites
    l_inferior, l_superior = np.asarray(limites_funcao).T
    limites = np.linspace(l_inferior, l_superior, 100)

    X = limites[:, 0]
    Y = limites[:, 1]
    X, Y = np.meshgrid(X, Y)
    Z = f_objetivo(np.array([X, Y]))

    # Plotando o gráfico de contorno
    plt.figure()
    contour = plt.contour(X, Y, Z, levels=10, cmap='viridis')
    plt.clabel(contour, inline=1, fontsize=10)

    # Scatter plot do ponto ótimo


    # Traçando a evolução até o ponto ótimo
    solucoes_intermediarias = np.array(solucoes_intermediarias)
    plt.scatter(solucoes_intermediarias[:, 0], solucoes_intermediarias[:, 1], color='blue', marker='x', label='Soluções Intermediárias')
    

    if funcaoObjetivo == '3':
        melhores_solucoes = [[0.08690935, -0.71188026]]
        for optimal_point in melhores_solucoes:
            plt.scatter(optimal_point[0], optimal_point[1], color='red', marker='o', s=70, label='Ponto Ótimo')
    else:
        optimal_point = melhor_solucao
        plt.scatter(optimal_point[0], optimal_point[1], color='red', marker='o', s=70, label='Ponto Ótimo')

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title(f'Gráfico de Contorno da Função Objetivo {funcaoObjetivo}')
    plt.legend()
    plt.show()