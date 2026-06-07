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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
