import pygal
import numpy as np

# Criar um gráfico de linha
line_chart = pygal.Line()

# Definir os pontos x para a função
x = np.linspace(-10, 10, 100)

# Definir a função com igualdade
y = 3 * x + 5 * x**2 - 18

# Adicionar a função ao gráfico
line_chart.add('Função', list(zip(x, y)))

# Renderizar o gráfico em um arquivo SVG
line_chart.render_to_file('function_chart.svg')
