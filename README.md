# README B10
Alvin Widi Nugroho - 2106751902 <br />
Ghayda Rafa Hernawan - 2106634332 <br />
Marietha Asnat Nauli Sitompul - 2106752413 <br />
Rakhan Yusuf Rivesa - 2106751852 <br />
Daffa Muhammad Faizan - 2106704156

#### [🔗 Link Aplikasi Pedulee](https://pedulee.herokuapp.com/) <br />

## CERITA APLIKASI
Sebuah platform yang menerima donasi dalam berbagai bentuk, seperti pakaian bekas layak pakai, dana atau uang, darah, sembako, dan lain sebaginya, untuk membantu isu-isu kemanusiaan yang berkaitan dengan G20. Beberapa isu terkait di antaranya seperti Agriculture and Food Security (donasi uang dan sembako), Climate Sustainability and Energy (donasi pakaian bekas layak pakai), Global Health (donor darah), Strong, Sustainable, Balanced and Inclusive Growth (volunteering). <br />

## DAFTAR MODUL (Fitur)
**1. Main Page (Halaman Utama)** <br />
Modul ini merupakan tampilan pertama yang akan dilihat oleh user saat membuka website (aplikasi) Pedulee. Pada modul ini, user dapat melihat semua modul yang tertera pada website, tetapi tidak semua modul dapat diakses oleh user yang belum login ke dalam website. Modul ini juga menampilkan informasi mengenai berita - berita isu G20 yang sedang terjadi, proyek - proyek yang sedang berjalan, sebuah carousel yang dapat mendirect user menuju link berita isu G20 atau proyek yang sedang berjalan. <br />

**2. Register + Login** <br />
Modul ini digunakan untuk mengindentifikasi user pada website.Modul ini akan meminta user untuk memberikan username dan password yang telah didaftarkan sebelumnya pada modul register. Modul Register akan mewajibkan calon user untuk mengisi beberapa informasi saja seperti nama, alamat, alamat email, nomor telepon, dan tanggal lahir. Informasi lebih lengkap dapat diisi oleh user lebih lanjut pada modul Profile. <br />

**3. Daftar Proyek** <br />
Modul ini akan menampilkan daftar proyek - proyek donasi yang sedang berjalan. Pada setiap proyek, akan ditampilkan informasi singkat mengenai proyek tersebut, link berita terkait proyek tersebut, jumlah donasi yang sudah diterima oleh tim Pedulee untuk proyek tersebut, dan durasi waktu berlangsungnya proyek tersebut.<br />

**4. Form Profile** <br />
Modul ini digunakan oleh user yang telah login untuk memodifikasi data profil milik user tersebut. Data yang dapat diubah adalah nama, deskripsi diri, dan menambahkan foto profil. Selain itu, kita dapat menambahkan identitas lebih spesifik. <br />

**5. Form Donasi Pakaian Bekas Layak Pakai (Rafa)** <br />
Modul ini digunakan oleh user yang telah login untuk mendonasikan pakaian bekas layak pakai yang mereka miliki. Pada modul ini, jenis pakaian yang akan di donasikan dapat dispesifikan berdasarkan jenis, pengguna (jenis kelamin), dan bahan pakaian tersebut. <br />

**6. Form Donasi Dana atau Uang (Daffa)** <br />
Modul ini digunakan oleh user yang telah login untuk berdonasi dalam bentuk uang ke proyek yang dipilih. Fitur yang dimiliki oleh modul ini adalah nama, nominal uang, dan pesan donasi. Setelah itu, user akan diminta metode pembayaran / donasi. <br />

**7. Form Donasi Sembako (Rakhan)** <br />
Modul ini digunakan oleh user yang telah login untuk memberikan donasi berupa sembako. Modul ini akan berisi formulir yang dapat diisi oleh user mengenai bentuk, jenis barang, serta banyak jumlahnya. Implementasi ide dari form ini akan diambil dari katalog yang ada pada menu Gofood. <br />

**8. Form Donasi (donor) Darah (Alvin)** <br />
Modul ini digunakan oleh user yang telah login untuk mendonor darah. Modul ini akan meminta data user berupa nama, tanggal lahir, domisili, golongan darah, rhesus, umur, penyakit bawaan, tempat user ingin donor (pilihan PMI mana). Setelah mendaftar form tersebut, user akan mendapat nomor antrian dan informasi umum yang telah diisi sebelumnya dapat dilihat pada bagian profile user. <br />

**9. Form Pendaftaran Volunteer (Asnat)** <br />
Modul ini digunakan oleh user yang telah login untuk mendaftar menjadi volunteer pada suatu project. Modul ini akan menampilkan project yang sedang membuka pendaftaran untuk volunteer, bidang atau divisi yang tersedia, dan rentang waktu menjadi volunteer. <br />

**10. Form Pendaftaran Proyek Donasi** <br />
Modul ini digunakan oleh user yang telah login untuk mendaftarkan proyek donasi baru yang nantinya akan diproses validitasnya oleh admin. Modul ini akan menampilkan nama proyek donasi, jenis donasi yang dibutuhkan, target donasi, dan waktu serta tempat proyek donasi ini dilaksanakan. <br />

## ROLE PENGGUNA
**a. Guest user** <br />
- Mengunjungi dan mengakses fitur pada Main Page <br />
- Mengunjungi Register dan Sign in Page <br />
- Melihat dan mengunjungi modul Daftar Proyek <br />

**b. Logged in user** <br />
- Mengunjungi dan mengakses fitur pada Main Page <br />
- Mengunjungi Reigster dan Sign in Page <br />
- Melihat dan mengunjungi modul Daftar Proyek <br />
- Mengakses dan mengedit bagian Profile user <br />
- Memberikan donasi berupa pakaian bekas layak pakai, dana atau uang, sembako, dan donor darah <br />
- Mendaftar menjadi volunteer untuk suatu proyek yang sedang berlangsung <br />
- Mendaftar proyek donasi baru <br />

## ROLE ADMIN
- Menampilkan informasi-informasi terkait fitur-fitur yang terdapat pada aplikasi kepada user dengan tampilan ui/ux yang mudah dimengerti dan digunakan <br />
- Mengolah data-data yang dimasukkan oleh user ke dalam formulir-formulir yang terdapat pada fitur-fitur aplikasi. Data-data yang ada dapat dimunculkan dan ditampilkan sebagai informasi kepada pengguna sebagai progress perjalanan donasi dan bantuan kemanusiaan kepada yang membutuhkan <br />
- Memvalidasi proyek baru yang didaftarkan oleh user <br />
