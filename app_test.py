# python -m venv .venv --> bikin environment
# .venv\Scripts\activate --> aktivasi environment di Windows atau 
# source .venv/bin/activate -> untuk linux / Mac
# pip install streamlit --> install streamlit
# jika install langsung dari requirements.txt --> pip install -r requirements.txt
# streamlit run namafile.py --> running

import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
		page_title = 'Iris',
		layout = 'wide',
	)

st.title('Iris Data Analysis done by Karel Widjaja')

with st.sidebar:
	st.header('Ini adalah Sidebar, silahkan pilih opsi dibawah:')
	st.markdown('**Pilih Species**')
	check_setosa = st.checkbox('Iris-setosa', value=True)
	check_versicolor = st.checkbox('Iris-versicolor', value=True)
	check_virginica = st.checkbox('Iris-virginica', value=True)

	species = []
	if check_setosa:
		species.append('Iris-setosa')
	if check_versicolor:
		species.append('Iris-versicolor')
	if check_virginica:
		species.append('Iris-virginica')
	
	st.markdown('**Pilih Variabel**')
	var1 = st.radio('Variabel Utama',
			('SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm')
		)
	var2 = st.radio('Variabel Sekunder',
			('SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm')
		)

data = pd.read_csv('iris_data.csv')
data = data.query('Species in @species')

col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

with col1:
	st.dataframe(data)

with col2:
	fig_pie = px.pie(data, names='Species')
	st.plotly_chart(fig_pie, use_container_width=True)

with col3:
	fig_box = px.box(data, x=var1, color='Species')
	st.plotly_chart(fig_box, use_container_width=True)

with col4:
	fig_scatter = px.scatter(data, x=var1, y=var2, color='Species')
	st.plotly_chart(fig_scatter, use_container_width=True)
