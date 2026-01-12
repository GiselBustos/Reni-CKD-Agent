# ⚙️ Installation and Setup Guide (Streamlit Web Edition)

This guide provides the necessary steps to deploy and run **Reni**, the Renal Health Assistant, as a standalone Web Application.

---

## 📋 Prerequisites

Before you begin, ensure your environment meets these requirements:
* **Python:** version 3.9 or higher.
* **Git:** for version control and deployment.
* **Clinical Models:** Verify that `Class_model.joblib` and `Stage_model.joblib` are located in the project root directory.

---

## 🛠️ Local Installation

### 1. Environment Preparation
To keep your system clean, it is highly recommended to use a virtual environment:

```bash
# Create the virtual environment
python -m venv venv

# Activate the environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

```

### 2. Dependency Installation

Install the necessary libraries for Machine Learning and the Web Interface:

```bash

pip install -r requirements.txt

```

### 3. Model Verification

Your folder structure should look like this:

**RENI-PROJECT/**

* **app.py** → Main Web Interface
* **reni_tool.py** → AI Logic & Features
* **Class_model.joblib** → ML Classifier
* **Stage_model.joblib** → ML Staging model
* **requirements.txt** → Dependencies
* **README.md** → Project Overview
* **INSTALL.md** → Setup Guide

-------------

## 🤖 Running the Agent

To launch Reni locally, execute the following command in your terminal:

```bash
streamlit run app.py

```
--------------

## ☁️ Production Deployment (Streamlit Cloud)

Reni is optimized for 24/7 availability via Streamlit Cloud. To deploy:

1.- Push your code to GitHub: Ensure all .py and .joblib files are included.
2.- Connect to Streamlit Cloud: Log in at share.streamlit.io.
3.- Deploy: Select your repository and point the "Main file path" to app.py.
4.- Environment: The platform will read your requirements.txt and build the clinical environment automatically.

> [!CAUTION]
> ### Professional Medical Disclaimer
> **Reni is a clinical decision support tool intended for use by qualified healthcare professionals.**
> It is NOT a replacement for clinical judgment. All predictions should be verified against laboratory gold standards and the patient's overall clinical presentation.

