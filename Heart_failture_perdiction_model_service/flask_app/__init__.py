#Import main library
import numpy as np

#Import Flask modules
from flask import Flask, request, render_template

#Import pickle to save our regression model
import pickle 

#Initialize Flask and set the template folder to "template"
app = Flask(__name__, template_folder = 'template')

#Open our model 
model = pickle.load(open('model.pkl','rb'))

#create our "home" route using the "index.html" page
@app.route('/')
def home():
    return render_template('index.html')

#Set a post method to yield predictions on page
@app.route('/', methods = ['POST'])
def predict():
    
    #obtain all form values and place them in an array, convert into integers
    int_features = [float(x) for x in request.form.values()]
    #Combine them all into a final numpy array
    final_features = [np.array(int_features)]
    #predict the price given the values inputted by user
    prediction = model.predict(final_features)
    output = prediction
    
    #If the output is negative, the values entered are unreasonable to the context of the application
    #If the output is greater than 0, return prediction
    if output == 0:
        return render_template('index.html', prediction_text = "You are healthy as a Horse :) ")
    elif output == 1:
        return render_template('index.html', prediction_text = "Maybe it's time to visit the doctor :0")

#Run app
if __name__ == "__main__":
    app.run(debug=True)