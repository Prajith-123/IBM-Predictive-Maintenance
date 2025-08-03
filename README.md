# 🔧 Predictive Maintenance – IBM Cloud ML App

This project is a machine learning–powered **Predictive Maintenance System** deployed on **IBM Cloud** and hosted using **Streamlit Cloud**. The model classifies the type of industrial machine failure using real-time sensor data.

> 🎯 Built for IBM Cloud (Lite Tier) — using AutoAI, Deployment API, and Streamlit

---

## 🚀 Live App

Try the app here:  
👉 [https://ibm-predictive-maintenance-iapksscqst65g9fwxb7ucq.streamlit.app/](https://ibm-predictive-maintenance-iapksscqst65g9fwxb7ucq.streamlit.app/)

---

## 🧠 Problem Statement

> **Predictive Maintenance of Industrial Machinery**  
Use machine learning to anticipate failures in industrial machines (e.g., tool wear, heat dissipation, power failure) before they happen. This helps reduce downtime and operational costs through proactive maintenance.

---

## 🗂 Tech Stack

| Layer | Tools Used |
|-------|------------|
| ML Model | IBM AutoAI (Classification) |
| Backend | IBM Cloud Deployment (Watsonx.ai) |
| Frontend | Streamlit App |
| Hosting | Streamlit Cloud |
| Data Source | [Kaggle Dataset](https://www.kaggle.com/datasets/shivamb/machine-predictive-maintenance-classification) |

---

## 🧾 Features

- Takes real-time machine sensor input
- Calls IBM-hosted ML model via secure API
- Displays predicted **Failure Type** immediately
- 100% serverless and cloud-native
- IBM Cloud + Streamlit = lightweight deployment

---

## 🖼 App Preview

<img width="1919" height="1079" alt="Screenshot 2025-08-03 225526" src="https://github.com/user-attachments/assets/d3a1d99e-7121-47f9-9f47-72a4bb5e85af" />


---

## 📦 Project Root  
├── app.py                # Main Streamlit application  
├── requirements.txt      # Python dependencies  
├── .streamlit/  
│   └── secrets.toml      # API keys and secrets (not shared or committed)  

---

## 🧪 How to Run Locally

```bash
git clone https://github.com/<your-username>/ibm-predictive-maintenance.git
cd ibm-predictive-maintenance
pip install -r requirements.txt
streamlit run app.py

Add your API details in .streamlit/secrets.toml:
[general]
API_URL = "https://<your-deployment-endpoint>"
API_KEY = "<your-ibm-api-key>"

```

🌐 Tags
#IBMCloud #MachineLearning #PredictiveMaintenance #Streamlit #AutoAI #CloudDeployment #MCAProject
