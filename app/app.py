from flask import Flask, jsonify, request
import numpy as np
import pygal 
from pygal.style import DarkSolarizedStyle
from math import cos


app = Flask(__name__)

@app.route('/api/grafico',  methods=['POST'])
def teste():
    data = request.get_json()   
    constrained = data.get('constrained')
    funcaoZ = data.get('funcaoZ')
    # print(constrained)
    restricoes = data.get('restricoes')     
    line_chart = pygal.XY()
    line_chart.title = 'Expressao'
    def calcularRaizes(vars,cost,line_chart):
        aux = list()
        for num in vars():
            raiz = num/cost 
            aux.append(raiz)
            aux.append(0)
        contador = (len(vars))
        print(contador)
        print(aux)                    
    
    for key, value in constrained.items():
        calcularRaizes(value['vars'],value['cost'],line_chart)
        # print(value['vars'])
        # print(value['cost'])
        # add('Série 2', [[xraizX],[y,raizY] ])
          
    line_chart.render_to_file('scatter_chart.svg')

    return jsonify(constrained)

if __name__ == "__main__":
    app.run(debug=True)

#Z
#3x+5x2

#Restricoes
#x1<=4
#2x2<=12
#3x1+2x2<=18
