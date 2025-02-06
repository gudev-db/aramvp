

import streamlit as st
import google.generativeai as genai
import uuid
from pymongo import MongoClient
import os

# Configuração do Gemini API
gemini_api_key = os.getenv("GEM_API_KEY")
genai.configure(api_key=gemini_api_key)
modelo_linguagem = genai.GenerativeModel("gemini-1.5-flash")




def gerar_relatorio(intelligence):
    prompt = f"""
                You are a highly skilled intelligence report writer. The user has written notes based on an interview with a person of interest.
                Your goal is to write an intelligence report based on these notes, following the format of the previous report.

                Notes:
                {intelligence}
                """
    output = modelo_linguagem.generate_content(prompt).text
    return output

def relatorio_inteligencia_page():
    st.subheader('Geração de Relatório de Inteligência')
    
    intelligence = st.text_input('Nome da Empresa:')
   
    
    if st.button('Gerar Relatório'):
        with st.spinner('Gerando relatório de inteligência...'):
            relatorio_output = gerar_relatorio(
                intelligence
            )
            
            st.header('Relatório de Inteligência Estratégica')
            st.markdown(relatorio_output)


if __name__ == "__main__":
    relatorio_inteligencia_page()
