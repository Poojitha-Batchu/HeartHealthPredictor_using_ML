from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

randomForest_model = pickle.load(open('./models/RandomorestModel.pkl', 'rb'))
columnTransform = pickle.load(open('./models/columnTransformer.pkl', 'rb'))

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        age = int(request.form.get('age'))
        gender = int(request.form.get('gender'))
        chest_pain_type = int(request.form.get('chest_pain_type'))
        blood_pressure = int(request.form.get('blood_pressure'))
        cholestoral = int(request.form.get('cholestoral'))
        blood_sugar = int(request.form.get('blood_sugar'))
        cardiographic = int(request.form.get('cardiographic'))
        heart_rate = int(request.form.get('heart_rate'))
        angina = int(request.form.get('angina'))
        oldpeak = round(float(request.form.get('oldpeak')), 1)
        slope = int(request.form.get('slope'))
        vessels = int(request.form.get('vessels'))
        thal = int(request.form.get('thal'))

        inputs = [[age, gender, chest_pain_type, blood_pressure, cholestoral, blood_sugar, cardiographic, heart_rate, angina, oldpeak, slope, vessels, thal]]
        columns=['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach','exang', 'oldpeak', 'slope', 'ca', 'thal']
        new_df = pd.DataFrame(data=inputs, columns=columns)
        new_scaled_data = columnTransform.transform(new_df)

        result = "Healthy" if randomForest_model.predict(new_scaled_data) == 0 else "Not Healthy"
        # print(result)
        return render_template('index.html', result=result)

    return render_template('index.html', result=None)


if __name__ == '__main__':
    app.run(debug=True)