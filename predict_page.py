import streamlit as st
import pandas as pd

def show_predict_page():
    df = pd.read_csv("data3.csv")
    st.title("Software for Fish Availability Exploration in Dholi Fish Market")
    st.sidebar.image("https://upload.wikimedia.org/wikipedia/en/e/e1/Dr._Rajendra_Prasad_Central_Agriculture_University_Logo.png",
                     use_column_width=True)
    st.write("""### We need some information to fetch fish availability data""")

    date = st.number_input(
        "Enter Date in DDMMYYYY Format",
        min_value=0,
        max_value=100000000000,
        step=1
    )
    ok = st.button("Get Availability Data")
    if ok:
        value = df[df["Date"] == date]
        st.write(f"The Available Fish are:")
        st.dataframe(value)



