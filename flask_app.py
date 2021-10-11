from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('./model/light.pkl', 'rb'))


@app.route('/')
def start():
    return render_template('start.html')

@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/predict', methods=['POST'])
def home():
    data1 = request.form.get('name1')
    data2 = request.form.get('name2')
    data3 = request.form.get('name3')
    data4 = request.form.get('name4')
    data5 = request.form.get('name5')
    data6 = request.form.get('name6')
    data7 = request.form.get('name7')
    data8 = request.form.get('name8')
    data9 = request.form.get('name9')
    data10 = request.form.get('name10')
    data11 = request.form.get('name11')
    arr = np.array([[data1, data2, data3, data4, data11, data5, data6, data7, data8, data9, data10 ]])
    pred = model.predict(arr)
    return render_template('after_.html', data=pred)


if __name__ == "__main__":
    app.run(debug=True)