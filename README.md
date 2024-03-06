# Model Deteksi PPE/APD (Alat Pelindung Diri)

## Persyaratan Sistem
- **Sistem Operasi:** Windows, MacOS, atau Linux
- **Python 3.10**
- **Git**
- **Ruang Disk:** Setidaknya 2GB ruang disk yang tersedia

## Pemeriksaan Pra-instalasi

1. **Periksa Instalasi Python:**
   - Buka Command Prompt (cmd).
   - Periksa apakah Python terinstal dengan menjalankan:
     
    ```bash
    python --version
    ```
     
   - Jika Python belum terinstal, unduh dan instal dari [python.org](https://www.python.org/downloads/). Pastikan untuk memilih versi yang kompatibel dengan sistem operasi Anda.

2. **Periksa Instalasi Git:**
   - Periksa apakah Git terinstal dengan menjalankan:
     ```bash
     git --version
     ```
   - Jika Git belum terinstal, unduh dan instal dari [git-scm.com](https://git-scm.com/downloads/).

## Langkah Instalasi

### 3. Navigasi ke Folder Proyek melalui Command Prompt:
   - Ubah direktori saat ini ke folder proyek Anda menggunakan perintah cd.

### 4. Buat Lingkungan Virtual dan Folder Proyek:
   - Buat folder baru dengan nama "ppe-project" menggunakan perintah berikut:
     ```bash
     mkdir ppe-project
     ```
   - Navigasi ke folder "ppe-project":
     ```bash
     cd ppe-project
     ```
   - Buat lingkungan virtual Python baru dengan nama "your-env-name" menggunakan perintah berikut:
     ```bash
     python -m venv your-env-name 
     ```
     atau 
     ```bash
     py -m venv your-env-name
     ```
     - Aktifkan lingkungan virtual:
       - Pada Windows:
         ```bash
         .\your-env-name\Scripts\activate
         ```
       - Pada MacOS/Linux:
         ```bash
         source your-env-name/bin/activate
         ```

Sekarang Anda telah menyiapkan folder proyek bernama "ppe-project" dengan lingkungan virtual Python bernama "your-env-name." Selanjutnya, lanjutkan dengan langkah instalasi yang tersisa dalam folder proyek ini.

### 5. Clone Berkas Proyek:
   - Klona repositori proyek yang berisi file notebook dan model pre-trained "best.pt" dari GitHub dengan perintah berikut:
     ```bash
     git clone https://github.com/dinosptr/PPE-detection.git
     ```
   - Navigasi ke folder repositori yang telah di-clone:
     ```bash
     cd PPE-detection
     ```

### 6. Buat Folder 'ppe' dan Klona YOLOv8 (Versi Ultralytics):
   - Install YOLOv8 (Versi Ultralytics) dengan pip menggunakan perintah berikut:
     ```bash
     pip install ultralytics
     ```

### 7. Menjalankan Kode
Sekarang, Anda dapat menjalankan prediksi YOLOv8 menggunakan contoh yang disediakan. Pastikan untuk mengganti "file.pt" dan "path/to/image.jpg" dengan jalur file model dan jalur file gambar yang sebenarnya, masing-masing.

Contoh:
```bash
yolo predict model="model/best.pt" imgsz=640 conf=0.25 source=0 show=True ✅

yolo predict model="model/best.pt" imgsz=640 conf=0.25 source="path/to/image.jpg" show=True✅

yolo predict --model yolov8n.pt --imgsz 640 --conf 0.25 ❌
```

## Parameters

- model: Jalur ke file model yolov8.
- imgsz: Ukuran gambar input (dalam piksel).
- conf: Ambang kepercayaan untuk deteksi objek.
- source: Jalur ke gambar atau video input, atau dapat berupa webcam.
- show: Jika True, menampilkan gambar atau video yang sudah diannotasi dalam jendela/screen. Berguna untuk umpan balik visual langsung selama pengembangan atau pengujian.

*Catatan:* Untuk parameter source, Anda dapat memberikan nilai berikut:
- Untuk Webcam: Gunakan source=0 untuk webcam default atau tentukan indeks webcam.
- Untuk Gambar: Jalur ke satu file gambar (contoh: source=" path/to/image.jpg").
- Untuk Video: Jalur ke file video (contoh: source="path/to/video.mp4").

# 8. Contoh Output
![Alt text](assets/giphy(1).gif)
![Alt text](assets/giphy(2).gif)
![Alt text](assets/giphy(3).gif)
![Alt text](assets/giphy(4).gif)

Sumber gif:
1. https://giphy.com/gifs/JoeMillionaireFOX-3jsw7GGcpJnHtpRTDv
2. https://giphy.com/gifs/hiltilatam-tools-hilti-jobsite-OjS6U09TzD8FPsGAYw
3. https://giphy.com/gifs/theblock-channel-9-block-the-2022-IxOLG81hZQQs0S9tg7
4. https://giphy.com/gifs/hiltilatam-tools-hilti-jobsite-teJ82BFyT1vjhdDEjK 

# 9. Analisis singkat video:
Dikarenakan video tidak dapat ditampilkan di dalam dokumentasi ini, Anda dapat mengakses video hasil prediksi pada link berikut:

Link video hasil prediksi:
[Result-predict](https://drive.google.com/drive/folders/1v466ISQPV8wDtIrislqu-4TY3b13qJYJ?usp=sharing)
terdiri dari:
1. result-AI-video-contoh-trim.avi (sample from quest predict)
2. result-AI-video-construction-japan.avi (another sample)
3. result-AI-predict-realtime.avi (real-time predict)

Silakan akses link di atas untuk melihat hasil prediksi pada ketiga video tersebut.

### 1. Analisis video sample (result-AI-video-contoh-trim.avi)

Model mampu mengenali objek dengan baik pada video ketika objek berada dalam jarak dekat. Namun, terdapat kesulitan saat objek berada pada jarak yang lebih jauh, seperti yang terlihat pada contoh video yang diberikan, di mana deteksi objek seperti hardhat, safety vest, dan orang menjadi kurang akurat pada jarak yang lebih jauh.

#### Faktor-faktor yang Mempengaruhi Kesulitan Deteksi pada Jarak Jauh:

- Ukuran Objek yang Kecil:
- Kurangnya Detail Visual:
- Kondisi Pencahayaan yang Kurang Baik:
- Faktor Dataset:
- Faktor Model Pelatihan:
    
Analisis ini menunjukkan bahwa jarak objek dalam video dapat mempengaruhi kemampuan model YOLO dalam mendeteksi objek dengan akurat. Faktor-faktor seperti ukuran objek, detail visual, kondisi pencahayaan, dataset, dan pelatihan model menjadi kritis dalam meningkatkan kinerja model, terutama pada objek yang berada pada jarak yang lebih jauh. Peningkatan pada parameter dan penyesuaian pada data latih yang melibatkan situasi jarak jauh dapat diperlukan untuk mengatasi kesulitan deteksi.

---

### 2. Analisis video sample (result-AI-video-construction-japan.avi)

Model berhasil mengenali objek dengan baik pada video kedua berkat beberapa faktor kunci, termasuk resolusi tinggi yang memungkinkan deteksi objek dengan akurat dan detail. Pencahayaan optimal di siang hari memberikan kejelasan visual pada objek, sementara kontras yang jelas antara objek dan latar belakang meningkatkan kemampuan model untuk membedakan objek dengan lebih baik. Faktor lain yang mendukung keberhasilan melibatkan jarak objek yang tidak terlalu jauh, lingkungan yang konsisten untuk kestabilan deteksi, dan kualitas rekaman video yang tinggi, mendukung analisis objek dengan detail baik. Semua faktor ini bersinergi untuk menciptakan kondisi yang mendukung deteksi objek yang akurat dan efektif pada video tersebut.

--- 

### Kesimpulan antara keduanya
Dengan faktor-faktor yang bersinergi secara optimal, video kedua mencerminkan keberhasilan model dalam mengenali objek dengan akurat dan efektif. Analisis mendalam terhadap resolusi tinggi, pencahayaan optimal, dan faktor-faktor pendukung lainnya memberikan wawasan yang berharga untuk pengembangan model deteksi objek pada situasi serupa. Keseluruhan, pencapaian ini memberikan landasan yang kuat untuk peningkatan lebih lanjut pada kinerja model, membuktikan bahwa kombinasi kondisi yang baik dapat memberikan hasil deteksi yang optimal.

# 10. Tambahan:
- Jika ukuran file notebooks terlalu besar dan tidak dapat ditampilkan langsung, Anda dapat mengunduh repositori ini atau mengakses link di bawah ini untuk melihat file Jupyter:
[PPE-detection](https://colab.research.google.com/drive/1G3SBZneEzEMXbKQEcSE8QJ7h7hN4VAIm?usp=sharing)