# -*- coding: utf-8 -*-
"""PPE-detection.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1G3SBZneEzEMXbKQEcSE8QJ7h7hN4VAIm

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

# Mount drive
"""

from google.colab import drive
drive.mount('/content/drive/')

"""# Unzip dataset"""

!unzip "/content/drive/MyDrive/healthkaton/PPE/Construction Site Safety.v28-yolov5pytorch.zip" -d "/content/"

"""# Eksplorasi Data

## Visualisasi Jumlah setiap data
"""

import os
import matplotlib.pyplot as plt

dataset_path = "/content/"  # Ganti dengan path dataset yolov5 Anda

# Menghitung jumlah gambar untuk setiap subset
train_images = len(os.listdir(os.path.join(dataset_path, "train", "images")))
val_images = len(os.listdir(os.path.join(dataset_path, "valid", "images")))
test_images = len(os.listdir(os.path.join(dataset_path, "test", "images")))

# Visualisasi persentase dataset
labels = ['Train', 'Validation', 'Test']
sizes = [train_images, val_images, test_images]

# Membuat diagram batang
fig, ax = plt.subplots()
bars = ax.bar(labels, sizes, color=['blue', 'orange', 'green'])

# Menambahkan label angka di tengah setiap bar
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), ha='center', va='bottom')

plt.title('Jumlah Gambar pada Dataset')
plt.xlabel('Subset')
plt.ylabel('Jumlah Gambar')
plt.show()

"""## Visualisasi Persentase Dataset"""

import os
import matplotlib.pyplot as plt

dataset_path = "/content/"

# Menghitung jumlah gambar untuk setiap subset
train_images = len(os.listdir(os.path.join(dataset_path, "train", "images")))
val_images = len(os.listdir(os.path.join(dataset_path, "valid", "images")))
test_images = len(os.listdir(os.path.join(dataset_path, "test", "images")))

# Visualisasi persentase dataset
labels = ['Train', 'Validation', 'Test']
sizes = [train_images, val_images, test_images]

plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title('Persentase Dataset')
plt.show()

"""## Tampilkan Sampel Gambar"""

# Commented out IPython magic to ensure Python compatibility.
import os
import cv2
import random
import matplotlib.pyplot as plt

# %matplotlib inline

# Path ke folder gambar dan anotasi
train_images_folder = "/content/train/images"
train_annotations_folder = "/content/train/labels"

# Daftar label sesuai dengan urutan yang diberikan
class_labels = ['Hardhat', 'Mask', 'NO-Hardhat', 'NO-Mask', 'NO-Safety Vest', 'Person', 'Safety Cone', 'Safety Vest', 'machinery', 'vehicle']

# Daftar warna yang sesuai dengan urutan kelas
class_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0),
                (255, 0, 255), (0, 255, 255), (255, 128, 0), (255, 0, 128), (0, 130, 0), (0, 255, 130)]

# Fungsi untuk menampilkan sampel gambar dengan dan tanpa bounding box
def display_sample_images(images_folder, annotations_folder, num_images=2):
    image_files = os.listdir(images_folder)

    if not image_files:
        print("No images found in the specified folder.")
        return

    selected_images = random.sample(image_files, min(num_images, len(image_files)))

    for image_file in selected_images:
        image_path = os.path.join(images_folder, image_file)
        annotation_path = os.path.join(annotations_folder, image_file.replace(".jpg", ".txt"))

        if not os.path.exists(image_path):
            print(f"Image file not found: {image_path}")
            continue

        image = cv2.imread(image_path)
        if image is None:
            print(f"Failed to read image: {image_path}")
            continue

        original_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Read bounding box annotations
        if os.path.exists(annotation_path):
            annotations = open(annotation_path, 'r').readlines()
            for annotation in annotations:
                try:
                    class_id, x_center, y_center, box_width, box_height = map(float, annotation.split()[:])
                except ValueError:
                    print(f"Error parsing annotation line: {annotation}")
                    continue

                # Convert class_id to integer and get the corresponding label and color
                class_id = int(class_id)
                label = class_labels[class_id]
                color = class_colors[class_id]

                x, y, w, h = (
                    int((x_center - box_width / 2) * image.shape[1]),
                    int((y_center - box_height / 2) * image.shape[0]),
                    int(box_width * image.shape[1]),
                    int(box_height * image.shape[0]),
                )

                # Draw bounding box with label and color on the image
                cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
                cv2.putText(image, label, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

            # Display image with bounding box, label, and color
            plt.figure(figsize=(10, 5))
            plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
            plt.title('Image with Bounding Box, Label, and Color')
            plt.show()
        else:
            print(f"No annotation file found for image: {image_file}")

# Menampilkan sampel gambar
display_sample_images(train_images_folder, train_annotations_folder)

"""## Distribusi Ukuran Gambar

"""

# Fungsi untuk menampilkan distribusi ukuran gambar
def display_image_size_distribution(images_path):
    image_files = os.listdir(images_path)
    image_sizes = []

    for image_file in image_files:
        image_path = os.path.join(images_path, image_file)
        image = cv2.imread(image_path)
        height, width, _ = image.shape
        image_sizes.append((width, height))

    widths, heights = zip(*image_sizes)

    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.hist(widths, bins=30, color='blue', alpha=0.7)
    plt.title('Distribusi Lebar Gambar')
    plt.xlabel('Lebar Gambar')
    plt.ylabel('Jumlah Gambar')

    plt.subplot(1, 2, 2)
    plt.hist(heights, bins=30, color='green', alpha=0.7)
    plt.title('Distribusi Tinggi Gambar')
    plt.xlabel('Tinggi Gambar')
    plt.ylabel('Jumlah Gambar')

    plt.tight_layout()
    plt.show()

# Menampilkan distribusi ukuran gambar
display_image_size_distribution(train_images_folder)

"""## Distribusi setiap kelas"""

import os
import matplotlib.pyplot as plt
import pandas as pd

# Path ke folder train, valid, dan test
train_folder = "/content/train"
valid_folder = "/content/valid"
test_folder = "/content/test"

# Daftar nama kelas
class_labels = ['Hardhat', 'Mask', 'NO-Hardhat', 'NO-Mask', 'NO-Safety Vest', 'Person', 'Safety Cone', 'Safety Vest', 'machinery', 'vehicle']

# Fungsi untuk menghitung distribusi kelas
def calculate_class_distribution(folder_path):
    class_distribution = [0] * len(class_labels)

    labels_folder = os.path.join(folder_path, "labels")

    for file_name in os.listdir(labels_folder):
        if file_name.endswith(".txt"):
            annotation_path = os.path.join(labels_folder, file_name)
            with open(annotation_path, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    class_id = int(line.split()[0])
                    class_distribution[class_id] += 1

    return class_distribution

# Menghitung distribusi kelas untuk setiap folder
train_distribution = calculate_class_distribution(train_folder)
valid_distribution = calculate_class_distribution(valid_folder)
test_distribution = calculate_class_distribution(test_folder)

# Membuat DataFrame dari data
df_train = pd.DataFrame({'Class': class_labels, 'Train': train_distribution})
df_valid = pd.DataFrame({'Class': class_labels, 'Valid': valid_distribution})
df_test = pd.DataFrame({'Class': class_labels, 'Test': test_distribution})

# Merge dataframes
df_merged = pd.merge(df_train, df_valid, on='Class')
df_merged = pd.merge(df_merged, df_test, on='Class')

# Plotting tabel
fig, ax = plt.subplots()
ax.axis('tight')
ax.axis('off')
ax.table(cellText=df_merged.values, colLabels=df_merged.columns, cellLoc='center', loc='center')

plt.title('Class Distribution in YOLOv5 Dataset (Train, Valid, Test)')
plt.show()

"""# Persiapan Data (Data Preparation)

Setelah mengunduh data dari Roboflow, tidak diperlukan lagi langkah persiapan data tambahan. Semua proses tersebut telah diurus oleh Roboflow. Namun, perlu diketahui bahwa data telah melalui beberapa teknik augmentasi untuk meningkatkan variasi dan kualitasnya.

Augmentasi yang diterapkan pada dataset melibatkan berbagai transformasi, termasuk:

* Flip: Melakukan flipping secara horizontal.
* Crop: Zoom minimum 0% dan zoom maksimum 20%.
* Rotation: Rotasi antara -12° dan +12°.
* Shear: Shear horizontal ±2° dan shear vertical ±2°.
* Grayscale: Diterapkan pada 10% dari gambar.
* Hue: Varian antara -15° dan +15°.
* Saturation: Varian antara -20% dan +20%.
* Brightness: Varian antara -25% dan +25%.
* Exposure: Varian antara -20% dan +20%.
* Blur: Diterapkan hingga 0.5px.
* Cutout: 6 kotak dengan ukuran masing-masing 2%.
* Mosaic: Teknik yang diterapkan untuk mencampur beberapa gambar dalam satu.


Semua augmentasi ini bertujuan untuk memperkaya dataset dan memastikan keberagaman yang cukup agar model dapat belajar dengan lebih baik dari data yang ada. Oleh karena itu, setelah unduhan dari Roboflow, fokus dapat dipindahkan langsung ke tahap pelatihan model tanpa perlu melakukan persiapan data tambahan.

# Training Model

## Alasan Penggunaan Yolov5

The decision to utilize the YOLOv5 algorithm stems from its proven potential in target tracking detection within real-world scenarios, showcasing competitive accuracy and real-time processing speed [1]. YOLOv5's demonstrated excellence in object detection, particularly in applications like surveillance, robotics, and autonomous driving, solidifies its position as a robust solution [2]. Noteworthy for outperforming other state-of-the-art models in both accuracy and speed, YOLOv5 emerges as a promising choice for diverse real-world applications [3]. Additionally, the enhancements brought by YOLOv4-5D, including improved detection accuracy and support for real-time operation exceeding 66 frames/s, make it especially effective for applications such as autonomous driving [4].

These studies collectively suggest that YOLOv5 and its variations are effective for real-time object detection, offering a balance between high accuracy and fast processing speeds across various applications such as autonomous driving, surveillance, and robotics.



---


Keputusan untuk menggunakan algoritma YOLOv5 berasal dari potensinya yang terbukti dalam deteksi pelacakan target di dalam skenario dunia nyata, menunjukkan akurasi yang kompetitif dan kecepatan pemrosesan real-time [1]. Keunggulan YOLOv5 dalam deteksi objek, khususnya dalam aplikasi seperti pengawasan, robotika, dan pengemudi otonom, memperkuat posisinya sebagai solusi yang tangguh [2]. Patut dicatat karena YOLOv5 mampu mengungguli model-model deteksi objek canggih lainnya dalam hal akurasi dan kecepatan, menjadikannya pilihan yang menjanjikan untuk berbagai aplikasi dunia nyata [3]. Selain itu, peningkatan yang dibawa oleh YOLOv4-5D, termasuk peningkatan akurasi deteksi dan dukungan untuk operasi real-time yang melebihi 66 frame/detik, membuatnya sangat efektif untuk aplikasi seperti pengemudi otonom [4].

Studi-studi ini secara kolektif menyarankan bahwa YOLOv5 dan varian-varian lainnya efektif untuk deteksi objek real-time, menawarkan keseimbangan antara akurasi tinggi dan kecepatan pemrosesan yang cepat di berbagai aplikasi seperti pengemudi otonom, pengawasan, dan robotika.


1. https://doi.org/10.54254/2755-2721/16/20230860.
2. https://doi.org/10.22214/ijraset.2023.51839.
3. https://doi.org/10.1051/e3sconf/202339101093.
4. https://doi.org/10.1109/TIM.2021.3065438.

### Clone Model
"""

# Commented out IPython magic to ensure Python compatibility.
!git clone https://github.com/ultralytics/yolov5  # clone
# %cd yolov5
!pip install -r requirements.txt  # install

"""### Atur Parameter

**Berikut adalah penjelasan rinci mengenai sejumlah parameter yang digunakan selama proses pelatihan model:**

* --img 640: Menentukan ukuran resolusi gambar input untuk pelatihan. Ukuran yang lebih besar mungkin meningkatkan kualitas deteksi objek tetapi memerlukan lebih banyak sumber daya komputasi. Pemilihan 640 disarankan karena memberikan keseimbangan yang baik antara kinerja dan akurasi.

* --batch 32: Menentukan ukuran batch untuk setiap iterasi pelatihan. Ukuran batch yang lebih besar dapat mempercepat pelatihan tetapi memerlukan lebih banyak memori GPU. Batch size 32 adalah nilai umum yang memberikan keseimbangan antara kecepatan pelatihan dan penggunaan memori.

* --epochs 30: Menentukan jumlah iterasi pelatihan. Jumlah iterasi ini harus cukup untuk memungkinkan model belajar pola dari dataset tetapi tidak terlalu besar untuk menghindari overfitting.

* --data '/content/data.yaml': Menentukan path ke file YAML dataset. File ini berisi konfigurasi dataset, seperti path ke file pelatihan, validasi, jumlah kelas, dan lainnya.

* --weights (cth: yolov5n.pt): Menentukan path ke file bobot awal model. Menggunakan bobot pre-trained dari model YOLOv5n memungkinkan model memulai pelatihan dengan representasi fitur yang sudah baik.

* --patience 5: Menentukan jumlah iterasi di mana validasi tidak memperlihatkan peningkatan sebelum pelatihan dihentikan. Early stopping dengan patience 5 dapat membantu menghindari pelatihan yang berlebihan.

* --project "../drive/MyDrive/healthkaton/PPE/model": Menentukan direktori proyek tempat menyimpan hasil pelatihan. Ini memudahkan organisasi eksperimen dan menyimpan model yang diperbarui.

* --name "yolov5s": Menentukan nama proyek atau eksperimen. Ini membantu mengidentifikasi setiap eksperimen dan menyimpannya dalam direktori yang sesuai.

* --hyp "data/hyps/hyp.no-augmentation.yaml": Menentukan path ke file YAML hiperparameter pelatihan. Hiperparameter termasuk learning rate, momentum, dan lainnya yang mempengaruhi tingkat konvergensi model.

* --optimizer "SGD": Menentukan algoritma optimizer yang akan digunakan selama pelatihan. SGD (Stochastic Gradient Descent) adalah optimizer yang umum digunakan dalam pelatihan model deep learning.

### yolov5n
"""

# traning
!python train.py --img 640 --batch 32 --epochs 30 --data '/content/data.yaml' --weights yolov5n.pt --patience 5 --project "../drive/MyDrive/healthkaton/PPE/model" --name "yolov5n" --hyp "data/hyps/hyp.no-augmentation.yaml" --optimizer "SGD"

# validation
!python val.py --batch 32 --task "train" --data "/content/data.yaml" --weights '../drive/MyDrive/healthkaton/PPE/model/yolov5n/weights/best.pt'  --img 640

# validation
!python val.py --batch 32 --task "test" --data "/content/data.yaml" --weights '../drive/MyDrive/healthkaton/PPE/model/yolov5n/weights/best.pt'  --img 640

# Commented out IPython magic to ensure Python compatibility.
# !tensorboard --logdir="../drive/MyDrive/healthkaton/PPE/model/yolov5n"
# %load_ext tensorboard
# %tensorboard --logdir "../drive/MyDrive/healthkaton/PPE/model/yolov5n"

"""### yolov5s"""

# traning
!python train.py --img 640 --batch 32 --epochs 30 --data '/content/data.yaml' --weights yolov5s.pt --patience 5 --project "../drive/MyDrive/healthkaton/PPE/model" --name "yolov5s" --hyp "data/hyps/hyp.no-augmentation.yaml" --optimizer "SGD"

!python val.py --batch 32 --task "train" --data "/content/data.yaml" --weights '../drive/MyDrive/healthkaton/PPE/model/yolov5s/weights/best.pt'  --img 640

# validation
!python val.py --batch 32 --task "test" --data "/content/data.yaml" --weights '../drive/MyDrive/healthkaton/PPE/model/yolov5s/weights/best.pt'  --img 640

# Commented out IPython magic to ensure Python compatibility.
# %load_ext tensorboard
# %tensorboard --logdir "../drive/MyDrive/healthkaton/PPE/model/yolov5s"

"""### yolov5m"""

# traning
!python train.py --img 640 --batch 32 --epochs 30 --data '/content/data.yaml' --weights yolov5m.pt --patience 5 --project "../drive/MyDrive/healthkaton/PPE/model" --name "yolov5m" --hyp "data/hyps/hyp.no-augmentation.yaml" --optimizer "SGD"

!python val.py --batch 32 --task "train" --data "/content/data.yaml" --weights '../drive/MyDrive/healthkaton/PPE/model/yolov5m/weights/best.pt'  --img 640

# validation
!python val.py --batch 32 --task "test" --data "/content/data.yaml" --weights '../drive/MyDrive/healthkaton/PPE/model/yolov5m/weights/best.pt'  --img 640

# Commented out IPython magic to ensure Python compatibility.
# %load_ext tensorboard
# %tensorboard --logdir "../drive/MyDrive/healthkaton/PPE/model/yolov5m"

"""### yolov5l"""

# traning
!python train.py --img 640 --batch 32 --epochs 30 --data '/content/data.yaml' --weights yolov5l.pt --patience 5 --project "../drive/MyDrive/healthkaton/PPE/model" --name "yolov5l" --hyp "data/hyps/hyp.no-augmentation.yaml" --optimizer "SGD"

!python val.py --batch 32 --task "train" --data "/content/data.yaml" --weights '../drive/MyDrive/healthkaton/PPE/model/yolov5l/weights/best.pt'  --img 640

# validation
!python val.py --batch 32 --task "test" --data "/content/data.yaml" --weights '../drive/MyDrive/healthkaton/PPE/model/yolov5l/weights/best.pt'  --img 640

# Commented out IPython magic to ensure Python compatibility.
# %load_ext tensorboard
# %tensorboard --logdir "../drive/MyDrive/healthkaton/PPE/model/yolov5l"

"""### yolov5x"""

# traning
!python train.py --img 640 --batch 32 --epochs 30 --data '/content/data.yaml' --weights yolov5x.pt --patience 5 --project "../drive/MyDrive/healthkaton/PPE/model" --name "yolov5x" --hyp "data/hyps/hyp.no-augmentation.yaml" --optimizer "SGD"

!python val.py --batch 32 --task "train" --data "/content/data.yaml" --weights '../drive/MyDrive/healthkaton/PPE/model/yolov5x/weights/best.pt'  --img 640

# validation
!python val.py --batch 32 --task "test" --data "/content/data.yaml" --weights '../drive/MyDrive/healthkaton/PPE/model/yolov5x/weights/best.pt'  --img 640

# Commented out IPython magic to ensure Python compatibility.
# %load_ext tensorboard
# %tensorboard --logdir "../drive/MyDrive/healthkaton/PPE/model/yolov5x"

"""## Alasan Penggunaan Yolov8

The YOLOv8 model demonstrates remarkable performance, achieving a mean Average Precision (mAP50-95) of 0.685 while maintaining an average inference speed of 50 frames per second (fps) for real-time detection of flying objects in 1080p videos [1]. Additionally, it proves effective in augmented reality environments, delivering satisfactory accuracy without offloading to external servers [2]. In the realm of video analysis from surveillance cameras, YOLOv8 excels in elevating object detection performance in real-time scenarios [3]. While demonstrating robustness in object detection, especially in real-world scenarios, YOLOv8 acknowledges the need for improvements to effectively handle challenges in mixed traffic, particularly during night-time conditions [4]. These studies collectively affirm YOLOv8 and its variants as effective solutions for real-time object detection, providing high accuracy and speed across various applications. Nonetheless, there is acknowledgment of potential for further refinement, particularly in addressing specific challenges, such as those encountered in mixed traffic scenarios at night.



---

Model YOLOv8 menunjukkan kinerja yang luar biasa, mencapai rata-rata Average Precision (mAP50-95) sebesar 0,685 dengan tetap mempertahankan kecepatan inferensi rata-rata 50 frame per detik (fps) untuk deteksi objek terbang secara real-time dalam video 1080p [1]. Selain itu, ini terbukti efektif dalam lingkungan augmented reality, memberikan akurasi yang memuaskan tanpa membebani server eksternal [2]. Dalam bidang analisis video dari kamera pengawas, YOLOv8 unggul dalam meningkatkan kinerja deteksi objek dalam skenario waktu nyata [3]. Meskipun menunjukkan ketangguhan dalam pendeteksian objek, terutama dalam skenario dunia nyata, YOLOv8 mengakui perlunya peningkatan untuk menangani tantangan secara efektif dalam lalu lintas campuran, terutama pada kondisi malam hari [4]. Penelitian-penelitian ini secara kolektif menegaskan YOLOv8 dan variannya sebagai solusi yang efektif untuk deteksi objek secara real-time, memberikan akurasi dan kecepatan yang tinggi di berbagai aplikasi. Meskipun demikian, ada potensi untuk penyempurnaan lebih lanjut, terutama dalam menangani tantangan khusus, seperti yang dihadapi dalam skenario lalu lintas campuran di malam hari.


**Referensi:**

1. https://doi.org/10.48550/arXiv.2305.09972
2. https://doi.org/10.1109/EDGE60047.2023.00059
3. https://doi.org/10.1109/ICRAIS59684.2023.10367122
4. https://doi.org/10.1109/COSITE60233.2023.10249521

### Setup yolov8
"""

!pip install ultralytics

import ultralytics

"""### Atur Parameter

* data: Parameter ini menentukan jalur ke file YAML yang berisi konfigurasi dataset. Ini mencakup informasi seperti nama kelas, pembagian data latih/validasi/uji, ukuran gambar, dan lain-lain.

* epochs: Jumlah epoch pelatihan. Satu epoch adalah satu kali penyebaran lengkap melalui seluruh dataset pelatihan.

* cache: Sebuah boolean yang menunjukkan apakah akan melakukan pengecekan cepat dalam RAM untuk pelatihan yang lebih cepat. Jika diatur ke True, ini dapat mempercepat pelatihan tetapi mungkin membutuhkan jumlah RAM yang signifikan.

* optimizer: Menentukan optimizer yang akan digunakan selama pelatihan. Dalam hal ini, diatur ke 'auto', yang berarti skrip akan memilih optimizer secara otomatis berdasarkan arsitektur model.

* batch: Ukuran batch adalah jumlah sampel yang diproses dalam satu iterasi. Ukuran batch yang lebih besar dapat meningkatkan penggunaan GPU tetapi juga dapat meningkatkan persyaratan memori.

* patience: Kesabaran penghentian dini. Jika model tidak menunjukkan peningkatan untuk sejumlah epoch tertentu (patience), pelatihan akan berhenti lebih awal.

* project: Direktori tempat hasil pelatihan akan disimpan, termasuk log, checkpoint, dan lain-lain.

* name: Nama unik untuk pelatihan yang berjalan. Ini berguna untuk mengorganisir dan mengidentifikasi eksperimen yang berbeda.

### yolov8n
"""

from ultralytics import YOLO

model = YOLO('yolov8n.pt')  # load a pretrained YOLOv8n segmentation model
model.train(data="/content/data.yaml", epochs=30, cache=True, optimizer='auto',
            batch=32, patience=5)  # train the model

from ultralytics import YOLO

model_yolov8n = YOLO('runs/detect/train/weights/best.pt')  # load a custom model

# Validate the model
metrics_yolov8n = model_yolov8n.val(data="/content/data.yaml", imgsz=640, batch=32, split='train')

metrics_yolov8n = model_yolov8n.val(data="/content/data.yaml", imgsz=640, batch=32, split='test')

"""### yolov8s"""

from ultralytics import YOLO

model = YOLO('yolov8s.pt')  # load a pretrained YOLOv8s model
model.train(data="/content/data.yaml", epochs=30, cache=True, optimizer='auto',
            batch=32, patience=5)  # train the model

model_yolov8s = YOLO('runs/detect/train2/weights/best.pt')  # load a custom model

# Validate the model
metrics_yolov8s = model_yolov8s.val(data="/content/data.yaml", imgsz=640, batch=32, split='train')

metrics_yolov8s = model_yolov8s.val(data="/content/data.yaml", imgsz=640, batch=32, split='test')

"""### yolov8m"""

from ultralytics import YOLO

model = YOLO('yolov8m.pt')  # load a pretrained YOLOv8m model
model.train(data="/content/data.yaml", epochs=30, cache=True, optimizer='auto',
            batch=32, patience=5)  # train the model

model_yolov8m = YOLO('runs/detect/train3/weights/best.pt')  # load a custom model

# Validate the model
metrics_yolov8m = model_yolov8m.val(data="/content/data.yaml", imgsz=640, batch=32, split='train')

metrics_yolov8m = model_yolov8m.val(data="/content/data.yaml", imgsz=640, batch=32, split='test')

"""### yolov8l"""

from ultralytics import YOLO

model = YOLO('yolov8l.pt')  # load a pretrained YOLOv8l model
model.train(data="/content/data.yaml", epochs=30, cache=True, optimizer='auto',
            batch=32, patience=5)  # train the model

model_yolov8l = YOLO('runs/detect/train4/weights/best.pt')  # load a custom model

# Validate the model
metrics_yolov8l = model_yolov8l.val(data="/content/data.yaml", imgsz=640, batch=32, split='train')

metrics_yolov8l = model_yolov8l.val(data="/content/data.yaml", imgsz=640, batch=32, split='test')

"""### yolov8x"""

from ultralytics import YOLO

model = YOLO('yolov8x.pt')  # load a pretrained YOLOv8x model
model.train(data="/content/data.yaml", epochs=30, cache=True, optimizer='auto',
            batch=32, patience=5)  # train the model

model_yolov8x = YOLO('runs/detect/train5/weights/best.pt')  # load a custom model

# Validate the model
metrics_yolov8x = model_yolov8x.val(data="/content/data.yaml", imgsz=640, batch=32, split='train')

metrics_yolov8x = model_yolov8x.val(data="/content/data.yaml", imgsz=640, batch=32, split='test')

# !cp -r "runs/detect/train" "/content/drive/MyDrive/healthkaton/PPE/model/"
# !cp -r "runs/detect/train2" "/content/drive/MyDrive/healthkaton/PPE/model/"
# !cp -r "runs/detect/train3" "/content/drive/MyDrive/healthkaton/PPE/model/"
# !cp -r "runs/detect/train4" "/content/drive/MyDrive/healthkaton/PPE/model/"
!cp -r "runs/detect/train5" "/content/drive/MyDrive/healthkaton/PPE/model/"

"""# Evaluate Setiap Model

Hasil evaluasi Precision, Recall, Map50, dan Map50-95 yang terdokumentasi dalam tabel mencerminkan **rata-rata** nilai dari setiap kelas pada **data test** yang sepenuhnya terpisah dari proses pelatihan, berlaku untuk seluruh versi algoritma YOLOv5 dan YOLOv8, termasuk  YOLOv5n, YOLOv5s, YOLOv5m, YOLOv5l, YOLOv5x, YOLOv8n, YOLOv8s, YOLOv8m, YOLOv8l dan YOLOv8x. Nilai-nilai ini dihitung berdasarkan prestasi model pada setiap kelas secara individu, dan hasil rata-rata diambil untuk menyajikan gambaran keseluruhan dari performa algoritma YOLOv5 pada berbagai versi.
"""

import pandas as pd

data = {
    'Nama Algoritma': [
        'YOLOv5n', 'YOLOv5s', 'YOLOv5m', 'YOLOv5l', 'YOLOv5x',
        'YOLOv8n', 'YOLOv8s', 'YOLOv8m', 'YOLOv8l', 'YOLOv8x'
        ],
    'Precision': [
        0.76, 0.776, 0.861, 0.903, 0.897,
        0.806, 0.911, 0.944, 0.942, 0.917
    ],
    'Recall': [
        0.605, 0.626, 0.681, 0.727, 0.756,
        0.652, 0.711, 0.832, 0.837, 0.77
    ],
    'Map50': [
        0.64, 0.69, 0.749, 0.802, 0.811,
        0.719, 0.788, 0.891, 0.893, 0.826
    ],
    'Map50-95': [
        0.272, 0.329, 0.392, 0.446, 0.465,
        0.399, 0.487, 0.713, 0.72, 0.555
    ]
}


# Membuat DataFrame baru yolov5
df = pd.DataFrame(data)

df

"""## Analisis singkat

Berdasarkan data evaluasi yang diberikan, kita dapat mengamati bahwa YOLOv8m dan YOLOv8l memiliki perbedaan yang tipis dalam sebagian besar metrik. Namun, kita dapat memberikan analisis lebih lanjut:

- Precision: YOLOv8m memiliki nilai tertinggi pada precision, menunjukkan kemampuan untuk memberikan hasil yang sangat akurat. YOLOv8l juga memiliki nilai precision yang sangat baik, meskipun sedikit lebih rendah dari YOLOv8m.

- Recall: YOLOv8m memiliki nilai recall yang lebih tinggi daripada YOLOv8l, menunjukkan kemampuan untuk mendeteksi sebagian besar objek yang sebenarnya dengan lebih baik.

- Map50 dan Map50-95: YOLOv8m memiliki nilai yang lebih tinggi pada kedua metrik ini dibandingkan YOLOv8l, menunjukkan kinerja yang lebih optimal dalam mendeteksi objek dengan keberagaman ukuran dan skor kepercayaan.


Meskipun perbedaan antara YOLOv8m dan YOLOv8l tipis, YOLOv8m masih menonjol sebagai pilihan yang sedikit lebih unggul secara keseluruhan. Beberapa alasan yang mendukung pemilihan YOLOv8m antara keduanya adalah:

1. Keakuratan yang Lebih Tinggi: YOLOv8m memiliki nilai precision dan recall yang lebih tinggi, menunjukkan kemampuan untuk memberikan hasil yang lebih akurat dan mendeteksi sebagian besar objek yang sebenarnya. Hal ini dapat sangat penting dalam kasus di mana akurasi deteksi sangat kritis.

2. Kinerja Optimal pada Metrik Map50 dan Map50-95: YOLOv8m memiliki nilai yang lebih tinggi pada metrik map50 dan map50-95, yang mencerminkan kinerja yang lebih baik dalam mendeteksi objek dengan keberagaman ukuran dan skor kepercayaan. Ini membuat YOLOv8m menjadi pilihan yang lebih handal dalam berbagai kondisi.

3. Fleksibilitas dan Kekompakan Model: YOLOv8m mungkin menawarkan keseimbangan yang baik antara kinerja dan ukuran model. Meskipun tidak memiliki informasi spesifik tentang ukuran model, seringkali model yang lebih kecil dapat lebih mudah diimplementasikan dan membutuhkan sumber daya komputasi yang lebih sedikit.

4. Pemeliharaan dan Efisiensi: Model dengan parameter yang lebih sedikit cenderung memerlukan lebih sedikit sumber daya untuk pemeliharaan dan pelatihan ulang. Jika keefisienan dan efisiensi operasional menjadi pertimbangan, YOLOv8m dapat menjadi pilihan yang lebih praktis.



Namun, perlu diingat bahwa pilihan antara YOLOv8m dan YOLOv8l tetap tergantung pada konteks spesifik proyek dan kebutuhan pengguna. Meskipun demikian, berdasarkan evaluasi yang telah dilakukan, model final yang dipilih untuk implementasi adalah **YOLOv8m**. Keunggulan dalam akurasi, kinerja optimal pada metrik Map50 dan Map50-95, serta fleksibilitas dan efisiensi operasional membuat YOLOv8m menjadi pilihan yang lebih unggul untuk keperluan deteksi objek dalam proyek ini. Evaluasi lebih lanjut dan uji coba di lingkungan proyek nyata akan memastikan bahwa model ini sesuai dengan kebutuhan yang ada.

# Testing dengan model terbaik
"""

# !python detect.py --weights "/content/drive/MyDrive/healthkaton/PPE/model/yolov5x/weights/best.pt" --source "https://www.youtube.com/watch?v=UPRtZJwd-cI"

from ultralytics import YOLO
from IPython.display import Image, display

# Load a model
model = YOLO('/content/drive/MyDrive/healthkaton/PPE/model/train3/weights/best.pt')  # pretrained YOLOv8n model
path_img = '/content/drive/MyDrive/healthkaton/PPE/sample/cth-image2.jpg'
# Predict and display the result
result = model.predict(path_img, imgsz=640, conf=0.2, save=True)
# The result object contains information about the prediction
# You can access the saved image path using result.save_path
image_path = result[0].save_dir + f"/{path_img.split('/')[-1]}"

# Display the image
display(Image(filename=image_path))

from ultralytics import YOLO
from IPython.display import Image, display

# Load a model
model = YOLO('/content/drive/MyDrive/healthkaton/PPE/model/train3/weights/best.pt')  # pretrained YOLOv8n model
path_vid = '/content/drive/MyDrive/healthkaton/PPE/sample/video-contoh-trim.mov'
# Predict and display the result
result = model.predict(path_vid, imgsz=640, conf=0.4, save=True)

!cp -r "/content/runs/detect/predict/video-contoh-trim.avi" "/content/drive/MyDrive/healthkaton/PPE/sample"

# Load a model
model = YOLO('/content/drive/MyDrive/healthkaton/PPE/model/train3/weights/best.pt')  # pretrained YOLOv8n model
path_vid = '/content/drive/MyDrive/healthkaton/PPE/sample/video-construction-japan.mp4'
# Predict and display the result
result = model.predict(path_vid, imgsz=640, conf=0.4, save=True)

!cp -r "/content/runs/detect/predict2/video-construction-japan.avi" "/content/drive/MyDrive/healthkaton/PPE/sample"
