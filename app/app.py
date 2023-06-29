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
        
        l_aux = list()
        
        i = 0
        for num in vars:
            aux = list()
            if(num != 0):
                raiz = cost/num
                # print(f'{raiz} = {cost}/{num}')
                aux = list()
                if(i == 0):
                    aux.append(raiz)
                    aux.append(0)
                    print(aux)
                    l_aux.append(aux)
                elif(i == 1):
                    aux.append(0)
                    aux.append(raiz)
                    print(aux)
                    l_aux.append(aux)
            
                
                l_aux.append(aux)
            line_chart.add(f'Restrição {i}:',l_aux)
            i+=1
            print(l_aux)    
    
    for key, value in constrained.items():
        calcularRaizes(value['vars'],value['cost'],line_chart)

    line_chart.render_to_file('function_chart.svg')
    # line_chart.render_to_file('scatter_chart.svg')

    return jsonify(constrained)

if __name__ == "__main__":
    app.run(debug=True)

#Z
#3x+5x2

#Restricoes
#x1<=4
#2x2<=12
#3x1+2x2<=18
