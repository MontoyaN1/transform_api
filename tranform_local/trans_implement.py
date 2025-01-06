from transformers import YolosImageProcessor, YolosForObjectDetection
import torch
import streamlit as st
import matplotlib.pyplot as plt


model = YolosForObjectDetection.from_pretrained("hustvl/yolos-tiny")
image_processor = YolosImageProcessor.from_pretrained("hustvl/yolos-tiny")


def objetc_detetion(image):
    try:
        st.text("Procesando la imagen...")

        inputs = image_processor(images=image, return_tensors="pt")
        outputs = model(**inputs)

        target_sizes = torch.tensor([image.size[::-1]])
        results = image_processor.post_process_object_detection(
            outputs, threshold=0.5, target_sizes=target_sizes
        )[0]

        if len(results["scores"]) == 0:
            st.warning("No se detectaron objetos en la imagen.")
            return
        labels = []
        scores = []

        for score, label, box in zip(
            results["scores"], results["labels"], results["boxes"]
        ):
            box = [round(i, 2) for i in box.tolist()]
            labels.append(model.config.id2label[label.item()])
            scores.append(round(score.item(), 3))

        if labels and scores:
            fig, ax = plt.subplots()
            ax.barh(labels, scores, color="skyblue")
            ax.set_xlabel("Confianza")
            ax.set_ylabel("Objeto Detectado")
            ax.set_title("Resultados de Detección de Objetos")
            st.pyplot(fig)
        else:
            st.warning("No se detectaron objetos con la confianza requerida.")

    except Exception as e:
        st.error(f"Ocurrió un error: {str(e)}")
