from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    
    return render_template('home.html')

@app.route('/chart')
def chart():
    
    return render_template('chart.html')

@app.route('/graph')
def graph():
    
    return render_template('graph.html')

@app.route('/list')
def list():
    
    return render_template('list.html')

@app.route('/help')
def help():
    
    return render_template('help.html')

if __name__ =="__main__":
    app.run(debug=True)