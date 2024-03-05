# Business Problem: Optimal Workplace Safety through APD Detection

Dalam lingkungan industri, keamanan tempat kerja adalah prioritas utama. Oleh karena itu, business problem yang perlu dipecahkan adalah bagaimana meningkatkan keamanan dan kepatuhan terhadap penggunaan Alat Pelindung Diri (APD) di lokasi kerja. 

## Objectives
1. **Meningkatkan Kepatuhan:** Mengembangkan sistem deteksi APD yang dapat meningkatkan kepatuhan pekerja terhadap penggunaan alat pelindung diri.
  
2. **Pengawasan Efektif:** Menciptakan solusi yang memungkinkan pengawasan efektif terhadap penggunaan APD di berbagai kondisi lingkungan dan lokasi kerja.

3. **Pencegahan Kecelakaan:** Mengurangi risiko kecelakaan dan cedera dengan memberikan peringatan otomatis jika terdeteksi pelanggaran penggunaan APD.

4. **Efisiensi Operasional:** Meningkatkan efisiensi operasional dengan mengurangi waktu yang diperlukan untuk pemeriksaan kepatuhan manual dan memastikan penyelesaian tugas-tugas tanpa hambatan keselamatan.

## Metrik Keberhasilan
1. **Persentase Kepatuhan:** Meningkatnya persentase kepatuhan pekerja terhadap pedoman penggunaan APD.
   
2. **Waktu Respon:** Menurunkan waktu respon dalam mendeteksi pelanggaran APD dan memberikan peringatan.

3. **Tingkat Kecelakaan Berkurang:** Menurunkan tingkat kecelakaan dan cedera yang disebabkan oleh ketidakpatuhan penggunaan APD.

## Solusi Potensial
Mengimplementasikan sistem deteksi APD berbasis kamera dan algoritma deep learning untuk memastikan keamanan di tempat kerja, dengan integrasi notifikasi otomatis dan pemantauan kepatuhan secara real-time. Solusi ini dapat diadopsi di berbagai industri yang memerlukan keamanan kerja yang optimal.

# Proses Pemilihan Dataset untuk Pengenalan APD

Dokumentasi ini menjelaskan kriteria seleksi dan alasan pemilihan dataset untuk pengenalan Alat Pelindung Diri (APD).

## Kriteria Seleksi

1. **Jenis APD:** Dataset mencakup berbagai jenis APD seperti Hardhat, Mask, NO-Hardhat, NO-Mask, NO-Safety Vest, Person, Safety Cone, Safety Vest, machinery, vehicle
2. **Variasi Pencahayaan:** Dataset mencakup variasi pencahayaan untuk memastikan keberlanjutan model di berbagai kondisi cahaya.
3. **Variasi Latar Belakang:** Dataset mencakup variasi latar belakang untuk meningkatkan ketangkapan keberagaman lingkungan.
4. **Jumlah Kelas Objek:** Dataset mencakup berbagai kelas objek APD yang relevan.
5. **Jumlah Instance per Image dan Label yang Relevan:** Informasi ini memberikan gambaran tentang seberapa sering objek atau elemen keselamatan kerja muncul dalam setiap gambar, dengan label yang diberikan secara relevan dan bermakna. Hal ini memudahkan pemahaman model terhadap konteks penggunaan peralatan perlindungan diri (APD) dalam berbagai kondisi kerja.

## Dataset Terpilih

## Informasi Dataset: PPE Dataset untuk Proyek Computer Vision Keselamatan Kerja

- **Sumber:** [Roboflow Universe](https://universe.roboflow.com/)
- **Jumlah Gambar Pelatihan:** 2605
- **Jumlah Gambar Validasi:** 114
- **Jumlah Gambar Pengujian:** 82
- **Jumlah Kelas:** 10 label

## Alasan Pemilihan

Dataset ini dipilih karena menyajikan berbagai jenis APD yang umum digunakan, mencakup variasi kondisi pencahayaan dan latar belakang. Lebih lanjut, dataset ini memiliki relevansi yang tinggi dengan sumber informasi yang saya temukan. Selain itu, sebagian besar gambar dalam dataset diambil saat APD digunakan oleh orang, bukan hanya sebagai objek. Keberagaman konteks penggunaan ini diharapkan dapat meningkatkan kemampuan model untuk mengenali dan mengklasifikasikan APD dengan akurat. Dengan jumlah gambar yang memadai, diharapkan dataset ini mendukung pembangunan model pengenalan APD yang efektif dan andal.

## Instruksi Penggunaan Dataset

1. Untuk mengunduh dataset, kunjungi https://universe.roboflow.com/roboflow-universe-projects/construction-site-safety/dataset/28
2. Login menggunakan account Google atau GitHub
3. Klik tombol "Download Dataset" atau tautan serupa yang disediakan di halaman tersebut.
4. Pilih opsi download yang sesuai, seperti ZIP atau format lainnya dan juga sesuaikan dengan algoritma yang akan digunakan (cth: YOLOv5 PyTorch).
5. Ekstrak file ZIP ke direktori yang sesuai dengan struktur proyek Anda.


# Penjelasan tambahan mengenai dataset
Penggunaan label "NO-" dalam konteks ini dapat memberikan informasi penting tentang kekurangan atau ketiadaan perlindungan tertentu pada individu. Lebih lanjut, informasi ini dapat digunakan untuk membuat sistem yang lebih canggih, seperti sistem pemicu alarm atau sistem pemantauan keamanan otomatis. Beberapa implikasi potensial dari adanya label "NO-" yang dapat memicu tindakan atau alarm melibatkan:

1. **Pemicuan Alarm Keselamatan:** Deteksi kekurangan perlindungan, seperti ketiadaan masker, hardhat, atau rompi keselamatan, dapat memicu sistem alarm keselamatan. Ini dapat memberi tahu personel keamanan atau manajemen untuk menanggapi situasi tersebut.

2. **Intervensi Otomatis:** Sistem dapat dirancang untuk memberikan tanggapan otomatis terhadap situasi ketiadaan perlindungan. Misalnya, dapat ada peringatan suara atau visual yang memberi tahu individu untuk segera memasang perlindungan diri.

3. **Pemantauan Keselamatan Real-time:** Informasi dari label "NO-" dapat diintegrasikan ke dalam sistem pemantauan keselamatan secara real-time. Ini memungkinkan untuk pemantauan aktif terhadap kepatuhan keselamatan di lokasi kerja.


Dengan memanfaatkan informasi yang diberikan oleh label "NO-", sistem dapat memberikan respons yang cepat dan efektif terhadap potensi risiko keselamatan, meningkatkan keamanan dan keselamatan di lingkungan kerja.


## Referensi

- https://depobeta.com/magazine/artikel/alat-pelindung-diri-di-bidang-konstruksi/
- https://roboflow.com/
- https://docs.roboflow.com/
