from flask import Flask, render_template, jsonify, redirect, url_for, request 

app = Flask(__name__)

estado_python = "¡Bienvenido! Haz clic para ejecutar código Python."

@app.route('/', methods=['GET', 'POST'])
def index():
    global estado_python
    
    if request.method == 'POST':
        estado_python = "¡Funcionalidad Python ejecutada con éxito!" 
        
        return redirect(url_for('index'))
    
    return render_template('index.html', mensaje_python=estado_python)

@app.route('/api/status', methods=['GET'])
def get_status():
    return jsonify({
        "status": "ok", 
        "language": "Python/Flask", 
        "message": "Servicio de Python corriendo y listo para procesamiento."
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)