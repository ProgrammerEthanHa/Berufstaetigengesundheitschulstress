import streamlit as st
import pandas as pd
import altair as alt

st.header("Gestresstes Deutschland")
st.subheader("Berufstätige im Gesundheits- und Pflegebereich")

source = pd.DataFrame({
        'Anteil (%)': [60, 91],
        'Betroffen': ['Stress davor', 'Seit Corona']
})
bar_chart = alt.Chart(source).mark_bar().encode(
        y='Anteil (%):Q',
        x='Betroffen:O',
    )
st.altair_chart(bar_chart, use_container_width=True)


txt = st.text_area('', '''
    2020; Basis: 2158 Personen
    ''')
st.text("Klicke an die Balken um die Daten genauer anzuschauen. Du kannst auch die Diagramm vergrößern und ein Bild davon machen")
st.text("Quelle: Swiss Life Deutschland und Yougov Deutschland")