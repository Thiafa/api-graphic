from flask import Flask, jsonify, request
import numpy as np
import pygal
from math import cos


app = Flask(__name__)

@app.route('/api/grafico',  methods=['POST'])
def teste():
    data = request.get_json()
    z = data.get('Z')
    restricoes = data.get('restricoes')
     
    chart = pygal.XY()
    chart.title = f"Gráfico {z}"
  
    quantidade_rest= len(restricoes[0])

    for a in restricoes:
      print(a)
      return jsonify(a)
      # chart.add(f'{a}')

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
