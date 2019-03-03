from flask import Flask, render_template
from keras import backend as K

from flask import *
from cropmodel import prediction

app=Flask(__name__,template_folder='template')
K.clear_session()
@app.route('/')
def index():
    return render_template('index.html')
    #request.method and request.form
    #nmpy_list from form
    #output = model(nmpy_list)


@app.route('/',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        result=request.form
        output = prediction(result)
   
        return render_template("result.html", result = result, output =output)



if __name__ == '__main__' :
    app.run(debug = True)
