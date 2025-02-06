import streamlit as st
import google.generativeai as genai
import os

# Configuração da API Gemini
gemini_api_key = os.getenv("GEM_API_KEY")
genai.configure(api_key=gemini_api_key)
modelo_linguagem = genai.GenerativeModel("gemini-1.5-flash")

def osint_report():
    st.subheader("Intelligence Report Generator")

    # Input do usuário
    intelligence = st.text_area("Write here the information for your report:")
    
    # Botão para gerar o relatório
    if st.button("Generate intelligence report"):
        if intelligence.strip():  # Verifica se o input não está vazio
            with st.spinner("Generating..."):
                prompt = f"""
                You are a highly skilled intelligence report writer. The user has written notes based on an interview with a person of interest.
                Your goal is to write an intelligence report based on these notes, following the format of the previous report.

                Notes:
                {intelligence}
                """

                # Gera o relatório com Gemini
                try:
                    response = modelo_linguagem.generate_content(prompt)
                    
                    # Verifica se a resposta foi gerada corretamente
                    if response and hasattr(response, 'text'):
                        osint_report_output = response.text
                    elif response and hasattr(response, 'candidates'):
                        osint_report_output = response.candidates[0].content
                    else:
                        osint_report_output = "Error: No valid response generated."
                
                except Exception as e:
                    osint_report_output = f"Error generating report: {e}"
                
                # Exibe o relatório no Streamlit
                st.subheader("Generated Intelligence Report")
                st.markdown(osint_report_output)

        else:
            st.warning("Please enter some text to generate the report.")

# Executa a função principal
osint_report()
