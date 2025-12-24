# 🧘 Klasifikasi Gerakan Yoga
## 📌Deskripsi Proyek
Proyek Klasifikasi Gaya Yoga ini bertujuan untuk mengembangkan sistem pengenalan pose/gaya yoga berbasis citra menggunakan metode Deep Learning. Sistem mampu mengklasifikasikan gambar pose yoga ke dalam beberapa kelas gaya yoga tertentu (misalnya: Downward Dog, Tree Pose, Warrior Pose).
Aplikasi ini dibangun sebagai website interaktif menggunakan Streamlit, sehingga pengguna dapat mengunggah gambar pose yoga dan memperoleh hasil prediksi secara langsung. Proyek ini dirancang sebagai implementasi pembelajaran pada mata kuliah Pembelajaran Mesin / Deep Learning.

## 📝Latar Belakang
Perkembangan teknologi computer vision dan deep learning telah mendorong pemanfaatan kecerdasan buatan dalam berbagai bidang, termasuk kesehatan dan kebugaran. Yoga sebagai salah satu aktivitas fisik dan mental yang populer memiliki beragam gaya atau pose yang memerlukan ketepatan gerakan agar manfaat yang diperoleh optimal serta meminimalkan risiko cedera. Namun, tidak semua praktisi yoga memiliki akses langsung ke instruktur profesional untuk memastikan kesesuaian pose yang dilakukan.

Di sisi lain, meningkatnya penggunaan perangkat digital dan ketersediaan data citra membuka peluang untuk mengembangkan sistem otomatis yang mampu mengenali dan mengklasifikasikan gaya yoga berdasarkan gambar. Sistem klasifikasi berbasis citra dapat membantu pengguna dalam mengenali pose yoga yang dilakukan, memberikan umpan balik awal, serta menjadi sarana pembelajaran mandiri yang mudah diakses.

Berdasarkan permasalahan tersebut, proyek ini dikembangkan untuk membangun sistem Klasifikasi Gaya Yoga Berbasis Citra menggunakan pendekatan Deep Learning. Dengan memanfaatkan model Convolutional Neural Network dan transfer learning, diharapkan sistem mampu memberikan hasil klasifikasi yang akurat dan efisien serta dapat diimplementasikan dalam bentuk aplikasi web interaktif menggunakan Streamlit.

## 🗂️ Dataset
Nama    : Yoga Pose Image classification dataset

Sumber  :https://www.kaggle.com/datasets/shrutisaxena/yoga-pose-image-classification-dataset

Jumlah Kelas    : 107 

Distribusi Training : 5994 files

## ⚙️reprocessing & Augmentasi
Tahapan preprocessing dan augmentasi data dilakukan untuk meningkatkan kualitas data serta performa model dalam melakukan generalisasi. Langkah-langkah yang diterapkan adalah sebagai berikut:

Preprocessing
- Resize Citra
Seluruh gambar diubah ukurannya menjadi 224 × 224 piksel agar sesuai dengan input model CNN dan model transfer learning.
- Normalisasi Pixel
Nilai pixel citra dinormalisasi ke rentang 0–1 dengan membagi nilai pixel dengan 255.
- Labeling Otomatis
Label kelas diberikan secara otomatis berdasarkan nama folder menggunakan flow_from_directory.
- Split Data
Dataset dibagi menjadi data training dan validation untuk mengevaluasi performa model.

Augmentasi Data
Augmentasi data diterapkan pada data training untuk mengurangi risiko overfitting. Teknik augmentasi yang digunakan meliputi:
- Rotasi acak gambar
- Horizontal flip
- Zoom acak
- Shear transformation

Augmentasi dilakukan menggunakan ImageDataGenerator dari TensorFlow/Keras, sehingga setiap epoch model menerima variasi citra yang berbeda.

Pendekatan preprocessing dan augmentasi ini membantu model menjadi lebih robust terhadap variasi posisi, sudut pengambilan gambar, dan skala pose yoga.
## 🧠 Model yang Digunakan
Pada proyek ini digunakan tiga model untuk melakukan klasifikasi gaya yoga :
1. Convolutional Neural Network (CNN) Sederhana
Model CNN sederhana digunakan sebagai baseline model dengan arsitektur utama:
- Convolutional Layer + ReLU
- Max Pooling Layer
- Fully Connected Layer
- Softmax Output
Model ini digunakan untuk melihat performa dasar klasifikasi citra yoga.
2. MobileNetV2 (Transfer Learning)
MobileNetV2 merupakan model transfer learning yang dirancang ringan dan efisien. Keunggulan model ini antara lain:
- Ukuran model kecil
- Waktu inferensi cepat
- Performa lebih baik dibanding CNN sederhana
Layer akhir MobileNetV2 disesuaikan dengan jumlah kelas gaya yoga.
3. EfficientNet
EfficientNet digunakan sebagai model lanjutan untuk meningkatkan akurasi klasifikasi. Model ini menerapkan compound scaling yang mengoptimalkan depth, width, dan resolusi secara bersamaan.
EfficientNet memberikan performa terbaik, namun membutuhkan sumber daya komputasi yang lebih besar.
## 📊 Hasil Evaluasi dan Analisis Perbandingan Model
## 🖼️ Visualisasi Performa

## 👤 Data Diri
Nama    : Muhammad Arif Rahman Maulana
Nim     : 202210370311196
Kelas   : Pembelajaran Mesin C
Jurusan         : Teknik
Program Studi   : Informatika
Universitas     : Universitas Muhammadiyah Malang







