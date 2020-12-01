from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np

app = Flask(__name__)

model1=pickle.load(open('breast.pkl','rb'))
model2=pickle.load(open('dia.pkl','rb'))
model3=pickle.load(open('heart.pkl','rb'))
model4=pickle.load(open('liverdta.pkl','rb'))

@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/breast')
def bre():
    return render_template('breast_cancer.html')

@app.route('/dia')
def diab():
    return render_template('diabetes.html')

@app.route('/heart')
def hea():
    return render_template('heart.html')

@app.route('/liver')
def liv():
    return render_template('liver.html')

@app.route('/breastcancer',methods=['POST','GET'])
def predict1():
    int_features=[int(x) for x in request.form.values()]
    final=[np.array(int_features)]
    print(int_features)
    print(final)
    prediction=model1.predict_proba(final)
    output='{0:.{1}f}'.format(prediction[0][1], 2)

    if output>str(0.5):
        return render_template('home.html',pred='Your Health is in Danger.\nProbability of Occurence of Breast cancer is {}'.format(output),bhai="You have a symptoms of getting Breast cancer")
    else:
        return render_template('home.html',pred='Your Health is safe.\n Probability of Occurence of Breast cancer is {}'.format(output),bhai="You don't have a symptoms of getting Breast cancer")

@app.route('/diabetes',methods=['POST','GET'])
def predict2():
    int_features=[float(x) for x in request.form.values()]
    final=[np.array(int_features)]
    print(int_features)
    print(final)
    prediction=model2.predict_proba(final)
    output='{0:.{1}f}'.format(prediction[0][1], 2)

    if output>str(0.5):
        return render_template('home.html',pred='Your Health is in Danger.\nProbability of Occurence of Diabetes is {}'.format(output),bhai="You have a symptoms of getting Breast cancer")
    else:
        return render_template('home.html',pred='Your Health is safe.\n Probability of Occurence of Diabetes is {}'.format(output),bhai="You don't have a symptoms of getting Breast cancer")

@app.route('/hea',methods=['POST','GET'])
def predict3():
    int_features=[float(x) for x in request.form.values()]
    final=[np.array(int_features)]
    print(int_features)
    print(final)
    prediction=model3.predict_proba(final)
    output='{0:.{1}f}'.format(prediction[0][1], 2)

    if output>str(0.5):
        return render_template('home.html',pred='Your Health is in Danger.\nProbability of Occurence of Heart disease is {}'.format(output),bhai="You have a symptoms of getting Heart disease")
    else:
        return render_template('home.html',pred='Your Health is safe.\n Probability of Occurence of Heart Disease is {}'.format(output),bhai="You don't have a symptoms of getting Heart disease")

@app.route('/liv',methods=['POST','GET'])
def predict4():
    int_features=[float(x) for x in request.form.values()]
    final=[np.array(int_features)]
    print(int_features)
    print(final)
    prediction=model4.predict_proba(final)
    output='{0:.{1}f}'.format(prediction[0][1], 2)

    if output>str(0):
        return render_template('home.html',pred='Your Health is in Danger.\nProbability of Occurence of Liver Disease is {}'.format(output),bhai="You have a symptoms of getting Liver disease")
    else:
        return render_template('home.html',pred='Your Health is safe.\n Probability of Occurence of Liver Disease is {}'.format(output),bhai="You don't have a symptoms of getting Liver disease")


if __name__ == '__main__':
    app.run(port='5000',debug=False)
