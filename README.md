# StudiKasus 6
Nama : Muhammad Indra Pratama<br>
Nim : 083<br>
Golongan : Ganjil

# Program Nilai Mahasiswa

Ini program sederhana buat mencatat nilai mahasiswa, dibuat pakai Python dan dijalankan lewat terminal. Kita bisa nambah data, ngubah nilai, hapus data, lihat data, dan simpan semuanya ke file JSON (`nilaimahasigma.json`). Karena disimpan ke file, datanya tidak akan hilang walaupun programnya ditutup.

## 1. Penjelasan Kode Program

**Import dan load data**

```python
import json
```

Modul `json` dipakai buat baca dan nulis file JSON. Setelah itu program coba buka `nilaimahasigma.json` dan isinya dimasukin ke variabel `data`. Kalau filenya belum ada atau isinya kosong/rusak, `data` dibikin list kosong aja supaya program tetap bisa jalan.

**`tambah_data(nama, nim, nilai)`**

Fungsi ini nambahin satu mahasiswa baru ke list `data`. Tiap mahasiswa disimpan dalam bentuk dictionary yang isinya nama, nim, dan nilai.

**`ubah_nilai(index, nilai_baru)`**

Dipakai buat ganti nilai mahasiswa yang urutannya sesuai `index`. Yang diubah cuma nilainya, nama dan nim tetap.

**`hapus_data(index)`**

Dipakai buat ngehapus data mahasiswa di urutan tertentu dari list `data`.

**`lihat_data()`**

Nampilin semua data yang ada beserta nomor urutnya (mulai dari 1). Kalau belum ada data sama sekali, bakal muncul tulisan "Data masih kosong."

**`simpan_data()`**

Nulis isi `data` ke file `nilaimahasigma.json`. Ini yang bikin data bisa tetap ada pas program dibuka lagi. Pakai `indent=4` biar isi filenya rapi dan gampang dibaca.

**Menu utama (`while True`)**

Bagian ini nampilin menu 1 sampai 6 terus-menerus sampai user milih keluar. Tiap pilihan manggil fungsi yang sesuai:

1. Tambah data
2. Ubah nilai
3. Hapus data
4. Lihat data
5. Simpan data
6. Keluar

Satu hal yang perlu diingat: perubahan baru benar-benar tersimpan di file kalau kita milih menu 5. Kalau langsung keluar lewat menu 6, perubahannya hilang.

---

## 2. Output Program

Screenshot di bawah ini nunjukin kalau programnya berhasil dijalankan.

**Tampilan menu**
<br>
<img width="557" height="219" alt="image" src="https://github.com/user-attachments/assets/9f50dc11-8021-447a-8446-035d37295927" />


**Tambah data**
<br>
<img width="538" height="227" alt="image" src="https://github.com/user-attachments/assets/f160677e-f55c-452e-bed8-446e3dfcc272" />


**Lihat data**
<br>
<img width="401" height="114" alt="image" src="https://github.com/user-attachments/assets/f2a90955-9c7b-4fe0-842c-69ad78fe649b" />


**Ubah nilai**
<br>
<img width="386" height="172" alt="image" src="https://github.com/user-attachments/assets/98e03cfd-935d-4778-a7af-7ce19318bf36" />


**Hapus data**
<br>
<img width="356" height="154" alt="image" src="https://github.com/user-attachments/assets/ee665c8e-8aae-44fd-8ec1-66a59cc5dbb0" />


**Simpan data**
<br>
<img width="319" height="51" alt="image" src="https://github.com/user-attachments/assets/93dc9a7c-dab4-45ab-b0c3-210b88eb4c95" />


---

## 3. Screenshot Data Tetap Tersimpan Setelah Program Dijalankan Lagi

Buat ngecek data beneran tersimpan, caranya:

1. Jalanin program, tambah data baru, terus pilih menu 5 (simpan data).
2. Keluar dari program lewat menu 6.
3. Jalanin programnya lagi, terus pilih menu 4 (lihat data). Data yang tadi ditambah harusnya masih ada.

**Sebelum keluar (data baru sudah ditambah dan disimpan)**
<br>
<img width="359" height="77" alt="image" src="https://github.com/user-attachments/assets/d4383ace-219c-4108-ac85-a39f25ef1d9e" />


**Setelah program dijalankan lagi (data masih ada)**

<img width="753" height="425" alt="image" src="https://github.com/user-attachments/assets/798d465a-34b2-4862-ac64-886ada544083" />
<br><br>

**Isi file `nilaimahasigma.json`**

<img width="409" height="261" alt="image" src="https://github.com/user-attachments/assets/50084502-1414-485d-ab30-4492daee960d" />
<br><br>

---
