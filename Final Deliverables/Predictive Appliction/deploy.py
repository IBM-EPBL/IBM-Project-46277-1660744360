from flask import Flask, render_template, request
import numpy as np


import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "<Your API>"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

app = Flask(__name__)


#home page
@app.route('/')
def home():
    return render_template('home.html')


#signup page
@app.route('/register')
def register():
    return render_template('register.html')


#login page
@app.route('/login')
def login():
    return render_template('login.html')


#prediction page
@app.route('/index')
def index():
    return render_template('index.html')


#result page prediction function
@app.route('/result', methods= ['POST'])
def result():
    try:
        if request.methods == 'POST':
            l=[]
            l.append(float(request.form['id']))
            l.append(float(request.form['cycle']))
            l.append(float(request.form['set1']))
            l.append(float(request.form['set2']))
            l.append(float(request.form['set3']))
            l.append(float(request.form['s1']))
            l.append(float(request.form['s2']))
            l.append(float(request.form['s3']))
            l.append(float(request.form['s4']))
            l.append(float(request.form['s5']))
            l.append(float(request.form['s6']))
            l.append(float(request.form['s7']))
            l.append(float(request.form['s8']))
            l.append(float(request.form['s9']))
            l.append(float(request.form['s10']))
            l.append(float(request.form['s11']))
            l.append(float(request.form['s12']))
            l.append(float(request.form['s13']))
            l.append(float(request.form['s14']))
            l.append(float(request.form['s15']))
            l.append(float(request.form['s16']))
            l.append(float(request.form['s17']))
            l.append(float(request.form['s18']))
            l.append(float(request.form['s19']))
            l.append(float(request.form['s20']))
            l.append(float(request.form['s21']))
            l.append(float(request.form['s22']))
            print(l)
            # NOTE: manually define and pass the array(s) of values to be scored in the next line
            payload_scoring = {"input_data": [{"fields": ['f0','f1','f2','f3','f4','f5','f6','f7','f8','f9','f10','f11','f12','f13','f14','f15','f16','f17','f18','f19','f20','f21','f22','f23','f24','f25','f26'], "values": [l]}]}

            response_scoring = requests.post('https://south.ml.cloud.ibm.com/ml/v4/deployments/c870b-1697-49d5-86e7-302bd8fccd/predictions?version=2022-11-14', json=payload_scoring,
            headers={'Authorization': 'Bearer ' + mltoken})
            print("Scoring response")
            print(response_scoring.json())
            pred = response_scoring.json()
            output = pred['predictions'][0]['values'][0][0]
            print(output)

            if output >=1 and output <=2 :
                return render_template('result.html',data="normal")
            elif output >2:
                return render_template('result.html',data="excess")
            else :
                return render_template('result.html',data="low")
    except:
        return render_template('result.html',data="error")
if __name__=="__main__":
    app.run(debug=True)