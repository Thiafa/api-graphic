from flask import Flask, jsonify, request, Response
import pygal
from pygal.style import DarkSolarizedStyle
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api', methods=['GET'])
def teste():
    return jsonify('Deu bom')

@app.route('/api/grafico', methods=['POST'])
def api_graph():
    try:
        # Recebendo os valores
        data = request.get_json()
        constrained = data.get('constrained')
        x_otimo = data.get('xOtimo')
        z_otimo = data.get('zOtimo')
        f = data.get('f')
        # print(data)
        print(constrained)
        # Iniciando o gráfico XY
        line_chart = pygal.XY()
        line_chart.title = 'Resolução Gráfica do Simplex'

        aux_z = []
        for i, num in enumerate(f):
            if(num < 0):
                num = num *-1
            if(i==0):
                num_aux = z_otimo/num
                aux_z.append([num_aux, 0])
            elif(i==1):
                num_aux = z_otimo/num
                aux_z.append([0,num_aux])
        line_chart.add('Ponto Otimo', aux_z)

        if x_otimo:
            x = x_otimo[0]
            y = x_otimo[1]
            line_chart.add(f'Z*', [[x,y]])
            
        aux = []
        for value in constrained.values():
            vars = value['vars']
            cost = value['cost']
           
            for i, num in enumerate(vars):
               if(i==0):
                   if(num == 0):
                        aux.insert(i,0)
                        # aux.insert(i+1,vars[i]+10)
                   if(num != 0):
                        aux.insert(i,cost/num)
                        # aux.insert(i+1,0)
                   
               elif(i==1):
                    if(num == 0):
                        aux.insert(i,0)
                        # aux.insert(i+1,vars[i]+10)
                    if(num!=0):
                        aux.insert(i,cost/num)
                        # aux.insert(i-1,0)
        def quebrar_em_pares(array):
            pares = []            
            for i in range(0, len(array), 2):
                par = array[i:i+2]
                pares.append(par)
            return pares
                  
        a = quebrar_em_pares(aux)
        for i, l in enumerate(a):
            t = []
            if(l[0] and l[1] != 0):
                l.insert(1,0)
                l.insert(2,0)
                t = quebrar_em_pares(l)
                print(t)
                line_chart.add('Restrição ', t)
            elif(l[0]==0 and l[1]!=0):
                print('x',l)
                l.append(l[1]*2)
                l.append(l[1])
                t = quebrar_em_pares(l)
                print(t)
                line_chart.add('Restrição ', t)
            elif(l[1]==0 and l[0]!=0):
                print('x',l)
                l.append(l[0])
                l.append(l[0]*2)
                t = quebrar_em_pares(l)
                print(t)
                line_chart.add('Restrição ', t)
                

        line_chart.render_to_file('../../Simplex/src/assets/function_chart.svg')
        line_chart.render_to_file('function_chart.svg')
        # img = open('function_chart.svg')
        # return img
        return jsonify('Imagem gerada com sucesso'), 200
    except Exception as e:
        print(e)
        return jsonify('Erro no Servidor Interno',e), 500

if __name__ == "__main__":
    app.run(debug=True)
