from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def index():

    ejeX = random.randint(11, 99)
    ejeY = random.randint(11, 99)

    return render_template(
        'index.html',
        ejeX=ejeX,
        ejeY=ejeY
    )
@app.route('/ejercicio1')
def ejercicio1():

    ejeX = random.randint(11, 99)

    return render_template(
        'ejercicio1.html',
        ejeX=ejeX
    )
@app.route('/ejercicio2')
def ejercicio2():

    ejeX = random.randint(11, 99)

    return render_template(
        'ejercicio2.html',
        ejeX=ejeX
    )
@app.route('/ejercicio3')
def ejercicio3():

    ejeX = random.randint(11, 99)

    return render_template(
        'ejercicio3.html',
        ejeX=ejeX
    )
@app.route('/ejercicio4')
def ejercicio4():
    return render_template('ejercicio4.html')
    
@app.route('/ejercicio5')
def ejercicio5():
    return render_template('ejercicio5.html')

@app.route('/ejercicio6')
def ejercicio6():

    ejeX = random.randint(11, 99)
    ejeY = random.randint(11, 99)

    return render_template(
        'ejercicio6.html',
        ejeX=ejeX,
        ejeY=ejeY
    )
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
