import requests
import streamlit as st

API_URL = "https://api-inference.huggingface.co/models/deepset/roberta-base-squad2"
headers = {"Authorization": "Bearer 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"}


def query(payload):
    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()
    except Exception as e:
        st.error(f"Ocurrió un error: {str(e)}")


def answer(question, context):
    output = query(
        {
            "inputs": {
                "question": question,
                "context": context,
            },
        }
    )
    return output['answer']
