import streamlit as st
import requests
import json
import BuscarCep
import pandas as pd


##### TÍTULO DA APLICAÇÃO #####

###### COLOCA UM TITULO
st. sidebar. title("Busca Cep")
st.sidebar.image("logo.png")
st.sidebar.write(" O que você deseja?!")
opcoes = ["Buscar CEP", "Descobrir CEP"]
opcao = st.sidebar.selectbox("Selecione a opcao desejada:", opcoes)
##### Lista de Opções #####


st.title("busca cep")
if opcao == "Buscar CEP":
    st.image("principal.png")
    cep = st.text_input(f"qual seu CEP?")
    if st.button('Buscar'):
        if len(cep) != 8 or not cep.isdigit():
            st.error("Por favor, insira um CEP válido com 8 dígitos numéricos.")
        else:
            try:
                endereco = BuscarCep.buscar_cep(cep)
                if endereco:
                    st.success("Endereco encontrado:")
                    st.write(f"CEP {endereco[0]}")
                    st.write(f"Endereco: {endereco[1]}")
                    st.write(f"Bairro:{endereco[2]} ")
                    st.write(f"Cidade {endereco[3]}")
                    st.write(f"Estado {endereco[4]}")



                    st.title("Localização no mapa")
                    df = pd.DataFrame({"latitude": [endereco[5]], "longitude": [endereco[6]]})
                    st.map(df, zoom=15)
                else:
                    st.error("CEP NÃO ENCONTRADO.")
            except Exception as e :
                st.error(f"Ocorreu um erro ao buscar o cep :{e}")




elif opcao == "Descobrir CEP":
    st.image("Descobrir.png")


elif opcao == "Descobrir CEP":
    st.header("Descobrir CEP pelo endereço")
    endereco_usuario = st.text_input("Digite o endereço (ex: Rua Olga, Barueri, SP)")