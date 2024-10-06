from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/equipo') 
def equipo():
    return render_template('Equipo.html')

@app.route('/51Pegasi') 
def pegasi():
    return render_template('51PegasiB.html')

@app.route('/kepler')  
def kepler():
    return render_template('Kepler-22b.html')

@app.route('/centauri')  
def centauri():
    return render_template('ProximaCentauriB.html')

@app.route('/sistema') 
def sistema():
    return render_template('SistemaHR.html')

@app.route('/trappist') 
def trappist():
    return render_template('SistemaTrappist1.html')

@app.route('/cancri') 
def cancri():
    return render_template('55CancriE.html')

@app.route('/test') 
def test():
    return render_template('test.html')

if __name__ == '__main__':
    app.run(debug=True)
