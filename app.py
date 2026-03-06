import streamlit as st

st.title("UPSI VBE & SC Evaluation System")

st.header("User Information")

role = st.selectbox(
"Select Role",
["Supervisor", "Internal Examiner", "Programme Coordinator"]
)

faculty = st.selectbox(
"Select Faculty",
[
"Fakulti Sains",
"Fakulti Bahasa",
"Fakulti Teknikal",
"Fakulti Seni",
"Fakulti Pendidikan"
]
)

st.write("Role:", role)
st.write("Faculty:", faculty)
