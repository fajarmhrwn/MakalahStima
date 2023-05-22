# Makalah Strategi Algoritma
<h2 align="center">
   <a href="" target="_blank">Solusi Tower of Hanoi dengan BFS</a>
</h2>
<hr>

## Table of Contents
1. [General Info](#general-information)
2. [Creator Info](#creator-information)
3. [Features](#features)
4. [Technologies Used](#technologies-used)
5. [Setup](#setup)
6. [Usage](#usage)
7. [Screenshots](#screenshots)
8. [Structure](#structure)
9. [Project Status](#project-status)
10. [Room for Improvement](#room-for-improvement)
11. [Acknowledgements](#acknowledgements)
12. [Contact](#contact)

<a name="general-information"></a>

## General Information
Program pembuatan permainan `Tower of Hanoi` sekaligus penyusunan solusi otomatis dengan algoritma `Breadth-First-Search`. Program akan menampilkan 3 tiang dengan piringan yang jumlahnya dapat divariasi. Pengguna dapat memilih piringan yang akan dipindahkan ke tiang tertentu atau menggunakan pencarian otomatis dengan algoritma BFS. Proyek ini merupakan repository untuk memenuhi `Tugas Makalah IF2211 - Strategi Algoritma ITB 2022/2023`.

<a name="creator-information"></a>

## Creator Information

| Nama                        | NIM      | E-Mail                      |
| --------------------------- | -------- | --------------------------- |
| Fajar Maulana Herawan       | 13521080 | 13521080@std.stei.itb.ac.id |

<a name="features"></a>

## Features
- `Memindahkan piringan` secara manual dengan klik kiri pada tiang dengan piringan yang ingin dipindahkan dan klik kiri pada tiang tujuan
- `Pencarian solusi otomatis BFS` dengan menekan tombol `s` pada keyboard
- `Reset permainan` dengan menekan tombol `r` pada keyboard
- `Menambah jumlah piringan` dengan menekan tombol `right arrow` pada keyboard 
- `Mengurangi jumlah piringan` dengan menekan tombol `left arrow` pada keyboard
- `Mempercepat game speed` dengan meneakn tombol `up arrow` pada keyboard
- `Memperlambat game speed` dengan menekan tombol `down arrow` pada keyboard

<a name="technologies-used"></a>

## Technologies Used
- Python - version 3.9.4
- PyGame - version 2.4.0

> Note: The version of the libraries above is the version that we used in this project. You can use the latest version of the libraries.

<a name="setup"></a>

## Setup
1. Download all of the requirements above by using command:
    ```bash
    pip install -r requirements.txt
    ```
2. Clone this repository
    ```bash
    https://github.com/fajarmhrwn/MakalahStima
    ```

<a name="usage"></a>

## Usage
1. Buka direktori proyek tempat kamu menyimpan repository ini
2. Ubah lokasi pada folder `src`
    ```bash
    cd src
    ```
3. Jalankan program dengan command: 
    ```bash
    python main.py
    ```
4. Program siap dimainkan!

<a name="videocapture"></a>
## Video Capture
<nl>

![Tower of Hanoi Gif](/img/hanoi.gif)
## Screenshots
<p>
  <p>Gambar 1. Tampilan Awal</p>
  <img src="/img/SS1.png/">
  <nl>
  <p>Gambar 2. Proses Penyelesaian</p>
  <img src="/img/SS2.png/">
  <nl>
  <p>Gambar 3. Kondisi Akhir</p>
  <img src="/img/SS3.png/">
  <nl>
</p>

<a name="structure"></a>

## Structure
```bash
│   README.md
│   requirements.txt
│
├───doc
│       13521080-FajarMaulanaHerawan.doc
│       13521080-FajarMaulanaHerawan.pdf
│
├───img
│       hanoi.gif
│       icon.png
│       SS1.png
│       SS2.png
│       SS3.png
│
└───src
        disk.py
        hanoi.py
```

<a name="project-status">

## Project Status
Status dari proyek ini: _complete_

<a name="room-for-improvement">

## Room for Improvement
Peningkatan yang dapat dilakukan:
- Mempercantik UI dari tampilan program
- Menambahkan fitur-fitur lain dalam game

<a name="acknowledgements">

## Acknowledgements
- Terima kasih kepada Allah SWT

<a name="contact"></a>

## Contact
<h4 align="center">
  Kontak : 13521080@std.stei.itb.ac.id<br/>
  2023
</h4>
<hr>
