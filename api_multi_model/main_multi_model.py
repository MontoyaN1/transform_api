import streamlit as st
from model import models, query_answer
from PIL import Image


st.set_page_config(page_title="Imagen a texto", page_icon="🔍", layout="wide")


st.title("Obten una descripción de una imagen por parte del modelo")


image_file = st.file_uploader("Selecciona una imagen", type=["jpg", "jpeg", "png"])


model_selection = st.selectbox(
    "Elige un modelo para describir la imagen:", list(models.keys())
)

if image_file is not None:
    image = Image.open(image_file)
    st.image(image, caption="Imagen cargada", use_container_width=True)

    with st.spinner(f"Procesando con {model_selection}..."):
        st.success(query_answer(image, models[model_selection]["REST_API_URL"]))
