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
