# SIMUTEH - Evaluasi Praktikum P1-P4 Computer Vision

Sistem Pemeriksaan Mutu Daun Teh Berbasis Citra untuk Kelompok Tani Teh Rakyat di Kabupaten Sukabumi.
Nama: Suci Oktavia Ramadhani | NIM: 2330511010 | **SEED = 1010**

## Cara menjalankan
1. Pasang pustaka: `pip install -r requirements.txt`
2. Bangkitkan dataset dari folder utama repository: `python src/buat_dataset_sintetis.py`
   (menghasilkan 60 citra di `data/sintetis/`; folder ini tidak diunggah karena dapat dibangkitkan ulang)
3. Jalankan notebook di folder `notebook/` secara berurutan dengan Restart & Run All: B1, B2, B3, B4, B5.
   Notebook dapat dijalankan di Google Colab dengan mengunggah `src/buat_dataset_sintetis.py` dan `src/utils_cv.py`.

## Struktur repository
- `src/` : buat_dataset_sintetis.py, utils_cv.py, praproses.py
- `notebook/` : B1_lingkungan, B2_citra_warna, B3_histogram, B4_penapisan, B5_praproses
- `hasil/` : gambar, tabel .csv, param_praproses.json
- `laporan/` : laporan dan slide

## Ringkasan hasil (SEED 1010)
- Kanal terpilih: **R**, KB tertinggi pada semua kondisi cahaya.
- Parameter praproses final (`hasil/param_praproses.json`): lebar 640, gamma 1,8, CLAHE kanal V (clip 1,0; tile 8), median 3x3, tanpa penajaman.
- KB kanal R sebelum -> sesudah praproses (40 citra berbercak): normal 8,26 -> 19,54; gelap 8,96 -> 46,73; terang 6,59 -> 11,60; kontras rendah 3,69 -> 8,38; bayangan 5,10 -> 13,22.
- Keterbatasan: KB naik sebagian karena simpangan baku daun mengecil (pada kondisi gelap dI justru turun); jumlah gumpalan terang pada daun sehat bertambah setelah praproses (kemungkinan tulang daun) sehingga perlu dikendalikan pada tahap segmentasi.

## Versi pustaka
OpenCV 5.0.0.93, NumPy 2.1.3, scikit-image 0.25.2, matplotlib 3.10.0, pandas 2.2.3, pillow 11.3.0 (lengkapnya di `requirements.txt`).

## Penggunaan AI
Alat bantu AI generatif dipakai untuk memahami konsep dan memeriksa kode. Seluruh kode dijalankan dan hasilnya dipahami sendiri.