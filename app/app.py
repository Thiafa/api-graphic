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
        data = request.get_json()
        constrained = data.get('constrained')
        x_otimo = data.get('xOtimo')
        z_otimo = data.get('zOtimo')
        line_chart = pygal.XY()
        line_chart.title = 'Resolução Gráfica do Simplex'

        if x_otimo:
            x = z_otimo / x_otimo[0]
            y = z_otimo / x_otimo[1]
            line_chart.add(f'Z', [[x, 0], [0, y]])

        for value in constrained.values():
            vars = value['vars']
            cost = value['cost']
            array_constrained = []
            for i, num in enumerate(vars):
                aux = []
                if vars[0] < 0 or vars[1] < 0:
                    if vars[0] < 0:
                        raiz = cost / num * -1
                        if i == 0:
                            aux.append(raiz)
                            aux.append(0)
                            array_constrained.append(aux)
                        elif i == 1:
                            aux.append(0)
                            aux.append(raiz)
                            array_constrained.append(aux)
                        line_chart.add(f'Restrição {i}:', array_constrained)
                    elif vars[1] < 0:
                        num_aux = cost / vars[0]
                        array_constrained.append((num, 0))
                        array_constrained.append((num_aux, num_aux + 6))
                        line_chart.add(f'Restrição {i}', array_constrained)

                elif num > 0:
                    raiz = cost / num
                    if i == 0:
                        aux.append(raiz)
                        aux.append(0)
                        array_constrained.append(aux)
                    elif i == 1:
                        aux.append(0)
                        aux.append(raiz)
                        array_constrained.append(aux)
                    line_chart.add(f'Restrição {i}:', array_constrained)

                else:
                    if vars.index(0) == 0:
                        num_aux = cost / vars[1]
                        array_constrained.append((0, num_aux))
                        array_constrained.append((num + 6, num_aux))
                        line_chart.add(f'Restrição {i}', array_constrained)
                    elif vars.index(0) == 1:
                        num_aux = cost / vars[0]
                        array_constrained.append((num_aux, 0))
                        array_constrained.append((num_aux, num_aux + 6))
                        line_chart.add(f'Restrição {i}', array_constrained)

        line_chart.render_to_file('function_chart.svg')
        return jsonify('Imagem gerada com sucesso'), 200
    except Exception as e:
        return jsonify('Erro no Servidor Interno'), 500

if __name__ == "__main__":
    app.run(debug=True)
