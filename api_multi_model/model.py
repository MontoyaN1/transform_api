import requests
import streamlit as st
from io import BytesIO


models = {
    "Microsoft/git-base-textcaps": {
        "REST_API_URL": "microsoft/git-base-textcaps",
    },
    "Salesforce/blip-image-captioning-base": {
        "REST_API_URL": "Salesforce/blip-image-captioning-base",
    },
    "Nlpconnect/vit-gpt2-image-captioning": {
        "REST_API_URL": "nlpconnect/vit-gpt2-image-captioning",
    },
    "Ayansk11/Image_Caption_using_ViT_GPT2": {
        "REST_API_URL": "Ayansk11/Image_Caption_using_ViT_GPT2",
    },
}


def query_answer(image, api_url):
    try:
        headers = {"Authorization": "Bearer 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"}
        API_URL = "https://api-inference.huggingface.co/models/" + api_url

        buffer = BytesIO()
        image.save(buffer, format="JPEG")  # Guarda la imagen como JPEG en el buffer
        buffer.seek(0)  # Regresar el cursor al inicio del buffer
        data = buffer.read()

        response = requests.post(API_URL, headers=headers, data=data)
        output = response.json()
        return output[0]["generated_text"]

    except Exception as e:
        st.error(f"Ocurrió un error: {str(e)}")
        return None
