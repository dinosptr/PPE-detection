import streamlit as st
import torch
from PIL import Image
from ultralytics import YOLO
import cv2
from tempfile import NamedTemporaryFile
import os
import shutil


@st.cache_data
def process_image(uploaded_file, _model, confidence_threshold):
    # Baca gambar
    image = Image.open(uploaded_file)

    # Jalankan inferensi pada gambar dengan confidence threshold yang ditetapkan
    results = _model(image, conf=confidence_threshold)  # return a list of Results objects
    for result in results:
        result.save(filename='result.jpg')

    # Tampilkan hasil deteksi
    result_image = Image.open('result.jpg')
    return result_image


def save_uploaded_file(uploaded_file):
    # Create a directory if it doesn't exist
    os.makedirs("uploads", exist_ok=True)
    # Save the uploaded file to a location
    with open(os.path.join("uploads", uploaded_file.name), "wb") as f:
        f.write(uploaded_file.getbuffer())

def clear_directory(directory):
    # Pastikan direktori ada
    if os.path.exists(directory):
        # Hapus semua isi direktori
        shutil.rmtree(directory)

def _display_detected_frames(conf, model, st_frame, image, is_display_tracking=None, tracker=None):
    """
    Display the detected objects on a video frame using the YOLOv8 model.

    Args:
    - conf (float): Confidence threshold for object detection.
    - model (YoloV8): A YOLOv8 object detection model.
    - st_frame (Streamlit object): A Streamlit object to display the detected video.
    - image (numpy array): A numpy array representing the video frame.
    - is_display_tracking (bool): A flag indicating whether to display object tracking (default=None).

    Returns:
    None
    """

    # Resize the image to a standard size
    image = cv2.resize(image, (720, int(720*(9/16))))

    # Display object tracking, if specified
    if is_display_tracking:
        res = model.track(image, conf=conf, persist=True, tracker=tracker)
    else:
        # Predict the objects in the image using the YOLOv8 model
        res = model.predict(image, conf=conf)

    # # Plot the detected objects on the video frame
    res_plotted = res[0].plot()
    st_frame.image(res_plotted,
                   caption='Detected Video',
                   channels="BGR",
                   use_column_width=True
                   )

def main():
    # Sidebar untuk memilih jenis input (gambar atau video) dan mengatur confidence threshold
    st.sidebar.title("Options")
    input_type = st.sidebar.selectbox("Select Input Type", ["Image", "Video", "Webcam"])
    confidence_threshold = st.sidebar.slider("Confidence Threshold", min_value=0.0, max_value=1.0, value=0.5, step=0.05)

    if input_type == "Image":
        st.title("Deteksi PPE (Personal Protective Equipment)")
        # Bagian untuk mengunggah gambar atau video
        upload_icon = ":camera:"
        uploaded_file = st.file_uploader(f"{upload_icon} Unggah Gambar PPE (Personal Protective Equipment)", type=["jpg", "jpeg", "png"])
        if uploaded_file is not None:
            # Load _model
            model = YOLO('model/best.pt')  # pretrained YOLOv8n model

            # Proses gambar dengan menggunakan st.cache
            result_image = process_image(uploaded_file, model, confidence_threshold)

            # Tampilkan hasil deteksi
            st.image(result_image, caption='Result PPE Detection', use_column_width=True)

    elif input_type == "Video":
        # # Nama direktori yang akan dihapus
        # directories_to_clear = ["runs", "uploads"]

        # # Hapus semua isi dari setiap direktori yang ditentukan
        # for directory in directories_to_clear:
        #     clear_directory(directory)
        uploaded_video = st.file_uploader("Upload Video (Max 10MB)", type=["mp4"], accept_multiple_files=False)
        save_uploaded_file(uploaded_file)
        if uploaded_video is not None:
            video_bytes = uploaded_video.read()
            st.video(video_bytes)
    elif input_type == "Webcam":
        source_webcam = 0
        model = YOLO('model/best.pt')  # pretrained YOLOv8n model
        # is_display_tracker, tracker = display_tracker_options()
        try:
            vid_cap = cv2.VideoCapture(source_webcam)
            st_frame = st.empty()
            while (vid_cap.isOpened()):
                success, image = vid_cap.read()
                if success:
                    _display_detected_frames(0.25,
                                                model,
                                                st_frame,
                                                image,
                                                False,
                                                None,
                                                )
                else:
                    vid_cap.release()
                    break
        except Exception as e:
            st.sidebar.error("Error loading video: " + str(e))

if __name__ == "__main__":
    main()
