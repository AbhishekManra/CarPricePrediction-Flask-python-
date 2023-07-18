from flask import Flask,render_template,request
import pandas as pd
import pickle

import os
filepath = '.ipynb_checkpoints/LinearRegressionModel.pkl'
if os.path.exists(filepath):
    file = open('.ipynb_checkpoints/LinearRegressionModel.pkl', 'rb')
    codedata = pickle.load(file)
    file.close()
else:
    print("File not present at desired location")


app = Flask(__name__)

df = pd.read_csv("./cleaned_car.csv")

@app.route('/')
def index():
    companies = sorted(df['company'].unique())
    car_models = sorted(df['name'].unique())
    car_year = sorted(df['year'].unique())
    fuel_type = df['fuel_type'].unique()
    return render_template('index.html',companies = companies , car_models = car_models , year = car_year , f_type = fuel_type)

@app.route('/predict',methods=['POST'])
def predict():
    company = request.form.get('companies')
    car_model = request.form.get('car_models')
    year = request.form.get('year')
    fuel_type = request.form.get('f_type')
    print(company,car_model,year,fuel_type)

    prediction = model.predict(pd.DataFrame([[car_model,company,year,fuel_type]],columns = ['name','company','year','kms_driven','fuel_type']))
    print(prediction)
    return " "

if __name__=="__main__":
    app.run(debug=True)