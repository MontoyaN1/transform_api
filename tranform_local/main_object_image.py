import streamlit as st
from trans_implement import objetc_detetion
from PIL import Image

st.set_page_config(
    page_title="Detección de objetos",
    page_icon="🔍",
    layout="wide",
)

# Título de la aplicación
st.title("Detectar objetos en una imagen")

# Subida de imagen
st.subheader("Cargar una imagen:")
image_file = st.file_uploader("Selecciona una imagen", type=["jpg", "jpeg", "png"])


if image_file is not None:
    image = Image.open(image_file)
    st.image(image, caption="Imagen cargada", use_container_width=True)
    objetc_detetion(image)
