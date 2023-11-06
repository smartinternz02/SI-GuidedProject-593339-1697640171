from flask import Flask, render_template, request
import pickle
import numpy as np
app = Flask(__name__)

model = pickle.load(open('5g_allocation.pkl', 'rb'))


@app.route('/')
def start():
    return render_template('index.html')

@app.route('/login',methods =['POST'])

def login():

    application_type = request.form['at'],
    signal_strength = request.form['ss'],
    latency = request.form['lt'],
    required_bandwidth = request.form['rb'],
    allocated_bandwidth = request.form['ab']

    t = [[float(application_type), float(signal_strength), float(latency), float(required_bandwidth), float(allocated_bandwidth)]]
    output = model.predict(t)
    print(output)


    return render_template('index.html', y = "The predicted Resource_Allocation is  "+str(np.round(output[0])))

if __name__ == '__main__':
    app.run(debug=True) 