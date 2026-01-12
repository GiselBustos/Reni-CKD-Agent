> [!WARNING]
> ⚠️ **WORK IN PROGRESS!** 
>   This project is not finished, it is under development and contains errors. 

# 🩺 Reni: Renal Health Assistant Agent

**Reni** is a specialized clinical decision support agent designed to assist healthcare professionals in the early detection and staging of **Chronic Kidney Disease (CKD)**. By integrating Machine Learning models with a professional, collaborative personality, Reni provides a seamless interface for clinical data analysis.

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

---

## 🌟 Key Features

### 1. Dual-Intelligence Engine

Reni utilizes two distinct Machine Learning models for high-precision results:

* **Classification Model (LDA):** Determines if the patient is *"Affected"* or *"Not Affected"* by CKD.
* **Staging Model (Decision Tree):** Predicts the specific clinical stage for affected patients.

### 2. Availability

* **Streamlit Web App:** A clean, form-based dashboard for detailed data entry and visual reporting.

### 3. Medical Persona

Reni acts as a **Senior Clinical Assistant**, following a strict protocol:

* **Professional Greeting:** Acknowledges the medical session.
* **Interactive Feedback:** Confirms data receipt before processing.
* **Clinical Concern:** Adapts tone based on severity (showing professional concern for positive results).

---

## 🧠 Clinical Variables

Reni analyzes **26 key clinical parameters**, including:

| Category | Variables |
| :--- | :--- |
| **Laboratory Data** | Serum Creatinine, Hemoglobin, eGFR (Glomerular Ratio), Sodium, Potassium, Albumin. |
| **Vital Signs** | Blood Pressure, Specific Gravity, Sugar Level. |
| **Medical History** | Hypertension, Diabetes Mellitus, Coronary Artery Disease, Anemia, Appetite. |

---

## 🛠️ Tech Stack

* **Core:** Python 3.9+
* **Machine Learning:** Scikit-learn, Joblib, Pandas, Numpy.
* **Bot Framework:** `python-telegram-bot` (Asynchronous).
* **Web Framework:** `Streamlit`.

---
> [!CAUTION]
> Reni is an Educational and Support Tool. It is designed to assist clinicians, not to replace professional medical judgment, diagnosis, or treatment. All predictions must be verified with gold-standard laboratory tests and expert clinical observation.
