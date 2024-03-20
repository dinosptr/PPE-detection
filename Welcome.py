import streamlit as st

def main():
    st.title("Deteksi PPE (Personal Protective Equipment)")
    st.write("Selamat datang di aplikasi deteksi PPE (Personal Protective Equipment). Aplikasi ini bertujuan untuk mendeteksi apakah seseorang telah menggunakan peralatan pelindung diri (PPE) dengan benar atau tidak.")

    st.header("Business Understanding")
    st.subheader("Problem Statements :thinking:")
    st.write("Dalam lingkungan tertentu seperti tempat kerja, penggunaan PPE dengan benar sangat penting untuk melindungi diri dari risiko cedera atau penyakit. Namun, seringkali sulit untuk memastikan bahwa orang-orang telah menggunakan PPE secara tepat.")

    st.subheader("Goals :dart:")
    st.write("- Mengembangkan model deteksi PPE yang dapat mengidentifikasi apakah seseorang telah menggunakan PPE secara benar.")
    st.write("- Membuat aplikasi yang memungkinkan pengguna untuk mengunggah gambar dan mendapatkan prediksi apakah PPE digunakan dengan benar.")

    st.subheader("Solution Statements :computer:")
    st.write("Untuk mencapai tujuan tersebut, saya akan menggunakan teknik deteksi objek menggunakan model YOLO (You Only Look Once) dengan dua varian, yaitu YOLOv5 dan YOLOv8. Kedua model ini memiliki kinerja yang sangat baik dalam mendeteksi objek dalam gambar, termasuk deteksi PPE. YOLOv5 dan YOLOv8 adalah pilihan yang tepat untuk tugas deteksi PPE karena kecepatan yang tinggi dan akurasi yang baik.")
    st.write("Setelah mengembangkan model deteksi menggunakan YOLOv5 dan YOLOv8, saya akan membuat aplikasi web menggunakan Streamlit. Aplikasi ini akan memungkinkan pengguna untuk mengunggah gambar dan melihat apakah PPE digunakan dengan benar atau tidak.")

if __name__ == "__main__":
    main()
