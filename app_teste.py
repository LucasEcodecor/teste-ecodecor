import streamlit as st

st.set_page_config(page_title="Teste Eco Decor", page_icon="🧪")

st.title("🚀 Sistema de Teste - Eco Decor")
st.write("Se você está vendo esta tela, significa que o GitHub e o Streamlit estão conversando perfeitamente!")

if st.button("Aperte o botão para testar"):
    st.balloons()
    st.success("Tudo funcionando 100%!")