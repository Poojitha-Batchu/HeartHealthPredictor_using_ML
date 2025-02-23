# Heart Health Predictor 🫀
The Heart Health Predictor is a machine learning-based web application designed to assess heart health risk based on user inputs. It uses a trained Random Forest Classifier to predict potential heart-related issues.

## 🚀 Features
Heart Health Prediction using ML models
User-Friendly Frontend built with Flask
Data Visualization for insights
Data Preprocessing:
Categorical data encoded using LabelEncoder
Numerical data standardized using StandardScaler
Optimized Hyperparameters using RandomizedSearchCV
High Accuracy achieved with Random Forest Classifier

## 📊 Dataset
Source: Kaggle - Heart Disease Dataset (https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset)

The dataset includes features like age, sex, chest pain type, resting BP, cholesterol levels, etc.

## 🧮 Tech Stack
Frontend: Flask
Backend: Python, Scikit-learn, Pandas, NumPy
ML Model: Random Forest Classifier
Visualization: Matplotlib, Seaborn

⚙️ Setup Instructions <br>
1. Clone the repository: <br>

        git clone https://github.com/Poojitha-Batchu/HeartHealthPredictor_using_ML.git
        cd heart-health-predictor

2. Create a virtual environment & activate it: <br>

       python -m venv venv
        source venv/bin/activate  # For Linux/Mac
        venv\Scripts\activate     # For Windows
3. Install dependencies: <br>

        pip install -r requirements.txt

4. pip install -r requirements.txt

        python app.py

5. Access the app:
    Open your browser and go to:

       http://127.0.0.1:5000/

## 🏆 Model Performance
Best Model: Random Forest Classifier

Hyperparameter Tuning: RandomizedSearchCV

Accuracy Achieved: 91%

## 📁 Folder Structure

    heart-health-predictor/
    │
    ├── static/              # CSS, JS, Images
    ├── templates/           # HTML templates
    ├── dataset/             # Heart dataset
    ├── app.py               # Flask application
    ├── model.pkl            # Trained Random Forest model
    ├── requirements.txt     # Python dependencies
    └── README.md            # Project documentation
