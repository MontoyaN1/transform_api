import streamlit as st
from create_quest import answer


st.set_page_config(
    page_title="Preguntas a modelo",
    page_icon="📝",
    layout="centered",
)

st.title("Preguntas y respuestas a un modelo")

st.header(
    "Haz tu pregunta y proporciona un contexto para que el modelo pueda respondes de la formas más correcta"
)


question = st.text_input(
    "Ingresa la pregunta que quieras hacer al modelo", placeholder="Escribe tu pregunta"
)


context = st.text_input(
    "Proporciona un contexto para una respuesta coherente a lo que quieres:",
    placeholder="Escribe el contexto de la pregunta",
)


if st.button("Enviar"):
    if question and context:
        st.write("")
        st.header("Respuesta: ")
        st.write("")
        st.write("")
        st.success(answer(question, context))
    else:
        st.warning("Es necesario una pregunta y contexto para generar una respuesta.")
