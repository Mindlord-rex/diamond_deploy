from flask import Flask,render_template,request
import pandas as pd
from models import predictor
app = Flask(__name__)

@app.route("/")
def name():
    return render_template('home.html')

@app.route('/result', methods=['POST', 'GET'])
def name1():
    if request.method == 'POST':
        a =  float(request.form["x"])      
        b =  float(request.form["y"])
        c =  float(request.form["z"])
        d =  float(request.form["carat"])
        e = int(request.form["color"])
        f = int(request.form["clarity"])
        g = float(request.form["depth"])
        h = float(request.form["table"])
        
        df ={
            "X" : [a],
            "Y" : [b],
            "Z" : [c],
            "Carat" : [d],
            "Color" : [e],
            "Clarity" : [f],
            "Depth" : [g],
            "Table" : [h]
            
        }
        data = pd.DataFrame(df)
        d1 = predictor(data)
        return render_template("sub.html",re  = d1)        

if __name__ =="__main__":
    app.run(debug=True)