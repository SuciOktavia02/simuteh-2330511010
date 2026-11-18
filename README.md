# SIMUTEH - Praktikum P1-P6 Computer Vision

Sistem Pemeriksaan Mutu Daun Teh Berbasis Citra untuk Kelompok Tani Teh Rakyat di Kabupaten Sukabumi.
Nama: Suci Oktavia Ramadhani | NIM: 2330511010 | **SEED = 1010**

## Cara menjalankan
1. Pasang pustaka: `pip install -r requirements.txt`
2. Bangkitkan dataset dari folder utama repository: `python src/buat_dataset_sintetis.py`
   (menghasilkan 60 citra di data/sintetis/; salinan hasilnya juga disertakan di repository)
3. Jalankan notebook di folder `notebook/` secara berurutan dengan Restart & Run All:
   B1, B2, B3, B4, B5 (Evaluasi P1-P4), lalu P5_tepi dan P6_morfologi (Praktikum P5-P6).
   Notebook dapat dijalankan di Google Colab: clone repository ke /content/simuteh, lalu jalankan
   sel persiapan di awal notebook (folder kerja `/content/simuteh/notebook`).

## Struktur repository
- `src/` : buat_dataset_sintetis.py, utils_cv.py, praproses.py, praproses_acuan.py, utils_tepi.py, bercak.py
- `notebook/` : B1_lingkungan, B2_citra_warna, B3_histogram, B4_penapisan, B5_praproses,
  P5_tepi (Bagian 1-2), P6_morfologi (Bagian 3-5)
- `hasil/` : gambar, tabel .csv (p5_*, p6_*), param_praproses.json, param_bercak.json
- `laporan/` : laporan dan slide

## Ringkasan hasil Evaluasi P1-P4 (SEED 1010)
- Kanal terpilih: **R**, KB tertinggi pada semua kondisi cahaya.
- Parameter praproses final (`hasil/param_praproses.json`): lebar 640, gamma 1,8, CLAHE kanal V (clip 1,0; tile 8), median 3x3, tanpa penajaman.
- KB kanal R sebelum -> sesudah praproses (40 citra berbercak): normal 8,26 -> 19,54; gelap 8,96 -> 46,73; terang 6,59 -> 11,60; kontras rendah 3,69 -> 8,38; bayangan 5,10 -> 13,22.

## Ringkasan hasil P5-P6
- Deteksi tepi (P5): Canny pada kanal R paling baik (F1 0,984) dan tidak menimbulkan tepi palsu pada daun sehat. Ambang persentil (q = 98) stabil di semua kondisi cahaya (F1 0,981 sampai 0,993).
- Morfologi (P6): citra biner bercak awal sangat kasar (94 sampai 174 komponen). Opening dan closing dengan SE persegi 7x7 memberi galat jumlah komponen terkecil (daun sehat 0,35, k = 4).
- Penyaringan bentuk: luas >= 20 piksel, kebulatan >= 0,5, rasio aspek <= 1,8 menurunkan galat jumlah bercak pada daun sehat dari 8,60 menjadi 3,30.
- Modul `src/bercak.py` (parameter bawaan, `hasil/param_bercak.json`) pada 60 citra: galat persen bercak 0,367; korelasi 0,964; akurasi kelas 0,850.
- Keterbatasan: data sintetis dengan bercak bulat; parameter dan batas kelas ditentukan dari 60 citra yang sama dengan data evaluasi sehingga akurasi bersifat optimistis; kesalahan terbanyak pada kondisi gelap (akurasi 0,67).

## Cara memakai analisis_daun
    import sys, json, cv2
    sys.path.insert(0, "src")
    import bercak
    from praproses import praproses
    PARAM = json.load(open("hasil/param_praproses.json"))
    hasil = bercak.analisis_daun(praproses(cv2.imread("daun.png"), PARAM))
    print(hasil["kelas"], hasil["persen_bercak"], hasil["jumlah_bercak"])
Parameter bercak dapat diubah lewat hasil/param_bercak.json atau argumen kedua analisis_daun.

## Versi pustaka
OpenCV 5.0.0.93, NumPy 2.1.3, scikit-image 0.25.2, matplotlib 3.10.0, pandas 2.2.3, pillow 11.3.0 (lengkapnya di `requirements.txt`).

## Penggunaan AI
Alat bantu AI generatif dipakai untuk memahami konsep dan memeriksa kode, serta membantu menulis beberapa bagian kode (grafik F1, canny_persentil, panel SE, diagram sebar, dan modul bercak.py). Seluruh kode dijalankan dan hasilnya dipahami sendiri.