# Proses Pemilihan Dataset untuk Pengenalan APD

Dokumentasi ini menjelaskan kriteria seleksi dan alasan pemilihan dataset untuk pengenalan Alat Pelindung Diri (APD).

## Kriteria Seleksi

1. **Jenis APD:** Dataset mencakup berbagai jenis APD seperti Boots, ear-protection, Glass, Glove,Helmet, Person, Mask, Vest.
2. **Variasi Pencahayaan:** Dataset mencakup variasi pencahayaan untuk memastikan keberlanjutan model di berbagai kondisi cahaya.
3. **Variasi Latar Belakang:** Dataset mencakup variasi latar belakang untuk meningkatkan ketangkapan keberagaman lingkungan.
4. **Jumlah Kelas Objek:** Dataset mencakup berbagai kelas objek APD yang relevan.

## Dataset Terpilih

### Nama Dataset: PPE Dataset for Workplace Safety Computer Vision Project

- **Sumber:** https://universe.roboflow.com/ 
- **Jumlah Gambar:** 1604 Gambar
- **Jumlah Kelas:** 8 label

## Alasan Pemilihan

Dataset ini dipilih karena menyajikan berbagai jenis APD yang umum digunakan, mencakup variasi kondisi pencahayaan dan latar belakang. Lebih lanjut, dataset ini memiliki relevansi yang tinggi dengan sumber informasi yang saya temukan. Selain itu, sebagian besar gambar dalam dataset diambil saat APD digunakan oleh orang, bukan hanya sebagai objek. Keberagaman konteks penggunaan ini diharapkan dapat meningkatkan kemampuan model untuk mengenali dan mengklasifikasikan APD dengan akurat. Dengan jumlah gambar yang memadai, diharapkan dataset ini mendukung pembangunan model pengenalan APD yang efektif dan andal.

## Instruksi Penggunaan Dataset

1. Untuk mengunduh dataset, kunjungi https://universe.roboflow.com/siabar/ppe-dataset-for-workplace-safety.
2. Login menggunakan account Google atau GitHub
3. Klik tombol "Download Dataset" atau tautan serupa yang disediakan di halaman tersebut.
4. Pilih opsi download yang sesuai, seperti ZIP atau format lainnya dan juga sesuaikan dengan algoritma yang akan digunakan (cth: YOLOv5 PyTorch).
5. Ekstrak file ZIP ke direktori yang sesuai dengan struktur proyek Anda.


## Referensi

- https://depobeta.com/magazine/artikel/alat-pelindung-diri-di-bidang-konstruksi/
- https://roboflow.com/
- https://docs.roboflow.com/