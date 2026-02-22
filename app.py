import streamlit as st
import pandas as pd

st.set_page_config(page_title="Excel Previewer", layout="wide")
st.title("Excel Upload & Preview")

uploaded_file = st.file_uploader("Upload an Excel file", type=["xls", "xlsx"])
if uploaded_file is not None:
    try:
        excel_data = pd.read_excel(uploaded_file, sheet_name=None)
        sheet_names = list(excel_data.keys())
        sheet = st.selectbox("Select sheet", sheet_names)
        df = excel_data[sheet]
        st.write(f"Preview of sheet: **{sheet}** — shape: {df.shape}")
        st.dataframe(df)
        if st.checkbox("Show raw data as table"):
            st.table(df)
    except Exception as e:
        st.error(f"Could not read the Excel file: {e}")
else:
    st.info("Upload an Excel file to preview its contents.")
