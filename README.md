
# Energy Consumption Predictor

The **Energy Consumption Predictor** is an AI-powered web application that predicts **household energy consumption (in kWh)** based on environmental conditions and usage patterns.
This project demonstrates a complete **end-to-end machine learning pipeline**, integrated with a **Flask-based web application**, making it suitable for both academic evaluation and portfolio presentation.


## Project Overview

* Predicts residential energy consumption accurately
* Uses a trained **machine learning regression model**
* Provides predictions through an interactive web interface
* Designed for **academic projects, internships, and portfolios**


## Key Features

* Uses a **Random Forest Regressor** for energy prediction
* Clean and simple **Flask-based frontend form**
* Accepts intuitive and user-friendly inputs
* Displays prediction results instantly after form submission


## Input Parameters

* Average Temperature (°C)
* Number of Occupants
* Air Conditioner Usage (Yes / No)
* Date


## Why These Inputs Were Selected

* **Temperature** has a direct impact on heating and cooling energy usage
* **Occupants** influence total electricity demand inside a household
* **Air Conditioner usage** is one of the highest contributors to energy consumption
* **Date-based features** help capture weekday behavior and seasonal patterns

These features ensure the model remains **simple, interpretable, and effective**, while maintaining good predictive performance.

## Technologies Used

* **Python 3.8**
* **Flask** for web application deployment
* **Pandas** for data processing
* **NumPy** for numerical computation
* **Scikit-learn** for model training and evaluation
* **Pickle** for model serialization
* **HTML & CSS** for frontend design

## Setup Instructions

It is recommended to create and use a **Python virtual environment** before running the project.

### 1. Clone the Repository

```bash
git clone https://github.com/Hari-10AI/energy-consumption-prediction.git
cd energy-consumption-predictor
```



### 2. Create and Activate a Virtual Environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```



### 3. Install Required Dependencies

```bash
pip install -r requirements.txt
```



### 4. Preprocess the Dataset

```bash
python src/data_preprocessing.py
python src/feature_engineering.py
```



### 5. Train the Machine Learning Model

```bash
python src/train_model.py
```



### 6. Run the Flask Application

```bash
python app.py
```



### 7. Open the Application in Your Browser

```bash
http://127.0.0.1:5000/
```



## Preview

![alt text](<preview.png>)







