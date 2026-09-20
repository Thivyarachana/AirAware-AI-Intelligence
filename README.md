# 🌿 AirAware — Urban Air Intelligence Platform

AirAware is an interactive data analytics platform that explores real-world urban air quality patterns using pollution, weather, time, and monitoring-station data.

## 🎯 Project Objective

The goal of AirAware is to transform complex air-quality data into understandable insights.

## 📊 Dataset

This project uses the Beijing Multi-Site Air Quality Dataset.

The dataset contains hourly observations collected from multiple monitoring stations between 2013 and 2017.

### Pollutants

- PM2.5
- PM10
- SO2
- NO2
- CO
- O3

### Environmental Variables

- Temperature
- Pressure
- Dew Point
- Rain
- Wind Direction
- Wind Speed

## 🚀 Features

### 🌱 Mission Control
Provides an overview of the dataset and major pollution trends.

### 📈 Pollution Patterns
Explore pollutant behavior by station, month, and hour.

### 🌦️ Weather & Pollution
Investigate relationships between environmental conditions and pollution levels.

### 📍 Station Intelligence
Compare pollution levels across monitoring stations.

### 🔬 Correlation Lab
Explore statistical relationships between pollutants and environmental variables.

### 🧪 Air Risk Simulator
Enter pollutant and environmental values to generate an educational screening score.

Note: The simulator is not an official AQI calculator, medical assessment, regulatory measurement, or emergency warning system.

### 📋 Data Quality
Explore missing values and dataset quality information.

## 🛠️ Technology Stack

- Python
- Pandas
- NumPy
- Plotly
- Streamlit
- Exploratory Data Analysis

## 📁 Project Structure

```text
AirAware/
├── app.py
├── requirements.txt
├── README.md
└── data/
    └── air_quality.csv
```

## ▶️ Run Locally

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

## 🔮 Future Development

AirAware can be extended into a real-time urban air intelligence system using:

- Live IoT air-quality sensors
- Real-time weather APIs
- Machine-learning pollution forecasting
- Location-based pollution alerts
- AQI forecasting
- Interactive city maps
- Cloud-based data pipelines
- Mobile applications

## 🌍 Vision

AirAware demonstrates how data analytics and AI can transform environmental data into accessible insights for smarter and more sustainable cities.