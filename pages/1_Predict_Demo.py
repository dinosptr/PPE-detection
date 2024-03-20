import streamlit as st
import torch
from PIL import Image
from ultralytics import YOLO

def main():
    # Judul aplikasi
    st.title("Deteksi PPE (Personal Protective Equipment)")

    # Sidebar untuk memilih jenis input (gambar atau video) dan mengatur confidence threshold
    st.sidebar.title("Options")
    input_type = st.sidebar.selectbox("Select Input Type", ["Image", "Video"])
    confidence_threshold = st.sidebar.slider("Confidence Threshold", min_value=0.0, max_value=1.0, value=0.5, step=0.05)

    # Bagian untuk mengunggah gambar atau video
    upload_icon = ":camera:"
    uploaded_file = st.file_uploader(f"{upload_icon} Unggah Gambar PPE (Personal Protective Equipment)", type=["jpg", "jpeg", "png"])

    if input_type == "Image":
        if uploaded_file is not None:
            # Pesan untuk memberi tahu pengguna bahwa gambar sedang diproses
            st.info("Sedang memproses gambar...")

            # Load model
            model = YOLO('model/best.pt')  # pretrained YOLOv8n model

            # Baca gambar
            image = Image.open(uploaded_file)

            # Jalankan inferensi pada gambar dengan confidence threshold yang ditetapkan
            results = model(image, conf=confidence_threshold)  # return a list of Results objects
            for result in results:
                result.save(filename='result.jpg')

            # Tampilkan hasil deteksi
            image = Image.open('result.jpg')
            st.image(image, caption='Result PPE Detection', use_column_width=True)

    elif input_type == "Video":
        # Pesan untuk memberi tahu pengguna bahwa fitur video belum diimplementasikan
        st.info("Fitur video belum diimplementasikan. Silakan pilih input gambar.")

if __name__ == "__main__":
    main()
