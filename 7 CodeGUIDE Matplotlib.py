# |====================================================================================================================|

# INTRODUÇÃO A BIBLIOTECA

# instruções de como se utilizar a biblioteca Matplotlib, sendo mais utilizada na criação
# de gráficos para analise de dados e visualização de dataframes

# o primeiro de tudo é importar a biblioteca para o seu arquivo
# P.S = normalmente utilizamos o nome mpl por que é mais facil de chamar quando for executar comandos

import matplotlib as mpl

# a segunda coisa é adicionar outra biblioteca que personaliza os gráficos gerados pelo mpl, ela se chama
# pyplot, então é so importar ela junto, lembrando que ela faz parte do mpl, então fica asssim:

import matplotlib.pyplot as plt

# Se estiver usando um JUPYTER NOTEBOOK:
# Uma opção interessante é fazer o mpl gerar os graficos na mesma pagina e não ficar abrindo outras
# janelas com o seguinte comando:

'''
%matplotlib inline
'''

# |====================================================================================================================|

# UTILIZANDO PYPLOT

# SEUS PRIMEIROS GRÁFICOS:
# A partir daqui entramos na sessão de explicação de cada tipo de gráfico com informações adicionais sobre cada um

# Plot padrão:
# esse tipo de gráfico só faz a associação de duas variáveis, então tudo que precisa é utilizar o plt.plot("Dados")
# que o gráfico está feito, segue o exemplo abaixo

plt.plot([1,3,5], [2,4,7])
plt.show() # P.S = Sempre lembrar de usar o .show() no final pra mostrar o gráfico ok

# para utilizar mais de uma linha no gráfico, basta colocar mais linhas .plot, pois cada comando server pra uma linha diferente

plt.plot([1,3,5], [2,4,7])
plt.plot([3,4,5], [4,6,7])
plt.show()

# argumentos do Plot padrão:

# label= "Str" = definição de legendas no gráifco, lembrar de usar o .legend() para aplicar elas no gráfico

plt.plot([1, 2, 3],[4, 5, 6], label= "Gráfico com Matplotlib")

# color= "Str" = definição da cor da variavel no gráfico, lembrar do nome das cores ou do atalho de uma letra da cor escolhida
# b : blue, g : green, r : red, c : cyan, m : magenta, y : yellow, k : black, w : white

plt.plot([1, 2, 3],[4, 5, 6], color= "blue")


# métodos do Plot Padrão:

# plt.xlabel("Str") = definição do nome do eixo X com o "Str" que estiver como argumento

plt.xlabel("Variável 1")


# plt.ylabel("Str") = definição do nome do eixo X com o "Str" que estiver como argumento

plt.ylabel("Variavel 2")


# plt.title("Str") = definição do título do gráfico com o "Str" que estiver como argumento

plt.title("Teste Plot")


# plt.legend() = aplicação da legenda no gráfico gerado com o argumento label="Str" dentro do .plot() 

plt.legend()
