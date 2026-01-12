import streamlit as st
import pandas as pd
from reni_tool import reni_predict_tool, FEATURES_ORDER

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(page_title="Reni - Renal Health Assistant", page_icon="🩺", layout="wide")

# Estilo personalizado para la personalidad de Reni
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #007bff; color: white; }
    </style>
    """, unsafe_allow_html=True)

# --- PROTOCOLO DE BIENVENIDA (PERSONALIDAD) ---
st.title("🩺 Reni | Renal Health Assistant")
st.markdown(f"**Hello, Doctor.** Reni here, ready to assist you with your patient's renal assessment. Please provide the clinical data whenever you are ready.")

# --- FORMULARIO DE DATOS ---
with st.form("clinical_data_form"):
    st.subheader("📋 Clinical Data Entry")
    
    # Organizamos los 26 campos en 3 columnas para que no sea eterno el scroll
    col1, col2, col3 = st.columns(3)
    
    data = {}
    
    with col1:
        st.info("General & History")
        data['Age'] = st.number_input("Age", min_value=1, max_value=120, value=40)
        data['Hypertension'] = st.selectbox("Hypertension", [0, 1], format_func=lambda x: "Yes" if x==1 else "No")
        data['DiabetesMellitus'] = st.selectbox("Diabetes Mellitus", [0, 1], format_func=lambda x: "Yes" if x==1 else "No")
        data['CoronaryArteryDisease'] = st.selectbox("Coronary Artery Disease", [0, 1], format_func=lambda x: "Yes" if x==1 else "No")
        data['Appetite'] = st.selectbox("Appetite", [0, 1], format_func=lambda x: "Poor" if x==0 else "Good")
        data['Anemia'] = st.selectbox("Anemia", [0, 1], format_func=lambda x: "Yes" if x==1 else "No")
        data['PedaEdema'] = st.selectbox("Peda Edema", [0, 1], format_func=lambda x: "Yes" if x==1 else "No")

    with col2:
        st.info("Vitals & Urine")
        data['BloodPressure'] = st.selectbox("High Blood Pressure?", [0, 1], format_func=lambda x: "Yes" if x==1 else "No")
        data['BloodPressureLimit'] = st.selectbox("BP Level", [0, 1, 2], format_func=lambda x: ["Normal", "Low", "High"][x])
        data['SpecificGravity'] = st.select_slider("Specific Gravity", options=[1.005, 1.010, 1.015, 1.020, 1.025])
        data['Albumin'] = st.slider("Albumin (Urine)", 0, 5, 0)
        data['SugarLevel'] = st.slider("Sugar Level (Urine)", 0, 5, 0)
        data['RedBloodCells'] = st.selectbox("Red Blood Cells", [0, 1], format_func=lambda x: "Normal" if x==1 else "Abnormal")
        data['PusCell'] = st.selectbox("Pus Cell", [0, 1], format_func=lambda x: "Normal" if x==1 else "Abnormal")
        data['PusCellClumps'] = st.selectbox("Pus Cell Clumps", [0, 1], format_func=lambda x: "Present" if x==1 else "Not Present")
        data['Bacteria'] = st.selectbox("Bacteria", [0, 1], format_func=lambda x: "Present" if x==1 else "Not Present")

    with col3:
        st.info("Laboratory (Blood)")
        data['BloodGlucoseRandom'] = st.number_input("Blood Glucose Random", value=120.0)
        data['BloodUrea'] = st.number_input("Blood Urea", value=36.0)
        data['SerumCreatinine'] = st.number_input("Serum Creatinine", value=1.2)
        data['Sodium'] = st.number_input("Sodium", value=138.0)
        data['Potassium'] = st.number_input("Potassium", value=4.4)
        data['Hemoglobin'] = st.number_input("Hemoglobin", value=15.4)
        data['PackedCellVolume'] = st.number_input("Packed Cell Volume", value=44.0)
        data['WhiteBloodCellCount'] = st.number_input("White Blood Cell Count", value=7800)
        data['RedBloodCellCount'] = st.number_input("Red Blood Cell Count", value=5.2)
        data['GlomerularRatio'] = st.number_input("Glomerular Ratio (eGFR)", value=90.0)

    submitted = st.form_submit_button("Analyze Patient Status")

# --- LÓGICA DE PROCESAMIENTO ---
if submitted:
    # Feedback interactivo de Reni
    with st.spinner("I have received the lab results. Let me analyze the CKD status for you..."):
        result = reni_predict_tool(data)
    
    if "error" in result:
        st.error(f"Analysis failed: {result['error']}")
    else:
        status = result['status']
        stage = result['stage']
        
        st.divider()
        
        if status == "AFFECTED":
            st.warning("### ⚠️ STAFF REPORT: ACTION REQUIRED")
            col_a, col_b = st.columns(2)
            col_a.metric("Status", status)
            col_b.metric("CKD Stage", f"Stage {stage}")
            st.write("Doctor, the analysis indicates Chronic Kidney Disease. I show professional concern regarding these values. Immediate clinical intervention is advised.")
        else:
            st.success("### ✅ STAFF REPORT: NORMAL RANGE")
            st.metric("Status", status)
            st.write("I am happy to report that the patient appears to be within normal parameters. However, please maintain professional caution and continue monitoring.")

st.sidebar.markdown("---")
st.sidebar.write("👨‍⚕️ **Medical Session Active**")
st.sidebar.write(f"Logged as: Senior Doctor")