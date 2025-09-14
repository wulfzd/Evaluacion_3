from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    resultado = None
    if request.method == 'POST':
        try:
            nota1 = int(request.form['nota1'])
            nota2 = int(request.form['nota2'])
            nota3 = int(request.form['nota3'])
            asistencia = int(request.form['asistencia'])
            
            # Validar rangos
            if not all(10 <= n <= 70 for n in [nota1, nota2, nota3]):
                resultado = {"error": "Todas las notas deben estar entre 10 y 70"}
            elif not (0 <= asistencia <= 100):
                resultado = {"error": "La asistencia debe estar entre 0 y 100"}
            else:
                promedio = (nota1 + nota2 + nota3) / 3
                aprobado = promedio >= 40 and asistencia >= 75
                resultado = {
                    "promedio": round(promedio, 2),
                    "asistencia": asistencia,
                    "aprobado": aprobado
                }
        except ValueError:
            resultado = {"error": "Todos los campos deben ser números válidos"}
    
    return render_template('ejercicio1.html', resultado=resultado)

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    resultado = None
    if request.method == 'POST':
        nombre1 = request.form['nombre1'].strip()
        nombre2 = request.form['nombre2'].strip()
        nombre3 = request.form['nombre3'].strip()
        
        # Validar que no estén vacíos
        if not all([nombre1, nombre2, nombre3]):
            resultado = {"error": "Todos los nombres deben ser completados"}
        else:
            # Encontrar el nombre más largo
            nombres = [nombre1, nombre2, nombre3]
            nombre_mas_largo = max(nombres, key=len)
            longitud = len(nombre_mas_largo)
            
            resultado = {
                "nombre_mas_largo": nombre_mas_largo,
                "longitud": longitud
            }
    
    return render_template('ejercicio2.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
