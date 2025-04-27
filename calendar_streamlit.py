import streamlit as st
import pandas as pd

# Načteme soubor
df = pd.read_csv("final_IMPORT_2025.csv")

st.title("🇩🇪 Německé svátky 2025")

# Ukážeme tabulku
st.dataframe(df)

# Možnost stáhnout CSV
st.download_button(
    label="📥 Stáhnout CSV",
    data=df.to_csv(index=False).encode('utf-8'),
    file_name='svatky_de_2025.csv',
    mime='text/csv'
)
