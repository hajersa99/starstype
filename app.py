

from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
@cross_origin()
def home():
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])
@cross_origin()
def predict():
    if request.method == "POST":
        '''
        For rendering results on HTML GUI
        '''
        int_features = [float(x) for x in request.form.values()]
        final_features = [np.array(int_features)]
        prediction = model.predict(final_features)
        output = (prediction[0])
        if output==0:

            text='Red dwarf'

        if output==1:

            text='Brown dwarf'

        if output==2:

            text='White dwarf'

        if output==3:

            text='Main sequence'

        else :

             text='Supergiants'

    return render_template('index.html',prediction_text=' Star type is {}'.format(text))
       

      
     

if __name__ == "__main__":
    app.run(debug=True)

