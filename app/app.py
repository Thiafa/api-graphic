from flask import Flask, jsonify, request
import pygal
from pygal.style import DarkSolarizedStyle
from flask_cors import CORS
import aspose.words as aw


app = Flask(__name__)
CORS(app)

@app.route('/api', methods=['GET'])
def teste():
    return jsonify('Deu bom')


@app.route('/api/grafico', methods=['POST'])
def api_graph():
    data = request.get_json()
    # print(data)
    constrained = data.get('constrained')
    funcaoZ = data.get('funcaoZ')
    line_chart = pygal.XY()
    line_chart.title = 'Expressao'

    def calcularRaizes(vars, cost, line_chart):
        l_aux = []
        j = 0
        for i, num in enumerate(vars):
            # print(f'[{i}] Vars {num} {cost}')
            aux = []
            print(num)
            if(vars[0] < 0 or vars[1] < 0):
                if(vars[0]<0):    
                    raiz=cost/num*-1        
                    if i == 0:
                        aux.append(raiz)
                        aux.append(0)
                        l_aux.append(aux)
                    elif i == 1:
                        aux.append(0)
                        aux.append(raiz)
                        l_aux.append(aux)       
                        line_chart.add(f'Restrição {i}:', l_aux)    
                elif(vars[1]<0):
                    print('asd')
                    line_chart.add(f'Restrição {i}', [(num, 0), (num_aux,num_aux+6)])

            elif num > 0:
                raiz = cost / num
                if i == 0:
                    aux.append(raiz)
                    aux.append(0)
                    l_aux.append(aux)
                elif i == 1:
                    aux.append(0)
                    aux.append(raiz)
                    l_aux.append(aux)
                line_chart.add(f'Restrição {i}:', l_aux)               
           
            else:
                if(vars.index(0) == 0 ):
                    num_aux=cost/vars[1]
                    # print('--->',num_aux)
                    line_chart.add(f'Restrição {i}', [(0, num_aux), (num+4,num_aux)])
                elif(vars.index(0) == 1 ):
                    num_aux=cost/vars[0]
                    # print('--------->',cost)
                    # print('--->',num_aux)
                    line_chart.add(f'Restrição {i}', [(num_aux, 0), (num_aux,num_aux+6)])
                
       

    for value in constrained.values():
        calcularRaizes(value['vars'], value['cost'], line_chart)

    line_chart.render_to_file('../../Simplex/src/assets/function_chart.svg')
    img = open('function_chart.svg', 'r')
    return 'Deu tudo certo';
    

if __name__ == "__main__":
    app.run(debug=True)
