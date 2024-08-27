# Inicio

import requests as rq
import streamlit as st

def buscar_letra(banda, musica):
    endpoint = f"https://api.lyrics.ovh/v1/{banda}/{musica}"
    response = rq.get(endpoint)
    letra = response.json()["lyrics"] if response.status_code == 200 else ""
    return letra

st.image("https://i.imgur.com/SmktDIH.png")
st.title("Letas de Músicas")

banda = st.text_input("Nome da banda: ", key="banda")
musica = st.text_input("Titulo da música: ", key="musica")
buscar = st.button("Buscar")

if buscar:
    letra = buscar_letra(banda, musica)
    if letra:
        st.success(f"Aqui esta a letra da música '{musica}' da banda '{banda}'.")
        st.text("")
        st.text(letra)
        st.balloons()
    else:
        st.error(f"Não encontramos a letra da música '{musica}' da banda '{banda}'.")
        
# Fim