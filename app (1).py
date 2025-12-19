import streamlit as st
import pickle
import numpy as np

st.set_page_config(page_title="Smart Loan Advisor", layout="centered")

model = pickle.load(open("loan_model.pkl", "rb"))
columns = pickle.load(open("columns.pkl", "rb"))

st.markdown("<h1 style='text-align:center;'>💳 Smart AI Loan Advisor</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>AI-powered eligibility & financial guidance</p>", unsafe_allow_html=True)

st.divider()

income = st.slider("💰 Monthly Income", 1000, 100000, 30000)
loan = st.slider("🏦 Loan Amount", 1000, 200000, 50000)
credit = st.selectbox("📊 Credit History", ["Good", "Bad"])

credit_val = 1 if credit == "Good" else 0

if st.button("🔍 Check Eligibility"):
    input_data = np.zeros(len(columns))
    input_data[0] = income
    input_data[1] = loan
    input_data[2] = credit_val

    prob = model.predict_proba([input_data])[0][1]
    score = int(prob * 100)

    st.subheader("📈 Loan Eligibility Score")
    st.progress(score)

    if score >= 70:
        st.success("✅ High chance of Loan Approval")
    elif score >= 40:
        st.warning("⚠️ Medium chance – Improve profile")
    else:
        st.error("❌ Low chance of Approval")

    st.subheader("🧠 AI Advice")
    if credit_val == 0:
        st.info("Improve your credit history to increase approval chances.")
    if loan > income * 0.6:
        st.info("Requested loan amount is high compared to income.")
    if score >= 70:
        st.info("Your financial profile looks strong.")

st.divider()
st.caption("🚀 AI-based Financial Decision Support System")
