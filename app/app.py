from flask import Flask, jsonify, request
import numpy as np
import pygal 
from pygal.style import DarkSolarizedStyle
from math import cos


app = Flask(__name__)

@app.route('/api/grafico',  methods=['POST'])
def teste():
    data = request.get_json()
    z = data.get('Z')
    restricoes = data.get('restricoes')     



    chart = pygal.XY(style=DarkSolarizedStyle)
    chart.title = f"Gráfico {z}"
    # chart.add(f'{a}')
    chart.add('Série 1', ([2,6],[4,3]), show_dots=False, fill=True)
    chart.add('Série 2', ([4,0],[4,6]), show_dots=False,fill=True)
    chart.add('Série 3', ([0,6],[5,6]), show_dots=False,fill=True)
    chart.add('Série 4', ([0,9],[6,0]), show_dots=False,fill=True)
    chart.render_to_file('chart.svg')
    # Render the chart to an SVG file
    # bar_chart.render_to_file('bar_achart.svg')
    return jsonify(z)



if __name__ == "__main__":
    app.run(debug=True)

#Z
#3x+5x2

#Restricoes
#x1<=4
#2x2<=12
#3x1+2x2<=18
