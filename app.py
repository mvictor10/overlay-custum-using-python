from flask import *

app = Flask(__name__)

@app.route("/")
def index():
	return render_template('index.html')

@app.route("/legenda/painel")
def legend_dash():
	return render_template('legenda-noticias/painel.html')

@app.route("/legenda/overlay")
def legend_overlay():
	return render_template('legenda-noticias/index.html')

@app.route("/placar/painel")
def placar_dash():
	return render_template('placa-de-jogos/dashboard.html')

@app.route("/placar/overlay")
def placar_overlay():
	return render_template('placa-de-jogos/index.html')

app.run(host='0.0.0.0', port=80, debug=True)