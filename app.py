import streamlit as st
import numpy as np
import json
import tensorflow as tf
import torch
from PIL import Image

from transformers import DistilBertTokenizerFast, DistilBertForSequenceClassification
from pytorch_tabnet.tab_model import TabNetClassifier


# =========================
# LOAD MODEL (CACHE)
# =========================

@st.cache_resource
def load_image_model():
    return tf.keras.models.load_model(
        "model_yoga_pose",
        compile=False
    )

@st.cache_resource
def load_class_names():
    with open("class_indices.json") as f:
        class_dict = json.load(f)
    # balik index → label
    return {int(v): k for k, v in class_dict.items()}

@st.cache_resource
def load_text_model():
    tokenizer = DistilBertTokenizerFast.from_pretrained(
        "model_kegiatan2_distilbert"
    )
    model = DistilBertForSequenceClassification.from_pretrained(
        "model_kegiatan2_distilbert"
    )
    return tokenizer, model

@st.cache_resource
def load_tabnet_model():
    clf = TabNetClassifier()
    clf.load_model("model_kegiatan3_tabnet.zip")
    return clf


image_model = load_image_model()
class_names = load_class_names()
tokenizer, text_model = load_text_model()
tabnet_model = load_tabnet_model()


# =========================
# SIDEBAR
# =========================

st.sidebar.title("📊 Dashboard Modul 6")
menu = st.sidebar.selectbox(
    "Pilih Model",
    ["Klasifikasi Citra", "Klasifikasi Teks", "Klasifikasi Tabular"]
)


# =========================
# KLASIFIKASI CITRA (POSE YOGA)
# =========================

if menu == "Klasifikasi Citra":
    st.title("🧘 Klasifikasi Pose Yoga")

    file = st.file_uploader(
        "Upload gambar pose yoga",
        type=["jpg", "jpeg", "png"]
    )

    if file:
        img = Image.open(file).convert("RGB")
        st.image(img, caption="Gambar Input", use_column_width=True)

        # Preprocessing
        img = img.resize((224, 224))
        arr = np.array(img) / 255.0
        arr = np.expand_dims(arr, axis=0)

        if st.button("🔍 Prediksi"):
            with st.spinner("Memproses gambar..."):
                preds = image_model.predict(arr)
                idx = np.argmax(preds)
                conf = np.max(preds) * 100

            st.success(f"🧠 Pose Yoga: **{class_names[idx]}**")
            st.write(f"📈 Confidence: **{conf:.2f}%**")

            st.subheader("📊 Probabilitas Kelas")
            for i, prob in enumerate(preds[0]):
                st.write(f"{class_names[i]}: {prob*100:.2f}%")
