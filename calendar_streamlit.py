import streamlit as st
import pandas as pd
from streamlit_calendar import calendar

# Načteme data
df = pd.read_csv("final_IMPORT_2025.csv")

st.title("🇩🇪 Německé svátky 2025")

# Převod dat na formát pro kalendář
events = []
for _, row in df.iterrows():
    events.append({
        "title": row["Subject"],
        "start": row["Start Date"],
        "end": row["Start Date"],
        "description": row["Description"]
    })

# Zobrazíme kalendář
calendar_options = {
    "initialView": "dayGridMonth",
    "locale": "de",  # Němčina
    "height": 600,
    "events": events
}

calendar(calendar_options, key="de-calendar")

# Možnost stáhnout CSV
st.download_button(
    label="📥 Stáhnout CSV",
    data=df.to_csv(index=False).encode('utf-8'),
    file_name='svatky_de_2025_final.csv',
    mime='text/csv'
)

