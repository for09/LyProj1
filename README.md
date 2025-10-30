# Financial Data Analysis & Stock Trend Prediction

## 📌 Overview
This project provides an **end-to-end workflow** for analyzing and predicting stock market trends using key technical indicators:  

- **Exponential Moving Average (EMA)**  
- **Simple Moving Average (SMA)**  
- **Relative Strength Index (RSI)**  
- **On Balance Volume (OBV)**  

The pipeline covers **data ingestion, preprocessing, feature engineering, exploratory data analysis (EDA), model training, and evaluation**. Modular Python scripts and Jupyter notebooks ensure **reproducibility, scalability, and ease of experimentation**.

---

## 📂 Repository Structure
LyProj1-main/
├── data/
│ ├── raw/ # Raw dataset (data.csv)
│ ├── processed/ # Cleaned & feature-engineered data
│ ├── EMA.csv
│ ├── SMA.csv
│ ├── RSI.csv
│ ├── OBV.csv
│ ├── feature_engineered.csv
│ └── preprocessed_data.csv
├── notebooks/ # Jupyter notebooks for EDA and modeling
│ ├── EDA.ipynb
│ ├── Exponential_Moving_Average.ipynb
│ ├── Simple_Moving_Average.ipynb
│ ├── RSI.ipynb
│ ├── On_Balance_Volume.ipynb
│ ├── model_training.ipynb
│ └── rough.ipynb
├── src/ # Python scripts for the pipeline
│ ├── data_ingestion.py
│ ├── data_preprocessing.py
│ ├── feature_engineering.py
│ ├── model.py
│ ├── model_evaluation.py
│ ├── split_data.py
│ └── main.py
└── individual_feature_engineering/
├── EMA.py
├── SMA.py
├── RSI.py
└── OBV.py


---

## ⚙ Features
- **Data ingestion** from raw CSV files  
- **Preprocessing**: cleaning, formatting, and handling missing values  
- **Feature engineering** using EMA, SMA, RSI, and OBV  
- **Exploratory Data Analysis (EDA)** via Jupyter notebooks  
- **Machine learning model training and evaluation**  
- **Modular structure** for scalability and reproducibility  

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+  
- Jupyter Notebook  

Install dependencies:
```bash
pip install -r requirements.txt
Running the Pipeline

Place your raw financial dataset in data/raw/data.csv.

Preprocess data:

python src/data_preprocessing.py


Generate features:

python src/feature_engineering.py


Train and evaluate model:

python src/main.py

📊 Notebooks

EDA.ipynb – Exploratory data analysis

Indicator Notebooks – Individual feature explorations (EMA, SMA, RSI, OBV)

model_training.ipynb – Model experiments, results, and evaluation

🔮 Applications

Stock trend prediction

Technical analysis for trading strategies

Feature engineering demonstrations in finance

Educational purposes: applying machine learning to time series

📜 License

This project is for educational and research purposes. Modify and use freely for learning or prototyping.
